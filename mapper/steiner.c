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

#include "steiner.h"
#include "validate.h"
#include "instance.h"
#include "prim.h"
#include "overlap.h"


/**************************************************************
                          Main Function                           
**************************************************************/
int main(int argc, char *argv[]) {

  int inputfile = 0, outputfile = 0;
  int i;
  int n = 0;
  
  // If there is only one argument given, then the user did not specify
  // an input file or an output file, so generate random instances based
  // on user inputs
  if (argc == 1) {
    generateInstances();
    return 10;
  }

  // We check to see if the "test" flag is present
  if (strcmp (argv[1], "-t") == 0) {
    test();
    return 69;
  }
    
  
  // iterate through the arguments given and find
  // the input / output files (if any)
  for (i = 1; i < argc; i++) {
    if (strcmp (argv[i], "-i") == 0)
      inputfile = i+1;
    else if (strcmp (argv[i], "-o") == 0)
      outputfile = i+1;
  }
  
  // if there was an output file given but no input
  // file, then the command line is invalid
  if ((outputfile != 0) && (inputfile == 0)) {
    printf(">%s [-i inputfile [-o outputfile]]\n", argv[0]);
    return -21;
  }

  // if there was more than one argument and there is no
  // input file, then the command line is invalid
  if ((inputfile == 0) && (argc > 1)) {
    printf(">%s [-i inputfile [-o outputfile]]\n", argv[0]);
    return -22;
  }
  
  n = fileStuff(argv[inputfile], argv[outputfile], inputfile, outputfile);
  return n;

}



/*******************************************************************************
 *                              Test Function                                  *
 * -Used for testing functionality and debugging                               *
 *******************************************************************************/
void test(void) {

  struct point p[10];

  for (int i = 0; i < 10; i++)
    {
    for (int j = 0; j < 8; j++)
      p[i].child[j] = -1;
    }
  
  p[0].index = 0;
  p[0].x = 0;
  p[0].y = 0;
  p[0].parent = -1;
  p[0].num_children = 1;
  p[0].child[0] = 9;
  p[0].overlap_hv = 0;
  p[0].overlap_vh = 0;

  p[1].index = 1;
  p[1].x = 0;
  p[1].y = 90;
  p[1].parent = 5;
  p[1].num_children = 0;
  p[1].overlap_hv = 0;
  p[1].overlap_vh = 0;

  p[2].index = 2;
  p[2].x = 70;
  p[2].y = 100;
  p[2].parent = 6;
  p[2].num_children = 0;
  p[2].overlap_hv = 0;
  p[2].overlap_vh = 0;

  p[3].index = 3;
  p[3].x = 100;
  p[3].y = 55;
  p[3].parent = 7;
  p[3].num_children = 0;
  p[3].overlap_hv = 0;
  p[3].overlap_vh = 0;

  p[4].index = 4;
  p[4].x = 30;
  p[4].y = 30;
  p[4].parent = 9;
  p[4].num_children = 2;
  p[4].child[0] = 8; p[4].child[1] = 5;
  p[4].overlap_hv = 0;
  p[4].overlap_vh = 0;

  p[5].index = 5;
  p[5].x = 30;
  p[5].y = 70;
  p[5].parent = 4;
  p[5].num_children = 1;
  p[5].child[0] = 1;
  p[5].overlap_hv = 0;
  p[5].overlap_vh = 0;

  p[6].index = 6;
  p[6].x = 70;
  p[6].y = 90;
  p[6].parent = 7;
  p[6].num_children = 1;
  p[6].child[0] = 2;
  p[6].overlap_hv = 0;
  p[6].overlap_vh = 0;

  p[7].index = 7;
  p[7].x = 70;
  p[7].y = 30;
  p[7].parent = 8;
  p[7].num_children = 2;
  p[7].child[0] = 3; p[7].child[1] = 6;
  p[7].overlap_hv = 0;
  p[7].overlap_vh = 0;

  p[8].index = 8;
  p[8].x = 50;
  p[8].y = 50;
  p[8].parent = 4;
  p[8].num_children = 1;
  p[8].child[0] = 7;
  p[8].overlap_hv = 0;
  p[8].overlap_vh = 0;

  p[9].index = 9;
  p[9].x = 45;
  p[9].y = 0;
  p[9].parent = 0;
  p[9].num_children = 1;
  p[9].child[0] = 4;
  p[9].overlap_hv = 0;
  p[9].overlap_vh = 0;

  overlap(p, 7);
  printf("HV Overlap: %d\nVH Overlap: %d\n", p[7].overlap_hv, p[7].overlap_vh);
  
  //for (int i = 0; i < 10; i++)
  //  printf("%d %d %d\n", p[i].x, p[i].y, p[i].parent);
  
}
