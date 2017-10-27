#include <iostream>
#include <iomanip>
using namespace std;

int main(int argc, char const *argv[])
{
	string name;
	cout<<"Enter the home owner's name: ";
	getline(cin, name);
	int price;
	cout<<"Enter the price: ";
	cin>>price;
	cin.ignore();
	cout<<setw(20)<<"House Owner"<<setw(20)<<"Price Of Home"<<setw(20)<<"Sellers cost"<<setw(20)<<"Agents commission"<<endl;
	cout<<setw(20)<<name<<setw(20)<<"$"<<price<<setw(20)<<"$"<<(price/100)*6<<setw(20)<<"$"<<(price/100)*1.5<<endl;
	return 0;
}