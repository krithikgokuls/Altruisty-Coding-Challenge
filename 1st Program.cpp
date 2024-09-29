#include <iostream>
#include <vector>
#include <algorithm>
#include <climits> // Include this for INT_MAX

int maxProfit(const std::vector<int>& prices) {
    int max_profit = 0; // Initialize maximum profit
    int min_price = INT_MAX; // Start with maximum integer value for min_price

    for (int price : prices) {
        // Update the minimum price if the current price is lower
        if (price < min_price) {
            min_price = price;
        }
        // Calculate the profit if the stock were sold at the current price
        int profit = price - min_price;
        // Update the maximum profit if this profit is higher
        max_profit = std::max(max_profit, profit);
    }

    return max_profit; // Return the maximum profit
}

int main() {
    int n;
    std::cout << "Enter the number of days: ";
    std::cin >> n; // Read number of days

    std::vector<int> prices(n); // Vector to store stock prices
    std::cout << "Enter the stock prices for " << n << " days: ";
    for (int i = 0; i < n; ++i) {
        std::cin >> prices[i]; // Read each day's stock price
    }

    int result = maxProfit(prices); // Calculate maximum profit
    std::cout << result << std::endl; // Output the result

    return 0;
}

