#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    ifstream input;
    input.open("input.txt", ios::in);

    //or
    //ifstream input( "input_tst.txt", ios::in);

    //int num;
    //while(input>>num){
    //    cout<<num<<endl;
    //}

    /*
    std::string line;
while (std::getline(infile, line))
{
    std::istringstream iss(line);
    int a, b;
    if (!(iss >> a >> b)) { break; } // error

    // process pair (a,b)
}
    */

    int sum=0;
    int maxVal=0;

    int first=0, second=0, third=0;
    vector<int> vec;

    for( std::string line; getline( input, line ); )
    {
        if (line.size()==0){
            cout<<"Empty line"<<endl;
            cout<<"Sum = "<<sum<<endl;
            maxVal = std::max(sum, maxVal);
            vec.push_back(sum);

            sum=0;
         }
        else{
            sum+=stoi(line);
        }
    }

    input.close();
    cout<<"Max value: "<<maxVal<<endl;

    for (auto x : vec){
            if(x>first){
                third=second;
                second=first;
                first=x;
            }
            else if(x>second){
                third=second;
                second=x;
            }
            else if(x>third){
                third = x;
            }
            else{
                ;//do nothging
            }
    }

    cout<<"1st = "<<first<<", 2nd = "<<second<<", 3rd = "<<third<<", SUM = "<<(first+second+third)<<endl;

    cout<<"Vector size: "<<vec.size()<<endl;
    sort(vec.begin(), vec.end());

    //How to sort in descending order?
    //sort() takes a third parameter that is used to specify the order in which elements are to be sorted.
    //We can pass “greater()” function to sort in descending order. This function does comparison in a way that puts greater elements before.

    sort(vec.begin(), vec.end(), greater<int>());

    cout<<vec[0]<<", "<<vec[1]<<", "<<vec[2]<<endl;
    for (auto x : vec)
        cout << x << " ";
    cout<<endl;

    cout<<"1st = "<<vec[0]<<", 2nd = "<<vec[1]<<", 3rd = "<<vec[2]<<", SUM = "<<(vec[0]+vec[1]+vec[2])<<endl;
    return 0;
}
