#include<iostream>
using namespace std;

class CoolClass{
public:
  virtual void set(int x){x_=x;};
  virtual int get(){return x_;};
private:
  int x_;
};

class __attribute__((__packed__)) CoolClassPacked{
public:
  virtual void set(int x){x_=x;};
  virtual int get(){return x_;};
private:
  int x_;
};

class PlainOldClass{
public:
  void set(int x){x_=x;};
  int get(){return x_;};
private:
  int x_;
};

int main() {

    cout << "Velicina u bajtovima CoolClass: " << sizeof(CoolClass) << endl;
    cout << "Velicina u bajtovima CoolClassPacked: " << sizeof(CoolClassPacked) << endl;
    cout << "Velicina u bajtovima PlainOldClass: " << sizeof(PlainOldClass) << endl;

    cout << "Velicina void pointera u bajtovima: " << sizeof(void*) << endl;

    return 0;
}