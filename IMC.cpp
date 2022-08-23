#include<iostream>

using namespace std;
int main()
{
	float IMC, altura_en_m, peso_en_kg;
    cout << "Ingresa el valor de altura en m: ";
    cin >> altura_en_m;
    cin.get();
    cout << "Ingresa el valor de peso en kg: ";
    cin >> peso_en_kg;
    cin.get();
    IMC=(peso_en_kg/altura_en_m/altura_en_m);
    cout << "Valor de IMC: " << IMC << endl;
    system ("pause");
    return 0;
}
