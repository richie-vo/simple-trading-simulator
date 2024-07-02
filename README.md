Welcome to the Simple Trading Simulator, a Python-based tool designed to test the effectiveness of risk management strategies in trading. This simulator allows users to evaluate the performance of their trading strategies when paired with custom risk management strategies.

## Features

- **Simulate Trades**: Run simulations for a specified number of trades.
- **Risk Management**: Calculate and adjust risk per trade based on current capital.
- **Performance Metrics**: Track and display key performance metrics, including win/loss count, longest win/loss streaks, maximum drawdown, and maximum profit run-up.
- **Capital Visualization**: Plot capital change over time.
- **Logging**: Log simulation results with timestamps for future reference.

## Getting Started

### Prerequisites

- Python 3.x
- Matplotlib (for plotting)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/richie-vo/simple-trading-simulator.git
    cd repository
    ```

2. **Install dependencies:**

    Install the required packages using pip:

    ```bash
    pip install matplotlib
    ```

### Running the Simulator

To run the simulator, execute the `main` function in the Python script:

```bash
python trading_simulator.py
```

Follow the prompts to enter the number of trades, initial capital, win rate, risk-reward ratio, and risk per trade. You can also choose whether to display the results of each trade.

## Usage

### Parameters

- **Number of Trades**: The number of trades to simulate.
- **Initial Capital**: The starting amount of capital.
- **Win Rate**: The percentage of trades that result in a win.
- **Risk-Reward Ratio**: The ratio of the amount won in a winning trade to the amount lost in a losing trade.
- **Risk Per Trade**: The percentage of total capital risked on each trade.
- **Display Trades**: Option to display the result of each trade.

### Example

```
How many trades would you want to simulate?
>> 100
Enter your initial capital
>> $10000
Enter the win rate % of your strategy
>> 55
Enter the risk reward ratio of your strategy
>> 2
Enter the % of total capital risking each trade
>> 1
Do you want to display EVERY trade?
'y' for yes
'n' for no
>> n
```

## Results

The simulator provides the following metrics after the simulation:

- Number of wins and losses
- Longest win and loss streaks
- Maximum profit run-up during a single win streak
- Maximum drawdown
- Final capital
- Return on Investment (ROI)

A graph showing capital change over the number of trades is also displayed.

## Logging

Each simulation run is logged with a timestamp in the `log.txt` file, including all the key metrics and parameters.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create an issue or submit a pull request.

## Acknowledgments

Thank you for using the Simple Trading Simulator! We hope it helps you develop and refine your trading strategies.
