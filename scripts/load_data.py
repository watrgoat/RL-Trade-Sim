import os
import yfinance as yf
import pandas as pd
from datetime import datetime


def fetch_and_save_data(tickers, start_date, end_date, data_dir="data"):
    """
    Fetch historical market data for the specified tickers and save to CSV.

    Parameters:
    -----------
    tickers : str or list of str
        A single stock ticker as a string or a list of stock tickers to fetch data for.
    start_date : str
        Start date for historical data in the format 'YYYY-MM-DD'.
    end_date : str
        End date for historical data in the format 'YYYY-MM-DD'.
    data_dir : str, optional
        Directory where the CSV files will be saved (default: "data").

    Returns:
    --------
    None
    """
    # Ensure tickers is a list
    if isinstance(tickers, str):
        tickers = [tickers]

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        try:
            data = yf.download(ticker, start=start_date, end=end_date)
            if data.empty:
                print(f"No data found for {ticker}. Skipping...")
                continue

            # Save data to CSV
            file_path = os.path.join(data_dir, f"{ticker}.csv")
            data.to_csv(file_path)
            print(f"Data for {ticker} saved to {file_path}.")
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")


if __name__ == "__main__":
    # Single ticker or list of tickers
    TICKERS = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN"]  # Replace with a single string for testing, e.g., "AAPL"

    # Date range
    START_DATE = "2020-01-01"
    END_DATE = datetime.now().strftime("%Y-%m-%d")  # Up to today's date

    # Directory to save data
    DATA_DIR = "data"

    # Fetch and save data
    fetch_and_save_data(TICKERS, START_DATE, END_DATE, DATA_DIR)
