
import requests

url = "http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/FR/eur/en-US/uk/us/anytime/anytime?apikey=fl364355903022705126954397234126"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
#####################################################################################################################

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
#This is a sample of how the output of LIVE API from skyscanner will be





APILive= {
  "SessionKey": "ab5b948d616e41fb954a4a2f6b8dde1a_ecilpojl_7CAAD17D0CFC34BFDE68DEBFDFD548C7",
  "Query": {
    "Country": "GB",
    "Currency": "GBP",
    "Locale": "en-gb",
    "Adults": 1,
    "Children": 0,
    "Infants": 0,
    "OriginPlace": "2343",
    "DestinationPlace": "13554",
    "OutboundDate": "2017-05-30",
    "InboundDate": "2017-06-02",
    "LocationSchema": "Default",
    "CabinClass": "Economy",
    #"GroupPricing": false
  },
  "Status": "UpdatesComplete",
  "Itineraries": [
    {
      "OutboundLegId": "11235-1705301925--32480-0-13554-1705302055",
      "InboundLegId": "13554-1706020700--32480-0-11235-1706020820",
      "PricingOptions": [
        {
          "Agents": [
            4499211
          ],
          "QuoteAgeInMinutes": 0,
          "Price": 83.41,
          "DeeplinkUrl": "http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=jzj5DawL5zJyT%2bnfe1..."
        },
        #there will be a lot of itineraries. so we need a for loop here
        ],
      "BookingDetailsLink": {
        "Uri": "/apiservices/pricing/v1.0/ab5b948d616e41fb954a4a2f6b8dde1a_ecilpojl_7CAAD17D0CFC34BFDE68DEBFDFD548C7/booking",
        "Body": "OutboundLegId=11235-1705301925--32480-0-13554-1705302055&InboundLegId=13554-1706020700--32480-0-11235-1706020820",
        "Method": "PUT"
      }
    },
   # ...
   ],
  "Legs": [
    {
      "Id": "11235-1705300650--32302,-32480-1-13554-1705301100",
      "SegmentIds": [
        0,
        1
      ],
      "OriginStation": 11235,
      "DestinationStation": 13554,
      "Departure": "2017-05-30T06:50:00",
      "Arrival": "2017-05-30T11:00:00",
      "Duration": 250,
      "JourneyMode": "Flight",
      "Stops": [
        13880
      ],
      "Carriers": [
        885,
        881
      ],
      "OperatingCarriers": [
        885,
        881
      ],
      "Directionality": "Outbound",
      "FlightNumbers": [
        {
          "FlightNumber": "290",
          "CarrierId": 885
        },
        {
          "FlightNumber": "1389",
          "CarrierId": 881
        }
      ]
    },
    #...
   ],
   "Segments": [
    {
      "Id": 0,
      "OriginStation": 11235,
      "DestinationStation": 13880,
      "DepartureDateTime": "2017-05-30T06:50:00",
      "ArrivalDateTime": "2017-05-30T07:55:00",
      "Carrier": 885,
      "OperatingCarrier": 885,
      "Duration": 65,
      "FlightNumber": "290",
      "JourneyMode": "Flight",
      "Directionality": "Outbound"
    },
  #  ...
  ],
    "Carriers": [
    {
      "Id": 885,
      "Code": "BE",
      "Name": "Flybe",
      "ImageUrl": "http://s1.apideeplink.com/images/airlines/BE.png",
      "DisplayCode": "BE"
    },
   # ...
  ],
  "Agents": [
    {
      "Id": 1963108,
      "Name": "Mytrip",
      "ImageUrl": "http://s1.apideeplink.com/images/websites/at24.png",
      "Status": "UpdatesComplete",
     # "OptimisedForMobile": true,
      "BookingNumber": "+448447747881",
      "Type": "TravelAgent"
    },
   # ...
  ],
  "Places": [
    {
      "Id": 11235,
      "ParentId": 2343,
      "Code": "EDI",
      "Type": "Airport",
      "Name": "Edinburgh"
    },
    #...
  ],
  "Currencies": [
    {
      "Code": "GBP",
      "Symbol": "£",
      "ThousandsSeparator": ",",
      "DecimalSeparator": ".",
    #  "SymbolOnLeft": true,
    #  "SpaceBetweenAmountAndSymbol": false,
      "RoundingCoefficient": 0,
      "DecimalDigits": 2
    },
   # ...
  ]
}

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
    print("You might want to loose some more coins!")
