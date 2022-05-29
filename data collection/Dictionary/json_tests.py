import urllib.request
import json
#
# webUrl=urllib.request.urlopen("http://www.google.com")
# print("the code :" + str(webUrl.getcode()))
# data=webUrl.read()
# print(data)
#
# def printResult(data):
#     theJson=json.loads(data)
#     print(theJson)

urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson"

webUrl = urllib.request.urlopen(urlData)
print("status code" + str(webUrl.getcode()))

if (webUrl.getcode() == 200):
    data = webUrl.read()
    # print(data)
    theJson = json.load(data)
    print(theJson)
    print(theJson)
else:
    print("error occurred")


