import streamlit
import pandas

streamlit.title('My Parents New Healty Diner')

streamlit.header('Breakfast Menu')
streamlit.text('π₯£ π₯ Omega 3 & Blueberry Oatmeal')
streamlit.text('π π₯Kale, Spinach & Rocket Smoothie')
streamlit.text('π Hard-Boiled Free-Range Egg')

streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
