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

#include "prim.h"
#define MAX(x, y) ((x) > (y) ? (x) : (y))



// Absolute value function
int ABS(int x) { ((x) >= 0) ? (x) : (x *= -1); return x; }


/*******************************************************************************
 *                         Calculate Distance                                  *
 * -takes two points in a cartesian plane and finds the distance between them  *
 *******************************************************************************/

int calcDistance(int x1, int x2, int y1, int y2) {

  int x = x1 - x2;
  int y = y1 - y2;

  x = ABS(x);
  y = ABS(y);

  return x + y;
}


/*******************************************************************************
 *                          Tie Breaker Function                               *
 * -resolves "ties"; when two distances between points are the same            *
 *******************************************************************************/
int tieBreaker(int i, int j, int pi, int pj, struct point *p) {

  // If the total vertical distances are not the same, then we check and see
  // which pair of points has the greater vertical distance
  if (ABS(p[i].y - p[pi].y) != ABS(p[j].y - p[pj].y)) {
    if (ABS(p[i].y - p[pi].y) > ABS(p[j].y - p[pj].y))
      return i;
    else
      return j;
  }

  // If the greatest x value is not the same amongst both pairs of points, then
  // we check and see which pair has the biggest x value
  if (MAX(p[pi].x, p[i].x) != MAX(p[pj].x, p[j].x)) {
    if (MAX(p[pi].x, p[i].x) > MAX(p[pj].x, p[j].x))
      return i;
    else
      return j;
  }

  // otherwise, we check to see which point has a lower index
  return ((i < j) ? i : j);
  
  
}

/*******************************************************************************
 *                        Re-Calculate Distances                               *
 * -updates parents of points based on new parent information                  *
 *******************************************************************************/

void recalcDistances(int test, int num_pt, struct point *p) {

  for (int i = 0; i < num_pt; i++) {

    // compute the distances between the old parent and the point with the potential new
    // parent(test) and the point
    int p1 = calcDistance(p[i].x, p[test].x, p[i].y, p[test].y);
    int p2 = calcDistance(p[i].x, p[p[i].parent].x, p[i].y, p[p[i].parent].y);
    
    // if the point is the same as the test, then we skip it
    if (i == test)
      ;

    // otherwise, we check to see if the new potential parent's distance to the point
    // is less than the original parent's distance to the point
    else
      if (p1 == p2)
	p[i].parent = tieBreaker(test, p[i].parent, i, i, p);
      else if (p1 < p2)
	p[i].parent = test;
  }

}

/*******************************************************************************
 *                Minimum Spanning Tree Function                               *
 * -creates the data for the minimum spanning tree                             *
 *******************************************************************************/
void minSpanTree(FILE *fp, FILE *fo, int *edges, struct point *p, int num_pt) {

  char color_tree[num_pt];
  bool done = false;
  bool all_black, start = true;
  int tempdist;
  int t_length = 0;

  fprintf(fo, "Choosing point 0 as the root ...\n");
  
  // initialize the parents
  for (int i = 1; i < num_pt; i++)
    p[i].parent = 0;
  
  // initialize the tree and set all points to 'w'
  color_tree[0] = 'b';
  for (int i = 1; i < num_pt; i++)
    color_tree[i] = 'w';

  // 3 important variables for the coming while loop
  int j = 0;
  int mindist = 0;
  int minpoint;
  
  // now we start iterating through our points to create a tree
  while (!done) {

    // until we check, assume "all black" to be true
    all_black = true;
    

    // now, we check to see if all the values are black, AND we re-check our
    // distances based on new parent information.
    for (int i = 0; i < num_pt; i++) {

      // if we come across a white point, then we check to see if it's going to have
      // the smallest edge in this "round"
      if (color_tree[i] == 'w') {

	// now we calc the distance between this point and it's parent, store
	// it in a temp variable
	tempdist = calcDistance(p[i].x, p[p[i].parent].x, p[i].y, p[p[i].parent].y);
	//##printf("$$$Point_%d -> Point_%d = %d\n", parents[i], i, tempdist);

	// if this is the first time going through the points of this for-loop, we have
	// to print some things to the console
	if (start)
	  fprintf(fo, "point %d has a distance %d to the tree, parent 0;\n", i, tempdist);

	// if mindist is 0, then it hasn't been set yet and this is the first iteration;
	// so we set it to the first computed distance that we have
	if (mindist == 0){
	  mindist = tempdist;
	  minpoint = i;
	}

	// next, we check to see if there is a tie that needs resolving
	else if (mindist == tempdist)
	  minpoint = tieBreaker(i, minpoint, p[i].parent, p[minpoint].parent, p);

	// otherwise, we check to see which is smaller
	else {

	  // if the temp point is smaller, we make that the new point
	  if (tempdist < mindist) {
	    minpoint = i;
	    mindist = tempdist;
	  }

	  // otherwise, we keep what we have
	  else
	    ;
	}
      }

    }

    // If this is the first iteration and there's only one black point (the root, point 0) then
    // we print a comment line to both the file and standard output
    if (start){
      fprintf(fo, "#Edges of the MST by Prim’s algorithm:\n");
      fprintf(fp, "#Edges of the MST by Prim’s algorithm:\n");
    }

    // whichever point "won" the minimum, we connect to that point, setting
    // it to 'b' and making it a parent. We also add the newly connectd point
    // to our edges array
    color_tree[minpoint] = 'b';
    edges[j] = p[minpoint].parent;
    edges[j+1] = minpoint;
    edges[j+2] = mindist;
    t_length += mindist;

    fprintf(fp, "%d\t%d\t%d\n", edges[j], edges[j+1], edges[j+2]);
    fprintf(fo, "%d\t%d\t%d\n", edges[j], edges[j+1], edges[j+2]);
    
    #ifdef DEBUG
    printf("Point_%d -> Point_%d =  %d\n",
	   edges[j], edges[j+1], edges[j+2]);
    printf("Total length(so far): %d\n", t_length);
    #endif

    // we increment j by 3, reset the mindist, and set the start flag to
    // false in preparation for the next round of the for-loop
    j += 3;
    mindist = 0;
    start = false;

    // we then check to see if all of the points are black
    for (int i = 0; i < num_pt; i++) {
      if (color_tree[i] == 'w')
	all_black = false;
      
      // if we come across a parent, we re-calculate distances
      else if (color_tree[i] == 'b')
	recalcDistances(i, num_pt, p);
    }

    
    // if all the points in the tree are black, then we are done
    if (all_black) {
      fprintf(fo, "The total length of the MST is %d.\n", t_length);
      break;
    }

  }

}
