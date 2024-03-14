
from bs4 import BeautifulSoup
import requests
import numpy
import pandas

#Function to extract the project Title

def get_title(soup):

    try:
        #Outer Tag Object
        title_string = soup.find("span", attrs={"id":"productTitle"}).text.strip()

    except AttributeError:
        title_string=""

    return title_string

#Function to extract the Amazon web page product price

def get_price(soup):
    
    try:
        price = soup.find("span", attrs={"class":"a-offscreen"}).text

    except:
        price = ""

    return price

#Function to extract the amazon product rating

def get_rating(soup):

    try: 
        rating = soup.find("span", attrs={"class":"a-icon-alt"}).text

    except:
        rating=""

    return rating

#Function to extract number of user reviews

def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'arcCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count=""

    return review_count

#Function to extract availability status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = "Not Available"

    return available
#-------------------------------------------------------------------------------
#Beginning of main program

if __name__ =='__main__':
    #add your user agent
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0', 'Accept-Language': 'en-US, en;q=0.5'})

    #add webpage url
    url = "https://www.amazon.com/Council-Tool-Michigan-Pattern-Straight/dp/B000IJRISU/ref=sr_1_1?crid=1AXQVNLYQX465&dib=eyJ2IjoiMSJ9.lqHQIUaSLHQenDlmoiGB-omexOyAjczwwon15xDYFSwe6yEVHIVLBcGuIakXM_tJdPCTsxrj465rMRM64KjqiexF9XMs3oBYHu6HOt8E0ZqTtg3Hh0nNZyRp5VMOhJsEdBJJevndTrcAr1GMLIVl7xKPctSAtbsglYpSpqwF1cYIU9s1ZcWF2IvrypraEZAOhLdd0OvN8QvEqZD4E9V7ohlDGiZ4pjFWqIjXklieDD_K6k3DfpHezXdY6TmxTc0-tGh3E_1G1nVAFjRBf44KcPXYUhgnYblKazZ_V7e0b4s.wIDSc91DIrv_gfqm0OWlsTVCZXx_ceWvs5u_7Lrddx8&dib_tag=se&keywords=council+tools+double+bit+michigan+axe&qid=1708806397&s=lawn-garden&sprefix=counsil+tools+double+bit+michigan+ax%2Clawngarden%2C200&sr=1-1"




    #HTTP Request
    webpage = requests.get(url, headers = HEADERS)

    #Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")

    #Fetch links as List of Tag Objects
    #links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})
    links = soup.find_all("a")


    #Store the links
    links_list = []

    #Loop for extracted links from tag objects
    for link in links:
        links_list.append(link.get('href'))

    d={"title":[], "price":[], "rating":[], "reviews":[], "availability":[]}

    #loop for extracting product details for each link
    for link in links_list: 
        #These conditions were added because my list of a tags was pretty rough and dirty, since the traditional attributed did not work in finding them. So this is the working result I have so far. 
        if type(link) is str and not link.startswith("https") and "/" in link:        
            #"javascript:void(0)":

            print(link)

            new_webpage = requests.get('https://www.amazon.com' + link, headers=HEADERS)
            new_soup = BeautifulSoup(new_webpage.content, "html.parser")

            #Function calls to display all necessary product information
            d['title'].append(get_title(new_soup))
            d['price'].append(get_price(new_soup))
            d['rating'].append(get_rating(new_soup))
            d['reviews'].append(get_review_count(new_soup))
            d['availability'].append(get_availability(new_soup))

    amazon_df = pandas.DataFrame.from_dict(d)
    amazon_df['title'].replace('', numpy.nan, inplace=True)
    amazon_df = amazon_df.dropna(subset=['title'])
    amazon_df.to_csv("amazon_data.csv", header=True, index=False)



























