import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime

# Styles
st.markdown(
    """
    <style>
        .css-1v3fvcr {
            color: #193366;
        }
    </style>
    """,
    unsafe_allow_html=True
) 

# App title
st.markdown('''
# Stock Price App
The **S&P 500** Stock Market Index 
''')
st.write('---')

# Sidebar
st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start Date", datetime.date(2019, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.date(2021, 1, 31))

# Retrieving tickers data
ticker_list = pd.read_csv('ticker-data.csv')
tickerSymbol = st.sidebar.selectbox('Stock Ticker', ticker_list) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker

# Ticker information
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

string_summary = tickerData.info['longBusinessSummary']
st.info(string_summary)

string_web = tickerData.info['website']
st.write(string_web)

#st.write('---')

# Ticker data
st.header('**Ticker data**')
st.write(tickerDf)

# Bollinger bands
st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)


st.header('**Stock Volume**')
st.line_chart(tickerDf.Volume)

####
#st.write('---')
#st.write(tickerData.info)