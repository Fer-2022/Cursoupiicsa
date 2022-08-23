#include <iostream>
#include <math.h>
using namespace std;
int main ()
{
    float apotema, area, longitud_de_lado, numero_de_lados, perimetro;
    
    cout<<"Ingresa el valor de apotema: "<<endl;
    cin>>apotema;
    
    cout<<"Ingresa el valor de longitud de lado: "<<endl;
    cin>>longitud_de_lado;
    
    cout<<"Ingresa el valor de numero de lados: "<<endl;
    cin>>numero_de_lados;
   
    perimetro=numero_de_lados*longitud_de_lado;
    area=apotema*apotema*numero_de_lados*tan(M_PI/numero_de_lados);
    printf ("Valor de area: %g\n", area);
    printf ("Valor de perimetro: %g\n", perimetro);
    
    system ("pause");
    return 0;
}

