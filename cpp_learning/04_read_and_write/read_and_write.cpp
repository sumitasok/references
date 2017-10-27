#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
	string name;
	int year;
	cout<<"Enter your name: ";
	// cin>>name;
	getline(cin, name);
	cout<<"Enter your year of birth: ";
	cin>>year;
	cin.ignore();
	cout<<name<<" is "<<2017 - year<<" years old now."<<endl;
	return 0;
}