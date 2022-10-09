import requests
import argparse as argp
from bs4 import BeautifulSoup

# Websites:
# Price: Flipkart, Amazon, eBay, Walmart
# Info: Wikipedia
class ParseWebsites:
    """
        Parsing the e-commerce websites:  Amazon, Flipkart, eBay and Walmart 
        to find the best price of an item
        and getting the link of the same to make purchase
    """

    def __init__(self, _query, _flipkart = True, _amazon = True, _ebay = True, _walmart = True, ) -> None:
        self.query = _query
        self.flipkart = _flipkart
        self.amazon = _amazon
        self.ebay = _ebay
        self.walmart = _walmart
    
    def get_from_src(self,src) -> BeautifulSoup:
        try:
            req = requests.get(src).text
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.TooManyRedirects:
            pass
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        return BeautifulSoup(req, 'lxml')

    def get_info(self) -> str:
        # info about product:
        pass

    def get_prices(self) -> dict:

        res = {}

        if self.flipkart:
            # Price from Flipkart: 
            url = 'https://www.flipkart.com/search?q=' + '+'.join(self.query.split())
            soup = self.get_from_src(url)
            try:
                res['Flipkart'] = [soup.body.div.div.contents[2].div.contents[1].contents[1].div.div.div.a.contents[1].contents[0].div.text,
                                soup.body.div.div.contents[2].div.contents[1].contents[1].div.div.div.a.contents[1].contents[1].div.div.div.text,
                                'https://www.flipkart.com' + soup.body.div.div.contents[2].div.contents[1].contents[1].div.div.div.a['href']]
            except Exception as e:
                print(e)
                res['Flipkart'].append()
        
        if self.amazon:
            # Price from Amazon:
            url = 'https://www.amazon.com/s?k=' + '+'.join(self.query.split())
            soup = self.get_from_src(url)
            try:
                res['Amazon'] = []
            except:
                res['Amazon'] = []
        return res

if __name__=='__main__':

    inp = input('Write a Product Name:')
    pw = ParseWebsites(inp)
    print('Details: ',pw.get_info())
    for website,price in pw.get_prices().items():
        print(website,': ',price,sep='')