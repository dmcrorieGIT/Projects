#-------------------------------------------------------------------------------
# Runequest Character Sheet Program
# Programmer: Dustin McRorie
#-------------------------------------------------------------------------------

import random

from graphics import *

import time

win = None

#-------------------------------------------------------------------------------
# Runequest Databank
#
#-------------------------------------------------------------------------------

#mydictionary = {'a' : 0, 'b': 0, 'c' : 0, 'd' : 0}

#for key in mydictionary:
#    print("key: %s , value: %s" % (key, mydictionary[key]))

Characteristics = ['STR', 'CON', 'SIZ', 'DEX', 'INT', 'POW', 'CHA']

StandardSkills = ['Athletics', 'Boating', 'Brawn', 'Conceal', 'Customs', 
                  'Dance', 'Deceit', 'Drive', 'Endurance', 'Evade', 'First Aid',
                  'Influence', 'Insight', 'Locale', 'Perception', 'Ride',
                  'Sing', 'Stealth', 'Swim', 'Unarmed', 'Willpower']
StandardSkillsParams = {'Athletics' : ['STR', 'DEX'], 'Boating': ['STR', 'CON'], 
                        'Brawn': ['STR', 'SIZ'], 'Conceal': ['DEX', 'POW'], 
                        'Customs': ['INT', 'INT'], 'Dance': ['DEX', 'CHA'], 
                        'Deceit': ['INT', 'CHA'], 'Drive': ['DEX', 'POW'],
                        'Endurance': ['CON', 'CON'], 'Evade': ['DEX', 'DEX'],
                        'First Aid': ['INT', 'DEX'],'Influence': ['CHA', 'CHA'],
                        'Insight': ['INT', 'POW'], 'Locale': ['INT', 'INT'], 
                        'Perception': ['INT', 'POW'], 'Ride': ['DEX', 'POW'],
                        'Sing': ['POW', 'CHA'], 'Stealth': ['INT', 'DEX'], 
                        'Swim': ['STR', 'CON'], 'Unarmed': ['STR', 'DEX'], 
                        'Willpower': ['POW', 'POW']}
ProfessionalSkills = ['Acting', 'Acrobatics', 'Art', 'ArtC', 'Binding', 'Bureaucracy', 'Combat Style1', 'Combat Style2', 
                      'Commerce', 'Courtesy', 'Craft', 'CraftC', 'Culture', 'Devotion', 
                      'Disguise', 'Engineering', 'Exhort', 'Folk Magic', 'Gambling',
                      'Healing', 'Invocation', 'Language', 'LanguageC', 'LanguageN', 'Literacy', 'Lockpicking',
                      'Mechanisms', 'Lore1', 'Lore2', 'LoreC', 'Meditation', 'Musicianship', 'MusicianshipC', 'Mysticism',
                      'Navigation', 'Oratory', 'Seamanship', 'Seduction', 'Shaping',
                      'Sleight', 'Streetwise', 'Survival', 'Teach', 'Track', 'Trance']

ProfessionalSkillsParams = {'Acting' : ['CHA', 'CHA'], 'Acrobatics': ['STR', 'DEX'], 'Art': ['POW', 'CHA'], 'Binding': ['POW', 'CHA'], 'Bureaucracy': ['INT', 'INT'], 'Combat Style1' : ['STR','DEX'], 'Combat Style2' : ['STR','DEX'],
                            'Commerce': ['INT', 'CHA'], 'Courtesy': ['INT','CHA'], 'Craft': ['DEX','INT'], 'Culture': ['INT','INT'], 'Devotion': ['POW','CHA'], 
                            'Disguise': ['INT','CHA'], 'Engineering': ['INT','INT'], 'Exhort': ['INT','CHA'], 'Folk Magic': ['POW','CHA'], 'Gambling': ['INT','POW'],
                            'Healing': ['INT','POW'], 'Invocation': ['INT','INT'], 'Language': ['INT','CHA'], 'Literacy': ['INT','INT'], 'Lockpicking': ['DEX','DEX'],
                            'Mechanisms': ['DEX','INT'], 'Lore1': ['INT','INT'], 'Lore2': ['INT','INT'], 'Meditation': ['INT','CON'], 'Musicianship': ['DEX','CHA'], 'Mysticism': ['POW','CON'],
                            'Navigation': ['INT','POW'], 'Oratory': ['POW','CHA'], 'Seamanship': ['INT','CON'], 'Seduction': ['INT','CHA'], 'Shaping': ['INT','POW'],
                            'Sleight': ['DEX','CHA'], 'Streetwise': ['POW','CHA'], 'Survival': ['CON','POW'], 'Teach': ['INT','CHA'], 'Track': ['INT','CON'], 'Trance': ['POW','CON'],
                            'ArtC': ['POW', 'CHA'], 'LoreC': ['INT','INT'], 'MusicianshipC': ['DEX','CHA'], 'CraftC': ['DEX','INT'], 'LanguageC': ['INT','CHA'], 'LanguageN': ['INT','CHA']}

Characteristics = ['STR', 'CON', 'SIZ', 'DEX', 'INT', 'POW', 'CHA']



#*******************************************************************************

AgentSS = ['Conceal', 'Deceit', 'Evade', 'Insight', 'Perception', 'Stealth', 'Combat Style1']
AgentPS = ['Culture', 'Disguise', 'Language', 'Sleight', 'Streetwise', 'Survival', 'Track' ]
Agent = [AgentSS, AgentPS]

AlchemistSS = ['Customs', 'Endurance', 'First Aid', 'Insight', 'Locale', 'Perception', 'Willpower']
AlchemistPS = ['Commerce', 'Craft', 'Healing', 'Language', 'Literacy', 'Lore1', 'Streetwise']
Alchemist = [AlchemistSS, AlchemistPS]

BeastHandlerSS = ['Drive', 'Endurance', 'First Aid', 'Influence', 'Locale', 'Ride', 'Willpower']
BeastHandlerPS = ['Commerce', 'Craft', 'Healing', 'Lore1', 'Survival', 'Teach', 'Track']
BeastHandler = [BeastHandlerSS, BeastHandlerPS]

CourtesanSS = ['Customs', 'Dance', 'Deceit', 'Influence', 'Insight', 'Perception', 'Sing']
CourtesanPS = ['Art', 'Courtesy', 'Culture', 'Gambling', 'Language', 'Musicianship', 'Seduction']
Courtesan = [CourtesanSS, CourtesanPS]

CourtierSS = ['Customs', 'Dance', 'Deceit', 'Influence', 'Insight', 'Locale', 'Perception']
CourtierPS = ['Art', 'Bureaucracy', 'Courtesy', 'Culture', 'Language', 'Lore1', 'Oratory' ]
Courtier = [CourtierSS, CourtierPS]

CrafterSS = ['Brawn', 'Drive', 'Influence', 'Insight', 'Locale', 'Perception', 'Willpower']
CrafterPS = ['Art', 'Commerce', 'Craft', 'Craft', 'Engineering', 'Mechanisms', 'Streetwise']
Crafter = [CrafterSS, CrafterPS]

EntertainerSS = ['Athletics', 'Brawn', 'Dance', 'Deceit', 'Influence', 'Insight', 'Sing']
EntertainerPS = ['Acrobatics', 'Acting', 'Oratory', 'Musicianship', 'Seduction', 'Sleight', 'Streetwise']
Entertainer = [EntertainerSS, EntertainerPS]

FarmerSS = ['Athletics', 'Brawn', 'Drive', 'Endurance', 'Locale', 'Perception', 'Ride']
FarmerPS = ['Commerce', 'Craft', 'Lore1', 'Lore2', 'Navigation', 'Survival', 'Track']
Farmer = [FarmerSS, FarmerPS]

FisherSS = ['Athletics', 'Boating', 'Endurance', 'Locale', 'Perception', 'Stealth', 'Swim']
FisherPS = ['Commerce', 'Craft', 'Lore1', 'Lore2', 'Navigation', 'Seamanship', 'Survival']
Fisher = [FisherSS, FisherPS]

HerderSS = ['Endurance', 'First Aid', 'Insight', 'Locale', 'Perception', 'Ride', 'Combat Style1']
HerderPS = ['Commerce', 'Craft', 'Healing', 'Navigation', 'Musicianship', 'Survival', 'Track']
Herder = [HerderSS, HerderPS]

HunterSS = ['Athletics', 'Endurance', 'Locale', 'Perception', 'Ride', 'Stealth', 'Combat Style1']
HunterPS = ['Commerce', 'Craft', 'Lore1', 'Mechanisms', 'Navigation', 'Survival', 'Track']
Hunter = [HunterSS, HunterPS]

MerchantSS = ['Boating', 'Drive', 'Deceit', 'Insight', 'Influence', 'Locale', 'Ride']
MerchantPS = ['Commerce', 'Courtesy', 'Culture', 'Language', 'Navigation', 'Seamanship', 'Streetwise']
Merchant = [MerchantSS, MerchantPS]

MinerSS = ['Athletics', 'Brawn', 'Endurance', 'Locale', 'Perception', 'Sing', 'Willpower']
MinerPS = ['Commerce', 'Craft', 'Engineering', 'Lore1', 'Mechanisms', 'Navigation', 'Survival']
Miner = [MinerSS, MinerPS]

MysticSS = ['Athletics', 'Endurance', 'Evade', 'Insight', 'Perception', 'Willpower', 'Combat Style1']
MysticPS = ['Art', 'Folk Magic', 'Literacy', 'Lore1', 'Meditation', 'Musicianship', 'Mysticism']
Mystic = [MysticSS, MysticPS]

OfficialSS = ['Customs', 'Deceit', 'Influence', 'Insight', 'Locale', 'Perception', 'Willpower']
OfficialPS = ['Bureaucracy', 'Commerce', 'Courtesy', 'Language', 'Literacy', 'Lore1', 'Oratory']
Official = [OfficialSS, OfficialPS]

PhysicianSS = ['Dance', 'First Aid', 'Influence', 'Insight', 'Locale', 'Sing', 'Willpower']
PhysicianPS = ['Commerce', 'Craft', 'Healing', 'Language', 'Literacy', 'Lore1', 'Streetwise']
Physician = [PhysicianSS, PhysicianPS]

PriestSS = ['Customs', 'Dance', 'Deceit', 'Influence', 'Insight', 'Locale', 'Willpower']
PriestPS = ['Bureaucracy', 'Devotion', 'Exhort', 'Folk Magic', 'Literacy', 'Lore1', 'Oratory']
Priest = [PriestSS, PriestPS]

SailorSS = ['Athletics', 'Boating', 'Brawn', 'Endurance', 'Locale', 'Swim', 'Combat Style1']
SailorPS = ['Craft', 'Culture', 'Language', 'Lore1', 'Navigate', 'Seamanship', 'Survival']
Sailor = [SailorSS, SailorPS]

ScholarSS = ['Customs', 'Influence', 'Insight', 'Locale', 'LanguageN', 'Perception', 'Willpower']
ScholarPS = ['Culture', 'Language', 'Literacy', 'Lore1', 'Lore2', 'Oratory', 'Teach']
Scholar = [ScholarSS, ScholarPS]

ScoutSS = ['Athletics', 'Endurance', 'First Aid', 'Perception', 'Stealth', 'Swim', 'Combat Style1']
ScoutPS = ['Culture', 'Healing', 'Language', 'Lore1', 'Navigation', 'Survival', 'Track']
Scout = [ScoutSS, ScoutPS]

ShamanSS = ['Customs', 'Dance', 'Deceit', 'Influence', 'Insight', 'Locale', 'Willpower']
ShamanPS = ['Binding', 'Folk Magic', 'Healing', 'Lore1', 'Oratory', 'Sleight', 'Trance']
Shaman = [ShamanSS, ShamanPS]

SorcererSS = ['Customs', 'Deceit', 'Influence', 'Insight', 'Locale', 'Perception', 'Willpower']
SorcererPS = ['Folk Magic', 'Invocation', 'Language', 'Literacy', 'Lore1', 'Shaping', 'Sleight']
Sorcerer = [SorcererSS, SorcererPS]

ThiefSS = ['Athletics', 'Deceit', 'Evade', 'Insight', 'Perception', 'Stealth', 'Combat Style1']
ThiefPS = ['Acting', 'Commerce', 'Disguise', 'Lockpicking', 'Mechanisms', 'Sleight', 'Streetwise']
Thief = [ThiefSS, ThiefPS]

