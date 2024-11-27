# AyomiAssignment
 Création d'une calculatrice en notation polonaise inverse (NPI)


# FastAPI

### How to run
- Learn how to use FastAPI to create a simple REST API : https://www.youtube.com/watch?v=iWS9ogMPOI0 
- Run the server with: `uvicorn main:app --reload`

### How to test (in console)
- Request : GET : `curl -X GET http://127.0.0.1:8000/endpoint_you_want`
- Request : simple POST : `curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/endpoint?value=test'`
- Request : object POST : `curl -X POST -H "Content-Type: application/json" -d '{"text":"apple"}' 'http://127.0.0.1:8000/items'`

### How to test / How to read the doc 
Automatic documentation and easy testing : 
- `http://127.0.0.1:8000/docs#/`
- `http://127.0.0.1:8000/redoc`

### How to understand HTTP error messages 
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status


# Sqlite 3 

### How to run 
- Learn how to use Sqlite 3 to create simple DB : https://www.youtube.com/watch?v=girsuXz0yA8
