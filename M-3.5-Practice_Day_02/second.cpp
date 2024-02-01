#include <iostream>

int main() {
    // Declare a variable to store user input
    int userInput;

    // Get input from the user
    std::cout << "Enter a number: ";
    std::cin >> userInput;

    // Display numbers in a loop up to the given number
    std::cout << "Numbers up to " << userInput << " are: " << std::endl;
    for (int i = 1; i <= userInput; ++i) {
        std::cout << i << " ";
    }

    // Print a newline at the end
    std::cout << std::endl;

    return 0;
}
