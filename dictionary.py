import json
from difflib import get_close_matches as gcm
data=json.load(open("data.json"))

def translate(word):
    word= word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(gcm(word,data.keys()))>0:
        print("Are you looking for %s?"%gcm(word,data.keys())[0])
        decide = input("press y for yes and n for no: ")
        if decide=="y":
            return data[gcm(word,data.keys())[0]]
        elif decide=="n":
            print("The word doesn't exist")
        else:
            print("keyboard hai toh kuch bhi likhoge jitna poocha hai utna type karo")
    else:
        print("The word doesn't exist")

word=input("Enter the word : ")
output=translate(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)  

