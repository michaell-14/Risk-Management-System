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
        //other values
        file.clear();
        file.seekg(0, std::ios::beg);
        std::getline(file, line);  // Skip header
        std::getline(file, line);  // Read first data line
        std::stringstream ss(line);
        std::string value;
        std::getline(ss, value, ',');  // Skip close prices
        std::getline(ss, value, ',');  // Average Return
        avg_return = std::stod(value);
        std::getline(ss, value, ',');  // Variance
        variance = std::stod(value);
        std::getline(ss, value, ',');  // Drift
        drift = std::stod(value);
        std::getline(ss, value, ',');  // Price Daily Return (Log)
        pdr_log = std::stod(value);
        std::getline(ss, value, ',');  // Price Daily Return (Simple)
        pdr_simple = std::stod(value);

        file.close();
    } else {
        std::cerr << "Unable to open file";
        return 1;
    }
    //Simulations
    const int num_simulations = 1000;
    vector<double> simulation_results;


    //Calculations
    for (int i = 0; i < num_simulations; i++){
        double ticker_std = sqrt(variance);
        double z = ((double) rand()/RAND_MAX); // random number between 0 and 1; the (double) is to convert the rand() to a double
        double s = close_prices.back() * exp(drift + ticker_std * z);
        simulation_results.push_back(s);
    }

    // Print
    for (int i = 0; i < num_simulations; ++i) {
        cout << "Simulation " << i + 1 << ": " << simulation_results[i] << endl;
    }

    //Write
    ofstream output_file("simulation_results.csv");
    if (output_file.is_open()){
        output_file << "Simulation Results\n";
        for (int i = 0; i < num_simulations; i++){
            output_file << simulation_results[i] << "\n";
        }
        output_file.close();
    } else {
        std::cerr << "Unable to open file";
        return 1;
    }
    return 0;
}
