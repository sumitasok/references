#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	/* code */
	int aScore = 0;
	int bScore = 0;
	int scoredBy;
	do {
		cout<<"Which team scored a goal\n\t1. A team\n\t2. B team\nanything else will stop the game counter"<<endl;
		cin>>scoredBy;
		switch(scoredBy) {
			case 1:
				aScore += 1; break;
			case 2:
				bScore += 1; break;
			default:
				break;
		}
	}while(scoredBy == 1 || scoredBy == 2);
	cout<<"A team scored "<<aScore<<"\nB team scored "<<bScore<<endl;
	return 0;
}