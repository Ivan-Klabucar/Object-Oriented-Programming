#include <dlfcn.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

typedef void (*func)();

func myfactory(char const* libname, int* size_needed) {
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
    func f_c = (func) dlsym(handle, "construct");
    if ((error = dlerror()) != NULL) {
        fputs(error, stderr);
        exit(1);
    }
    func f_s = (func) dlsym(handle, "size");
    if ((error = dlerror()) != NULL) {
        fputs(error, stderr);
        exit(1);
    }
    *size_needed = (*(int(*)())f_s)();
    return f_c;
}