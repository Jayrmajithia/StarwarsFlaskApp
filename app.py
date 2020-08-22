from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/')
def index():
    s ='''
    Hello Welcome to Star Wars API endpoint using dockerized version of application <br>
    There are two endpoints in this application. This application uses "swapi.dev" for the data <br>
    1) "/films": This endpoint returns the list of Star wars film available and arranged in the order of their release date.<br>
    2) "/characters?filmid=film_id": This end point uses the film_id and returnsthe characters name that were in the movie in the sorted order.
    '''
    return s

# Provides the list of films in sorted by release date of the movie
@app.route('/films')
def filmsList():
    req = requests.get("https://swapi.dev/api/films/") # Fetches the list of film from the swapi endpoint
    res = req.json()
    ans = "<html><head><title>Star Wars Film</title></head><table border= \"1px solid black\"><tr><th>Film_id</th><th>Film</th><th>Released Year</th></tr>"
    for film_id in range(len(res['results'])):
        r = res['results'][film_id]
        ans += "<tr><td>"+ str(film_id+1) +"</td>" + "<td>" + r['title']  + "</td>" + "<td>" + r['release_date']  + "</td>" +"</td></tr>"
    ans += "</table>"
    return ans

@app.route('/characters')
def characterList():
    if "filmid" in request.args:
        id = request.args["filmid"]
        req = requests.get("https://swapi.dev/api/films/" + id) # Fetches the data from the swapi for the particular film
        res = req.json()
        characters = []
        for people in res['characters']:
            req = requests.get(people) # Fetching the details about differnt film
            p = req.json()
            characters.append(p['name'])
        characters.sort() # Sorting the characters name
        res = "<ul>"
        for name in characters:
            res += "<li>" + name + "</li>"
        res += "</ul>"
        return res
    else:
        return "Provide Prameter filmid in the URL"

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
