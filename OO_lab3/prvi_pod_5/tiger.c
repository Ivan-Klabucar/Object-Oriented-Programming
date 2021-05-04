#include <stdlib.h> 
typedef char const* (*PTRFUN)();

struct Tiger{
  PTRFUN* vtable;
  const char* name_;
};

char const* Tiger_name(void* this) {
    struct Tiger* t = (struct Tiger*)this;
    return t->name_;
}

char const* Tiger_greet() {
    return "ROAR";
}

char const* Tiger_menu() {
    return "Antilopa";
}

int size() {
    return sizeof(struct Tiger);
}

PTRFUN TIGER_VTABLE[3] = { Tiger_name, Tiger_greet, Tiger_menu };

void construct(void* x, char const* name) {
    struct Tiger* t = (struct Tiger*)x;
    t->vtable = TIGER_VTABLE;
    t->name_ = name;
}

void* create(char const* name) {
    struct Tiger* t = (struct Tiger*)malloc(sizeof(struct Tiger*));
    construct((void*)t, name);
    return (void*)t;
}


