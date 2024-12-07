"""
import urllib
use ullib.request tog et the data from the url
write a function that takes a url
return a responce
"""

import urllib.request as urllib

def main(url):
    print("checking connectivity")

    response=urllib.urlopen(url)
    print("connected to",url,"successfully")
    print("the response code was : ",response.getcode())

print("this is a site connectivity checker program")
input_url=input("input the url of the site you want to check : ")
main(input_url)    