WarriorSS = ['Athletics', 'Brawn', 'Endurance', 'Evade', 'Unarmed', 'Combat Style1', 'Combat Style2']
WarriorPS = ['Craft', 'Engineering', 'Gambling', 'Lore1', 'Lore2', 'Oratory', 'Survival']
Warrior = [WarriorSS, WarriorPS]








#*******************************************************************************


CivilizedSS = ['Conceal', 'Deceit', 'Drive', 'Influence', 'Insight', 'Locale', 'Willpower']
CivilizedPS = ['ArtC', 'Commerce', 'CraftC', 'Courtesy', 'LanguageC', 'LoreC', 'MusicianshipC', 'Streetwise']

BarbarianSS = ['Athletics', 'Brawn', 'Endurance', 'First Aid', 'Locale', 'Perception'] # Ride or Boating; option
BarbarianPS = ['CraftC', 'Healing', 'LoreC', 'MusicianshipC', 'Navigate', 'Seamanship', 'Survival', 'Track']

NomadSS = ['Endurance', 'First Aid', 'Locale', 'Perception', 'Stealth'] # + 2 of the following: Athletics, Boating, Swim, Drive, or Ride
NomadPS = ['CraftC', 'Culture', 'LanguageC', 'LoreC', 'MusicianshipC', 'Navigate', 'Survival', 'Track']

PrimitiveSS = ['Brawn', 'Endurance', 'Evade', 'Locale', 'Perception', 'Stealth'] # and one of either Athletics, Boating or Swim
PrimitivePS = ['CraftC', 'Healing', 'LoreC', 'MusicianshipC', 'Navigate', 'Survival', 'Track']

CivilizedCareers = [Agent, Alchemist, BeastHandler, Courtesan, Courtier, Crafter, Entertainer,
                    Farmer, Fisher, Herder, Hunter, Merchant, Miner, Mystic, Official,
                    Physician, Priest, Sailor, Scholar, Scout, Shaman, Sorcerer, Thief, Warrior]

CivilizedCareersN = ['Agent', 'Alchemist', 'BeastHandler', 'Courtesan', 'Courtier', 'Crafter', 'Entertainer',
                    'Farmer', 'Fisher', 'Herder', 'Hunter', 'Merchant', 'Miner', 'Mystic', 'Official',
                    'Physician', 'Priest', 'Sailor', 'Scholar', 'Scout', 'Shaman', 'Sorcerer', 'Thief', 'Warrior']

BarbarianCareers = [BeastHandler, Crafter, Entertainer, Farmer, Fisher, Herder, Hunter, Merchant,
                    Miner, Mystic, Official, Physician, Priest, Sailor, Scholar, Scout, Shaman, Thief, Warrior]

BarbarianCareersN = ['BeastHandler', 'Crafter', 'Entertainer', 'Farmer', 'Fisher', 'Herder', 'Hunter', 'Merchant',
                    'Miner', 'Mystic', 'Official', 'Physician', 'Priest', 'Sailor', 'Scholar', 'Scout', 'Shaman', 'Thief', 'Warrior']

NomadCareers = [BeastHandler, Crafter, Fisher, Herder, Hunter, Merchant, Official, Physician, Priest, Sailor, Scholar, Scout, Shaman, Thief, Warrior]

NomadCareersN = ['BeastHandler', 'Crafter', 'Fisher', 'Herder', 'Hunter', 'Merchant', 'Official', 'Physician', 'Priest', 'Sailor', 'Scholar', 'Scout', 'Shaman', 'Thief', 'Warrior']

PrimitiveCareers = [BeastHandler, Crafter, Fisher, Hunter, Physician, Sailor, Scholar, Scout, Shaman, Thief, Warrior]

PrimitiveCareersN = ['BeastHandler', 'Crafter', 'Fisher', 'Hunter', 'Physician', 'Sailor', 'Scholar', 'Scout', 'Shaman', 'Thief', 'Warrior']





#*******************************************************************************




#-------------------------------------------------------------------------------




#-------------------------------------------------------------------------------
# Purpose: Character sheet class
#
#
#
#-------------------------------------------------------------------------------

class CharacterSheet:
    
    def __init__(self):
        
        
        #-----------------------------------------------------------------------
        # Step 1: The Characteristics
        # - The first thing we need to do is figure out what characteristics the
        # player will have. We can do this one of three ways: preset values
        # determined by the user, randomly rolled, or point buy.
        #-----------------------------------------------------------------------
        
        Characteristics = ['STR', 'CON', 'SIZ', 'DEX', 'INT', 'POW', 'CHA']
        self.playercharacteristics = {}
        self.name = str(input("What is the name of this Character? "))
        test01 = str(input('Do you have your own characteristics? (Y/N): '))
        
        # Method 1: Preset Characteristics:
        #-----------------------------------------------------------------------
        if test01 == 'Y':
            for char in Characteristics:
                x = int(input('please enter your value for ' + str(char) + ': '))
                self.playercharacteristics[char] = x
        #-----------------------------------------------------------------------
        
        elif test01 == 'N':
            
            test02 = str(input('Do you want to use point buy? (Y/N): '))
            
            # Method 2: Randomly Rolled
            #-------------------------------------------------------------------
            if test02 == 'N':
                Str = threeDsix()
                print('STR: ' + str(Str))
                time.sleep(1)
                Con = threeDsix()
                print('CON: ' + str(Con))
                time.sleep(1)                
                Siz = twoDsix() + 6
                print('SIZ: ' + str(Siz))
                time.sleep(1)                
                Dex = threeDsix()
                print('DEX: ' + str(Dex))
                time.sleep(1)                
                Int = twoDsix() + 6
                print('INT: ' + str(Int))
                time.sleep(1)                
                Pow = threeDsix()
                print('POW: ' + str(Pow))
                time.sleep(1)                
                Cha = threeDsix()
                print('CHA: ' + str(Cha))
                time.sleep(1)                
                nums = [Str, Con, Siz, Dex, Int, Pow, Cha]
                x = 0
                for char in Characteristics:
                    self.playercharacteristics[char] = nums[x]
                    x += 1
            #-------------------------------------------------------------------
            
            # Method 3: Point Buy
            #-------------------------------------------------------------------
            elif test02 == 'Y':
                self.playercharacteristics['STR'] = 3
                self.playercharacteristics['CON'] = 3
                self.playercharacteristics['SIZ'] = 8
                self.playercharacteristics['DEX'] = 3
                self.playercharacteristics['INT'] = 8
                self.playercharacteristics['POW'] = 3
                self.playercharacteristics['CHA'] = 3
                cmax = 18
                points = 49
                print('STR: ' + str(self.playercharacteristics['STR']))
                print('CON: ' + str(self.playercharacteristics['CON']))
                print('SIZ: ' + str(self.playercharacteristics['SIZ']))
                print('DEX: ' + str(self.playercharacteristics['DEX']))
                print('INT: ' + str(self.playercharacteristics['INT']))
                print('POW: ' + str(self.playercharacteristics['POW']))
                print('CHA: ' + str(self.playercharacteristics['CHA']))
                print('you have ' + str(points) + ' left to spend')                
                while points != 0:
                    chosenchar = str(input('which characteristic would you like to improve? (STR, CON, SIZ, DEX, INT, POW, CHA): '))
                    if chosenchar not in Characteristics:
                        print('please choose a valid characteristic from the options provided')
                        continue
                    amount = int(input('by how much? '))
                    if (points - amount) < 0:
                        print('not enough points')
                        continue
                    if (self.playercharacteristics[chosenchar] + amount) > cmax:
                        print('The amount you requested will exceed the maximum; choose another number')
                        continue
                    self.playercharacteristics[chosenchar] = self.playercharacteristics[chosenchar] + amount
                    points = points - amount
                    print('STR: ' + str(self.playercharacteristics['STR']))
                    print('CON: ' + str(self.playercharacteristics['CON']))
                    print('SIZ: ' + str(self.playercharacteristics['SIZ']))
                    print('DEX: ' + str(self.playercharacteristics['DEX']))
                    print('INT: ' + str(self.playercharacteristics['INT']))
                    print('POW: ' + str(self.playercharacteristics['POW']))
                    print('CHA: ' + str(self.playercharacteristics['CHA']))
                    print('you have ' + str(points) + ' left to spend')
                print('All points have been spent, and your characteristics are now complete')
            #-------------------------------------------------------------------
            
        #-----------------------------------------------------------------------
        # Skills
        #
        #
        #-----------------------------------------------------------------------
        
        self.PlayerSkills = {}
        self.PlayerSkills[StandardSkills[0]] = (self.playercharacteristics['STR'] + self.playercharacteristics['DEX']) #Athletics
        self.PlayerSkills[StandardSkills[1]] = (self.playercharacteristics['STR'] + self.playercharacteristics['CON']) #Boating
        self.PlayerSkills[StandardSkills[2]] = (self.playercharacteristics['STR'] + self.playercharacteristics['SIZ']) #Brawn
        self.PlayerSkills[StandardSkills[3]] = (self.playercharacteristics['DEX'] + self.playercharacteristics['POW']) #Conceal
        self.PlayerSkills[StandardSkills[4]] = (self.playercharacteristics['INT'] + self.playercharacteristics['INT']) #Customs
        self.PlayerSkills[StandardSkills[5]] = (self.playercharacteristics['DEX'] + self.playercharacteristics['CHA']) #Dance
        self.PlayerSkills[StandardSkills[6]] = (self.playercharacteristics['INT'] + self.playercharacteristics['CHA']) #Deciet
        self.PlayerSkills[StandardSkills[7]] = (self.playercharacteristics['DEX'] + self.playercharacteristics['POW']) #Drive
        self.PlayerSkills[StandardSkills[8]] = (self.playercharacteristics['CON'] + self.playercharacteristics['CON']) #Endurance
        self.PlayerSkills[StandardSkills[9]] = (self.playercharacteristics['DEX'] + self.playercharacteristics['DEX']) #Evade
        self.PlayerSkills[StandardSkills[10]] = (self.playercharacteristics['INT'] + self.playercharacteristics['DEX']) #First Aid
        self.PlayerSkills[StandardSkills[11]] = (self.playercharacteristics['CHA'] + self.playercharacteristics['CHA']) #Influence
        self.PlayerSkills[StandardSkills[12]] = (self.playercharacteristics['INT'] + self.playercharacteristics['POW']) #Insight
        self.PlayerSkills[StandardSkills[13]] = (self.playercharacteristics['INT'] + self.playercharacteristics['INT']) #Locale
        self.PlayerSkills[StandardSkills[14]] = (self.playercharacteristics['INT'] + self.playercharacteristics['POW']) #Perception
        self.PlayerSkills[StandardSkills[15]] = (self.playercharacteristics['DEX'] + self.playercharacteristics['POW']) #Ride
        self.PlayerSkills[StandardSkills[16]] = (self.playercharacteristics['POW'] + self.playercharacteristics['CHA']) #Sing
        self.PlayerSkills[StandardSkills[17]] = (self.playercharacteristics['INT'] + self.playercharacteristics['DEX']) #Stealth
        self.PlayerSkills[StandardSkills[18]] = (self.playercharacteristics['STR'] + self.playercharacteristics['CON']) #Swim
        self.PlayerSkills[StandardSkills[19]] = (self.playercharacteristics['STR'] + self.playercharacteristics['DEX']) #Unarmed
        self.PlayerSkills[StandardSkills[20]] = (self.playercharacteristics['POW'] + self.playercharacteristics['POW']) #Willpower
        
        #-----------------------------------------------------------------------
        # Action points, strike rank, etc:
        #
        #-----------------------------------------------------------------------
        
        self.actionpoints = calcActionPoints(self.playercharacteristics['INT'], self.playercharacteristics['DEX'])
        self.damagemodifier = calcDamageModifier(self.playercharacteristics['STR'], self.playercharacteristics['SIZ'])
        self.expmodifier = calcExpModifier(self.playercharacteristics['CHA'])
        self.healingrate = calcHealingRate(self.playercharacteristics['CON'])
        self.maxhitpoints = calcHitPoints(self.playercharacteristics['CON'], self.playercharacteristics['SIZ'])
        self.movementrate = 6
        self.strikerank = calcStrikeRank(self.playercharacteristics['INT'], self.playercharacteristics['DEX'])
        self.magicpoints = self.playercharacteristics['POW']
        self.luckpoints = calcLuckPoints(self.playercharacteristics['POW'])
            

        #-----------------------------------------------------------------------
        # Picking a Culture
        #-----------------------------------------------------------------------
        
        self.culturalskills = {}        
        self.culture = int(input("What is your character's culture?: \n1 for civilized, 2 for Barbaric, 3 for Nomadic, 4 for primitive \n"))

