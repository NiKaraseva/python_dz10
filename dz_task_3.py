class Stocks:

    _initial_value = {}

    def __init__(self, stocks: dict, prices: dict, current_prices: dict):
        self.stocks = stocks
        self.prices = prices
        self.current_prices = current_prices


    def calculate_portfolio_value(self) -> float:
        if len(self._initial_value) == 0:
            for key, value in self.prices.items():
                self._initial_value[key] = value
        sum_stocks = 0
        for key, value in self.stocks.items():
            sum_stocks += value * self.prices[key]
        return round(sum_stocks, 2)


    def get_most_profitable_stock(self) -> str:
        res_dict = {key: value - self._initial_value[key] for key, value in self.current_prices.items()}
        final_dict = max(res_dict.items(), key=lambda k_v: k_v[1])
        return final_dict[0]


if __name__ == "__main__":
    st = Stocks({"AAPL": 10, "GOOGL": 5, "MSFT": 8, "TSLA": 7},
                {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50, "TSLA": 253.86},
                {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50, "TSLA": 503.86})

    res_previous_value = st.calculate_portfolio_value()
    profitable_stock = st.get_most_profitable_stock()

    print(f"Общая стоимость портфеля акций = {res_previous_value}")
    print(f"Наиболее прибыльная акция = {profitable_stock}")