from bs4 import BeautifulSoup
import requests


with open("daum.html", "r") as f:
    data = f.read()
    print(BeautifulSoup(f, 'html.parser'))
