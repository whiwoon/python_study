from requests import get
from bs4 import BeautifulSoup

url = "https://www.google.com"

response = get(url)

soup =BeautifulSoup(response.text,"html.parser")

