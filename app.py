import streamlit as st
import requests


API_ENDPOINT_URL = 'https://bsextract.onrender.com/scrape-url'
# Function to send data to the API (similar to your Flask logic)
def send_data_to_api(data):
    response = requests.post(API_ENDPOINT_URL, json=data)
    return response.json()

# Streamlit UI
st.title('Product Information Form')

# Form fields
product_name = st.text_input('Product Name')
manufacturer = st.text_input('Manufacturer')
product_name = st.text_input('productName')
manufacturer = st.text_input('manufacturer')
key_claims_product = st.text_input('keyClaimsProduct')
key_claims_category = st.text_input('keyClaimsCategory')
experts = st.text_input('experts')
studies = st.text_input('studies')
other_input = st.text_input('otherInput')
urls = st.text_input('url')
# Submit button
if st.button('Submit'):
    # Prepare data
    data = {
            'productName': product_name,
            'manufacturer': manufacturer,
            'key_claims_prod':key_claims_product,
            'key_claims_category': key_claims_category,
            'experts':experts,
            'studies':studies,
            'other_input':other_input,
            'url':urls,
    }

    # Send data to API
    response_data = send_data_to_api(data)

    # Display response data
    if 'paragraphs' in response_data:
        for paragraph in response_data['paragraphs']:
            st.write(paragraph)

    if 'links' in response_data:
        for link in response_data['links']:
            st.markdown(f"[{link}]({link})")
