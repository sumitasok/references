#include <iostream>
#include <string>
using namespace std;

int global = 10;

void function1(int local3)
{
	int local1 = 20;
	local1 += global;
	cout<<"from function1: "<<local1<<endl;
	cout<<"value: "<<local3<<endl;
}

int main(int argc, char const *argv[])
{
	int local2 = 30;
	local2 += global;
	cout<<"from main: "<<local2<<endl;
	function1(30);
	return 0;
}