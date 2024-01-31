import streamlit as st
from datetime import datetime
import pandas as pd 
df = pd.read_csv(r"G:\My Drive\Compter\Python PAIN\Movie database streamlit\10000 most popular movie.csv")
pqdf = df
pd.options.display.max_rows = 10000
st.title("Top 10,000 Most Popular Movies")
option = st.selectbox(
    'What do you want to search for?',
    ('','Title', 'Release Year', 'Rating'))
if option == 'Title':
    title = st.text_input('Movie title')
    pqdf = df.loc[df['title'] == title]
if option == 'Release Year':
    release_range = st.text_input('Release date range (start_date-end_date)')
    start_date_str, end_date_str = release_range.split('-')
    start_date = pd.to_datetime(start_date_str, infer_datetime_format=True)
    end_date = pd.to_datetime(end_date_str, infer_datetime_format=True)
    df['release_date'] = pd.to_datetime(df['release_date'],errors='coerce')
    pqdf = df.loc[(df['release_date'] >= start_date) & (df['release_date'] <= end_date)]
if option == 'Rating':
    rating_range = st.text_input('Rating range (e.g., 9-10)')
    rating_range = [float(val) for val in rating_range.split('-')]
    min_rating, max_rating = rating_range
    pqdf = df.loc[(df['vote_average'] >= min_rating) & (df['vote_average'] <= max_rating)]
st.dataframe(pqdf)