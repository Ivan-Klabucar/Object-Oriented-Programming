#include <dlfcn.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

typedef void* (*func)();

void* myfactory(char const* libname, char const* ctorarg) {
    char libname_expanded[strlen(libname) + 5 + 10];
    memset(libname_expanded, '\0', sizeof(libname_expanded));
    char *error;
    strcat(libname_expanded, "./");
    strcat(libname_expanded, libname);
    strcat(libname_expanded, ".so");
    void* handle = dlopen(libname_expanded, RTLD_LAZY);
    if (!handle) {
        fputs (dlerror(), stderr);
        exit(1);
    }
    func f_ptr = (func) dlsym(handle, "create");
    if ((error = dlerror()) != NULL) {
        fputs(error, stderr);
        exit(1);
    }
    return (*f_ptr)(ctorarg);
}