#include <iostream>
using namespace std;

int main(){

    //for loop
    cout << "counting from 1 to 5" << endl;

    for(int i = 1; i <= 5; i++){
        cout << i << endl;
    }

    cout << "counting from 5 to 1" << endl;

    int i = 5;
    for(; i >= 1; i--){
        cout << i << endl;
    }

    //creates infinite loop
    for(;;){ 
        if(i > 10){
            break;
        }
        cout << "hello" << endl;
        i++;
    }

    // creates empty loop
    for(int j = 1; j <= 10; j++);{
        cout << (3 * j); //error: undeclared indetifier 'j'.
    }

    //creates empty loop
    for(int j = 1; j <= 10; j++);{ 
        cout << "hello" << endl;
    }

   return 0;
}