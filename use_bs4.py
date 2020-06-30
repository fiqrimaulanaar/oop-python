import requests
from bs4 import BeautifulSoup

url = "https://ap.iti.ac.id"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Response Code : {response.status_code}")
        soup = BeautifulSoup(response.text, features="html.parser")
        print(soup.title.string)
       # print(f"Content : {response.text}")
        print("Sukses")

except Exception as e:
    print(f"Error : {e}")

print("End Program")