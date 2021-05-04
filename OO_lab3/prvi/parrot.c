#include <stdlib.h> 
typedef char const* (*PTRFUN)();

struct Parrot{
  PTRFUN* vtable;
  const char* name_;
};

char const* Parrot_name(void* this) {
    struct Parrot* p = (struct Parrot*)this;
    return p->name_;
}

char const* Parrot_greet() {
    return "Chrip Chrip";
}

char const* Parrot_menu() {
    return "Sjemenke";
}

PTRFUN PARROT_VTABLE[3] = { Parrot_name, Parrot_greet, Parrot_menu };

void constructParrot(struct Parrot* t, char const* name) {
    t->vtable = PARROT_VTABLE;
    t->name_ = name;
}

void* create(char const* name) {
    struct Parrot* p = (struct Parrot*)malloc(sizeof(struct Parrot*));
    constructParrot(p, name);
    return (void*)p;
}


