#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

typedef double (*PTRFUN)();

struct Unary_Function {
    PTRFUN* tvf;
    int lower_bound;
    int upper_bound;
};
typedef struct Unary_Function Unary_Function;

struct Square {
    Unary_Function base;
};
typedef struct Square Square;

struct Linear {
    Unary_Function base;
    double a;
    double b;
};
typedef struct Linear Linear;

double negative_value_at(Unary_Function* f, double x) {
    return - f->tvf[0](f, x);
}

void tabulate(Unary_Function* f) {
    for(int x = f->lower_bound; x <= f->upper_bound; x++) {
    printf("f(%d)=%lf\n", x, f->tvf[0](f, (double)x));
    }
}

bool same_functions_for_ints(Unary_Function *f1, Unary_Function *f2, double tolerance) {
    if(f1->lower_bound != f2->lower_bound) return false;
    if(f1->upper_bound != f2->upper_bound) return false;
    for(int x = f1->lower_bound; x <= f1->upper_bound; x++) {
        double delta = f1->tvf[0](f1, x) - f2->tvf[0](f2, x);
        if(delta < 0) delta = -delta;
        if(delta > tolerance) return false;
    }
    return true;
}

double value_at_Square(Square* f, double x) {
    return x*x;
}

double value_at_Linear(Linear* f, double x) {
    return f->a*x + f->b;
};

PTRFUN SQUARE_TVF[2] = { value_at_Square, negative_value_at };
PTRFUN LINEAR_TVF[2] = { value_at_Linear, negative_value_at };
PTRFUN UNARY_FUNCTION_TVF[2] = { NULL, negative_value_at };

void constructUnary_Function(Unary_Function* f, int lb, int ub) {
    f->tvf = UNARY_FUNCTION_TVF;
    f->lower_bound = lb;
    f->upper_bound = ub;
}

void constructSquare(Square* square, int lb, int ub) {
    constructUnary_Function((Unary_Function *) square, lb, ub);
    ((Unary_Function *)square)->tvf = SQUARE_TVF;
}

void constructLinear(Linear* linear, int lb, int ub, double a, double b) {
    constructUnary_Function((Unary_Function *) linear, lb, ub);
    ((Unary_Function *)linear)->tvf = LINEAR_TVF;
    linear->a = a;
    linear->b = b;
}

Square* createSquare(int lb, int ub) {
    Square* square = (Square*)malloc(sizeof(Square));
    constructSquare(square, lb, ub);
    return square;
}

Linear* createLinear(int lb, int ub, double a, double b) {
    Linear* linear = (Linear*)malloc(sizeof(Linear));
    constructLinear(linear, lb, ub, a, b);
    return linear;
}

int main(void) {
    Unary_Function *f1 = (Unary_Function *)createSquare(-2, 2);
    tabulate(f1);
    Unary_Function *f2 = (Unary_Function *)createLinear(-2, 2, 5, -2);
    tabulate(f2);
    printf("f1==f2: %s\n", same_functions_for_ints(f1, f2, 1E-6) ? "DA" : "NE");
    printf("neg_val f2(1) = %lf\n", f2->tvf[1](f2, 1.0));
    free(f1);
    free(f2);
    return 0;
}