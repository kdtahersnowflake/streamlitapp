import streamlit

streamlit.title('My parents new healthy Dinner')

streamlit.header('Breakfast Menu')

streamlit.text('Boiled Eggs')
streamlit.text('Omlette')

streamlit.header('Build your own fruit smoothie')

import pandas
my_fruit_list = pandas.read.csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
