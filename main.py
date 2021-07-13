

##INSPIRE ME ALGORITHM
###################################################################################################################

val = float(input("Enter your travel budget: ")) #we can enter both integer and float values here for input budget
print("Your input budget: ", val)

def percent(num):
    num = float(num)
    percentage = '{0:.2f}'.format((num  * 30/100)) # Function to divide the ratio in 70:30
    return percentage

Flight= percent(val)  # Flight Budget 
print("Your Flight Budget: ",Flight)

Flight=float(Flight)

Acm= val- Flight
print("Your Hotel Budget:",Acm)

#######################################################################################################################

## below the 2nd part of the code which is interacting with API's to get the real-time data

import json

import requests

url = "http://partners.api.skyscanner.net/apiservices/pricing/v1.0?API Key=fl364355903022705126954397234126"

payload='cabinclass=Economy&country=UK&currency=GBP&locale=en-GB&locationSchema=iata&originplace=EDI&destinationplace=LHR&outbounddate=2021-09-02&inbounddate=2021-09-30&adults=1&children=0&infants=0&apikey=fl364355903022705126954397234126'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
dict = response.headers

print(dict)

location = dict['Location']#this provides the location header from POST create session and we got the unique session key
                                            

#####################################################################################################################
#here in the part below, we are putting the session key and again sending request to skyscanner server to the whole set of itneraries


url = location 
apikey = "?APIKey=fl364355903022705126954397234126"
url = url+apikey

##url = "https://partners.api.skyscanner.net/apiservices/pricing/uk2/v1.0/78bf477e-4631-423b-b659-626e1b66ccc3-c2?APIKey=fl364355903022705126954397234126"

payload='APIKey=fl364355903022705126954397234126'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("GET", url, headers=headers, data=payload)

APILive = response.text
#print(APIOutput)
#print("Got it")


print("SessionKey:",APILive["SessionKey"])
APILive["Query"]["Country"]
APILive["Query"]["Currency"]
APILive["Query"]["Adults"]
APILive["Query"]["Children"]
APILive["Query"]["Infants"]
APILive["Query"]["OutboundDate"]
APILive["Query"]["InboundDate"]
APILive["Query"]["CabinClass"]

print("\tFly Box:"                                                         #make it Bold
      ,"\nCountry:",APILive["Query"]["Country"]
      ,"\nCurrency:",APILive["Query"]["Currency"]
      ,"\nAdults:",APILive["Query"]["Adults"]
      ,"\nChildren:",APILive["Query"]["Children"]
      ,"\nInfants:",APILive["Query"]["Infants"]
      ,"\nOutboundDate:",APILive["Query"]["OutboundDate"]
      ,"\nInboundDate:",APILive["Query"]["InboundDate"]
      ,"\nCabinClass:",APILive["Query"]["CabinClass"])

APILive["Itineraries"][0]['OutboundLegId']                         #loop iternaries here n=0,1,2,3,4,5,6,7,8,9......
Price= APILive["Itineraries"][0]["PricingOptions"][0]["Price"]
APILive["Itineraries"][0]["PricingOptions"][0]["DeeplinkUrl"]
APILive["Itineraries"][0]["BookingDetailsLink"]["Uri"]
APILive["Itineraries"][0]["BookingDetailsLink"]["Body"]
APILive["Itineraries"][0]["BookingDetailsLink"]["Method"]
APILive["Legs"][0]['Departure']
APILive["Legs"][0]['Arrival']
APILive["Legs"][0]['Duration']
APILive["Legs"][0]['Directionality']
APILive["Legs"][0]['FlightNumbers'][0]                              #if carrier and flight ID required see here.

print("OutboundLegId:",APILive["Itineraries"][0]['OutboundLegId']
      ,"\nPrice:",APILive["Itineraries"][0]["PricingOptions"][0]["Price"]
      ,"\nDeeplinkUrl:",APILive["Itineraries"][0]["PricingOptions"][0]["DeeplinkUrl"]
      ,"\nUri:",APILive["Itineraries"][0]["BookingDetailsLink"]["Uri"]
      ,"\nBody:",APILive["Itineraries"][0]["BookingDetailsLink"]["Body"]
      ,"\nMethod:",APILive["Itineraries"][0]["BookingDetailsLink"]["Method"]
      ,"\nDeparture:",APILive["Legs"][0]['Departure']
      ,"\nArrival:",APILive["Legs"][0]['Arrival']
      ,"\nDuration:",APILive["Legs"][0]['Duration']
      ,"\nDirectionality:",APILive["Legs"][0]['Directionality']
      ,"\nFlightNumbers:",APILive["Legs"][0]['FlightNumbers'][0]
    
     )
#APILive["Query"]
#print(APILive["Query"])
print(Price)

#This will cross check and validate the budget to proceed forward with the booking

if Price<=Flight:                         
    print("Awesome! you got the flight within budget")
else:
    print("Oh no!,You might want to loose some more coins!")
