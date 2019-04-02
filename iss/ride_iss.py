import urllib.request
import json
## Trace the ISS
majortom = 'http://api.open-notify.org/astros.json'

## Call the webservice
groundctrl = urllib.request.urlopen(majortom)

## put fileobject into helmet
helmet = groundctrl.read()

## decode json to python data structure
helmetson = json.loads(helmet.decode('utf-8'))

people = helmetson['people']

## display our pythonic data
#print("\n\nConverted python data")
#print(helmetson)

#prints the people in space at ISS
print("People in Space: ", helmetson['number'])
#pull data from the library by name by person
for person in helmetson["people"]:
   print("{} on the ISS" .format(person['name']) )

#people = helmetson['people']
#print(people)
