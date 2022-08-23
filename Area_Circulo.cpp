#include <iostream>
#include <cmath>

using namespace std;
int main() 

{
    int radio;
    float pi=3.1416,area;
    
    cout<<"Ingrese el radio "<<endl;
    cin>>radio;
    
    area=pi*pow(radio,2);
    cout<<"El area del circulo es :"<<area<<endl;
    
    system ("pause");
    
    return 0;
}


