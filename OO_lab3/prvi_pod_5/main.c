#include "myfactory.h"

#include <stdio.h>
#include <stdlib.h>

typedef char const* (*PTRFUN)();

struct Animal{
  PTRFUN* vtable;
  // vtable entries:
  // 0: char const* name(void* this);
  // 1: char const* greet();
  // 2: char const* menu();
};

// parrots and tigers defined in respective dynamic libraries

//Prevodenje:
// gcc main.c myfactory.c -ldl
// gcc -shared -fPIC tiger.c -o tiger.so
// gcc -shared -fPIC parrot.c -o parrot.so
// ./a.out tiger parrot parrot tiger....

void animalPrintGreeting(struct Animal* animal) {
    printf("%s pozdravlja: %s\n", animal->vtable[0](animal), animal->vtable[1]());
}

void animalPrintMenu(struct Animal* animal) {
    printf("%s voli %s\n", animal->vtable[0](animal), animal->vtable[2]());
}

int main(int argc, char *argv[]){
  for (int i=1; i<argc; ++i){
    int size_needed;
    VOIDFUN constructor=(VOIDFUN)myfactory(argv[i], &size_needed);
    if (!constructor){
      printf("Creation of plug-in object %s failed.\n", argv[i]);
      continue;
    }
    char obj[size_needed];
    (*constructor)((void*)obj, "Modrobradi");
    struct Animal* a = (struct Animal*)obj;


    animalPrintGreeting(a);
    animalPrintMenu(a);
  }
}