# Civilized --------------------------------------------------------------------
        if self.culture == 1:
            self.culture = "Civilized"
            for i in range(len(CivilizedSS)):
                self.culturalskills[CivilizedSS[i]] = 0
            for i in range(len(CivilizedPS)):
                print(str(i) + "=" + str(CivilizedPS[i]))
            cond = 0
            while cond == 0:
                a = int(input("Enter the number that corresponds to the skill you want. Pick 3: "))
                b = int(input("Pick another one: "))
                c = int(input("One more: "))
                if a == b or a == c or c == b:
                    print("Cannot choose the same skill twice. Try again.")
                    continue
                if a >= len(CivilizedPS) or b >= len(CivilizedPS) or c >= len(CivilizedPS) or a < 0 or b < 0 or c < 0:
                    print("One of your choices is not a valid number. Try again.")
                    continue
                print("Well Done!")
                self.culturalskills[CivilizedPS[a]] = 0
                self.culturalskills[CivilizedPS[b]] = 0
                self.culturalskills[CivilizedPS[c]] = 0
                self.PlayerSkills[CivilizedPS[a]] = (self.playercharacteristics[ProfessionalSkillsParams[CivilizedPS[a]][0]] + self.playercharacteristics[ProfessionalSkillsParams[CivilizedPS[a]][1]])
                self.PlayerSkills[CivilizedPS[b]] = (self.playercharacteristics[ProfessionalSkillsParams[CivilizedPS[b]][0]] + self.playercharacteristics[ProfessionalSkillsParams[CivilizedPS[b]][1]])
                self.PlayerSkills[CivilizedPS[c]] = (self.playercharacteristics[ProfessionalSkillsParams[CivilizedPS[c]][0]] + self.playercharacteristics[ProfessionalSkillsParams[CivilizedPS[c]][1]])
                cond = 1
# Barbarian --------------------------------------------------------------------
        elif self.culture == 2:
            self.culture = "Barbaric"
            check2 = int(input("1 for Boating, 2 for Ride: "))
            if check2 == 1:
                self.culturalskills['Boating'] = 0
            elif check2 == 2:
                self.culturalskills['Ride'] = 0
            for i in range(len(BarbarianSS)):
                self.culturalskills[BarbarianSS[i]] = 0
            for i in range(len(BarbarianPS)):
                print(str(i) + "=" + str(BarbarianPS[i]))
            cond = 0
            while cond == 0:
                a = int(input("Enter the number that corresponds to the skill you want. Pick 3: "))
                b = int(input("Pick another one: "))
                c = int(input("One more: "))
                if a == b or a == c or c == b:
                    print("Cannot choose the same skill twice. Try again.")
                    continue
                if a >= len(BarbarianPS) or b >= len(BarbarianPS) or c >= len(BarbarianPS) or a < 0 or b < 0 or c < 0:
                    print("One of your choices is not a valid number. Try again.")
                    continue
                print("Well Done!")
                self.culturalskills[BarbarianPS[a]] = 0
                self.culturalskills[BarbarianPS[b]] = 0
                self.culturalskills[BarbarianPS[c]] = 0
                self.PlayerSkills[BarbarianPS[a]] = (self.playercharacteristics[ProfessionalSkillsParams[BarbarianPS[a]][0]] + self.playercharacteristics[ProfessionalSkillsParams[BarbarianPS[a]][1]])
                self.PlayerSkills[BarbarianPS[b]] = (self.playercharacteristics[ProfessionalSkillsParams[BarbarianPS[b]][0]] + self.playercharacteristics[ProfessionalSkillsParams[BarbarianPS[b]][1]])
                self.PlayerSkills[BarbarianPS[c]] = (self.playercharacteristics[ProfessionalSkillsParams[BarbarianPS[c]][0]] + self.playercharacteristics[ProfessionalSkillsParams[BarbarianPS[c]][1]])
                cond = 1
# Nomadic ----------------------------------------------------------------------
        elif self.culture == 3:
            self.culture = "Nomadic"
            cond1 = 0
            # + 2 of the following: Athletics, Boating, Swim, Drive, or Ride
            while cond1 == 0:
                a1 = int(input("Pick 1 of the following: 1 for Athletics, 2 for Boating, 3 for Swim, 4 for for Ride \n>>"))
                a2 = int(input("Pick another, different one of the following: 1 for Athletics, 2 for Boating, 3 for Swim, 4 for for Ride \n>>"))
                if a1 == a2:
                    print("Two of the same, try again \n")
                    continue
                if a1 == 1 or a2 == 1:
                    self.culturalskills['Athletics'] = 0
                if a1 == 2 or a2 == 2:
                    self.culturalskills['Boating'] = 0
                if a1 == 3 or a2 == 3:
                    self.culturalskills['Swim'] = 0
                if a1 == 4 or a2 == 4:
                    self.culturalskills['Ride'] = 0
                cond1 = 1
            for i in range(len(NomadSS)):
                self.culturalskills[NomadSS[i]] = 0
            for i in range(len(NomadPS)):
                print(str(i) + "=" + str(NomadPS[i]))
            cond = 0
            while cond == 0:
                a = int(input("Enter the number that corresponds to the skill you want. Pick 3: "))
                b = int(input("Pick another one: "))
                c = int(input("One more: "))
                if a == b or a == c or c == b:
                    print("Cannot choose the same skill twice. Try again.")
                    continue
                if a >= len(NomadPS) or b >= len(NomadPS) or c >= len(NomadPS) or a < 0 or b < 0 or c < 0:
                    print("One of your choices is not a valid number. Try again.")
                    continue
                print("Well Done!")
                self.culturalskills[NomadPS[a]] = 0
                self.culturalskills[NomadPS[b]] = 0
                self.culturalskills[NomadPS[c]] = 0
                self.PlayerSkills[NomadPS[a]] = (self.playercharacteristics[ProfessionalSkillsParams[NomadPS[a]][0]] + self.playercharacteristics[ProfessionalSkillsParams[NomadPS[a]][1]])
                self.PlayerSkills[NomadPS[b]] = (self.playercharacteristics[ProfessionalSkillsParams[NomadPS[b]][0]] + self.playercharacteristics[ProfessionalSkillsParams[NomadPS[b]][1]])
                self.PlayerSkills[NomadPS[c]] = (self.playercharacteristics[ProfessionalSkillsParams[NomadPS[c]][0]] + self.playercharacteristics[ProfessionalSkillsParams[NomadPS[c]][1]])
                cond = 1
# Primitive --------------------------------------------------------------------
        elif self.culture == 4:
            self.culture = "Primitive"
            check2 = int(input("1 for Athletics, 2 for Boating, 3 for Swim: "))
            if check2 == 1:
                self.culturalskills['Athletics'] = 0
            elif check2 == 2:
                self.culturalskills['Boating'] = 0
            elif check2 ==3:
                self.culturalskills['Swim'] = 0
            for i in range(len(PrimitiveSS)):
                self.culturalskills[PrimitiveSS[i]] = 0
            for i in range(len(PrimitivePS)):
                print(str(i) + "=" + str(PrimitivePS[i]))
            cond = 0
            while cond == 0:
                a = int(input("Enter the number that corresponds to the skill you want. Pick 3: "))
                b = int(input("Pick another one: "))
                c = int(input("One more: "))
                if a == b or a == c or c == b:
                    print("Cannot choose the same skill twice. Try again.")
                    continue
                if a >= len(PrimitivePS) or b >= len(PrimitivePS) or c >= len(PrimitivePS) or a < 0 or b < 0 or c < 0:
                    print("One of your choices is not a valid number. Try again.")
                    continue
                print("Well Done!")
                self.culturalskills[PrimitivePS[a]] = 0
                self.culturalskills[PrimitivePS[b]] = 0
                self.culturalskills[PrimitivePS[c]] = 0
                self.PlayerSkills[PrimitivePS[a]] = (self.playercharacteristics[ProfessionalSkillsParams[PrimitivePS[a]][0]] + self.playercharacteristics[ProfessionalSkillsParams[PrimitivePS[a]][1]])
                self.PlayerSkills[PrimitivePS[b]] = (self.playercharacteristics[ProfessionalSkillsParams[PrimitivePS[b]][0]] + self.playercharacteristics[ProfessionalSkillsParams[PrimitivePS[b]][1]])
                self.PlayerSkills[PrimitivePS[c]] = (self.playercharacteristics[ProfessionalSkillsParams[PrimitivePS[c]][0]] + self.playercharacteristics[ProfessionalSkillsParams[PrimitivePS[c]][1]])
                cond = 1
#-------------------------------------------------------------------------------
# Careers
#
#-------------------------------------------------------------------------------

        if self.culture == "Civilized":
            for i in range(len(CivilizedCareersN)):
                print(str(i) + "=" + CivilizedCareersN[i])
            careerinp = int(input("please pick the career you wish to be, based on the number that corresponds to it: \n>>"))
            self.career = CivilizedCareers[careerinp]
            self.careername = CivilizedCareersN[careerinp]

        elif self.culture == "Barbaric":
            for i in range(len(BarbarianCareersN)):
                print(str(i) + "=" + BarbarianCareersN[i])
            careerinp = int(input("please pick the career you wish to be, based on the number that corresponds to it: \n>>"))
            self.career = BarbarianCareers[careerinp]
            self.careername = BarbarianCareersN[careerinp]

        elif self.culture == "Nomadic":
            for i in range(len(NomadCareersN)):
                print(str(i) + "=" + NomadCareersN[i])
            careerinp = int(input("please pick the career you wish to be, based on the number that corresponds to it: \n>>"))
            self.career = NomadCareers[careerinp]
            self.careername = NomadCareersN[careerinp]

        elif self.culture == "Primitive":
            for i in range(len(PrimitiveCareersN)):
                print(str(i) + "=" + PrimitiveCareersN[i])
            careerinp = int(input("please pick the career you wish to be, based on the number that corresponds to it: \n>>"))
            self.career = PrimitiveCareers[careerinp]
            self.careername = PrimitiveCareersN[careerinp]
        
        self.profskills = {}
        for i in range(len(self.career[0])):
            if self.career[0][i] not in StandardSkills:
                self.PlayerSkills[self.career[0][i]] = (self.playercharacteristics[ProfessionalSkillsParams[self.career[0][i]][0]] + self.playercharacteristics[ProfessionalSkillsParams[self.career[0][i]][1]])
        for i in range(len(self.career[0])):
            self.profskills[self.career[0][i]] = 0

        for i in range(len(self.career[1])):
            print(str(i) + "=" + str(self.career[1][i]))
            condp = 0
        while condp == 0:
            a = int(input("Enter the number that corresponds to the skill you want. Pick 3: "))
            b = int(input("Pick another one: "))
            c = int(input("One more: "))
            if a == b or a == c or c == b:
                print("Cannot choose the same skill twice. Try again.")
                continue
            if a >= len(self.career[1]) or b >= len(self.career[1]) or c >= len(self.career[1]) or a < 0 or b < 0 or c < 0:
                print("One of your choices is not a valid number. Try again.")
                continue
            print("Well Done!")
            self.profskills[self.career[1][a]] = 0
            self.profskills[self.career[1][b]] = 0
            self.profskills[self.career[1][c]] = 0
            self.PlayerSkills[self.career[1][a]] = (self.playercharacteristics[ProfessionalSkillsParams[self.career[1][a]][0]] + self.playercharacteristics[ProfessionalSkillsParams[self.career[1][a]][1]])
            self.PlayerSkills[self.career[1][b]] = (self.playercharacteristics[ProfessionalSkillsParams[self.career[1][b]][0]] + self.playercharacteristics[ProfessionalSkillsParams[self.career[1][b]][1]])
            self.PlayerSkills[self.career[1][c]] = (self.playercharacteristics[ProfessionalSkillsParams[self.career[1][c]][0]] + self.playercharacteristics[ProfessionalSkillsParams[self.career[1][c]][1]])
            condp = 1
        checkcs = input("Do you want to take a combat style as a cultural skill? (Y/N): \n>>")
        if checkcs == 'Y':
            self.culturalskills['Combat StyleC'] = 0
            self.PlayerSkills['Combat StyleC'] = (self.playercharacteristics['STR'] + self.playercharacteristics['DEX'])

