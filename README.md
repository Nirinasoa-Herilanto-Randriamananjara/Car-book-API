# Car Book API

Hello, this project is an exercise of practicing API with Flask and how to create an documentation of an project. My goals is to have an good understanding in API and project documentation.

## Getting Started

### Pre-require and Local development

Developers who want to use this project locally should have an python version 3, during development of this project I use python 3.10.5

All packages necessary of this application are already inside requirements.txt, so please make sure to install all dependencies to avoid any errors. You can run `pip install -r requirements.txt`

Before running this application, wrap the project inside our parent folder for example:

```
frontend
|__your client app

backend
|__this project(Car Book API)

```

To execute this application, you should be inside our backend folder in your terminal command then you can follow this command:

```
set FLASK_APP=flaskr
set FLASK_ENV=development //to enable DEBUG mode
flask run
```

By default, this application run at `http://127.0.0.1:5000/`

### Testing API

In order to run the test, please follow this command:

- Make sure you have an other database:
  - psql command
    ```
      drop database carbook_test;
      create database carbook_test;
    ```
- Then you can run `python test_flaskr.py`

## API Reference

### Getting Started

- Base Url: On this moment, this app can run locally not also hosted. The backend app is hosted by default at `http://127.0.0.1:5000/` or we can access it with `http://localhost:5000/`.
- Authentication: The version of the application doesn't require authentication or API Keys for now.

### Error Handling

All errors are return as JSON object with the following format:

```
{
  "error": 404,
  "message": "resource not found",
  "success": false
}

```

The API will return four(04) errors types when request fail:

- 400 bad request
- 404 resource not found
- 405 method not allowed
- 422 unprocessable

### Resource Endpoints

#### GET /cars

- General:

  - Returns a lists of cars objects with success value and total numbers of cars.
  - Results are paginated in groups of 10. Include a request argument to choose page number, by default start from 1.
    Example:`curl http://127.0.0.1:5000/cars?page=2` or `curl http://localhost:5000/cars?page=2`

- Example:
  `curl http://127.0.0.1:5000/cars` or `curl http://localhost:5000/cars`

```
{
  "cars": [
    {
      "id": 1,
      "image_link": "image url",
      "model": "Z-5",
      "name": "BMW"
    },
    {
      "id": 2,
      "image_link": "http://unspalsh-cars",
      "model": "MC-60",
      "name": "Mercedes"
    },
    {
      "id": 4,
      "image_link": "http://...",
      "model": "J-XVII",
      "name": "Jaguar"
    },
    {
      "id": 5,
      "image_link": "http://...",
      "model": "J-XVII",
      "name": "Voiture 5"
    },
    {
      "id": 6,
      "image_link": "http://...",
      "model": "J-XVII",
      "name": "Voiture 6"
    },
    {
      "id": 7,
      "image_link": "http://...",
      "model": "J-XVII",
      "name": "Voiture 7"
    },
    {
      "id": 8,
      "image_link": "http://...",
      "model": "J-XVII",
      "name": "Voiture 8"
    },
    {
      "id": 9,
      "image_link": "http://...",
      "model": "J-XVII",
      "name": "Voiture 9"
    },
    {
      "id": 10,
      "image_link": "http://...",
      "model": "J-XVII",
      "name": "Voiture 10"
    },
    {
      "id": 11,
      "image_link": "http://...",
      "model": "J-XVII",
      "name": "Voiture 11"
    },
  ],
  "success": true,
  "total_cars": 3
}

```

#### GET /cars/{car_id}

- General: Return single car by id given and return an success value
- Example: `curl http://127.0.0.1:5000/cars/2` or `curl http://localhost:5000/cars/2`

```
{
  "car": {
    "id": 2,
    "image_link": "http://unspalsh-cars",
    "model": "MC-60",
    "name": "Mercedes"
  },
  "success": true
}

```

#### POST /cars

- General: We can create a new booking car by submitting name, model and image link of the car. It return a success value, created id of the new car, message who confirm that new car was created successfully, all lists of cars paginated and the total number of the cars.

- Example creating new car:
  `curl -X POST -H "Content-Type: application/json" -d'{"name":"Hummer", "model":"H4", "image_link":"http://hummer"}' http://localhost:5000/cars `

