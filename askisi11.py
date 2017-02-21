import urllib.request, json, requests
from email.mime.text import MIMEText

url = "https://api.punkapi.com/v2/beers/random"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
beer = data[0]

name = beer['name']
tagline = beer['tagline']
description = beer['description']
image_url = beer['image_url']

email = input('Δώστε το email σας: ')

msgString = '<p>Here is the random beer you asked for. Enjoy!</p><hr>'
msgString += '<h1>' + name + '</h1>'
msgString += '<h2>' + tagline + '</h2>'
msgString += '<p>' + description + '</p><hr>'
msgString += '<img src="' + image_url + '" alt="' + name + '">'

key = 'key-d971ef34fe87ea5bc26c3bd290bc4438'
request_url = 'https://api.mailgun.net/v3/sandboxa99895715fa249d8abb3b872898c2dd7.mailgun.org/messages'
request = requests.post(request_url, auth=('api', key), data={
    'from': 'BeerHelper <unipi@mailinator.com>',
    'to': email,
    'subject': 'Random Beer',
    'text': msgString
})

if (request.status_code == 200) :
    print ("A random beer was sent to your inbox.")
else :
    print ("There was an error. Please try again.")

