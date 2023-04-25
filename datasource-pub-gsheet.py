# streamlit_app.py

import pandas as pd
import streamlit as st
sheets_url = "https://docs.google.com/spreadsheets/d/1mUrRe9SlUWKlUtt0LPmV3hgt6heyFAZr0RsHhg4mKcw/edit#gid=0"

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets['demo']["public_gsheets_url"])

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
## 2nd Public Google Sheet
#
# import streamlit as st
# import pandas as pd
#
#
# # Load data from public Google Sheet
# csv_url = 'https://docs.google.com/spreadsheets/d/1qhxNih6mJFp1YjDAoq-mdWuxUb7_-TUyo42fd8tLWsY/edit?usp=sharing'
# df = pd.read_csv(csv_url)
#
# # Display the data in Streamlit
# st.dataframe(df)


# Installing the required library
#pip install streamlit gspread pandas

# Importing the required libraries
# import gspread
# import pandas as pd
# from oauth2client.service_account import ServiceAccountCredentials
# import streamlit as st
#
# # Authenticating with the Google Sheets API
# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
# client = gspread.authorize(creds)
#
# # Accessing the public Google Sheet
# sheet = client.open('SheetName').sheet1
#
# # Fetching the data from the sheet and displaying it in the Streamlit app
# data = sheet.get_all_records()
# df = pd.DataFrame(data)
# st.write(df)
