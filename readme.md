# Credit Policy verification app

This application is created for learning and presentation purpose.

Within this application I have tried to demonstrate how you can build multi 
rule checker design pattern which can be applied to any data model. Data 
model could be REST API request object or various fields from database.

In this application we have build the pattern and demonstrated with REST API
 request validation where multiple rules will applied to request data and 
 result will be thrown based on rules defined.
 
#### Dependencies

To run this application you need to have
```
- python3
- Docker (version > 2)
```
installed on your machine.

### Test and Run this application
```
cd <project-dir>
docker build -t policy:latest .
docker-compose up [-d]
```

``docker-compose`` command it will first execute test cases and then run the
 app on port 5000. It's been done intentional to showcase that test cases 
 has been written and executed before running the app.

