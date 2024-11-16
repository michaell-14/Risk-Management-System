#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <random>   // For random_device, mt19937, normal_distribution
#include <ctime>    // For time()

using namespace std;

int main() {
    // Seed the random number generator
    random_device rd;
    mt19937 gen(rd());
    normal_distribution<double> d(0, 1); //d for distribution

    // Read data from CSV file
    ifstream file("retrieved_data.csv");
    string line;
    vector<double> close_prices;
    double avg_return, variance, drift, pdr_log;

    if (file.is_open()) {
        getline(file, line); // Read the header

        while (getline(file, line)) {
            stringstream ss(line);
            string value;
            getline(ss, value, ',');
            close_prices.push_back(stod(value));
        }

        // Read the other values
        file.clear();
        file.seekg(0, ios::beg);
        getline(file, line);  // Skip header
        getline(file, line);  // Read first data line
        stringstream ss(line);
        string value;
        getline(ss, value, ',');  // Skip close prices
        getline(ss, value, ',');  // Average Return
        avg_return = stod(value);
        getline(ss, value, ',');  // Variance
        variance = stod(value);
        getline(ss, value, ',');  // Drift
        drift = stod(value);
        getline(ss, value, ',');  // Price Daily Return (Log)
        pdr_log = stod(value);

        file.close();
    } else {
        cerr << "Unable to open file";
        return 1;
    }

    // Number of simulations
    const int num_simulations = 10000;
    vector<double> simulation_results;

    // Perform simulations; Geometric Brownian Motion
    for (int i = 0; i < num_simulations; ++i) {
        double ticker_std = sqrt(variance);
        double Z = d(gen); // Random number from standard normal distribution
        double S = close_prices.back() * exp(drift + ticker_std * Z);
        simulation_results.push_back(S);
    }

    // Output directory
    string output_directory = "/mnt/c/Users/micha/OneDrive/Documents/GitHub/Stocks-Project/python_files/"; // Change this to your desired directory
    string output_file_path = output_directory + "simulation_results.csv";

    // Write sim to CSV file
    ofstream output_file(output_file_path);
    if (output_file.is_open()) {
    // Write the header
        output_file << "Simulation,Predicted Price,Average Return,Log Return\n";

        // Write the data
        for (int i = 0; i < num_simulations; ++i) {
            output_file << i + 1 << "," << simulation_results[i] << "," << avg_return << "," << pdr_log << "\n";
        }

        output_file.close();
        cout << "Simulation results have been written to 'simulation_results.csv'" << endl;
    } else {
        cerr << "Unable to open file for writing";
        return 1;
    }

    return 0;
}
