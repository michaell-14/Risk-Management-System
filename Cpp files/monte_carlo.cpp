#include <iostream>
#include <fstream> // std::ifstream; for file I/O
#include <sstream> // std::stringstream; for string manipulation
#include <string>
#include <vector>
#include <cmath>

using namespace std;
int main() {
    //Read
    ifstream file("recieved_data.csv");
    string line;
    vector<double> close_prices;
    double avg_return, variance, drift, pdr_log, pdr_simple;

    if (file.is_open()){
        getline(file, line); // read the header
        
        while (getline(file, line)){
            stringstream ss(line);
            string value;
            getline(ss, value, ',');
            close_prices.push_back(std::stod(value));
        }
    }
}
