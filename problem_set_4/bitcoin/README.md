# Bitcoin

Here’s a clear, slightly longer README for your bitcoin.py exercise:

bitcoin.py is a program that calculates the cost of buying a specified number of Bitcoins in real time, using live data from the CoinCap Bitcoin Price Index.

The script works as follows:

Expects the user to provide the number of Bitcoins to buy as a command-line argument. If the argument is missing or invalid, the program exits with an error message.

Fetches the current price of Bitcoin in USD from the CoinCap API (an API key is required).

Calculates and displays the total cost in USD to four decimal places, using commas as thousands separators.

Handles network and API errors gracefully.

This program uses the requests module for HTTP requests.
Install it first with:

 # pip install requests

Run with **python bitcoin.py** 2.5 (replace 2.5 with the number of Bitcoins you want to buy), and see the current total cost based on live market prices.
Created for a CS50 exercise on command-line arguments, API usage, and error handling.