#-------------------------------------------------------------------------------
# Distribution of points
#
#-------------------------------------------------------------------------------

# Professional Points ----------------------------------------------------------
        profpoints = 100
        while profpoints > 0:
            for key in self.profskills:
                print("key: %s , value: %s" % (key, self.profskills[key]))
            print("You have " + str(profpoints) + " left to spend.")
            profcheck = input("What skill would you like to increase? \n>> ")
            profnamecheck = 0
            for key in self.profskills:
                if profcheck == key:
                    profnamecheck = 1
                    if self.profskills[profcheck] == 15:
                        print("cannot raise this skill any further with proffesional points. Try again")
                        continue
                    profincrem = int(input("How much points would you like to increase this skill by? \n>> "))
                    if self.profskills[profcheck] + profincrem > 15:
                        print("Cannot increase skill by that much, as it exceed # of proffesional points \nfor that skill. Try again")
                        time.sleep(1)
                        continue
                    if profpoints - profincrem < 0:
                        print("Not enough proffessional points in the pool to spend that much. Try again")
                        time.sleep(1)
                        continue
                    checkvar = self.PlayerSkills.get(profcheck)
                    if checkvar == None:
                        self.PlayerSkills[profcheck] = (self.playercharacteristics[ProfessionalSkillsParams[profcheck][0]] + self.playercharacteristics[ProfessionalSkillsParams[profcheck][1]])
                    self.profskills[profcheck] += profincrem
                    self.PlayerSkills[profcheck] += profincrem
                    profpoints -= profincrem
                    continue
            if profnamecheck == 0:
                print("not a valid skill name, try again")
                time.sleep(1)
                continue

# Cultural Points --------------------------------------------------------------
        cultpoints = 100
        for key in self.culturalskills:
            self.culturalskills[key] += 5
            self.PlayerSkills[key] += 5
            cultpoints -=5
        while cultpoints > 0:
            for key in self.culturalskills:
                print("key: %s , value: %s" % (key, self.culturalskills[key]))
            print("You have " + str(cultpoints) + " left to spend.")
            cultcheck = input("What skill would you like to increase? \n>> ")
            cultnamecheck = 0
            for key in self.culturalskills:
                if cultcheck == key:
                    cultnamecheck = 1
                    if self.culturalskills[cultcheck] == 15:
                        print("cannot raise this skill any further with proffesional points. Try again")
                        continue
                    cultincrem = int(input("How much points would you like to increase this skill by? \n>> "))
                    if self.culturalskills[cultcheck] + cultincrem > 15:
                        print("Cannot increase skill by that much, as it exceed # of culture points \nfor that skill. Try again")
                        time.sleep(1)
                        continue
                    if cultpoints - cultincrem < 0:
                        print("Not enough culture points in the pool to spend that much. Try again")
                        time.sleep(1)
                        continue
                    self.culturalskills[cultcheck] += cultincrem
                    self.PlayerSkills[cultcheck] += cultincrem
                    cultpoints -= cultincrem
                    continue
            if cultnamecheck == 0:
                print("not a valid skill name, try again")
                time.sleep(1)
                continue       

# Free Points ------------------------------------------------------------------

        freepoints = 150
        self.freeskills = {}
        for key in self.PlayerSkills:
            self.freeskills[key] = 0
        while freepoints > 0:
            for key in self.freeskills:
                print("key: %s , value: %s" % (key, self.freeskills[key]))
            print("You have " + str(freepoints) + " left to spend.")
            freecheck = input("What skill would you like to increase? \n>> ")
            freenamecheck = 0
            for key in self.freeskills:
                if freecheck == key:
                    freenamecheck = 1
                    if self.freeskills[freecheck] == 15:
                        print("cannot raise this skill any further with proffesional points. Try again")
                        continue
                    freeincrem = int(input("How much points would you like to increase this skill by? \n>> "))
                    if self.freeskills[freecheck] + freeincrem > 15:
                        print("Cannot increase skill by that much, as it exceed # of culture points \nfor that skill. Try again")
                        time.sleep(1)
                        continue
                    if freepoints - freeincrem < 0:
                        print("Not enough culture points in the pool to spend that much. Try again")
                        time.sleep(1)
                        continue
                    self.freeskills[freecheck] += freeincrem
                    self.PlayerSkills[freecheck] += freeincrem
                    freepoints -= freeincrem
                    continue
            if freenamecheck == 0:
                print("not a valid skill name, try again")
                time.sleep(1)
                continue            
#-------------------------------------------------------------------------------
# Calculating non-standard skills ----------------------------------------------
        self.NonStandard = []
        for key in self.PlayerSkills:
            if key not in StandardSkills:
                self.NonStandard.append(key)






#-------------------------------------------------------------------------------
def printstuff():
    for c in range(5):
        x = random.randint(1, 5)
        print(x)
def oneDfour():
    x = random.randint(1,4)
    return(x)


def oneDsix():
    x = random.randint(1,6)
    return int(x)
def twoDsix():
    x = random.randint(1,6)
    y = random.randint(1,6)
    t = x + y
    return int(t)
def threeDsix():
    x = random.randint(1,6)
    y = random.randint(1,6)
    z = random.randint(1,6)
    t = x + y + z
    return int(t)

def rollDhundred():
    x = random.randint(1, 100)
    return int(x)


def makealist():
    testlist = [1,2,3,4,
                5,6,7,8,
                9,10]
    return testlist
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Calculations of other parameters
#
#-------------------------------------------------------------------------------

def calcActionPoints(DEX, INT):
    value = (DEX + INT)
    if value % 12 == 0:
        return int(value / 12)
    value /= 12
    return int(value) + 1

damagemodifierdice = ['-1D8', '-1D6', '-1D4', '-1D2', '0', '1D2', '1D4', 
                      '1D6', '1D8', '1D10', '1D12', '2D6', '1d8+1d6', 
                       '2D8', '1d10+1d8', '2D10', '2d10+1d2', '2d10+1d4']

def calcDamageModifier(STR, SIZ):
    value = (STR + SIZ)
    if value > 50:
        if value % 10 == 0:
            finalvalue = int((value - 50) / 10) + 9
            return damagemodifierdice[finalvalue]
        finalvalue = int((value - 50) / 10) + 10
        return damagemodifierdice[finalvalue]        
    if value % 5 == 0:
        finalvalue = int(value / 5) - 1
        return damagemodifierdice[finalvalue]
    value /= 5
    finalvalue = int(value)
    return damagemodifierdice[finalvalue]

def calcExpModifier(CHA):
    value = CHA
    if value % 6 == 0:
        return int(value / 6) - 2
    value /= 6
    return int(value) -1

def calcHealingRate(CON):
    value = CON
    if value % 6 == 0:
        return int(value / 6)
    value /= 6
    return int(value) + 1

def calcHitPoints(CON, SIZ):
    value = (CON + SIZ)
      
    if value % 5 == 0:
        finalvalue = int(value / 5) - 1
        
    else:
        value /= 5
        finalvalue = int(value)
    
    HitLocations = [1, 3, 2, 0, 0, 1, 1]
    
    for i in range(7):
        HitLocations[i] += finalvalue
        if HitLocations[i] == 0:
            HitLocations[i] = 1
    
    return HitLocations

def calcStrikeRank(DEX, INT):
    value = (DEX + INT)
    if value % 2 == 1:
        value /= 2
        finalvalue = int(value) + 1
        return finalvalue
    finalvalue = value / 2
    return int(finalvalue)

def calcLuckPoints(POW):
    value = POW
    if value % 6 == 0:
        return int(value / 6)
    value /= 6
    return int(value) + 1



#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Purpose: To make a number of lines, n, going vertically downwards
# Syntax: makelines(3, 20, 50, 60, 13, win)
# Parameters: numlines; number of horizontal lines to be made, linesize; size of
#             the lines that are made, measured in pixels, xcor; x-coordinate of
#             the line, ycor; y-coordinate of the line, linespace; space between
#             each line made, win; graphics window to be drawn in.
# Return: Nothing returned; draws lines in the graphics window.
#-------------------------------------------------------------------------------

def makelines(numlines, linesize, xcor, ycor, linespace, win):
    for i in range(numlines):
        line = Line(Point(xcor, ycor), Point(xcor+linesize, ycor))
        line.draw(win)
        ycor += linespace
#-------------------------------------------------------------------------------
# Purpose: Allows user to use a number of experience rolls on a character
# Syntax: expRolls(dustin, 4)
# Parameter(s): charactersheet; character sheet to be given rolls
#               numrolls; amount of exp rolls to be given to a character
# Return: Character sheet, modified by the exp rolls
#-------------------------------------------------------------------------------

def expRolls(charactersheet, numrolls):
    
    nums = numrolls
    
    while nums != 0:
        if nums >= 3:
            ask = input("Do you want to increase a stat?(Y/N) \n>> ")
            if ask == "Y":
                ask2 = input("Which one? (STR, CON, SIZ, DEX, INT, POW, CHA) \n>> ")
                if ask2 not in Characteristics:
                    print("Not a valid stat. Try again")
                    continue
                else:
                    charactersheet.playercharacteristics[ask2] += 1
                    recalculateSkills(charactersheet, ask2)
                    charactersheet.actionpoints = calcActionPoints(charactersheet.playercharacteristics['INT'], charactersheet.playercharacteristics['DEX'])
                    charactersheet.damagemodifier = calcDamageModifier(charactersheet.playercharacteristics['STR'], charactersheet.playercharacteristics['SIZ'])
                    charactersheet.expmodifier = calcExpModifier(charactersheet.playercharacteristics['CHA'])
                    charactersheet.healingrate = calcHealingRate(charactersheet.playercharacteristics['CON'])
                    charactersheet.maxhitpoints = calcHitPoints(charactersheet.playercharacteristics['CON'], charactersheet.playercharacteristics['SIZ'])
                    charactersheet.movementrate = 6
                    charactersheet.strikerank = calcStrikeRank(charactersheet.playercharacteristics['INT'], charactersheet.playercharacteristics['DEX'])
                    charactersheet.magicpoints = charactersheet.playercharacteristics['POW']
                    charactersheet.luckpoints = calcLuckPoints(charactersheet.playercharacteristics['POW'])                    
                    nums -=3
                    continue
                
        for i in range(21):
            print(str(i) + "= " + str(StandardSkills[i]) + ": " + str(charactersheet.PlayerSkills[StandardSkills[i]]))
        
        print("\n" +"-----------------------------------------------------------------" + "\n")
        ix = 21
        for i in range(len(charactersheet.NonStandard)):
            print(str(ix) + "= " + str(charactersheet.NonStandard[i]) + ": " + str(charactersheet.PlayerSkills[charactersheet.NonStandard[i]]))
            ix += 1

            
        chosen = input(str("Which skill would you like to roll for? \n>> "))
        level = int(charactersheet.PlayerSkills[chosen])
        newlevel = rollForSkill(level)
        charactersheet.PlayerSkills[chosen] = newlevel
        
        
        nums -=1






#-------------------------------------------------------------------------------

def rollForSkill(level):
    check = rollDhundred()
    print(check)
    time.sleep(1)
    if check >= level:
        incremx = oneDfour()
        Increm = 1 + incremx
        level += Increm
    elif check < level:
        level += 1
    
    return level








#-------------------------------------------------------------------------------

def recalculateSkills(charactersheet, characteristic):
    for key in charactersheet.PlayerSkills:
        if key in StandardSkills:
            if characteristic in StandardSkillsParams[key]:
                if characteristic == StandardSkillsParams[key][0] and characteristic == StandardSkillsParams[key][1]:
                    charactersheet.PlayerSkills[key] += 2
                else:
                    charactersheet.PlayerSkills[key] += 1
        elif key in ProfessionalSkills:
            if characteristic in ProfessionalSkillsParams[key]:
                if characteristic == ProfessionalSkillsParams[key][0] and characteristic == ProfessionalSkillsParams[key][1]:
                    charactersheet.PlayerSkills[key] += 2
                else:
                    charactersheet.PlayerSkills[key] += 1








