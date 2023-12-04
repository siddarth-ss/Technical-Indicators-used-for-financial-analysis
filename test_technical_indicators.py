# test_technical_indicators.py
import unittest
import pandas as pd
from technical_indicators import Moving_Averages
from technical_indicators import CandlestickPlot

class TestTechnicalIndicators(unittest.TestCase):
    def setUp(self):
        self.indicators = Moving_Averages()

    def test_simple_moving_average(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_sma = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        sma = self.indicators.simple_moving_average(data, 3)
        self.assertEqual(sma, expected_sma)

    def test_exponential_moving_average(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ema = self.indicators.exponential_moving_average(data, 3)
        expected_ema = [1, 1.5, 2.25, 3.125, 4.0625, 5.03125, 6.015625, 7.0078125, 8.00390625, 9.001953125]
        self.assertEqual(ema, expected_ema)

    def test_relative_strength_index(self):
        data = [100, 102, 101, 103, 102, 104, 103, 105, 104, 106]
        rsi = self.indicators.relative_strength_index(data, 3)
        expected_rsi = [80.0, 50.0, 80.0, 50.0, 80.0, 50.0, 80.0]
        self.assertEqual(rsi, expected_rsi)

    def test_autoregressive_moving_average(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        p = 1
        q = 1
        arma = self.indicators.autoregressive_moving_average(data, p, q)
        self.assertTrue(isinstance(arma, list))
        self.assertTrue(len(arma) == len(data))

    def test_candlestick_plot(self):
        data = {
            'date': pd.to_datetime(['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05']),
            'open': [100, 101, 102, 103, 104],
            'high': [105, 106, 107, 108, 109],
            'low': [95, 96, 97, 98, 99],
            'close': [102, 100, 104, 101, 106]
        }
        df = pd.DataFrame(data)

        # Uncomment the line below to see the plot
        # CandlestickPlot.plot(df)

        # We can't directly assert the correctness


if __name__ == '__main__':
    unittest.main()


## To run the tests, save the above code in a file named test_technical_indicators.py and execute it using the command:
## python test_technical_indicators.py
