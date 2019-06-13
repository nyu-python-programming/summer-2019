import urllib.request

response = urllib.request.urlopen("http://python.org") #make a request to a web server, and store the response

html = str(response.read()) #convert the response to a string


startingPosition = 0
numberOfLinks = 0
searchTerm = "http://"

while startingPosition >= 0:
    startingPosition = html.find(searchTerm, startingPosition + 1)
    numberOfLinks = numberOfLinks + 1

print("Found", numberOfLinks, "links in this web page")