#-------------------------------------------------------------------------------


def blankcharactersheet(charactersheet):

    inf = 1
    #if win == None:
    win = GraphWin("Character Sheet", 800, 1100)



#-------------------------------------------------------------------------------
# First Box; player information, top left
#
#-------------------------------------------------------------------------------

    GPlayer = Text(Point(70, 30), 'Player:')
    GPlayer.setSize(9)
    GPlayer.draw(win)

    Gplayerline = Line(Point(92, 35), Point(203, 35))
    Gplayerline.draw(win)
    
    GCharacter = Text(Point(235, 30), 'Character:')
    GCharacter.setSize(9)
    GCharacter.draw(win)    

    Gcharacterline = Line(Point(265, 35), Point(380, 35))
    Gcharacterline.draw(win)
 
    GAge = Text(Point(65, 60), 'Age:')
    GAge.setSize(9) 
    GAge.draw(win)
 
    Gageline = Line(Point(78, 65), Point(95, 65))
    Gageline.draw(win)
 
    GGender = Text(Point(120, 60), 'Gender:')
    GGender.setSize(9)
    GGender.draw(win)
 
    Ggenderline = Line(Point(143, 65), Point(164, 65))
    Ggenderline.draw(win)
 
    GHandedness = Text(Point(205, 60), 'Handedness:')
    GHandedness.setSize(9)
    GHandedness.draw(win)
 
    Ghandednessline = Line(Point(245, 65), Point(268, 65))
    Ghandednessline.draw(win)
 
    GFrame = Text(Point(72, 90), 'Frame:')
    GFrame.setSize(9)
    GFrame.draw(win)
 
    Gframeline = Line(Point(93, 95), Point(113, 95))
    Gframeline.draw(win)
    
    GHeight = Text(Point(135, 90), 'Height:')
    GHeight.setSize(9)
    GHeight.draw(win)
 
    Gheightline = Line(Point(156, 95), Point(177, 95))
    Gheightline.draw(win)
 
    GWeight = Text(Point(200, 90), 'Weight:')
    GWeight.setSize(9)
    GWeight.draw(win)
 
    Gweightline = Line(Point(222, 95), Point(243, 95))
    Gweightline.draw(win)
 
    GCulture = Text(Point(73, 120), 'Culture:')
    GCulture.setSize(9)
    GCulture.draw(win)
 
    Gcultureline = Line(Point(97, 125), Point(166, 125))
    Gcultureline.draw(win)
   
    GHomeland = Text(Point(200, 120), 'Homeland:')
    GHomeland.setSize(9)
    GHomeland.draw(win)
 
    Ghomelandline = Line(Point(233, 125), Point(313, 125))
    Ghomelandline.draw(win)
 
    GCult = Text(Point(330, 120), 'Cult:')
    GCult.setSize(9)
    GCult.draw(win)
 
    Gcultline = Line(Point(345, 125), Point(405, 125))
    Gcultline.draw(win)
 
    GCareer = Text(Point(72, 150), 'Career:')
    GCareer.setSize(9)
    GCareer.draw(win)
 
    Gcareerline = Line(Point(95, 155), Point(178, 155))
    Gcareerline.draw(win)
 
    GSocialClass = Text(Point(217, 150), 'Social Class:')
    GSocialClass.setSize(9)
    GSocialClass.draw(win)
 
    Gsocialclassline = Line(Point(255, 155), Point(365, 155))
    Gsocialclassline.draw(win)
 
    rect01 = Rectangle(Point(40,15), Point(415, 170))
    rect01.draw(win)
 
    GLuckPoints = Text(Point(355, 55), 'Luck Points')
    GLuckPoints.setSize(13)
    GLuckPoints.draw(win)
 
    GLuckPointsCircle = Circle(Point(355, 85), 18)
    GLuckPointsCircle.setWidth(2)
    GLuckPointsCircle.draw(win)
 
 #-------------------------------------------------------------------------------
 
 #-------------------------------------------------------------------------------
 # Second box; RuneQuest, Character Notes
 #
 #-------------------------------------------------------------------------------
 
    GR = Text(Point(450, 45), 'R')
    GR.setSize(36)
    GR.draw(win)
 
    GQ = Text(Point(540, 45), 'Q')
    GQ.setSize(36)
    GQ.draw(win)
 
    Gune = Text(Point(495, 45), 'UNE')
    Gune.setSize(20)
    Gune.draw(win)
 
    Guest = Text(Point(592, 45), 'UEST')
    Guest.setSize(20)
    Guest.draw(win)
     
    GChaNotesBox = Rectangle(Point(430, 70), Point(750, 170))
    GChaNotesBox.draw(win)
 
    GCharacterNotes = Text(Point(513, 80), 'CHARACTER NOTES')
    GCharacterNotes.setSize(13)
    GCharacterNotes.draw(win)


#-------------------------------------------------------------------------------

    GChaAtt = Text(Point(375, 185), 'CHARACTERISTICS & ATTRIBUTES')
    GChaAtt.setSize(18)
    GChaAtt.draw(win)

#-------------------------------------------------------------------------------
# Characteristics Box
#
#-------------------------------------------------------------------------------

    GSTR = Text(Point(64, 195), 'STR')
    GSTR.setSize(13)
    GSTR.draw(win)
 
    GCON = Text(Point(64, 225), 'CON')
    GCON.setSize(13)
    GCON.draw(win)
 
    GSIZ = Text(Point(64, 255), 'SIZ')
    GSIZ.setSize(13)
    GSIZ.draw(win)
 
    GDEX = Text(Point(64, 285), 'DEX')
    GDEX.setSize(13)
    GDEX.draw(win)
 
    GINT = Text(Point(64, 315), 'INT')
    GINT.setSize(13)
    GINT.draw(win)
 
    GPOW = Text(Point(64, 345), 'POW')
    GPOW.setSize(13)
    GPOW.draw(win)
 
    GCHA = Text(Point(64, 375), 'CHA')
    GCHA.setSize(13)
    GCHA.draw(win)

    dist01 = 195
    for i in range(7):
        statcirc = Circle(Point(99, dist01), 12)
        statcirc.setWidth(2)
        statcirc.draw(win)
        dist01 += 30
 
    rect02 = Rectangle(Point(40, 178), Point(120, 400))
    rect02.draw(win)
    
    #while inf == 1:
        #win.getMouse()    


#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Hit Locations Box
#
#-------------------------------------------------------------------------------

    rect03 = Rectangle(Point(130 ,200), Point(440, 400))
    rect03.draw(win)
    
    HitLocations = Text(Point(200, 215), 'HIT LOCATIONS')
    HitLocations.setSize(13)
    HitLocations.draw(win)
    
    HitGuy = Polygon(Point(360, 270), Point(360, 310), Point(330, 310), Point(330, 245), Point(420, 245), Point(420, 310), Point(390, 310), Point(390, 270),
                     Point(390, 310), Point(410, 310), Point(410, 380), Point(380, 380), Point(380, 340), Point(370, 340), Point(370, 380), Point(340, 380),
                     Point(340, 310), Point(360, 310), Point(360, 270))
    HitGuy.draw(win)
    
    HitGuyHead = Rectangle(Point(357, 215), Point(393, 245))
    HitGuyHead.draw(win)
    
    HitLocationsStuff = ['R. Leg', 'L. Leg', 'Abdom.', 'Chest', 'R. Arm', 'L. Arm', 'Head']
    
    HLGuyx = [355, 395, 375, 375, 345, 405, 371]
    HLGuyy = [340, 340, 300, 252, 270, 270, 220]
    
    for i in range(7):
        atext = Text(Point(HLGuyx[i], HLGuyy[i]), HitLocationsStuff[i])
        btext = Text(Point(HLGuyx[i] - 7, HLGuyy[i] + 10), 'AP:')
        ctext = Text(Point(HLGuyx[i] - 7, HLGuyy[i] + 20), 'HP:')
        
        atext.setSize(5)
        btext.setSize(5)
        ctext.setSize(5)        

        atext.draw(win)
        btext.draw(win)
        ctext.draw(win)
    
    HitLocationsStuff2 = ['1d20', 'Armour Worn', 'ENC']
    HitLocationsStuff3 = ['1-3', '4-6', '7-9', '10-12', '13-15', '16-18', '19-20']
    
    HLtextx1 = [144, 240, 300]
    
    
    
    for i in range(3):
        atext = Text(Point(HLtextx1[i], 235), HitLocationsStuff2[i])
        atext.setSize(7)
        atext.draw(win)
    
    hly = 250
    for i in range(7):
        atext = Text(Point(145, hly), HitLocationsStuff3[i])
        btext = Text(Point(178, hly), HitLocationsStuff[i])
        atext.setSize(8)
        btext.setSize(8)
        atext.draw(win)
        btext.draw(win)
        hly += 16
    
    makelines(7, 70, 208, 255, 16, win)
    makelines(7, 25, 288, 255, 16, win)
    
    shieldtext = Text(Point(275, 365), 'Shield')
    strikepentext = Text(Point(175, 365), 'Strike Rank Penalty')
    shieldtext.setSize(7)
    strikepentext.setSize(7)
    shieldtext.draw(win) 
    strikepentext.draw(win)
    
    strikepencirc = Circle(Point(175, 384), 12)
    strikepencirc.setWidth(2)
    strikepencirc.draw(win)
    
    shieldrect = Rectangle(Point(230, 372), Point(320, 395))
    shieldrect.setWidth(2)
    shieldrect.draw(win)





#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Combat Styles Section
#
#-------------------------------------------------------------------------------

    rect04 = Rectangle(Point(450, 260), Point(750, 400))
    rect04.draw(win)

    CombatSectionStuff = ['Action', 'Points', 'Damage', 'Modifier', 'Exp', 'Modifier', 
                      'Healing', 'Rate', 'Movement', 'Rate', 'Strike', 'Rank']
    nextpos01x = 475
    nextword01 = 0


    for i in range(6):
        GCStext = Text(Point(nextpos01x, 210), CombatSectionStuff[nextword01])
        GCStext.setSize(7)
        GCStext.draw(win)
        nextword01 += 1
        GCStext = Text(Point(nextpos01x, 220), CombatSectionStuff[nextword01])
        GCStext.setSize(7)
        GCStext.draw(win)
        nextword01 += 1
        nextpos01x += 50


        dist02 = 475
        for i in range(6):
            testcirc = Circle(Point(dist02, 240), 12)
            testcirc.setWidth(2)
            testcirc.draw(win)
            dist02 += 50
        
        CombStyl = Text(Point(573, 275), 'COMBAT STYLES (STR+DEX)')
        CombStyl.setSize(12)
        CombStyl.draw(win)
        
        StylNam = Text(Point(490, 290), 'Style Name')
        StylNam.setSize(7)
        StylNam.draw(win)
        
        Per01 = Text(Point(580, 290), '%')
        Per01.setSize(7)
        Per01.draw(win)
        
        WeapInc = Text(Point(660, 290), 'Weapons Included')
        WeapInc.setSize(7)
        WeapInc.draw(win)
        
        makelines(6, 80, 465, 320, 13, win)
        makelines(6, 20, 570, 320, 13, win)
        makelines(6, 110, 620, 320, 13, win)

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Weapons Box
#
#-------------------------------------------------------------------------------

    rect05 = Rectangle(Point(40, 410), Point(750, 500))
    rect05.draw(win)

    WeaponsBoxStuff = ['Weapon', 'Damage', 'Size', 'Reach', 'AP / HP', 'Effects',
                   'ENC', 'Range', 'Load']

    WeaponsBoxIncr = [80, 200, 290, 335, 385, 445, 545, 605, 712]
    
    for i in range(9):
        atext = Text(Point(WeaponsBoxIncr[i], 420), WeaponsBoxStuff[i])
        atext.setSize(7)
        atext.draw(win)
    
    makelines(5, 108, 63, 440 , 13, win) # Weapon
    makelines(5, 85, 183, 440, 13, win) # Damage
    makelines(5, 25, 282, 440, 13, win) # Size
    makelines(5, 25, 323, 440, 13, win) # Reach
    makelines(5, 50, 368, 440, 13, win) # AP / HP
    makelines(5, 95, 428, 440, 13, win) # Effects
    makelines(5, 25, 534, 440, 13, win) # ENC
    makelines(5, 100, 590, 440, 13, win) # Range
    makelines(5, 25, 702, 440, 13, win) # Load

