import yfinance as yf
import sqlite3

# Function to get stock price
def get_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        if not data.empty:
            return round(data['Close'].iloc[-1], 2)
        return None
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None

# Initialize database
def create_database():
    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS portfolio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            buy_price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to add stock
def add_stock():
    symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
    quantity = int(input("Enter number of shares: "))
    buy_price = float(input("Enter buy price per share: "))
    
    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO portfolio (symbol, quantity, buy_price) VALUES (?, ?, ?)", 
                   (symbol, quantity, buy_price))
    conn.commit()
    conn.close()
    print(f"{quantity} shares of {symbol} added at ${buy_price} per share.")

# Function to remove stock
def remove_stock():
    symbol = input("Enter stock symbol to remove: ").upper()
    
    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM portfolio WHERE symbol = ?", (symbol,))
    conn.commit()
    conn.close()
    print(f"{symbol} removed from portfolio.")

# Function to view portfolio
def view_portfolio():
    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()
    cursor.execute("SELECT symbol, quantity, buy_price FROM portfolio")
    stocks = cursor.fetchall()
    conn.close()

    print("\nYour Portfolio:")
    print("-" * 50)
    for stock in stocks:
        symbol, quantity, buy_price = stock
        current_price = get_stock_price(symbol)
        profit_loss = round((current_price - buy_price) * quantity, 2) if current_price else "N/A"
        print(f"{symbol} | Shares: {quantity} | Buy Price: ${buy_price} | Current Price: ${current_price} | P/L: ${profit_loss}")
    print("-" * 50)

# Menu for user input
def main():
    create_database()
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            remove_stock()
        elif choice == "3":
            view_portfolio()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()