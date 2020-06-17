#include<bits/stdc++.h>
#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

float dotprod(float *x,float *y,int n){
    float result =0.0;
    for(int i=0;i<n;i++){
        result += x[i]*y[i];
    }
 return result;
}
int main(){
     string str1;
     string str2;
     getline(cin,str1);
     getline(cin,str2);
     int k= str1.length();
     int l= str2.length();
     float x[k],y[l];
     for(int i=0;i<k;i++){
        x[i]= str1[i]-'0';
     }
     for(int i=0;i<l;i++){
         y[i]=str2[i]-'0';
     }
     int n = min(k,l);
     float result=dotprod(x,y,n);
     cout << result << endl;
return 0;
}
