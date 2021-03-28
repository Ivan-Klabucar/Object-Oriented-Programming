#include <iostream>
#include <string>
#include <vector>
#include <set>
using namespace std;


int gt_int(int f, int s) {
    if (f > s) {
        return 1;
    }
    return 0;
}

int gt_char(char f, char s) {
    if (f > s) {
        return 1;
    }
    return 0;
}

int gt_str(string f, string s) {
    if (f > s) {
        return 1;
    }
    return 0;
}

template <typename Iterator, typename Predicate>
Iterator mymax(
  Iterator first, Iterator last, Predicate pred){

    Iterator curr_max = first;
    while(first != last) {
        if(pred(*first, *curr_max)) curr_max = first;
        first++;
    }
    return curr_max;
}

int arr_int[] = { 1, 3, 5, 7, 4, 6, 9, 2, 0 };
vector<string> vec_string({ "ovca", "puz", "koala", "svizac", "puh" });
set<char> set_char({ 'a', 'f', 'd', 'x', 'w' });
string arr_str[] = { "puh", "tasmanijski vrag", "cudnovati kljunas", "krokodil" };

int main(void) {
    const int* maxint = mymax( &arr_int[0],
    &arr_int[sizeof(arr_int)/sizeof(*arr_int)], gt_int);
    cout << "Max int u arr_int: " <<*maxint <<"\n";

    vector<string>::iterator maxstr = mymax( vec_string.begin(), vec_string.end(), gt_str);
    cout << "Max string u vec_string: " << *maxstr << endl;

    set<char>::iterator maxchar = mymax( set_char.begin(), set_char.end(), gt_char);
    cout << "Max char u set_char: " << *maxchar << endl;

    string* maxstr2 = mymax( &arr_str[0],  &arr_str[sizeof(arr_str)/sizeof(*arr_str)], gt_str);
    cout << "Max string u arr_str: " << *maxstr2 << endl;
}