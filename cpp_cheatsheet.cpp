// forrange

int a[] = { 1, 2, 3, 4 };
for (int i : a) { }

char *cp = "str";
for (char c : cp) {
	if (c == 0) break;
}

#include <string>
string s = "str";

// For

char s[] = "str";
for (char *cp = s; *cp; ++cp) {
	printf("%c", *cp);
}

for(int i = 0; i < 7; ++i) {

}

// While

do {
	++i;
} while( i < 5);

while(i < 7) {
	++i;
}

// Switch

const int iOne = 1
switch(x) {
	case iOne: // has to be a constant.
	case 2: // has to be a constant.
		puts("1");
		break;
	default:
		puts("default");
		break;
}

// Condition

if (x < y) {

} else if {

} else {

}

if (x > y)
	puts("works for single block");

z = x > y ? x : y; // ternary conditional operation.
// header file ad preprocessor conditions.

// Array
// array is a fixed sixe container
int ia[5];
ia[0] = 1;
*ia = 1;
int *ip = ia; // asign an array to another variable
*ip = 2; // asign the first element of that array
++ip; // increment the pointer to point to the next element.
*ip  = 3;
*(++ip) = 4;
int ia[4] = {1, 2, 3, 4};
// C String
char s[] = { 's', 't', 'r', 0}; // terminated with 0
char s[] = "str";

for(char * cp = s; *cp; ++cp) {

}

for(char c : s) {
	if (c == 0) break;
}


// References

int &y = x; // cannot be changed, y is a reference initialised with the address of x.
// reference is immutable.
// used in functions and classes.

// Pointers

int *ip;
ip = &x;
y = *ip;

// Variables

// strongly typed
// initialise it where it is defined
// uninitialised are dangerous

const int i = 7;

// Identifiers

// [A-Za-z]
// key words and tokens
// case sensitive
// any length - 63 chars guaranted to check, 31 - external identifiers
// _priv_identifiers
// __system_user_only

// Statement

// a unit of code. always terminated with ;.

int x;
x = 42; // assignment expression
printf("x is %d\n", x); // x here is an expression that returns the vlaue of x.
printf("x is %d\n", x = 42); // is correct

// anatomy
#include <iostream>

cout << "text";
// tokens separated by spaces.

#include <cstdio> // directive for pre processor. name of file in <>.
using namespace std; // using namespace
// std::puts("text")

int main(int argc, char const *argv[]) // main entr point for a c program. one and only one.
// int main() is legal
{
	/* code */
	puts("text");
	// no new line
	printf("text")
	return 0;
}

// line oriented comment

// Sentinal values

// for loop

for(auto i=0; i <= 1234; i ++) {
	if (i%2 != 0) {
		cout<<i<<" ";
	}

}
// do while

do {

} while(true);

// infinite loop

while(done==true);

// while loop

while(done==true) {

}
