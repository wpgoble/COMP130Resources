english = ["one", "two", "three"]
german = ["eins", "zwei", "drei"]
spanish = ["uno", "dos", "tres"]

##for i in range(len(english)):
##    print(english[i], german[i])

# key: zip-code
# value: city name
locations = {"06824": "Fairfield",
             "21212": "Baltimore",
             "90210": "LA",
             "17013": "Carlisle"}

print(locations["17013"])

locations2 = {
    "Carlisle":["17013", "17015"]
    }

print(locations2["Carlisle"])

if "North Garden" in locations:
    print(locations["22959"])
else:
    locations["22959"] = "North Garden"


if "North Garden" in locations.values():
    print(locations["22959"])




    


