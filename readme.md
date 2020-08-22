## Star Wars Flask API
Hello Welcome to Star Wars API endpoint using dockerized version of application
There are two endpoints in this application. This application uses "swapi.dev" for the data
# "/films"
This endpoint returns the list of Star wars film available and arranged in the order of their release date.
# "/characters?filmid=film_id"
This end point uses the film_id and returnsthe characters name that were in the movie in the sorted order.

# To execute this docker following steps you can do to execute Docker file
```$ docker build -t starwar-flask```
```$ docker run -d -p 5000:5000 starwar-flask```

# Example to execute the API endpoints
```http://localhost:5000/films```: This would display the list of Star Wars Film in a sorted manner with their filmid

```http://localhost:5000/characters?filmid=2```: This would display the Name of the characters in the sorted manner for the film whose filmid is 2
