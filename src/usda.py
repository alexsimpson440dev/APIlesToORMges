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
        URL = 'https://api.nal.usda.gov/ndb/search/?format=json&q=' + searchItem + '&ds=Standard+Reference&fg=Fruits+and+Fruit+Juices&offset=0&max=10&sort=n&api_key=' + self.key
        try:
            readURL = request.urlopen(URL).read().decode('utf-8')
            parse = json.loads(readURL)
            n = 0
            names = []
            while n < 10:
                names.append(parse['list']['item'][n]['name'])
                n += 1
            return names

        except KeyError as e:
            print("Please try a different item, search returned zero results!")

    #gets the users search item
    def get_search(self):
        userSearch = input("What food would you like to search? ")
        userSearch = userSearch.replace(' ', '+')
        return userSearch


#basic main function to call stuff
def main():
    api = USDA()
    userSearch = api.get_search()
    url = api.get_url(userSearch)
    # loop that will pop from the url list and display all of the results
    count = 1
    while len(url):
        print("Item " + str(count) + ": " + url.pop())
        count += 1
#calls main function
main()