print("Previous Flight Budget",Flight)
print("Previous Hotel Budget",Acm)

Flight = Price 
print("Updated Flight Charges",Flight)
Acm= val- Flight
print("New Hotel Budget",Acm)
### cross verify if else statement here

#Now we will use this Acm for Hotel API calling

HotelAPI= {
    "correlation_id": "3889f7d3-65d2-40e8-8034-4accb18bade9",
    "meta": {
        "status": "COMPLETED",
        "search_id": "915c591f9fd48c64c9c0ad748d6e6851f09f5dbc4d608495479f1a07e1e7a968",
        "total": 311,
        "completion_percentage": 100,
        "total_available": 73,
        "hotels_filtered": 73,
        "offers": 459,
        "total_available_filtered": 73,
        "request_id": "e3f5c49b-3139-4311-99e1-5ca746541f58"
    },
    "results": {
        "location": [
            {
                "entity_type": "Island",
                "entity_id": "81972530",
                "name": "Malta Island"
            },
            {
                "entity_type": "Nation",
                "entity_id": "29475371",
                "name": "Malte"
            }
        ],
        "hotels": [
            {
                "coordinates": [
                    14.50658,
                    35.91218
                ],
                "stars": "3",
                "offer_types": [
                    "META"
                ],
                "district": "[]",
                "reviews_count": 868,
                "city": "33349710",
                "cheapest_offer_type": "META",
                "amenities": [
                    "Lift",
                    "ConciergeService",
                    "Laundry",
                   # ...
                ],
                "property_type": "Hotel",
                "distance": 6142.49539734,
                "rating": {
                    "desc": "rating_satisfactory",
                    "value": 6.9
                },
                "name": "Roma Hotel",
                "hotel_id": "47053033",
                "images": [
                    {
                        "gallery": "https://d2xf5gjipzd8cd.cloudfront.net/available/353235256/mca.jpg",
                        "provider": "h_ct",
                        "category": "Beach",
                        "dynamic": "https://d2xf5gjipzd8cd.cloudfront.net/available/353235256/353235256_WxH.jpg",
                        "thumbnail": "https://d2xf5gjipzd8cd.cloudfront.net/available/353235256/mt.jpg"
                    },
                   # ...
                ],
                "offers": [
                    {
                        "partner_id": "h_hc",
                        "price": 78,
                        "price_gbp": 69,
                       # "available": null,
                      #  "strike_through": null,
                        "meal_plan": "breakfast_included",
                     #   "is_official": true,
                       # "closed_user_groups": null,
                    #    "dbook_link": null,
                        "room_type": [
                            "triple_room"
                        ],
                        "deeplink": "www.skyscanner.fr/hotel_deeplink/4.0/FR/fr-FR/EUR/h_hc/47053033/2019-06-18/2019-06-19/hotel/hotel/hotels?guests=1&rooms=1&legacy_provider_id=17&request_id=e3f5c49b-3139-4311-99e1-5ca746541f58&q_datetime_utc=2019-06-13T02%3A44%3A29&appName=mobileweb&appVersion=2.0&ticket_price=78&deeplink_data=eyJ1cmwiOiAiaHR0cHM6Ly9mci5ob3RlbHMuY29tL1BQQ0hvdGVsRGV0YWlscz9hZHVsdHNQZXJSb29tPTEmdmlldz1wcmljZXMmbXBoPTAmcG9zPUhDT01fRlImbnVtYmVyT2ZSb29tcz0xJnJhdGVwbGFuaWQ9MjA2Nzc3OTk1JmhvdGVsaWQ9Mjk5NTg4JmRlcGFydHVyZURhdGU9MTkvMDYvMjAxOSZsb2NhbGU9ZnJfRlImYXJyaXZhbERhdGU9MTgvMDYvMjAxOSIsICJmaWVsZHMiOiB7InNpZ25hdHVyZSI6ICJmNTkyYjZiNjU0OWUxMDBiYTNkNzM1NDNhOGZmNGNmOSJ9fQ%3D%3D&max_price=78.0&channel=website&max_price=78.0&channel=website",
                       # "cancellation_text": null,
                        "cancellation": "non_refundable"
                    },
                   # ...
                ],
                "relevance": 2000000.3686611408
            },
          #  ...
        ],
        "price_includes": [
            "vat",
            "other_taxes"
        ],
        "average_min_price": 139.73,
        "filters": {
            "stars": [
                {
                    "id": "5",
                   # "max_price": null,
                    "count": 7,
                    "min_price": 182
                },
               # ...
            ],
            "chain": [
                {
                    "id": "Corinthia",
                  #  "max_price": null,
                    "count": 1,
                    "min_price": 182
                }
            ],
            "price_buckets": [
                {
                    "id": "PR_BK_0",
                    "max_price": 50,
                    "count": 7,
                   # "min_price": null
                },
               # ...
            ],
            "district": [],
            "city": [
                {
                    "id": "33350111",
                   # "max_price": null,
                    "count": 27,
                    "min_price": 36
                },
               # ...
            ],
            "meal_plan": [
                {
                    "id": "breakfast_included",
                   # "max_price": null,
                    "count": 43,
                    "min_price": 28
                },
                ...
            ],
            "guest_rating": [
                {
                    "id": "6",
                    "text": "rating_satisfactory",
                    "count": 3,
                   # "min_price": null,
                   # "max_price": null
                },
              #  ...
            ],
            "amenities": [
                {
                    "id": "WifiService",
                  #  "max_price": null,
                    "count": 70,
                    "min_price": 20
                },
               # ...
            ],
            "property_type": [
                {
                    "id": "Hotel",
                 #   "max_price": null,
                    "count": 42,
                    "min_price": 50
                },
                #...
            ],
            "guest_type": [
                {
                    "id": "solo",
                 #   "max_price": null,
                    "count": 1,
                   # "min_price": null
                },
                ...
            ],
            "cancellation": [
                {
                    "id": "free_cancellation",
                 #   "max_price": null,
                    "count": 26,
                    "min_price": 28
                },
               # ...
            ]
        },
        "partners": [
            {
                "website_id": "h_ay",
              #  "is_dbook": false,
                "logo": "www.skyscanner.fr/images/websites/220x80/h_ay.png",
                "name": "ibis Styles",
              #  "is_official": true,
                "partner_type": "Group"
            },
           # ...
        ],
      #  "hotel_pivot": null,
        "map_boundary": {
            "s_w_lng": 14.448729,
            "s_w_lat": 35.893651,
            "n_e_lat": 35.913651,
            "n_e_lng": 14.51241
        },
        "closed_user_group_deals": [],
        "entity": {
            "name": "Luqa",
            "entity_type": "City",
            "centroid": {
                "type": "Point",
                "coordinates": [
                    14.4886111132,
                    35.858888893
                ]
            },
            "entity_id": "46395655",
            "official_center": {
                "type": "Point",
                "coordinates": [
                    14.4892913,
                    35.859653
                ]
            }
        }
    },
    "count": 15,
    "translations": {
        "CUG_create_account_to_unlock_deals_msg": "Créez un compte pour avoir accès à des offres exclusives",
        "CUG_deal": "OFFRE",
        
       # ...
    }
}
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
    

    #Compile both Fly Box and Hot Box and push into Fly app widget.
