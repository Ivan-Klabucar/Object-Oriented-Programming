#include<iostream>
using namespace std;

class B{
public:
  virtual int prva()=0;
  virtual int druga(int)=0;
};

class D: public B{
public:
  virtual int prva(){return 42;}
  virtual int druga(int x){return prva()+x;}
};

typedef int (*PTRFUN1)(void*);
typedef int (*PTRFUN2)(void*, int);

void testFunctions(B* pb) {
    void* p_to_table = *(void**)pb;
    cout << "Izaz od prva: " << ((PTRFUN1*)p_to_table)[0](pb) << endl;
    cout << "Izaz od druga: " << ((PTRFUN2*)p_to_table)[1](pb, 8) << endl;
}

int main() {
    B* b = (B*) new D();
    testFunctions(b);
    free(b);
    return 0;
}