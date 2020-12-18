#include <iostream>

using namespace std;

int main()
{
   float x;
   cin >> x;
   float a=0,b,c;
   b= 0.25*(x)+0.5;
   int q =2;
   float delta = 0.25486;
   for(int i=0;i<=q;i++){
       c= max(a,b);
       b= (0.5)*(b+a+delta);
       a = c;
       delta = delta/4;
   }
    cout << a << endl;
    cout << b << endl;
    a= min(a,b);
    return 0;
}

// It is from a paper Approximation of Sigmoid function and the derivative Piece wise linear implementation,
