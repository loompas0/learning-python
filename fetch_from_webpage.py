# retrieve google page from internet
import urllib.request
# now invoke request for retieving url
urlDest = "https://www.google.com"
googleRequest = urllib.request.urlopen(urlDest)
print (googleRequest.getcode()) # return the status code of the get
# print (googleRequest.read()) # return the content of the url
fileName = "google.html"
# retrieve content of web page to a file
urllib.request.urlretrieve(urlDest,fileName) 
