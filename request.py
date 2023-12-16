import requests
import time



# print(res.status_code)

while True:
    res = requests.get("https://youtube.com")
    if res.status_code != 200:
        print("Website was down")
    print(res.status_code)
    time.sleep(1)