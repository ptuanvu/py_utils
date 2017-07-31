import requests
import json

LOW = 50000000
HIGH = 90000000
isFree = 1

fo = open("foo.html", "w+")
fo.write("<html lang=\"en\">\r\n  <head>\r\n    <!-- Required meta tags -->\r\n    <meta charset=\"utf-8\">\r\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">\r\n\r\n    <!-- Bootstrap CSS -->\r\n    <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css\" integrity=\"sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ\" crossorigin=\"anonymous\">\r\n    <link rel=\"stylesheet\" href=\"./style.css\" >\r\n  </head>\r\n  <body>")

DETAIL_URL = "https://gateway.chotot.com/v1/public/ad-listing/"
def findDetail( pId ):
  rdetail = requests.get(DETAIL_URL + str(pId))
  if rdetail.status_code == 200:
    respone_detail = json.loads(rdetail.text)
    fo.write("<span class=\"card-text\">" + respone_detail["ad"]["phone"].encode('utf-8') + "</span>")
    if respone_detail["ad"].has_key("body"):
       fo.write("<p>" + respone_detail["ad"]["body"].encode('utf-8') + "</p>")
    fo.write("<div class=\"images-detail\">")
    if respone_detail["ad"].has_key("images"):
       for img in respone_detail["ad"]["images"]:
          fo.write("<img src=\"" + img.encode('utf-8') + "\" alt=\"\" />")
    fo.write("</div>")
  else:
    print "REQUEST DETAIL FAILED"
  return

def findBike( url ):
  # print "FIND BIKE: " + url
  r = requests.get(url)

  if r.status_code == 200:
    #  print "REQUEST SUCCESSFUL"
     respone_native = json.loads(r.text)
     for ads in respone_native["ads"]:
      if ads.has_key("price") and ads["price"] > LOW and ads["price"] < HIGH:
        fo.write("<div class=\"card\">")
        fo.write("<div class=\"card-block\">")
        fo.write("<h4 class=\"card-title\">" + ads["subject"].encode('utf-8') + "</h4>")
        fo.write("<span class=\"card-text\">" + ads["price_string"].encode('utf-8') + "</span>")
        fo.write("<span class=\"card-text\">" + ads["date"].encode('utf-8') + "</span>")
        findDetail(ads["list_id"])
        fo.write("</div>")
        fo.write("</div>")
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
cg = "2020" # 2020: Xe may # 1000: thue nha
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

fo.write("   <!-- jQuery first, then Tether, then Bootstrap JS. -->\r\n    <script src=\"https://code.jquery.com/jquery-3.1.1.slim.min.js\" integrity=\"sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n\" crossorigin=\"anonymous\"></script>\r\n    <script src=\"https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js\" integrity=\"sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb\" crossorigin=\"anonymous\"></script>\r\n    <script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js\" integrity=\"sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn\" crossorigin=\"anonymous\"></script>\r\n  </body>\r\n</html>")
print "Good bye!"
fo.close()
