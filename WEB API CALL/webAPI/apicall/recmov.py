from ..cacher import CacheIt
import requests

@CacheIt
def get_movie_recom(movie_name):
    '''Takes movie title and return 5 recommended movies titles only.
        fetching the results from: https://tastedive.com/read/api

        REQUEST PARAMETERS:
        q: search query, movie name
        type: query type of results music, movies, shows, etc..
        limit: maximum number of recommendations to retrieve. Default is 20
        k:  Your API access key'''

    api = "336737-movierec-MSYFZUOB"
    url = "https://tastedive.com/api/similar"
    param = {"q": movie_name, "type": "movie", "limit": 5, "k": api}
    print("Connecting to TesrDive ..")
    resp = requests.get(url, params=param)
    respData = resp.json()
    reqUrl = (resp.url)
    print("Connected Successfully @:  {}".format(reqUrl))
    moviesList = respData['Similar']['Results']
    moviesTitles = [movie['Name'] for movie in moviesList]
    print("Found similar movies check them now!")
    movieReco = {"data": moviesTitles, "url": reqUrl}
    response = movieReco

    return response