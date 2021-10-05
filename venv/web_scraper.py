import bs4
import requests
from bs4.dammit import EncodingDetector

def scrape(url : str):
    try:
        useragent = ["Mozilla/5.0 (compatible; Googlebot/2.1; +http://google.com/bot.html)",
                     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
                     "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
                     "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"]
        headers = {"User-Agent": useragent[1]}
        search_response = requests.get(f'{url}', headers=headers)
        search_response.raise_for_status()
        html_encoding = EncodingDetector.find_declared_encoding(search_response.content, is_html=True)
        search_soup = bs4.BeautifulSoup(search_response.content, from_encoding=html_encoding, features="lxml")
        index = 0
        selection_dict = {}
        print(search_soup.prettify())

    except Exception as e:
        print(e)


if __name__ == "__main__":
    scrape("https://ca.finance.yahoo.com/quote/^gstpe")