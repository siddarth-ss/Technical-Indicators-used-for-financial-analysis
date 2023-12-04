# Technical_Indicators

The Moving Averages and Candlestick Plotting Package provides a collection of technical indicators commonly used in financial analysis. 
This package aims to make it easy for traders and analysts by offering a set of tools for analyzing time series data, which include Simple Moving Average (SMA), 
Exponential Moving Average (EMA), Relative Strength Index (RSI), Autoregressive Moving Average (ARMA) models, and candlestick plotting.

## Design
The package consists of Two classes and Five Functions. Existing libraries like NumPy, pandas, and Matplotlib are used for data manipulation and visualization.

### Class: Moving_Averages

###### Function: (1) `simple_moving_average`
`simple_moving_average` calculates the average price of a security over a specified time period, using the below:

![image](https://user-images.githubusercontent.com/67727487/233853607-04499faf-89a8-4ba6-ab20-d2e9392276b6.png)

###### Function: (2) `exponential_moving_average`
`exponential_moving_average` calculates a similar average, but gives more weight to recent prices, using the below:

![image](https://user-images.githubusercontent.com/67727487/233853723-58b1027d-e345-481b-a83d-8e3a4f75b5ac.png)

###### Function: (3) `relative_strength_index`
- The `relative_strength_index` calculates the strength of a security's price trend by comparing the average gains to the average losses over a specified time period, using the below:

![image](https://user-images.githubusercontent.com/67727487/233853677-d92da374-2a9c-4076-ba31-a655dd9eafd5.png)


###### Function: (4) `autoregressive_moving_average`
- The `autoregressive_moving_average` estimates the parameters of an autoregressive moving average (ARMA) model using the Yule-Walker equations, using the below:

![image](https://user-images.githubusercontent.com/67727487/233854354-6561d532-5671-4a6c-b578-ba7607bdf05b.png)


### Class: CandlestickPlot

###### Function: (5) `CandlestickPlot`
- The `candlestick_plot` generate a candlestick plot. Users can adjust the data input and plot parameters as needed

Each class has a method that accepts historical price data and returns the corresponding indicator values.

## Usage
To use the package, users can first install it using pip. They can then import the classes they need from the package and create an instance of the desired class. They can then call the method of the instance to calculate the corresponding indicator values.

## Discussion
Compared to similar libraries in Python, this package provides a more comprehensive set of tools for financial analysis. It is also designed to be user-friendly and easy to use, making it accessible to both novice and advanced users. One possible improvement to the package could be to include additional technical indicators commonly used in financial analysis to overcome the large dataset problem. However, the current set of indicators should be sufficient for most use cases.

## References
- [NumPy](http://www.numpy.org)
- [pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Statsmodels](https://www.statsmodels.org/stable/index.html)
- ProjectPro. "How to Build ARIMA Model in Python", ProjectPro,
https://www.projectpro.io/article/how-to-build-arima-model-in-python/544. Accessed
23 April 2023
- Alpharithms. "Relative Strength Index (RSI) in Python." Alpharithms, 27 Aug. 2021,
https://www.alpharithms.com/relative-strength-index-rsi-in-python-470209/
- GeeksforGeeks. "How to Calculate Moving Average in a Pandas Dataframe."
geeksforgeeks.org, 18 June 2021, https://www.geeksforgeeks.org/how-to-calculatemoving-average-in-a-pandas-dataframe/
- Plotly - Candlestick Charts in Python, https://plotly.com/python/candlestick-charts/
- Technical Analysis, https://www.investopedia.com/technical-analysis-4689657
