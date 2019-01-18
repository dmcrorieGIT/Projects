steiner: steiner.o validate.o instance.o prim.o overlap.o
	gcc -Wall -std=c99 steiner.o validate.o instance.o prim.o overlap.o -o steiner

steiner.o: steiner.c steiner.h validate.h instance.h prim.h overlap.h
	gcc -Wall -std=c99 -c steiner.c

validate.o: validate.c validate.h prim.h
	gcc -Wall -std=c99 -c validate.c

instance.o: instance.c instance.h
	gcc -Wall -std=c99 -c instance.c

prim.o: prim.c prim.h
	gcc -Wall -std=c99 -c prim.c

overlap.o: overlap.c overlap.h prim.h
	gcc -Wall -std=c99 -c overlap.c

clean:
	rm *.o
