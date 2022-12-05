#include <iostream>
#include <fstream>
#include <string>
//#include <vector>
//#include <algorithm>
#include <sstream> //istringstream

using namespace std;

int main(){
    ifstream input;
    input.open("input.txt", ios::in);

    int score1=0;
    int score2=0;
    for( std::string line; getline( input, line ); )
    {
        std::istringstream iss(line);
        char a, b;
        if (!(iss >> a >> b)) { break; } // error

        //cout<<a<< " " << b<< endl;

        //part1
        if (b=='X') score1+=1;
        else if(b=='Y') score1+=2;
        else score1+=3;

        if( (a=='A' && b=='X') || (a=='B' && b=='Y') || (a=='C' && b=='Z')) score1+=3;
        else if((a=='C' && b=='X') || (a=='B' && b=='Z') || (a=='A' && b=='Y')) score1+=6;
        else score1+=0; //loss

        if (b=='X'){
            score2+=0;
            if (a=='A') score2+=3;
            if (a=='B') score2+=1;
            if (a=='C') score2+=2;
        }
        else if (b=='Y'){
            score2+=3;
            if (a=='A') score2+=1;
            if (a=='B') score2+=2;
            if (a=='C') score2+=3;
        }
        else if (b=='Z'){
            score2+=6;
            if (a=='A') score2+=2;
            if (a=='B') score2+=3;
            if (a=='C') score2+=1;
        }
    }


    cout<< "Part1: "<<score1<<endl;
    //14069
    cout<< "Part2: "<<score2<<endl;
    //12411 - CORRECT !!!

    input.close();

    return 0;
}
