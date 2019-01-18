#ifndef PRIM_H
#define PRIM_H

#define MAX(x, y) ((x) > (y) ? (x) : (y))

struct point
{
  int index;        /* the order in the instance file              */
  int x;            /* x coordinate                                */
  int y;            /* y coordinate                                */
  int parent;       /* parent in the tree when added               */
  int num_children; /* has value 0 -- 8                            */
  int child[8];     /* point index of the child                    */
  int overlap_hv;   /* total overlap when horizontal then vertical */
  int overlap_vh;   /* total overlap when the other way            */
};

int ABS(int x);
int calcDistance(int x1, int x2, int y1, int y2);
void minSpanTree(FILE *fp, FILE *fo, int *edges, struct point *p,int num_pt);
int tieBreaker(int i, int j, int pi, int pj, struct point *p);
void recalcDistances(int test, int num_pt, struct point *p);

#endif
