from ..cacher import CacheIt
import requests

@CacheIt
def get_movie_info(movie_name):
    '''Takes list of movie names and fetches each movie ratings
        the movies ratings are fetched from http://www.omdbapi.com/
        then the movies are sorted based on Rotten Tomatoes rating
        REQUEST PARAMETERS:
        t: Movie title to search for.
        r: The data type to return.
        apikey: user api key'''

    movieInfo = {}
    url = " http://www.omdbapi.com"
    params = {"r": "json", "t": movie_name, "apikey": "578687a"}
    print("Connecting to OMDB ..")
    resp = requests.get(url, params)
    respData = resp.json()
    reqUrl = resp.url
    print("Connected Successfully @:  {}".format(reqUrl))
    movieInfo["data"] = {"Director": respData["Director"],
                         "Actor": respData["Actors"],
                         "Ratings": respData["Ratings"]}
    movieInfo["url"] = reqUrl
    print("Found movie ({}) necessary info!".format(movie_name))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    response = movieInfo

    return response