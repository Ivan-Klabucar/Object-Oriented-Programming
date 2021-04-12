#include <iostream>
#include <assert.h>
#include <stdlib.h>
//NULTI

class Point{
public:
    int x; int y;
    Point() {
        x = y = 0;
    }
};

class Shape{
public:
    virtual void draw() = 0;
    virtual void move(int) = 0;
};

class Circle : public Shape{
public:
    double radius_;
    Point center_;
    virtual void draw() {
        std::cerr <<"in drawCircle\n";
    }
    virtual void move(int t) {
        center_.x += t;
        center_.y += t;
        std::cerr <<"in moveCircle\n";
    }
};

class Square : public Shape{
public:
    double radius_;
    Point center_;
    virtual void draw() {
        std::cerr <<"in drawSquare\n";
    }
    virtual void move(int t) {
        center_.x += t;
        center_.y += t;
        std::cerr <<"in moveSquare\n";
    }
};

class Rhomb : public Shape{
public:
    double rhomb_side_;
    Point center_;
    virtual void draw() {
        std::cerr <<"in drawRhomb\n";
    }
    virtual void move(int t) {
        center_.x += t;
        center_.y += t;
        std::cerr <<"in moveRhomb\n";
    }
};

void drawShapes(Shape** shapes, int n){
    for (int i=0; i<n; ++i){
        struct Shape* s = shapes[i];
        s->draw();
    }
}

void moveShapes(Shape** shapes, int n, double t) {
    for (int i=0; i<n; ++i){
        struct Shape* s = shapes[i];
        s->move(t);
    }
}

int main(){
    Shape* shapes[5];
    shapes[0]=(Shape*)new Circle;
    shapes[1]=(Shape*)new Square;
    shapes[2]=(Shape*)new Square;
    shapes[3]=(Shape*)new Circle;
    shapes[4]=(Shape*)new Rhomb;

    drawShapes(shapes, 5);
    moveShapes(shapes, 5, 2);
  }