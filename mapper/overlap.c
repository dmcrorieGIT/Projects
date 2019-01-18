#include <stdio.h>
#include "prim.h"
#include "overlap.h"



void overlap(struct point *p, int point)
{
  // First, we check horizontal - vertical
  int i, temp;
  int bounds[2] = {p[point].y, p[point].y};
  
  for (i = 0; i <= p[point].num_children; i++)
    {
      // trick to get the parent in this loop
      if (i == p[point].num_children)
	temp = p[point].parent;
      else
	temp = p[point].child[i];
      
      // Case 1: boundary is 0
      if (bounds[0] == bounds[1])
	{
	  extendBounds(bounds, p[temp].y);
	}

      // Case 2: the y is within the bounds
      else if ( (p[temp].y >= bounds[0]) || p[temp].y <= bounds[1])
	{
	  p[point].overlap_hv += ABS(p[temp].y - p[point].y);
	}

      // Case 3: The y is outside the bounds
      else
	{

	// We first check to see if there is any portion of the y that
	// is within the bounds
	if ( (p[temp].y > bounds[1]) && (bounds[1] >= p[point].y) )
	  {
	    p[point].overlap_hv += (bounds[1] - p[point].y);
	    extendBounds(bounds, p[temp].y);
	  }

	// We do the same for the lower bounds
	if ( (p[temp].y < bounds[0]) && (bounds[0] <= p[point].y) )
	  {
	    p[point].overlap_hv += (p[point].y - bounds[0]);
	    extendBounds(bounds, p[temp].y);
	  }
	
	}
    }

  // Reset the bounds
  bounds[0] = p[point].x;
  bounds[1] = p[point].x;
  // Now we check vertical - horizontal
  for (i = 0; i <= p[point].num_children; i++)
    {
      // trick to get the parent in this loop
      if (i == p[point].num_children)
	temp = p[point].parent;
      else
	temp = p[point].child[i];
      
      // Case 1: boundary is 0
      if (bounds[0] == bounds[1])
	{
	  extendBounds(bounds, p[temp].x);
	}

      // Case 2: the y is within the bounds
      else if ( (p[temp].x >= bounds[0]) || p[temp].x <= bounds[1])
	{
	  p[point].overlap_vh += ABS(p[temp].x - p[point].x);
	}

      // Case 3: The y is outside the bounds
      else
	{

	// We first check to see if there is any portion of the y that
	// is within the bounds
	if ( (p[temp].x > bounds[1]) && (bounds[1] >= p[point].x) )
	  {
	    p[point].overlap_vh += (bounds[1] - p[point].x);
	    extendBounds(bounds, p[temp].x);
	  }

	// We do the same for the lower bounds
	if ( (p[temp].y < bounds[0]) && (bounds[0] <= p[point].y) )
	  {
	    p[point].overlap_vh += (p[point].x - bounds[0]);
	    extendBounds(bounds, p[temp].x);
	  }
	
	}
    }

  
}

void extendBounds(int a[], int new_value)
{
  if (new_value < a[0])
    a[0] = new_value;

  if (new_value > a[1])
    a[1] = new_value;

}
