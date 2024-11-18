# app.py
import requests
import numpy as np

def fetch_data(url):
    response = requests.get(url)
    return response.json()

def process_data(data):
    return np.mean(data)

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/posts"
    data = fetch_data(url)
    print(f"Processed Data Mean: {process_data([item['id'] for item in data])}")
