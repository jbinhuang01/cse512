import streamlit as st
import yfinance as yf

def backtest_investment(ticker, start_date, end_date, investment_amount):
    data = yf.download(ticker, start=start_date, end=end_date)
    if len(data) == 0:
        st.error(f"No data available for {ticker} from {start_date} to {end_date}.")
        return
    initial_price = data['Close'].iloc[0]
    final_price = data['Close'].iloc[-1]
    final_value = (investment_amount / initial_price) * final_price
    st.write(f"Backtest results for {ticker} from {start_date} to {end_date}:")
    st.write(f"Initial investment amount: ${investment_amount}")
    st.write(f"Initial price: ${initial_price:.2f}")
    st.write(f"Final price: ${final_price:.2f}")
    st.write(f"Final value of investment: ${final_value:.2f}")

st.title("Stock Investment Backtester")

backtest_ticker = st.text_input("Enter a stock ticker for backtesting:")
investment_amount = st.number_input("Enter the investment amount in USD:", min_value=0.0, value=1000.0)
backtest_start_date = st.date_input("Enter the backtesting start date:")
backtest_end_date = st.date_input("Enter the backtesting end date:")

if st.button("Run Backtest"):
    if backtest_ticker and investment_amount and backtest_start_date and backtest_end_date:
        backtest_investment(backtest_ticker, str(backtest_start_date), str(backtest_end_date), investment_amount)
    else:
        st.error("Please provide all inputs.")
