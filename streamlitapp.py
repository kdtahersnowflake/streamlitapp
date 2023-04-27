import streamlit

streamlit.title('My parents new healthy Dinner')

streamlit.header('Breakfast Menu')

streamlit.text('Boiled Eggs')
streamlit.text('Omlette')

streamlit.header('Build your own fruit smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("pick some fruits:", list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)