print("Previous Flight Budget",Flight)
print("Previous Hotel Budget",Acm)

Flight = Price 
print("Updated Flight Charges",Flight)
Acm= val- Flight
print("New Hotel Budget",Acm)
### cross verify if else statement here


#################################################################################################################

##Hotel API here 
import requests

url = "https://gateway.skyscanner.net/hotels/v1/prices/search/entity/27548283?market=UK&locale=en-GB&checkin_date=2021-09-01&checkout_date=2021-09-14&currency=GBP&adults=2&rooms=1&images=3&image_resolution=high&boost_official_partners=1&sort=-relevance&limit=30&offset=0&partners_per_hotel=3&enhanced=filters,partners,images,location,amenities,extras,query_location&apiKey=fl364355903022705126954397234126"

payload={}
headers = {
  'x-user-agent': 'M;B2B'
}

response = requests.request("GET", url, headers=headers, data=payload)

HoyelAPI = response.text
#print(HotelAPI)


HotelAPI["correlation_id"]
print("CorrelationID:",HotelAPI["correlation_id"])


HotelAPI["meta"]["status"]
HotelAPI["meta"]["total_available"]
HotelAPI["meta"]["hotels_filtered"]
HotelAPI["meta"]["offers"]
HotelAPI["results"]["location"][0]['entity_type']
HotelAPI["results"]["location"][0]['name']
HotelAPI["results"]["location"][1]['entity_type']
HotelAPI["results"]["location"][1]['name']
HotelAPI["results"]["hotels"][0]['stars'] 
HotelAPI["results"]["hotels"][0]['amenities']
HotelAPI["results"]["hotels"][0]['property_type']
HotelAPI["results"]["hotels"][0]['name'] 
HotelAPI["results"]["hotels"][0]['images'] [0]['gallery']
HotelAPI["results"]["hotels"][0]['images'] [0]['category']
HotelAPI["results"]["hotels"][0]['images'] [0]['dynamic']
HotelAPI["results"]["hotels"][0]['images'] [0]['thumbnail']
HotelAPI["results"]["hotels"][0]['offers'][0]['price']
HotelAPI["results"]["hotels"][0]['offers'][0]['price_gbp']
HotelAPI["results"]["hotels"][0]['offers'][0]['meal_plan']
HotelAPI["results"]["hotels"][0]['offers'][0]['room_type']
HotelAPI["results"]["hotels"][0]['offers'][0]['deeplink']
HotelAPI["results"]["hotels"][0]['offers'][0]['cancellation']


print("\tHotel Box:"                                                         #make it Bold
      ,"\nstatus:",HotelAPI["meta"]["status"]
      ,"\nTotal Hotels Available:",HotelAPI["meta"]["total_available"]
      ,"\nYour Hotels:",HotelAPI["meta"]["hotels_filtered"]
      ,"\nOffers:",HotelAPI["meta"]["offers"]
      ,"\nCategoryOfPlace:",HotelAPI["results"]["location"][0]['entity_type']
      ,"\nPlace Name:",HotelAPI["results"]["location"][1]['name']
      ,"\nEntity Type:",HotelAPI["results"]["location"][1]['entity_type']
      ,"\nEntity Name:",HotelAPI["results"]["location"][1]['name']
      #,"\nEntity Type:",HotelAPI["results"]["location"][1]['entity_type']
      ,"\nLocation Name:",HotelAPI["results"]["location"][1]['name']
        ,"\nStars:",HotelAPI["results"]["hotels"][0]['stars'] 
        ,"\namenities:",HotelAPI["results"]["hotels"][0]['amenities']
        ,"\nproperty_type:",HotelAPI["results"]["hotels"][0]['property_type']
        ,"\nName of Hotel:",HotelAPI["results"]["hotels"][0]['name'] 
        ,"\nHotel Images:",HotelAPI["results"]["hotels"][0]['images'] [0]['gallery']
        ,"\ncategory:",HotelAPI["results"]["hotels"][0]['images'] [0]['category']
        ,"\nMovingPicture:",HotelAPI["results"]["hotels"][0]['images'] [0]['dynamic']
      ,"\nthumbnail:",HotelAPI["results"]["hotels"][0]['images'] [0]['thumbnail']
      ,"\nprice:",HotelAPI["results"]["hotels"][0]['offers'][0]['price']
      ,"\nprice_gbp:",HotelAPI["results"]["hotels"][0]['offers'][0]['price_gbp']
      ,"\nmeal_plan:",HotelAPI["results"]["hotels"][0]['offers'][0]['meal_plan']
      ,"\nroom_type:",HotelAPI["results"]["hotels"][0]['offers'][0]['room_type']
      ,"\ndeeplink:",HotelAPI["results"]["hotels"][0]['offers'][0]['deeplink']
      ,"\ncancellation:",HotelAPI["results"]["hotels"][0]['offers'][0]['cancellation'])
    

print("Dear Customer, this is your complete Journey information, Hope you enjoy it!")