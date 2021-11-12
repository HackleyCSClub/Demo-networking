import requests

"""
Introduction to curl with python

There are in total 39 different verbs to use with curl so we are going to cover only the main ones.
"""

"""
GET - Sends a request returning back html, css, and js .

the object returned is a status code.
From there you can have a .content / .json / .headers / or with .cookies method to extract data from the content.
For now we'll look at content

response.content returns a byte string
which can be converted to string via .decode("utf-8")
where utf-8 is the encoding standard

"""

response = requests.get("https://example.com/")
print(response.content.decode("utf-8"))


"""
response returns a code

if you use response.content you can access the data within

use the method .decode("utf-8") to return it in strings

returns the value in bytes
"""



"""
POST - Sends data to the server from where the server can access it.

headers method allows you to see headers returned in the request

posts work when parsing json (javascript object notation) data
"""

response = requests.post("https://example.com/")
#print(response.content)



"""
HEAD - Returns the headers of your client IE data you post when making a connection
"""

head = requests.head("https://reqbin.com/echo/post/json")
#print(head.headers)



"""
OPTIONS - To see curl requests

"""
response = requests.options("https://example.com/")
#print(response.headers)



"""
Other methods:

DELETE and PUT allow users to update info on a database
Many databases and api dont use it as most browsers don\'t include them natively.

"""




"""
How to use Headers

Useragent is how you can specify what device you wanna use. As some pages render differently on different browsers and devices.

IE: mobile phone vs laptop

Page of different User agents

https://developers.whatismybrowser.com/useragents/explore/


"""


url = "https://example.com/"

headers = {
    'User-Agent': 'Mozilla/5.0',
}

response = requests.get(url, headers=headers)
print(response.content)
