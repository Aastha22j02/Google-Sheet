# Connect Streamlit to a public Google Sheet
### Introduction
This guide explains how to securely access a public Google Sheet from Streamlit Community Cloud. It uses the [pandas](https://pandas.pydata.org/) library and Streamlit's [secrets management](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management).

![GSpread](https://github.com/Aastha22j02/Google-Sheet/blob/main/Image/public-gsheet-1.png)


### Add the Sheets URL to your local app secrets
Your local Streamlit app will read secrets from a file .streamlit/secrets.toml in your app's root directory. Create this file if it doesn't exist yet and add the share link of your Google Sheet to it as shown below:
#### .streamlit/secrets.toml

 

>  public_gsheets_url = https://docs.google.com/spreadsheets/d/xxxxxxx/edit#gid=0

### Copy your app secrets to the cloud
As the secrets.toml file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on Edit Secrets. Copy the content of secrets.toml into the text area. More information is available at [Secrets Management](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management).

![Secrets](https://github.com/Aastha22j02/Google-Sheet/blob/main/Image/edit-secrets.png)

### Write your Streamlit app
```bash
# streamlit_app.py

import pandas as pd
import streamlit as st

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
```



![your app should look like this](https://github.com/Aastha22j02/Google-Sheet/blob/main/Image/streamlit-app.png)

### Successfully Done!!
