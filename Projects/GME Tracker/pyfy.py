import os
import yfinance as yf

# Resize the terminal window
if os.name == "nt":
    # Windows
    os.system("mode con: cols=73 lines=50")

# GameStop Banner
banner = """
-------------------------------------------------------------------------

  ▄████  ▄▄▄       ███▄ ▄███▓▓█████   ██████ ▄▄▄█████▓ ▒█████   ██▓███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██░  ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   ░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██░ ██▓▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▄█▓▒ ▒
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒▒██████▒▒  ▒██▒ ░ ░ ████▓▒░▒██▒ ░  ░
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ▒▓▒░ ░  ░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░░ ░▒  ░ ░    ░      ░ ▒ ▒░ ░▒ ░     
░ ░   ░   ░   ▒   ░      ░      ░   ░  ░  ░    ░      ░ ░ ░ ▒  ░░       
      ░       ░  ░       ░      ░  ░      ░               ░ ░           
                                                                        
                                                        By: Wayahlife
-------------------------------------------------------------------------
"""

# Print the banner to the console
print(banner)

# Get the stock data for GameStop
gme = yf.Ticker("GME")

try:
    # Get the current price of the stock
    while True:
        price = gme.info["regularMarketPrice"]
        print(f"The current price of GME is ${price}")
# Handle keyboard interrupt
except KeyboardInterrupt:
    print("Keyboard interrupt detected. Hedgies R' Fuk.")
