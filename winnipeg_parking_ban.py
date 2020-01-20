import json
import urllib.request

myZone = input("What is your zone? ")

url = 'https://data.winnipeg.ca/resource/tix9-r5tc.json?plow_zone=' + myZone.upper()
response = urllib.request.urlopen(url)
result = json.loads(response.read())

for value in result:
  forPrint = "Plow Zone: {0} start-time: {1} end-time: {2}"
  print(forPrint.format(value['plow_zone'], value['shift_start'], value['shift_end']))