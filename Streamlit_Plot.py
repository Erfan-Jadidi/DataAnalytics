import yfinance as yf
import plotly.graph_objs as go
import streamlit as st

btc = yf.download("BTC-USD")

fig = go.Figure(data=[go.Candlestick(
    x=btc.index,
    open=btc.Open,
    close=btc.Close,
    high=btc.High,
    low=btc.Low,
)])


st.plotly_chart(fig, use_container_width=True)