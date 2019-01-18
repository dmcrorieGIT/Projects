/*
0;136;0cCMPUT 201 Assignment #1

Submitting student: Dustin McRorie
Collaborating classmates: None
Other collaboraters: None
References: www.stackoverflow.com/questions/8013471/how-to-use-rand-to-generate-numbers-in-a-range

Also used framework code for file reading given in lecture slides
*/


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#include "instance.h"

/*******************************************************************************
 *                                Build Array                                  *
 * -returns an array of values from 0 to the number of the first parameter     *
 *  given: 0, 1, 2, 3, ..., num_pos                                            *
 *******************************************************************************/
void buildArray(int num_pos, int *array) {

  #ifdef DEBUG
  printf("Building array...\n");
  #endif
  
  int i;
  for (i = 0; i < num_pos; i++) {
    array[i] = i;
  }

  #ifdef DEBUG
  printf("Building done\n");
  #endif
}


/*******************************************************************************
 *                               Shuffle Array                                 *
 * -shuffles the values of a 1-D array                                         *
 *******************************************************************************/
void shuffleArray(int num_pos, int array[num_pos]){

  #ifdef DEBUG
  printf("Shuffling array...\n");
  #endif
  
  srand(time(NULL));
  int i, k, r1, r2;

  for (i = 0; i < num_pos; i++){
    r1 = rand() % num_pos;
    r2 = rand() % num_pos;
    k = array[r1];
    array[r1] = array[r2];
    array[r2] = k;
  }

  #ifdef DEBUG
  printf("Shuffling done\n");
  #endif

}


/*******************************************************************************
 *                        Generate Instances                                   *
 * -generates instaces with random data based on values entered by the user    *
 ****************************************************************************0***/
int generateInstances () {
  int *array;
  int **pointarray;
  int max_x, max_y, num_pt, num_inst;

  // gather data from the user about:
  // 1. the max x and max y coordinates
  // 2. the number of points per file
  // 3. the number of instances to generate
  printf("Generating random instances...\n");
  printf("Enter the circuit board size MAX_X MAX_Y: ");
  if ((scanf("%d %d", &max_x, &max_y)) == 0)
    return -31;
  printf("Enter the number of points NUM_PT: ");
  if ((scanf("%d", &num_pt)) == 0)
    return -32;
  printf("Enter the number of random instances to be generated: ");
  if ((scanf("%d", &num_inst)) == 0)
    return -33;

  // initializing 'name' and 'buffer' strings for later use with filenames,
  // and initializes number of possible points based on given max_x and max_y values
  char name[30] = {'i', 'n', 's', 't', 'a', 'n', 'c', 'e'};
  char buffer[10];
  int num_pos = (max_x+1)*(max_y+1);

  // if the number of possible points is less than the number of points the user
  // wants per file, then it will be impossible for all the points in the file to be
  // unique, and so the instances cannot be generated
  if (num_pos < num_pt) {
    printf("Error in generating instances!\n");
    return -34;
  }

  // further sets up the 'name' variable for later filenaming use
  snprintf(buffer, 10, "%d", num_pt);
  strcat(name, buffer);
  strcat(name, "_");

  int i, k, j = 0;

  // alocates memory for the (probably) massive pointarray, to
  // help prevent memory leaks
  pointarray = malloc(num_pos * sizeof(int*));
  for (i = 0; i < num_pos; i++)
    pointarray[i] = malloc(2 * sizeof(int));

  // allocates the position array, and then builds the array with values
  // from 0, 1, 2, 3, ..., num_pos
  array = (int *)malloc(num_pos * sizeof(int));
  buildArray(num_pos, &array[0]);

  // creates every possible point within the boudaries of
  // the given max_x and max_y values
  #ifdef DEBUG
  printf("Initializing pointarray...\n");
  #endif
  for (i = 0; i <= max_x; i++) {
    for (k = 0; k <= max_y; k++) {
      pointarray[j][0] = i;
      pointarray[j][1] = k;
      j++;
    }
    
  }

  // generate files based on user's inputs, repeatedly
  // opens files and writes to them based on the number of
  // instances the user has enetered
  for (i = 0; i < num_inst; i++) {

    // creates and concatenates string to be used as the filename
    char rname[30] = {};
    strncpy (rname, name, 30);
    snprintf(buffer, 10, "%d", i+1);
    strcat(rname, buffer);
    strcat(rname, ".txt");

    // opens the file and writes the max x and y coordinateds, as
    // well as the number of points in the first two lines of the file
    FILE *fp;
    fp = fopen(rname, "w");
    fprintf(fp, "%d %d\n", max_x, max_y);
    fprintf(fp, "%d\n", num_pt);

    // shuffles the position array, then uses these shuffled values to
    // print values from the point possibilities pseudo-randomly to the file 
    shuffleArray(num_pos, array);
    for (k = 0; k < num_pt; k++) {	
      fprintf(fp, "%d %d\n", pointarray[array[k]][0], pointarray[array[k]][1]);
    }

    // close file and print the generation success of the file
    fclose(fp);
    printf("%s generated\n", rname);
  }

  // frees the malloc'd memory for pointarray from the heap
  for (i = 0; i < num_pos; i++)
    free(pointarray[i]);
  free(pointarray);
  
  return 1;

}