```
{
  "cars": [
    {
      "id": 1,
      "image_link": "image url",
      "model": "Z-5",
      "name": "BMW"
    },
    {
      "id": 2,
      "image_link": "http://unspalsh-cars",
      "model": "MC-60",
      "name": "Mercedes"
    },
    {
      "id": 4,
      "image_link": "http://...",
      "model": "J-XVII",
      "name": "Jaguar"
    },
    {
      "id": 6,
      "image_link": "http://hummer",
      "model": "H4",
      "name": "Hummer"
    }
  ],
  "created": 6,
  "message": "Car created successfully",
  "success": true,
  "total_cars": 4
}


```

other example `curl -X POST -H "Content-Type: application/json" -d'{"name":"Land Rover", "model":"V5", "image_link":"http://land-rover"}' http://127.0.0.1:5000/cars`

```
{
  "cars": [
    {
      "id": 1,
      "image_link": "image url",
      "model": "Z-5",
      "name": "BMW"
    },
    {
      "id": 2,
      "image_link": "http://unspalsh-cars",
      "model": "MC-60",
      "name": "Mercedes"
    },
    {
      "id": 4,
      "image_link": "http://...",
      "model": "J-XVII",
      "name": "Jaguar"
    },
    {
      "id": 6,
      "image_link": "http://hummer",
      "model": "H4",
      "name": "Hummer"
    },
    {
      "id": 7,
      "image_link": "http://land-rover",
      "model": "V5",
      "name": "Land Rover"
    }
  ],
  "created": 7,
  "message": "Car created successfully",
  "success": true,
  "total_cars": 5
}

```

#### PUT, PATCH /cars/{car_id}

- General: It require the id of the car that we want to update or patch. We can update all car object or specific data that we want to update. Then it returns an success value, id of the car updated and an message to confirm the action.

- Example:
  `curl http://127.0.0.1:5000/cars/7 -X PATCH -H "Content-Type: application/json" -d'{"image_link":"http://new-image-land-rover"}' `

  ```
  {
  "car_id": 7,
  "message": "Car updated successfully",
  "success": true
  }

  ```

  other example `curl http://localhost:5000/cars/7 -X PUT -H "Content-Type: application/json" -d'{"model":"V8", "image_link":"http://land-rover-V8"}' `

  ```
  {
  "car_id": 7,
  "message": "Car updated successfully",
  "success": true
  }

  ```

#### DELETE /cars/{car_id}

- General: Will delete the car by ID given if it exists. It returns an success value, id of car deleted, message who confirm the action, all lists of cars and total number of cars.

- Example:
  `curl -X DELETE http://localhost:5000/cars/6 `

  ```
  {
  "cars": [
    {
      "id": 1,
      "image_link": "image url",
      "model": "Z-5",
      "name": "BMW"
    },
    {
      "id": 2,
      "image_link": "http://unspalsh-cars",
      "model": "MC-60",
      "name": "Mercedes"
    },
    {
      "id": 4,
      "image_link": "http://...",
      "model": "J-XVII",
      "name": "Jaguar"
    },
    {
      "id": 7,
      "image_link": "http://land-rover-V8",
      "model": "V8",
      "name": "Land Rover"
    }
  ],
  "deleted": 6,
  "message": "Car deleted successfully",
  "success": true,
  "total_cars": 4
  }

  ```

other example `curl -X DELETE http://127.0.0.1:5000/cars/1 `

```
{
  "cars": [
    {
      "id": 2,
      "image_link": "http://unspalsh-cars",
      "model": "MC-60",
      "name": "Mercedes"
    },
    {
      "id": 4,
      "image_link": "http://...",
      "model": "J-XVII",
      "name": "Jaguar"
    },
    {
      "id": 7,
      "image_link": "http://land-rover-V8",
      "model": "V8",
      "name": "Land Rover"
    }
  ],
  "deleted": 1,
  "message": "Car deleted successfully",
  "success": true,
  "total_cars": 3
}


```

#### Search Functionnality with POST /cars

- General: We can search car by the name of the car (case-insensitive) using search_term. It returns an success value, results of the search and total number of results.

- Example:
  `curl -X POST -H "Content-Type: application/json" -d'{"search_term":"rover"}' http://localhost:5000/cars `

  or `curl -X POST -H "Content-Type: application/json" -d'{"search_term":"rover"}' http://127.0.0.1:5000/cars `

```
{
  "results": [
    {
      "id": 7,
      "image_link": "http://land-rover-V8",
      "model": "V8",
      "name": "Land Rover"
    }
  ],
  "success": true,
  "total_results": 1
}

```

## Deployement N/A

## Authors

Randriamananjara Nirinasoa Herilanto

## Acknowledgements

Full-Stack-03 Teams Students, Coachs
