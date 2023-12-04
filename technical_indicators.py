# technical_indicators.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from statsmodels.tsa.arima.model import ARIMA

class Moving_Averages:
    def __init__(self):
        pass

    def simple_moving_average(self, data, window):
        """
        Calculate the Simple Moving Average (SMA) of the given data.

        :param data: A list of historical price data.
        :param window: An integer representing the moving average window size.
        :return: A list containing the Simple Moving Averages.
        """
        if window <= 0:
            raise ValueError("Window size must be greater than 0")

        sma = []
        for i in range(len(data) - window + 1):
            sma.append(sum(data[i:i + window]) / window)
        return sma

    def exponential_moving_average(self, data, window):
        """
        Calculate the Exponential Moving Average (EMA) of the given data.

        :param data: A list of historical price data.
        :param window: An integer representing the moving average window size.
        :return: A list containing the Exponential Moving Averages.
        """
        if window <= 0:
            raise ValueError("Window size must be greater than 0")

        ema = []
        multiplier = 2 / (window + 1)
        for i in range(len(data)):
            if i == 0:
                ema.append(data[0])
            else:
                ema.append((data[i] - ema[-1]) * multiplier + ema[-1])
        return ema

    def relative_strength_index(self, data, window):
        """
        Calculate the Relative Strength Index (RSI) of the given data.

        :param data: A list of historical price data.
        :param window: An integer representing the RSI window size.
        :return: A list containing the Relative Strength Index values.
        """
        if window <= 0:
            raise ValueError("Window size must be greater than 0")

        gains = []
        losses = []

        for i in range(1, len(data)):
            change = data[i] - data[i - 1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))

        avg_gains = self.simple_moving_average(gains, window)
        avg_losses = self.simple_moving_average(losses, window)

        rsi = []
        for i in range(len(avg_gains)):
            rs = avg_gains[i] / avg_losses[i] if avg_losses[i] != 0 else float("inf")
            rsi_value = 100 - (100 / (1 + rs))
            rsi.append(rsi_value)

        return rsi

    def autoregressive_moving_average(self, data, p, q):
        """
        Fit an Autoregressive Moving Average (ARMA) model to the given data.

        :param data: A list of historical price data.
        :param p: The order of the autoregressive model.
        :param q: The order of the moving average model.
        :return: A list containing the fitted ARMA model values.
        """
        if p <= 0 or q <= 0:
            raise ValueError("Both p and q must be greater than 0")

        # Fit an ARMA model to the data
        model = ARIMA(data, order=(p, 0, q))
        model_fit = model.fit()

        # Get the fitted values
        fitted_values = model_fit.fittedvalues

        return fitted_values.tolist()

## Please make sure to install the statsmodels package if you haven't already, by running:
## pip install statsmodels

## pip install matplotlib


class CandlestickPlot:

    @staticmethod
    def plot(df, title="Candlestick Chart", xlabel="Date", ylabel="Price", date_format="%Y-%m-%d"):
        """
        Plot a candlestick chart from a DataFrame with columns: 'date', 'open', 'high', 'low', 'close'.
        :param df: DataFrame with columns: 'date', 'open', 'high', 'low', 'close'
        :param title: Title of the plot
        :param xlabel: X-axis label
        :param ylabel: Y-axis label
        :param date_format: Date format for the x-axis
        """
        # Convert dates to numbers for plotting
        df['date'] = [mdates.date2num(d) for d in df['date']]

        # Create a figure and axis
        fig, ax = plt.subplots()

        # Configure x-axis formatting
        ax.xaxis.set_major_formatter(DateFormatter(date_format))

        # Plot the candlesticks
        for idx, row in df.iterrows():
            open_price, high_price, low_price, close_price = row[['open', 'high', 'low', 'close']]
            color = 'green' if close_price >= open_price else 'red'
            ax.plot([row['date'], row['date']], [low_price, high_price], color=color)
            ax.plot([row['date'], row['date']], [open_price, close_price], color=color, linewidth=5)

        # Set plot labels and title
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)

        # Show the plot
        plt.show()

