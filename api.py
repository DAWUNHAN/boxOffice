import requests

API_KEY = '1549868c'

title = 'Avatar'
movieInfo = requests.get('http://www.omdbapi.com/?apikey='+API_KEY+'&t='+title).json()
print(movieInfo['BoxOffice'])