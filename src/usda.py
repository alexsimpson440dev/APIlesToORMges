import urllib.request as request
import json
#usda api class
#sets the key (need to move location) Using this for ease.
class USDA():
    def __init__(self):
        self.key = "diIswWW88jOytljMnEadwn3WmseuWGVRe6c7YL7r"

    #gets the url based off the searchItem (will add more)
    #then loops the 5 set results into an array
    #returns the array
    def get_url(self, searchItem):
        URL = 'https://api.nal.usda.gov/ndb/search/?format=json&q=' + searchItem + '&ds=Standard+Reference&fg=Fruits+and+Fruit+Juices&offset=0&max=5&sort=n&api_key=' + self.key
        readURL = request.urlopen(URL).read().decode('utf-8')
        parse = json.loads(readURL)
        n = 0
        names = []
        while n < 5:
            names.append(parse['list']['item'][n]['name'])
            n += 1
        name1 = names[0]
        return name1

    #gets the users search item
    def get_search(self):
        userSearch = input("What food would you like to search? ")
        return userSearch

#basic main function to call stuff
def main():
    api = USDA()
    result = api.get_search()
    url = api.get_url(result)
    print(url)

#calls main function
main()