#-------------------------------------------------------------------------------

    SkillsInfo = ['Skill', 'Characteristics', '%']

#-------------------------------------------------------------------------------
# Standard Skills Box
#
#-------------------------------------------------------------------------------

    rect06 = Rectangle(Point(40, 510), Point(270, 900))
    rect06.draw(win)

    ssstuff = ['Skill', 'Characteristics', '%']
    ssx = [70, 155, 235]
    
    for i in range(3):
        ssy = 545
        atext = Text(Point(ssx[i], ssy), ssstuff[i])
        atext.setSize(9)
        atext.draw(win)
    
    StandSkill = Text(Point(125, 525), 'STANDARD SKILLS')
    StandSkill.setSize(13)
    StandSkill.draw(win)
    
    IncremPos02 = 565
    
    for i in range(21):
        atext = Text(Point(70, IncremPos02), StandardSkills[i])
        atext.setSize(8)
        atext.draw(win)
        IncremPos02 += 16
    
    IncremPos02 = 565
    
    for i in StandardSkills:
        askill = '(' + str(StandardSkillsParams[i][0]) + ' + ' + str(StandardSkillsParams[i][1]) + ')'
        atext = Text(Point(155, IncremPos02), askill)
        atext.setSize(8)
        atext.draw(win)
        IncremPos02 += 16
    
    makelines(21, 25, 225, 565, 16, win)

#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Professional Skills Box
#
#-------------------------------------------------------------------------------

    rect07 = Rectangle(Point(280, 510), Point(500, 780))
    rect07.draw(win)
    
    ProffSkill = Text(Point(385, 525), 'PROFESSIONAL SKILLS')
    ProffSkill.setSize(13)
    ProffSkill.draw(win)
    
    psx = [310, 405, 475]
    
    for i in range(3):
        atext = Text(Point(psx[i], 545), ssstuff[i])
        atext.setSize(9)
        atext.draw(win)
    
    makelines(8, 65, 290, 570, 16, win)
    makelines(8, 45, 383, 570, 16, win)
    makelines(8, 25, 463, 570, 16, win)
    
    
    
    pslx = [323, 410, 475]
    plstuff = ['Languages', '(INT + CHA)', '%']
    
    for i in range(3):
        atext = Text(Point(pslx[i], 700), plstuff[i])
        atext.setSize(9)
        atext.draw(win)
    
    makelines(3, 139, 293, 725, 16, win)
    makelines(3, 25, 463, 725, 16, win)


#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Passions Box
#
#-------------------------------------------------------------------------------

    rect08 = Rectangle(Point(280, 790), Point(500, 900))
    rect08.draw(win)
    
    Passions = Text(Point(385, 807), 'PASSIONS (POW+CHA)')
    Passions.setSize(13)
    Passions.draw(win)
    
    passion1text = Text(Point(318, 828), "Passion")
    passion1text.setSize(9)
    passion1text.draw(win)

    passion2text = Text(Point(475, 828), "%")
    passion2text.setSize(9)
    passion2text.draw(win)
    
    makelines(4, 139, 293, 848, 16, win)
    makelines(4, 25, 463, 848, 16, win)

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Magic Points Box
#
#-------------------------------------------------------------------------------

    rect09 = Rectangle(Point(510, 510), Point(750, 580))
    rect09.draw(win)
    
    MagicPoints = Text(Point(578, 525), 'MAGIC POINTS')
    MagicPoints.setSize(13)
    MagicPoints.draw(win)
    
    mpx = [525]
    
    for i in range(12):
        mp = Text(Point(int(mpx[0]), 545), str(i))
        mp.setSize(7)
        mpx[0] = int(mpx[0]) + 19
        mp.draw(win)
    
    mpx = [525]
    
    for i in range(12, 24):
        mp = Text(Point(int(mpx[0]), 565), str(i))
        mp.setSize(7)
        mpx[0] = int(mpx[0]) + 19
        mp.draw(win)
    

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Magic Skills Box
#
#-------------------------------------------------------------------------------

    rect10 = Rectangle(Point(510, 590), Point(750, 760))
    rect10.draw(win)
    
    MagicSkills = Text(Point(578, 605), 'MAGIC SKILLS')
    MagicSkills.setSize(13)
    MagicSkills.draw(win)
    
    msx = [540, 645, 725] # 95, 70
    
    for i in range(3):
        atext = Text(Point(msx[i], 625), ssstuff[i])
        atext.setSize(9)
        atext.draw(win)
    
    makelines(7, 70, 520, 648, 16, win)
    makelines(7, 50, 620, 648, 16, win)
    makelines(7, 25, 715, 648, 16, win)    


#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Fatigue Box
#
#-------------------------------------------------------------------------------

    rect10 = Rectangle(Point(510, 770), Point(750, 900))
    rect10.draw(win)
    
    Fatigue = Text(Point(555, 785), 'FATIGUE')
    Fatigue.setSize(13)
    Fatigue.draw(win)
    
    fatiguestuff = ['Current Level', 'Skills', 'Move', 'Strike Rank', 'Action Points']
    
    fsy = 810
    for i in range(5):
        atext = Text(Point(550, fsy), fatiguestuff[i])
        atext.setSize(8)
        atext.draw(win)
        fsy += 18
    
    makelines(5, 135, 600, 816, 18, win)
    
    
    writecharacter(win, charactersheet)
    
    while inf == 1:
        win.getMouse()    





#-------------------------------------------------------------------------------




#-------------------------------------------------------------------------------
# Purpose: To put the values on the character sheet
# Syntax: writecharacter(win)
#
#
#-------------------------------------------------------------------------------

def writecharacter(win, charactersheet):
    

#-------------------------------------------------------------------------------
# Characteristics Box
#-------------------------------------------------------------------------------


    wccby = 195
    
    for i in range(7):
        atext = Text(Point(99, wccby), str(charactersheet.playercharacteristics[Characteristics[i]]))
        atext.setSize(8)
        atext.setTextColor('blue')
        atext.draw(win)
        wccby += 30

#-------------------------------------------------------------------------------
# Standard Skills Box
#-------------------------------------------------------------------------------

    wcssy = 560
    
    for i in range(21):
        atext = Text(Point(237, wcssy), str(charactersheet.PlayerSkills[StandardSkills[i]]))
        atext.setSize(8)
        atext.setTextColor('blue')
        atext.draw(win)
        wcssy += 16




#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Hit Locations
#
#-------------------------------------------------------------------------------

    hlcy = [360, 272, 320, 290, 290, 240, 360]
    hlcx = [358, 378, 378, 348, 408, 374, 398]
    for i in range(7):
        atext = Text(Point(hlcx[i], hlcy[i]), charactersheet.maxhitpoints[i])
        atext.setSize(5)
        atext.setTextColor("blue")
        atext.draw(win)
        
        



#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Magic Points
#
#-------------------------------------------------------------------------------
    
    mptest = charactersheet.playercharacteristics['POW']
    if mptest >= 0 and mptest < 12:
        mpx = 525 + (mptest * 19)
        mpy = 545
        acirc = Circle(Point(mpx, mpy), 9)
        acirc.setOutline("blue")
        acirc.draw(win)
    elif mptest >= 12:
        mpx = 525 + ((mptest-12) * 19)
        mpy = 565
        acirc = Circle(Point(mpx, mpy), 9)
        acirc.setOutline("blue")
        acirc.draw(win)
        



#-------------------------------------------------------------------------------
# write character sheet to a text file
#
#-------------------------------------------------------------------------------

def characterTextFile(charactersheet):
    textfile = charactersheet.name + ".txt"
    file = open(textfile, "w")
    
    file.write(charactersheet.name + "\n")
    file.write(charactersheet.careername + "\n" + "\n")
    
    file.write("-----------------------------------------------------------------" + "\n")
    file.write("STR: " + str(charactersheet.playercharacteristics["STR"]) + "\n")
    file.write("CON: " + str(charactersheet.playercharacteristics["CON"]) + "\n")
    file.write("SIZ: " + str(charactersheet.playercharacteristics["SIZ"]) + "\n")
    file.write("DEX: " + str(charactersheet.playercharacteristics["DEX"]) + "\n")
    file.write("INT: " + str(charactersheet.playercharacteristics["INT"]) + "\n")
    file.write("POW: " + str(charactersheet.playercharacteristics["POW"]) + "\n")
    file.write("CHA: " + str(charactersheet.playercharacteristics["CHA"]) + "\n")
    file.write("-----------------------------------------------------------------" + "\n")
    file.write("Action Points: " + str(charactersheet.actionpoints) + "\n")
    file.write("Damage Modifier: " + str(charactersheet.damagemodifier) + "\n")
    file.write("EXP Modifier: " + str(charactersheet.expmodifier) + "\n")
    file.write("Healing Rate: " + str(charactersheet.healingrate) + "\n")
    file.write("Movement Rate: " + str(charactersheet.movementrate) + "\n")
    file.write("Strike Rank: " + str(charactersheet.strikerank) + "\n")
    file.write("Magic Points: " + str(charactersheet.magicpoints) + "\n")
    file.write("Luck Points: " + str(charactersheet.luckpoints) + "\n")
    file.write("-----------------------------------------------------------------" + "\n")
    for i in range(21):
        file.write(str(StandardSkills[i]) + ": " + str(charactersheet.PlayerSkills[StandardSkills[i]]) + "\n")
    
    file.write("-----------------------------------------------------------------" + "\n")
    for i in range(len(charactersheet.NonStandard)):
        file.write(str(charactersheet.NonStandard[i]) + ": " + str(charactersheet.PlayerSkills[charactersheet.NonStandard[i]]) + "\n")
    
    
    file.write("-----------------------------------------------------------------" + "\n")
    
    file.write("Head HP: " + str(charactersheet.maxhitpoints[0]) + "\n")
    file.write("Chest HP: " + str(charactersheet.maxhitpoints[1]) + "\n")
    file.write("Abdomen HP: " + str(charactersheet.maxhitpoints[2]) + "\n")
    file.write("Right Arm HP: " + str(charactersheet.maxhitpoints[3]) + "\n")
    file.write("Left Arm HP: " + str(charactersheet.maxhitpoints[4]) + "\n")
    file.write("Right Leg HP: " + str(charactersheet.maxhitpoints[5]) + "\n")
    file.write("Left Leg HP: " + str(charactersheet.maxhitpoints[6]) + "\n")
    file.write("-----------------------------------------------------------------" + "\n")
    
    file.close()    



# self.PlayerSkills[StandardSkills[0]]
'''
        self.actionpoints = calcActionPoints(self.playercharacteristics['INT'], self.playercharacteristics['DEX'])
        self.damagemodifier = calcDamageModifier(self.playercharacteristics['STR'], self.playercharacteristics['SIZ'])
        self.expmodifier = calcExpModifier(self.playercharacteristics['CHA'])
        self.healingrate = calcHealingRate(self.playercharacteristics['CON'])
        self.maxhitpoints = calcHitPoints(self.playercharacteristics['CON'], self.playercharacteristics['SIZ'])
        self.movementrate = 6
        self.strikerank = calcStrikeRank(self.playercharacteristics['INT'], self.playercharacteristics['DEX'])
        self.magicpoints = self.playercharacteristics['POW']
        self.luckpoints = calcLuckPoints(self.playercharacteristics['POW'])
'''












