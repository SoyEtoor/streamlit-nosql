import streamlit as st
import requests
import pandas as pd
import json

def post_spark_job(user, repo, job, token, code_url=None, dataset_url=None):
    # Define the API endpoint
    url = 'https://api.github.com/repos/' + user + '/' + repo + '/dispatches'
    # Define the data to be sent in the POST request
    payload = {
      "event_type": job
    }

    headers = {
      'Authorization': 'Bearer ' + token,
      'Accept': 'application/vnd.github.v3+json',
      'Content-type': 'application/json'
    }

    st.write(url)
    st.write(payload)
    st.write(headers)

    # Make the POST request
    response = requests.post(url, json=payload, headers=headers)
    return response
    
def get_spark_results(url_results):
    response = requests.get(url_results)
    st.write(response)

    if (response.status_code == 200):
        st.write(response.json())

    # Display the response in the app
    st.write(response)

st.title("Spark & streamlit")

# First section
st.header("spark-submit Job (Basic)")
github_user1 = st.text_input('Github user (Basic)', value='adsoftsito', key='github_user1')
github_repo1 = st.text_input('Github repo (Basic)', value='bigdata', key='github_repo1')
spark_job1 = st.text_input('Spark job (Basic)', value='spark', key='spark_job1')
github_token1 = st.text_input('Github token (Basic)', value='***', key='github_token1')

if st.button("POST spark submit (Basic)", key='submit1'):
    response = post_spark_job(github_user1, github_repo1, spark_job1, github_token1)
    st.write(response)

# Results section
st.header("spark-submit results")
url_results = st.text_input('URL results', value='https://raw.githubusercontent....', key='url_results')

if st.button("GET spark results", key='get_results'):
    get_spark_results(url_results)

# Second section
st.header("spark-submit Job (Advanced)")
github_user2 = st.text_input('Github user (Advanced)', value='adsoftsito', key='github_user2')
github_repo2 = st.text_input('Github repo (Advanced)', value='spark-labs', key='github_repo2')
spark_job2 = st.text_input('Spark job (Advanced)', value='spark', key='spark_job2')
github_token2 = st.text_input('Github token (Advanced)', value='***', key='github_token2')
code_url = st.text_input('Code URL', value='', key='code_url')
dataset_url = st.text_input('Dataset URL', value='', key='dataset_url')

if st.button("POST spark submit (Advanced)", key='submit2'):
    response = post_spark_job(github_user2, github_repo2, spark_job2, github_token2, code_url, dataset_url)
    st.write(response)