# Purpose

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.amazon.com/Council-Tool-Michigan-Pattern-Straight/dp/B000IJRISU/ref=sr_1_1?crid=1AXQVNLYQX465&dib=eyJ2IjoiMSJ9.lqHQIUaSLHQenDlmoiGB-omexOyAjczwwon15xDYFSwe6yEVHIVLBcGuIakXM_tJdPCTsxrj465rMRM64KjqiexF9XMs3oBYHu6HOt8E0ZqTtg3Hh0nNZyRp5VMOhJsEdBJJevndTrcAr1GMLIVl7xKPctSAtbsglYpSpqwF1cYIU9s1ZcWF2IvrypraEZAOhLdd0OvN8QvEqZD4E9V7ohlDGiZ4pjFWqIjXklieDD_K6k3DfpHezXdY6TmxTc0-tGh3E_1G1nVAFjRBf44KcPXYUhgnYblKazZ_V7e0b4s.wIDSc91DIrv_gfqm0OWlsTVCZXx_ceWvs5u_7Lrddx8&dib_tag=se&keywords=council+tools+double+bit+michigan+axe&qid=1708806397&s=lawn-garden&sprefix=counsil+tools+double+bit+michigan+ax%2Clawngarden%2C200&sr=1-1"

#headers for requests
HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0', 'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(url, headers=HEADERS)

#print(webpage)

type(webpage.content)

#soup object containing all data
#it looks like beautiful soup is parsing the html code of the webpage. 
soup = BeautifulSoup(webpage.content, "html.parser")

#This output is the html document in question.
#print(soup)

#fetch links as list of tag objectives
# This seems to be the best way to find all a tags in the html document. Anything more fine grained 
#results in an empty list
links = soup.find_all("a")
#printing all a tag lines found
#print(links)

Link_href=links[12].get('href')

product_list = "https://amazon.com" + Link_href

Title_Extract=soup.find("span", attrs={"id":"productTitle"}).text.strip()

Price_Extract=soup.find("span", attrs={"class":"a-offscreen"}).text
        
Rating_Extract = soup.find("span", attrs={"class":"a-icon-alt"}).text


#<span class="a-offscreen">$59.99</span>

print(Rating_Extract)

