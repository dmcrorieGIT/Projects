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

#include "validate.h"
#include "prim.h"


int fileStuff(char *infile, char *outfile, int inputfile, int outputfile);


/*******************************************************************************
 *                              File Handling                                  *
 * -reads, writes, and does error checking on files                            *
 * -also computes minimum spanning tree with the data collected                *
 *******************************************************************************/
int fileStuff(char *infile, char *outfile, int inputfile, int outputfile) {

  FILE *fp, *fo;
  int max_x, max_y, num_pt, i, k;
  struct point *p;

  // We check to see if there's an output file given in the arguments. If there is, we open
  // and write to it. Otherwise, we print the coordinates to standard out
  if (outputfile > 0) {
    if ((fo = fopen(outfile, "w")) == NULL) {
      // open file error
      return -2;
    }
  }
  // if there was no output file given, we print to standard out
  else {
    fo = stdout;
  }
  
  // check to see if the file can be opened successfully
  if ((fp = fopen(infile, "a+")) == NULL)
    return -2;

  // Scan the file for the next integer, max_x
  while (fscanf(fp, "%d", &max_x) != 1) {
    if (ferror(fp)) {
      // read error
      fclose(fp);
      return -3;
    }
    if (feof(fp)) {
      // no integer to read
      fclose(fp);
      return -4;
    }
    fscanf(fp, "%*[^\n]"); // skip the rest of line
  }

  

  // scan the file for the next integer, max_y
  while (fscanf(fp, "%d", &max_y) != 1) {
    if (ferror(fp)) {
      //read error
      fclose(fp);
      return -6;
    }
    else if (feof(fp)) {
      //no integer to read
      fclose(fp);
      return -6;
    }
    else {
      // max_y not following max_x
      fclose(fp);
      return -5;
    }
    fscanf(fp, "%*[^\n]"); //skip rest of line
  }

  // scan the file for next integer, num_pt
  while (fscanf(fp, "%d", &num_pt) != 1){
    if (ferror(fp)) {
      //read error
      fclose(fp);
      return -7;
    }
    if (feof(fp)) {
      //no integer to read
      fclose(fp);
      return -8;
    }
    fscanf(fp, "%*[^\n]"); //skip rest of line
  }

  // allocate memory for the pointers
  p = (struct point *)malloc(num_pt * sizeof(struct point));

  // initialize pointers
  for (i = 0; i < num_pt; i++)
    {
      p[i].index = i;
      p[i].x = -1;
      p[i].y = -1;
      p[i].parent = -1;
      p[i].num_children = 0;
      for (int j = 0; j < 8; j++)
	p[i].child[j] = -1;
      p[i].overlap_hv = -1;
      p[i].overlap_vh = -1;
    }

  // read the x and y coordinates of the file
  for (i = 0; i < num_pt; i++) {

    while (fscanf(fp, "%d", &p[i].x) != 1) {
      if (ferror(fp)) {
	//read error
	fclose(fp);
	return -9;
      }
      if (feof(fp)) {
	//no integer to read
	printf("Error in reading instance file!\n");
	fclose(fp);
	return -10;
      }
      fscanf(fp, "%*[^\n]"); //skip rest of line
    }

    if (fscanf(fp, "%d", &p[i].y) != 1) {
      //y_coordinate not following x_coordinate
      printf("Error in reading instance file!\n");
      fclose(fp);
      return -11;
    }
  }

  //check correctness of the x/y coordinates
  for (i = 0; i < num_pt; i++){

    //check that x or y aren't bigger than the max_x or max_y
    if (p[i].x > max_x){

      printf("Error in reading instance file!\n");
      return -12;
    }
    if (p[i].y > max_y){
      printf("Error in reading instance file!\n");
      return -13;
    }
    
    for (k = 0; k < num_pt; k++) {
      
      //check for duplicate points
      if ((k != i) && (p[i].x == p[k].x) && (p[i].y == p[k].y)){
	printf("Error in reading instance file!\n");
	return -14;
      }
    }
  }

  // We calculate the MST and append it to the input file
  int edges[(num_pt - 1) * 3];
  minSpanTree(fp, fo, edges, p, num_pt);
  fclose(fp);
  fclose(fo);

  // the allocated data for the x and y coordinates must be freed from the heap
  // before the program terminates
  free(p);
  
  return 0;
}
