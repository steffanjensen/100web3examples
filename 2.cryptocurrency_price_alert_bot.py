import requests
import time

# Set the cryptocurrency and threshold values
crypto = "BTC"
threshold = 10000

while True:
  # Get the current price of the cryptocurrency
  url = f"https://api.coinmarketcap.com/v1/ticker/{crypto}/"
  response = requests.get(url).json()
  price = float(response[0]["price_usd"])

  # Check if the price has reached the threshold
  if price >= threshold:
    # Send an alert
    send_alert(f"{crypto} price has reached ${price}!")

  # Sleep for a minute before checking the price again
  time.sleep(60)


"""
This code uses the CoinMarketCap API to retrieve the current price of the specified cryptocurrency (in this case, BTC) and checks if the price has reached the specified threshold. If the threshold is reached, an alert is sent using the send_alert function (which would need to be defined elsewhere in the code). The code then sleeps for a minute before checking the price again.

I hope this example is helpful! Let me know if you have any questions or need further clarification.
"""
