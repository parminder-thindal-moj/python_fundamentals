import requests


class LimitQuery:
    # this class will keep track of the state

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        """Class keeps track of the number of times a functio nto query to an API has been run"""
        """Once it reaches the limit the decorator stops the function from executing"""
        # No @ character
        # Decorator executred hwen an instance of a class is created.
        self.limit = args[0]
        if self.count < self.limit:
            self.count += 1
            return self.func(*args, **kwargs)
        else:
            print(f"No queries left. All {self.count} queries used.")
            return


@LimitQuery
def get_coin_price(limit):
    """View the Bitcoin Price Index (BPI)"""

    url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    if url.status_code == 200:
        text = url.json()
        return f"${float(text['bpi']['USD']['rate_float']):.2f}"


print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))