#*******************************************************************************
class CharacterSheetAUTO:
    
    def __init__(self):
        
        
        #-----------------------------------------------------------------------
        # Step 1: The Characteristics
        # - The first thing we need to do is figure out what characteristics the
        # player will have. We can do this one of three ways: preset values
        # determined by the user, randomly rolled, or point buy.
        #-----------------------------------------------------------------------
        
        Characteristics = ['STR', 'CON', 'SIZ', 'DEX', 'INT', 'POW', 'CHA']
        self.playercharacteristics = {}
        self.name = 'Test'
        test01 = 'N'
        
        # Method 1: Preset Characteristics:
        #-----------------------------------------------------------------------
        if test01 == 'Y':
            for char in Characteristics:
                x = int(input('please enter your value for ' + str(char) + ': '))
                self.playercharacteristics[char] = x
        #-----------------------------------------------------------------------
        
        elif test01 == 'N':
            
            test02 = 'N'
            
            # Method 2: Randomly Rolled
            #-------------------------------------------------------------------
            if test02 == 'N':
                Str = threeDsix()
                print('STR: ' + str(Str))
                time.sleep(1)
                Con = threeDsix()
                print('CON: ' + str(Con))
                time.sleep(1)                
                Siz = twoDsix() + 6
                print('SIZ: ' + str(Siz))
                time.sleep(1)                
                Dex = threeDsix()
                print('DEX: ' + str(Dex))
                time.sleep(1)                
                Int = twoDsix() + 6
                print('INT: ' + str(Int))
                time.sleep(1)                
                Pow = threeDsix()
                print('POW: ' + str(Pow))
                time.sleep(1)                
                Cha = threeDsix()
                print('CHA: ' + str(Cha))
                time.sleep(1)                
                nums = [Str, Con, Siz, Dex, Int, Pow, Cha]
                x = 0
                for char in Characteristics:
                    self.playercharacteristics[char] = nums[x]
                    x += 1
            #-------------------------------------------------------------------
            
            # Method 3: Point Buy
            #-------------------------------------------------------------------
            elif test02 == 'Y':
                self.playercharacteristics['STR'] = 3
                self.playercharacteristics['CON'] = 3
                self.playercharacteristics['SIZ'] = 8
                self.playercharacteristics['DEX'] = 3
                self.playercharacteristics['INT'] = 8
                self.playercharacteristics['POW'] = 3
                self.playercharacteristics['CHA'] = 3
                cmax = 18
                points = 49
                print('STR: ' + str(self.playercharacteristics['STR']))
                print('CON: ' + str(self.playercharacteristics['CON']))
                print('SIZ: ' + str(self.playercharacteristics['SIZ']))
                print('DEX: ' + str(self.playercharacteristics['DEX']))
                print('INT: ' + str(self.playercharacteristics['INT']))
                print('POW: ' + str(self.playercharacteristics['POW']))
                print('CHA: ' + str(self.playercharacteristics['CHA']))
                print('you have ' + str(points) + ' left to spend')                
                while points != 0:
                    chosenchar = str(input('which characteristic would you like to improve? (STR, CON, SIZ, DEX, INT, POW, CHA): '))
                    if chosenchar not in Characteristics:
                        print('please choose a valid characteristic from the options provided')
                        continue
                    amount = int(input('by how much? '))
                    if (points - amount) < 0:
                        print('not enough points')
                        continue
                    if (self.playercharacteristics[chosenchar] + amount) > cmax:
                        print('The amount you requested will exceed the maximum; choose another number')
                        continue
                    self.playercharacteristics[chosenchar] = self.playercharacteristics[chosenchar] + amount
                    points = points - amount
                    print('STR: ' + str(self.playercharacteristics['STR']))
                    print('CON: ' + str(self.playercharacteristics['CON']))
                    print('SIZ: ' + str(self.playercharacteristics['SIZ']))
                    print('DEX: ' + str(self.playercharacteristics['DEX']))
                    print('INT: ' + str(self.playercharacteristics['INT']))
                    print('POW: ' + str(self.playercharacteristics['POW']))
                    print('CHA: ' + str(self.playercharacteristics['CHA']))
                    print('you have ' + str(points) + ' left to spend')
                print('All points have been spent, and your characteristics are now complete')
            #-------------------------------------------------------------------
            
        #-----------------------------------------------------------------------
        # Skills
        #
        #
        #-----------------------------------------------------------------------
        
        self.PlayerSkills = {}
        self.PlayerSkills[StandardSkills[0]] = (self.playercharacteristics['STR'] + self.playercharacteristics['DEX']) #Athletics
        self.PlayerSkills[StandardSkills[1]] = (self.playercharacteristics['STR'] + self.playercharacteristics['CON']) #Boating
        self.PlayerSkills[StandardSkills[2]] = (self.playercharacteristics['STR'] + self.playercharacteristics['SIZ']) #Brawn
        self.PlayerSkills[StandardSkills[3]] = (self.playercharacteristics['DEX'] + self.playercharacteristics['POW']) #Conceal
        self.PlayerSkills[StandardSkills[4]] = (self.playercharacteristics['INT'] + self.playercharacteristics['INT']) #Customs
        self.PlayerSkills[StandardSkills[5]] = (self.playercharacteristics['DEX'] + self.playercharacteristics['CHA']) #Dance
        self.PlayerSkills[StandardSkills[6]] = (self.playercharacteristics['INT'] + self.playercharacteristics['CHA']) #Deciet
        self.PlayerSkills[StandardSkills[7]] = (self.playercharacteristics['DEX'] + self.playercharacteristics['POW']) #Drive
        self.PlayerSkills[StandardSkills[8]] = (self.playercharacteristics['CON'] + self.playercharacteristics['CON']) #Endurance
        self.PlayerSkills[StandardSkills[9]] = (self.playercharacteristics['DEX'] + self.playercharacteristics['DEX']) #Evade
        self.PlayerSkills[StandardSkills[10]] = (self.playercharacteristics['INT'] + self.playercharacteristics['DEX']) #First Aid
        self.PlayerSkills[StandardSkills[11]] = (self.playercharacteristics['CHA'] + self.playercharacteristics['CHA']) #Influence
        self.PlayerSkills[StandardSkills[12]] = (self.playercharacteristics['INT'] + self.playercharacteristics['POW']) #Insight
        self.PlayerSkills[StandardSkills[13]] = (self.playercharacteristics['INT'] + self.playercharacteristics['INT']) #Locale
        self.PlayerSkills[StandardSkills[14]] = (self.playercharacteristics['INT'] + self.playercharacteristics['POW']) #Perception
        self.PlayerSkills[StandardSkills[15]] = (self.playercharacteristics['DEX'] + self.playercharacteristics['POW']) #Ride
        self.PlayerSkills[StandardSkills[16]] = (self.playercharacteristics['POW'] + self.playercharacteristics['CHA']) #Sing
        self.PlayerSkills[StandardSkills[17]] = (self.playercharacteristics['INT'] + self.playercharacteristics['DEX']) #Stealth
        self.PlayerSkills[StandardSkills[18]] = (self.playercharacteristics['STR'] + self.playercharacteristics['CON']) #Swim
        self.PlayerSkills[StandardSkills[19]] = (self.playercharacteristics['STR'] + self.playercharacteristics['DEX']) #Unarmed
        self.PlayerSkills[StandardSkills[20]] = (self.playercharacteristics['POW'] + self.playercharacteristics['POW']) #Willpower
        
        #-----------------------------------------------------------------------
        # Action points, strike rank, etc:
        #
        #-----------------------------------------------------------------------
        
        self.actionpoints = calcActionPoints(self.playercharacteristics['INT'], self.playercharacteristics['DEX'])
        self.damagemodifier = calcDamageModifier(self.playercharacteristics['STR'], self.playercharacteristics['SIZ'])
        self.expmodifier = calcExpModifier(self.playercharacteristics['CHA'])
        self.healingrate = calcHealingRate(self.playercharacteristics['CON'])
        self.maxhitpoints = calcHitPoints(self.playercharacteristics['CON'], self.playercharacteristics['SIZ'])
        self.movementrate = 6
        self.strikerank = calcStrikeRank(self.playercharacteristics['INT'], self.playercharacteristics['DEX'])
        self.magicpoints = self.playercharacteristics['POW']
        self.luckpoints = calcLuckPoints(self.playercharacteristics['POW'])
            

        #-----------------------------------------------------------------------
        # Picking a Culture
        #-----------------------------------------------------------------------
        
        self.culturalskills = {}        
        self.culture = 1

# Civilized --------------------------------------------------------------------
        if self.culture == 1:
            self.culture = "Civilized"
            for i in range(len(CivilizedSS)):
                self.culturalskills[CivilizedSS[i]] = 0
            for i in range(len(CivilizedPS)):
                print(str(i) + "=" + str(CivilizedPS[i]))
            cond = 0
            while cond == 0:
                a = 1
                b = 2
                c = 3
                if a == b or a == c or c == b:
                    print("Cannot choose the same skill twice. Try again.")
                    continue
                if a >= len(CivilizedPS) or b >= len(CivilizedPS) or c >= len(CivilizedPS) or a < 0 or b < 0 or c < 0:
                    print("One of your choices is not a valid number. Try again.")
                    continue
                print("Well Done!")
                self.culturalskills[CivilizedPS[a]] = 0
                self.culturalskills[CivilizedPS[b]] = 0
                self.culturalskills[CivilizedPS[c]] = 0
                self.PlayerSkills[CivilizedPS[a]] = (self.playercharacteristics[ProfessionalSkillsParams[CivilizedPS[a]][0]] + self.playercharacteristics[ProfessionalSkillsParams[CivilizedPS[a]][1]])
                self.PlayerSkills[CivilizedPS[b]] = (self.playercharacteristics[ProfessionalSkillsParams[CivilizedPS[b]][0]] + self.playercharacteristics[ProfessionalSkillsParams[CivilizedPS[b]][1]])
                self.PlayerSkills[CivilizedPS[c]] = (self.playercharacteristics[ProfessionalSkillsParams[CivilizedPS[c]][0]] + self.playercharacteristics[ProfessionalSkillsParams[CivilizedPS[c]][1]])
                cond = 1
# Barbarian --------------------------------------------------------------------
        elif self.culture == 2:
            self.culture = "Barbaric"
            check2 = int(input("1 for Boating, 2 for Ride: "))
            if check2 == 1:
                self.culturalskills['Boating'] = 0
            elif check2 == 2:
                self.culturalskills['Ride'] = 0
            for i in range(len(BarbarianSS)):
                self.culturalskills[BarbarianSS[i]] = 0
            for i in range(len(BarbarianPS)):
                print(str(i) + "=" + str(BarbarianPS[i]))
            cond = 0
            while cond == 0:
                a = int(input("Enter the number that corresponds to the skill you want. Pick 3: "))
                b = int(input("Pick another one: "))
                c = int(input("One more: "))
                if a == b or a == c or c == b:
                    print("Cannot choose the same skill twice. Try again.")
                    continue
                if a >= len(BarbarianPS) or b >= len(BarbarianPS) or c >= len(BarbarianPS) or a < 0 or b < 0 or c < 0:
                    print("One of your choices is not a valid number. Try again.")
                    continue
                print("Well Done!")
                self.culturalskills[BarbarianPS[a]] = 0
                self.culturalskills[BarbarianPS[b]] = 0
                self.culturalskills[BarbarianPS[c]] = 0
                self.PlayerSkills[BarbarianPS[a]] = (self.playercharacteristics[ProfessionalSkillsParams[BarbarianPS[a]][0]] + self.playercharacteristics[ProfessionalSkillsParams[BarbarianPS[a]][1]])
                self.PlayerSkills[BarbarianPS[b]] = (self.playercharacteristics[ProfessionalSkillsParams[BarbarianPS[b]][0]] + self.playercharacteristics[ProfessionalSkillsParams[BarbarianPS[b]][1]])
                self.PlayerSkills[BarbarianPS[c]] = (self.playercharacteristics[ProfessionalSkillsParams[BarbarianPS[c]][0]] + self.playercharacteristics[ProfessionalSkillsParams[BarbarianPS[c]][1]])
                cond = 1
