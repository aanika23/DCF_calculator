
import xlwings as xw
import pandas as pd
import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser


def get_beta(company):
    text = urllib.parse.quote_plus(company)
    url = 'https://ca.finance.yahoo.com/quote/' + text
    headers = {"User-Agent":"Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    beta = soup.select("div span[data-reactid*='87']")[0].text
    return float(beta)

def main():
    beta = get_beta("NIO")
    print(beta)

if __name__ == "__main__":
    main()
