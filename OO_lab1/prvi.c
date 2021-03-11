#include<stdio.h>
#include <stdlib.h> 

typedef char const* (*PTRFUN)();

struct Animal {
    PTRFUN* vtf_;
    char const * name_;
};

typedef struct Animal Animal;

char const* dogGreet(Animal* animal){
  return "vau!";
}
char const* dogMenu(Animal* animal){
  return "kuhanu govedinu";
}
char const* catGreet(Animal* animal){
  return "mijau!";
}
char const* catMenu(Animal* animal){
  return "konzerviranu tunjevinu";
}

PTRFUN DOG_VTABLE[2] = { dogGreet, dogMenu };
PTRFUN CAT_VTABLE[2] = { catGreet, catMenu };

void constructDog(Animal* animal, char const* name) {
    animal->vtf_ = DOG_VTABLE;
    animal->name_ = name;
}

void constructCat(Animal* animal, char const* name) {
    animal->vtf_ = CAT_VTABLE;
    animal->name_ = name;
}

Animal* createDog(char const* name) {
    Animal* animal = (Animal*)malloc(sizeof(Animal));
    constructDog(animal, name);
    return animal;
}

Animal* createCat(char const* name) {
    Animal* animal = (Animal*)malloc(sizeof(Animal));
    constructCat(animal, name);
    return animal;
}

void animalPrintGreeting(Animal* animal) {
    printf("%s pozdravlja: %s\n", animal->name_, animal->vtf_[0](animal));
}

void animalPrintMenu(Animal* animal) {
    printf("%s voli %s\n", animal->name_, animal->vtf_[1](animal));
}

Animal* createNDogs(int n, char const* names[]) {
    Animal* animal = (Animal*)malloc(n * sizeof(Animal));
    for(int i = 0; i < n; i++) {
        constructDog(animal + i, names[i]);
    }
    return animal;
}

void testAnimals(void){
  struct Animal* p1=createDog("Hamlet");
  struct Animal* p2=createCat("Ofelija");
  struct Animal* p3=createDog("Polonije");

  animalPrintGreeting(p1);
  animalPrintGreeting(p2);
  animalPrintGreeting(p3);

  animalPrintMenu(p1);
  animalPrintMenu(p2);
  animalPrintMenu(p3);

  free(p1); free(p2); free(p3);
}

int main(void) {
    testAnimals();

    // Animal na stogu
    printf("\nAnimal na stogu:\n");
    Animal dog1;
    dog1.vtf_ = DOG_VTABLE;
    dog1.name_ = "Kviki";
    animalPrintGreeting(&dog1);
    animalPrintMenu(&dog1);

    // N pasa
    printf("\n3 Psa na gomili:\n");
    char const* names[3] = { "miki", "kiki", "sliki" };
    Animal* dogs = createNDogs(3, names);
    for(int i = 0; i < 3; i++) {
        animalPrintGreeting(dogs + i);
        animalPrintMenu(dogs + i);
    }
    return 0;
}