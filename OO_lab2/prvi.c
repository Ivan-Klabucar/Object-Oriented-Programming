#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//PRVI 1.

const void* mymax(
  const void *base, size_t nmemb, size_t size,
  int (*compar)(const void *, const void *)) {
    
    const void* curr_max = base;
    for(size_t i = 1; i < nmemb; i++) {
        const void* ith_elem = (const void*)(((const char*)base) + size*i);
        if (compar(ith_elem, curr_max) == 1) {
            curr_max = ith_elem;
        }
    }
    return curr_max;
}

int gt_int(const void * f, const void * s) {
    if (*(const int*)f > *(const int*)s) {
        return 1;
    }
    return 0;
}

int gt_char(const void * f, const void * s) {
    if (*(const char*)f > *(const char*)s) {
        return 1;
    }
    return 0;
}

int gt_str(const void * f, const void * s) {
    if (strcmp(*(const char**)f, *(const char**)s) > 0) {
        return 1;
    }
    return 0;
}


int main() {
    int arr_int[] = { 1, 3, 5, 7, 4, 6, 9, 2, 0 };
    char arr_char[]="Suncana strana ulice";
    const char* arr_str[] = {
    "Gle", "malu", "vocku", "poslije", "kise",
    "Puna", "je", "kapi", "pa", "ih", "njise", "aaa"
    };

    int max_int = *(int*)mymax(arr_int, sizeof(arr_int)/sizeof(arr_int[0]), sizeof(int), gt_int);
    printf("max u arr_int: %d\n", max_int);

    char max_char = *(char*)mymax(arr_char, sizeof(arr_char)/sizeof(arr_char[0]), sizeof(char), gt_char);
    printf("max u arr_char: %c\n", max_char);

    const char* max_str = *(const char**)mymax(arr_str, sizeof(arr_str)/sizeof(arr_str[0]), sizeof(const char*), gt_str);
    printf("max u arr_str: %s\n", max_str);

    return 0;
}