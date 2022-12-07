import os
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf

# Define main
if __name__ == "__main__":
    pass

# Resize the terminal window
if os.name == "nt":
    # Windows
    os.system("mode con: cols=72 lines=22")

# GameStop Banner
banner = """
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
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""

# Print the banner to the console
print(banner)

# Get the stock data for GameStop
gme = yf.Ticker("GME")

# Option Menu
print("1. Get the current price of GME.")
print("2. Get the historical data of GME.")
print("3. Plot the historical data of GME.")
print("4. Go to r/Superstonk.")
print("5. Exit\n")

# Get the user's choice
choice = int(input("Enter your choice: "))

# Handle the user's choice
try:
    if choice == 1:
        # Get the current price of the stock
        os.system("start python3 price.py")
        os.system("python3 main.py")

    elif choice == 2:

        # Get the historical data for the stock
        data = gme.history(period="1y")
        print(data)

        # Option
        print("\nSelect another option? (y/n)")
        option = input("Enter an option: ")
        if option == "y" or option == "Y":
            os.system("python3 main.py")

    elif choice == 3:

        # Get the historical data for the stock
        data = gme.history(period="1y")

        # Plot the data
        mpf.plot(data, type="candle", style="charles", volume=True, title="GameStop (GME)")

        # Show the plot
        plt.show()

        # Option
        print("\nSelect another option? (y/n)")
        option = input("Enter an option: ")
        if option == "y" or option == "Y":
            os.system("python3 main.py")

    elif choice == 4:

        # Open the subreddit in a new window
        os.system("start https://www.reddit.com/r/Superstonk/")

        print("\nSelect another option? (y/n)")
        option = input("Enter an option: \n")
        if option == "y" or option == "Y":
            os.system("python3 main.py")
except (KeyboardInterrupt):
    print("\nKeyboard interrupt detected. Hedgies R' Fuk.\n")
