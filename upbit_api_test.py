# Coin List

# import requests

# url = "https://api.upbit.com/v1/market/all?isDetails=false"

# headers = {"Accept": "application/json"}

# response = requests.request("GET", url, headers=headers)

# print(response.text)

# 60분 전보다 몇프로 떨어진거 정렬

import requests
import matplotlib.pyplot as plt

url = "https://api.upbit.com/v1/candles/minutes/5?market=KRW-BTC&count=120"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

# print(response.text)

plt.plot(response.text)
plt.ylabel('some price')
plt.show()