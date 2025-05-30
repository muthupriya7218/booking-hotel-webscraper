# This app scrap data from booking.com

# library installed
# 1. beautifulsoup4
# 2. requests

import requests
from bs4 import BeautifulSoup
import lxml
import csv
import time
import random

url_text = "https://www.booking.com/searchresults.html?ss=Meghalaya%2C+India&efdco=1&aid=355028&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=3481&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=e5255529393b011e&ac_meta=GhBlNTI1NTUyOTM5M2IwMTFlIAAoATICZW46Bk1lZ2hhbEAASgBQAA%3D%3D&checkin=2025-05-01&checkout=2025-05-09&group_adults=1&no_rooms=1&group_children=0"


def web_scraper(web_url,file_name):

    #Greetings
    print('Thank you for sharing the url and file name!\n⏳\nStarting the webscrapping')

    num = random.randint(2,7)

    #Processing
    time.sleep(num)

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}


    response = requests.get(web_url, headers = header)

    if response.status_code == 200:
        print('Connected to the website')
        html_content = response.text

        #Creating Soup
        soup = BeautifulSoup(html_content, 'lxml')
        #print(soup.prettify())
        
        #Main Containers
        
        hotel_divs = soup.find_all("div", role = "listitem")

        with open(file_name+'.csv','w',encoding='utf-8', newline='') as file_csv:
            writer = csv.writer(file_csv)
            #Adding header
            writer.writerow(['hotel_name','location','price','review','rating','review_count','link'])
        
            for hotel in hotel_divs:
                hotel_name_tag = hotel.find('div', class_ = 'b87c397a13 a3e0b4ffd1')
                hotel_name = hotel_name_tag.text.strip() if hotel_name_tag else "NA"

                location_tag = hotel.find('span',class_ = 'd823fbbeed f9b3563dd4')
                location = location_tag.text.strip() if location_tag else "NA"

                price_tag = hotel.find('span', class_='b87c397a13 f2f358d1de ab607752a2')
                price = price_tag.text.strip().replace('₹', '').replace('\u00a0', '').replace(',', '') if price_tag else ""

                review_tag = hotel.find('div', class_='f63b14ab7a f546354b44 becbee2f63')
                review = review_tag.text.strip() if review_tag else "NA"

                rating_tag = hotel.find('div',class_ = 'f63b14ab7a dff2e52086')
                rating = rating_tag.text.strip() if rating_tag else "NA"

                review_count_tag = hotel.find('div',class_ = 'fff1944c52 fb14de7f14 eaa8455879')
                review_count = review_count_tag.text.strip() if review_count_tag else "NA"

                #Getting link
                link_tag = hotel.find('a', href=True)
                link = link_tag.get('href') if link_tag else "No link available"

            
                #Saving the file into csv
                writer.writerow([hotel_name,location,price,review,rating,review_count,link])
       
        #print(hotel_name)
        #print(location)
        #print(price)
        #print(review)
        #print(rating)
        #print(review_count)
        #print(link)
        print("Web Scrapping done")
        #print('')
            
        #print(hotel_divs)
    else:
        print(f'Connection failed! {response.status_code}')

    #print(response.status_code)

if __name__ == '__main__':
    web_url = input("Please enter url: ")
    file_name = input("Please give file name: ")

    web_scraper(web_url,file_name)