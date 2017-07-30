import requests
import json

LOW = 50000000
HIGH = 90000000
isFree = 1
def findBike( url ):
  # print "FIND BIKE: " + url
  r = requests.get(url)

  if r.status_code == 200:
    #  print "REQUEST SUCCESSFUL"
     respone_native = json.loads(r.text)
     for ads in respone_native["ads"]:
      if ads.has_key("price") and ads["price"] > LOW and ads["price"] < HIGH:
        print "___TITLE: " + ads["subject"].encode('utf-8')
        print "___PRICE: " + ads["price_string"].encode('utf-8')
        print "___DATE: " + ads["date"].encode('utf-8')
        print "______________________________________________________________"
      isFree = 1
  else:
     print "REQUEST FAILED"
  return

# BASE_URL = "https://gateway.chotot.com/v1/public/ad-listing?region=13&cg=2020&w=1&sp=0&limit=20&o=0&st=s,k"
BASE_URL = "https://gateway.chotot.com/v1/public/ad-listing"
LIMIT = 50

f_type = "p" # p -> personal, c -> company
region = "13" # TP HCM
cg = "2020" # Xe may
sp = "0" # filter

BASE_URL += "?region=" + region
BASE_URL += "&cg=" + cg
BASE_URL += "&w=1"
BASE_URL += "&f=" + f_type
BASE_URL += "&sp=0"
BASE_URL += "&limit=20"

count = 0
while (count < LIMIT):
   if 1:
     url = BASE_URL + "&o=" + str(count * 20) + "&st=s,k"
     findBike(url)
     isFree = 0
     count = count + 1
   else:
     print "HOLDING"

print "Good bye!"
