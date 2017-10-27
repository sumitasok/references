#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
	double x{45.765};
	int y = static_cast<int>(x);
	int b = true;
	int c = 'a';
	cout<<"x: "<<x<<endl;
	cout<<"y: "<<y<<endl;
	cout<<"b: "<<b<<endl;
	cout<<"c: "<<c<<endl;
	return 0;
}