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

int size() {
    return sizeof(struct Parrot);
}

PTRFUN PARROT_VTABLE[3] = { Parrot_name, Parrot_greet, Parrot_menu };

void construct(void* x, char const* name) {
    struct Parrot* p = (struct Parrot*) x;
    p->vtable = PARROT_VTABLE;
    p->name_ = name;
}

void* create(char const* name) {
    struct Parrot* p = (struct Parrot*)malloc(sizeof(struct Parrot*));
    construct((void*)p, name);
    return (void*)p;
}


