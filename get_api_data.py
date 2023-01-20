import san
from datetime import date


# Set your API key
san.ApiConfig.api_key = 'put_your_token_here'

# Get today's date in string format
today = (date.today()).strftime('%Y-%m-%d')


# Set API to get BTC and ETH data for today's date with interval of 1 hour between metrics
def get_api_data():

    results = san.get_many(
        "price_usd",
        slugs=["bitcoin", "ethereum"],
        from_date=today,
        to_date=today,
        interval="1h"
    )

    return results