# Nomadic ----------------------------------------------------------------------
        elif self.culture == 3:
            self.culture = "Nomadic"
            cond1 = 0
            # + 2 of the following: Athletics, Boating, Swim, Drive, or Ride
            while cond1 == 0:
                a1 = int(input("Pick 1 of the following: 1 for Athletics, 2 for Boating, 3 for Swim, 4 for for Ride \n>>"))
                a2 = int(input("Pick another, different one of the following: 1 for Athletics, 2 for Boating, 3 for Swim, 4 for for Ride \n>>"))
                if a1 == a2:
                    print("Two of the same, try again \n")
                    continue
                if a1 == 1 or a2 == 1:
                    self.culturalskills['Athletics'] = 0
                if a1 == 2 or a2 == 2:
                    self.culturalskills['Boating'] = 0
                if a1 == 3 or a2 == 3:
                    self.culturalskills['Swim'] = 0
                if a1 == 4 or a2 == 4:
                    self.culturalskills['Ride'] = 0
                cond1 = 1
            for i in range(len(NomadSS)):
                self.culturalskills[NomadSS[i]] = 0
            for i in range(len(NomadPS)):
                print(str(i) + "=" + str(NomadPS[i]))
            cond = 0
            while cond == 0:
                a = int(input("Enter the number that corresponds to the skill you want. Pick 3: "))
                b = int(input("Pick another one: "))
                c = int(input("One more: "))
                if a == b or a == c or c == b:
                    print("Cannot choose the same skill twice. Try again.")
                    continue
                if a >= len(NomadPS) or b >= len(NomadPS) or c >= len(NomadPS) or a < 0 or b < 0 or c < 0:
                    print("One of your choices is not a valid number. Try again.")
                    continue
                print("Well Done!")
                self.culturalskills[NomadPS[a]] = 0
                self.culturalskills[NomadPS[b]] = 0
                self.culturalskills[NomadPS[c]] = 0
                self.PlayerSkills[NomadPS[a]] = (self.playercharacteristics[ProfessionalSkillsParams[NomadPS[a]][0]] + self.playercharacteristics[ProfessionalSkillsParams[NomadPS[a]][1]])
                self.PlayerSkills[NomadPS[b]] = (self.playercharacteristics[ProfessionalSkillsParams[NomadPS[b]][0]] + self.playercharacteristics[ProfessionalSkillsParams[NomadPS[b]][1]])
                self.PlayerSkills[NomadPS[c]] = (self.playercharacteristics[ProfessionalSkillsParams[NomadPS[c]][0]] + self.playercharacteristics[ProfessionalSkillsParams[NomadPS[c]][1]])
                cond = 1
# Primitive --------------------------------------------------------------------
        elif self.culture == 4:
            self.culture = "Primitive"
            check2 = int(input("1 for Athletics, 2 for Boating, 3 for Swim: "))
            if check2 == 1:
                self.culturalskills['Athletics'] = 0
            elif check2 == 2:
                self.culturalskills['Boating'] = 0
            elif check2 ==3:
                self.culturalskills['Swim'] = 0
            for i in range(len(PrimitiveSS)):
                self.culturalskills[PrimitiveSS[i]] = 0
            for i in range(len(PrimitivePS)):
                print(str(i) + "=" + str(PrimitivePS[i]))
            cond = 0
            while cond == 0:
                a = int(input("Enter the number that corresponds to the skill you want. Pick 3: "))
                b = int(input("Pick another one: "))
                c = int(input("One more: "))
                if a == b or a == c or c == b:
                    print("Cannot choose the same skill twice. Try again.")
                    continue
                if a >= len(PrimitivePS) or b >= len(PrimitivePS) or c >= len(PrimitivePS) or a < 0 or b < 0 or c < 0:
                    print("One of your choices is not a valid number. Try again.")
                    continue
                print("Well Done!")
                self.culturalskills[PrimitivePS[a]] = 0
                self.culturalskills[PrimitivePS[b]] = 0
                self.culturalskills[PrimitivePS[c]] = 0
                self.PlayerSkills[PrimitivePS[a]] = (self.playercharacteristics[ProfessionalSkillsParams[PrimitivePS[a]][0]] + self.playercharacteristics[ProfessionalSkillsParams[PrimitivePS[a]][1]])
                self.PlayerSkills[PrimitivePS[b]] = (self.playercharacteristics[ProfessionalSkillsParams[PrimitivePS[b]][0]] + self.playercharacteristics[ProfessionalSkillsParams[PrimitivePS[b]][1]])
                self.PlayerSkills[PrimitivePS[c]] = (self.playercharacteristics[ProfessionalSkillsParams[PrimitivePS[c]][0]] + self.playercharacteristics[ProfessionalSkillsParams[PrimitivePS[c]][1]])
                cond = 1
#-------------------------------------------------------------------------------
# Careers
#
#-------------------------------------------------------------------------------

        if self.culture == "Civilized":
            for i in range(len(CivilizedCareersN)):
                print(str(i) + "=" + CivilizedCareersN[i])
            careerinp = 23
            self.career = CivilizedCareers[careerinp]
            self.careername = CivilizedCareersN[careerinp]

        elif self.culture == "Barbaric":
            for i in range(len(BarbarianCareersN)):
                print(str(i) + "=" + BarbarianCareersN[i])
            careerinp = int(input("please pick the career you wish to be, based on the number that corresponds to it: \n>>"))
            self.career = BarbarianCareers[careerinp]
            self.careername = BarbarianCareersN[careerinp]

        elif self.culture == "Nomadic":
            for i in range(len(NomadCareersN)):
                print(str(i) + "=" + NomadCareersN[i])
            careerinp = int(input("please pick the career you wish to be, based on the number that corresponds to it: \n>>"))
            self.career = NomadCareers[careerinp]
            self.careername = NomadCareersN[careerinp]

        elif self.culture == "Primitive":
            for i in range(len(PrimitiveCareersN)):
                print(str(i) + "=" + PrimitiveCareersN[i])
            careerinp = int(input("please pick the career you wish to be, based on the number that corresponds to it: \n>>"))
            self.career = PrimitiveCareers[careerinp]
            self.careername = PrimitiveCareersN[careerinp]
        
        self.profskills = {}
        for i in range(len(self.career[0])):
            if self.career[0][i] not in StandardSkills:
                self.PlayerSkills[self.career[0][i]] = (self.playercharacteristics[ProfessionalSkillsParams[self.career[0][i]][0]] + self.playercharacteristics[ProfessionalSkillsParams[self.career[0][i]][1]])
        for i in range(len(self.career[0])):
            self.profskills[self.career[0][i]] = 0

        for i in range(len(self.career[1])):
            print(str(i) + "=" + str(self.career[1][i]))
            condp = 0
        while condp == 0:
            a = 1
            b = 2
            c = 3
            if a == b or a == c or c == b:
                print("Cannot choose the same skill twice. Try again.")
                continue
            if a >= len(self.career[1]) or b >= len(self.career[1]) or c >= len(self.career[1]) or a < 0 or b < 0 or c < 0:
                print("One of your choices is not a valid number. Try again.")
                continue
            print("Well Done!")
            self.profskills[self.career[1][a]] = 0
            self.profskills[self.career[1][b]] = 0
            self.profskills[self.career[1][c]] = 0
            self.PlayerSkills[self.career[1][a]] = (self.playercharacteristics[ProfessionalSkillsParams[self.career[1][a]][0]] + self.playercharacteristics[ProfessionalSkillsParams[self.career[1][a]][1]])
            self.PlayerSkills[self.career[1][b]] = (self.playercharacteristics[ProfessionalSkillsParams[self.career[1][b]][0]] + self.playercharacteristics[ProfessionalSkillsParams[self.career[1][b]][1]])
            self.PlayerSkills[self.career[1][c]] = (self.playercharacteristics[ProfessionalSkillsParams[self.career[1][c]][0]] + self.playercharacteristics[ProfessionalSkillsParams[self.career[1][c]][1]])
            condp = 1
        checkcs = 'Y'
        if checkcs == 'Y':
            self.culturalskills['Combat StyleC'] = 0
            self.PlayerSkills['Combat StyleC'] = (self.playercharacteristics['STR'] + self.playercharacteristics['DEX'])

#-------------------------------------------------------------------------------
# Distribution of points
#
#-------------------------------------------------------------------------------

# Professional Points ----------------------------------------------------------
        profpoints = 100
        theseskills = ['Combat Style1', 'Combat Style2', 'Endurance', 'Evade', 'Athletics', 'Brawn', 'Unarmed']
        skillsnums = [15, 15, 15, 15, 15, 15, 10]
        i = 0
        while profpoints > 0:
            for key in self.profskills:
                print("key: %s , value: %s" % (key, self.profskills[key]))
            print("You have " + str(profpoints) + " left to spend.")
            profcheck = theseskills[i]
            profnamecheck = 0
            for key in self.profskills:
                if profcheck == key:
                    profnamecheck = 1
                    if self.profskills[profcheck] == 15:
                        print("cannot raise this skill any further with proffesional points. Try again")
                        continue
                    profincrem = skillsnums[i]
                    if self.profskills[profcheck] + profincrem > 15:
                        print("Cannot increase skill by that much, as it exceed # of proffesional points \nfor that skill. Try again")
                        time.sleep(1)
                        continue
                    if profpoints - profincrem < 0:
                        print("Not enough proffessional points in the pool to spend that much. Try again")
                        time.sleep(1)
                        continue
                    checkvar = self.PlayerSkills.get(profcheck)
                    if checkvar == None:
                        self.PlayerSkills[profcheck] = (self.playercharacteristics[ProfessionalSkillsParams[profcheck][0]] + self.playercharacteristics[ProfessionalSkillsParams[profcheck][1]])
                    self.profskills[profcheck] += profincrem
                    self.PlayerSkills[profcheck] += profincrem
                    profpoints -= profincrem
                    i += 1
                    continue
            if profnamecheck == 0:
                print("not a valid skill name, try again")
                time.sleep(1)
                continue

# Cultural Points --------------------------------------------------------------
        cultpoints = 100
        i = 0
        theseskills2 = ['Combat StyleC', 'Willpower', 'Deceit', 'Conceal', 'Influence']
        skillsnums2 = [10, 10, 10, 10, 5]
        for key in self.culturalskills:
            self.culturalskills[key] += 5
            self.PlayerSkills[key] += 5
            cultpoints -=5
        while cultpoints > 0:
            for key in self.culturalskills:
                print("key: %s , value: %s" % (key, self.culturalskills[key]))
            print("You have " + str(cultpoints) + " left to spend.")
            cultcheck = theseskills2[i]
            cultnamecheck = 0
            for key in self.culturalskills:
                if cultcheck == key:
                    cultnamecheck = 1
                    if self.culturalskills[cultcheck] == 15:
                        print("cannot raise this skill any further with proffesional points. Try again")
                        continue
                    cultincrem = skillsnums2[i]
                    if self.culturalskills[cultcheck] + cultincrem > 15:
                        print("Cannot increase skill by that much, as it exceed # of culture points \nfor that skill. Try again")
                        time.sleep(1)
                        continue
                    if cultpoints - cultincrem < 0:
                        print("Not enough culture points in the pool to spend that much. Try again")
                        time.sleep(1)
                        continue
                    self.culturalskills[cultcheck] += cultincrem
                    self.PlayerSkills[cultcheck] += cultincrem
                    cultpoints -= cultincrem
                    i += 1
                    continue
            if cultnamecheck == 0:
                print("not a valid skill name, try again")
                time.sleep(1)
                continue       

# Free Points ------------------------------------------------------------------
        theseskills3 = ['Combat Style1', 'Combat Style2', 'Endurance', 'Evade', 'Athletics', 'Brawn', 'Unarmed', 'Combat StyleC', 'Willpower', 'Deceit']
        skillsnums3 = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
        freepoints = 150
        i = 0
        self.freeskills = {}
        for key in self.PlayerSkills:
            self.freeskills[key] = 0
        while freepoints > 0:
            for key in self.freeskills:
                print("key: %s , value: %s" % (key, self.freeskills[key]))
            print("You have " + str(freepoints) + " left to spend.")
            freecheck = theseskills3[i]
            freenamecheck = 0
            for key in self.freeskills:
                if freecheck == key:
                    freenamecheck = 1
                    if self.freeskills[freecheck] == 15:
                        print("cannot raise this skill any further with proffesional points. Try again")
                        continue
                    freeincrem = skillsnums3[i]
                    if self.freeskills[freecheck] + freeincrem > 15:
                        print("Cannot increase skill by that much, as it exceed # of culture points \nfor that skill. Try again")
                        time.sleep(1)
                        continue
                    if freepoints - freeincrem < 0:
                        print("Not enough culture points in the pool to spend that much. Try again")
                        time.sleep(1)
                        continue
                    self.freeskills[freecheck] += freeincrem
                    self.PlayerSkills[freecheck] += freeincrem
                    freepoints -= freeincrem
                    i += 1
                    continue
            if freenamecheck == 0:
                print("not a valid skill name, try again")
                time.sleep(1)
                continue            
#-------------------------------------------------------------------------------
# Calculating non-standard skills ----------------------------------------------
        self.NonStandard = []
        for key in self.PlayerSkills:
            if key not in StandardSkills:
                self.NonStandard.append(key)

#dustin = CharacterSheetAUTO()
