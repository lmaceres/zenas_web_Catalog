import streamlit as st

my_cnx = st.connection("snowflake")
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.title("Hello from Snowflake:")
st.write(my_data_row)
