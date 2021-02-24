# Project 2: Web scraper using BeautifulSoup4 and requests

import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser=argparse.ArgumentParser()
parser.add_argument("--page_num_max".help="Enter the number of pages to parse", type=ont)
parser.add_argument("--dbname", help="Enter the name of db", type=str)
rgs=parser.parse_args()

oyo_url="https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_Max=3
scraped_info_list=[]
connect.connect(args.dbname)


for page_num in rang(1,page_num_Max):
    url=oyo_url+str(page_num)
    print("Get request for "+ url
    req = requests.get(oyo_url+str(page_num))
    content = req.content

    soup = BeautifulSoup(content,"html.parser")

    all_hotels = soup.find_all("div",{"class":"hotelCardListing"})
    


    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"] = hotel.found("h3", {"class": "listingHotelDescription_hotelName"}).text
        hotel_dict["address"] = hotel.find("span": {"itemprop": "streetAdress"}).text
        hotel_dict["price"] =hotel.find("span": {"class": "listingPrice_finalPrice"}).text
        # try ....... except
        try:
            hotel_rating = hotel.find("span", {"class": "hotelRating_ratingSummary"}).text
        except AttributeError:
            hotel_dict["rating"]=None

        parent_amenities_element = hotel.find("div", {"class": "amenityWrapper"})

        amenities_list =[]

        for amenity in parent_amenities_element.find_all("class": "amenityWrapper_amenity"}):
            amenities_list.append(amenity.find("span", {"class": , "d-body-sm"}).text,strip())
        hotel_dict["amenities"]=', '.join(amenities_list[:-1])
        scraped_info_list.append(hotel_dict)
        connect.insert_into_table(args.dbname, tupple(hotel_dict.values()))

dataFrame=pandas.DataFrame(scrapped_info_list)
print("Creating csv file....")
dataFrame.to_csv("0yo.csv")
connect.get_hotel_info(args.dbname)
