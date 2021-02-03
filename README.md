# Spring Boot + Hibernate + Redis + MySQL Demo

## Overview
A sample application that demonstrates using Redis/Redis Enterprise as a second-level cache for Hibernate.
MySQL is used as the backend database in this example.

The script _setup/insert_data.py_ is used to load sample data (InitObjects) into the backend database. 

The Spring Boot app exposes 2 endpoints for fetching data:
- `/init` --> fetch all InitObjects from the database (or cache)
- `/init/{id}` --> fetch a single InitObject with id=`{id}` from the database or cache

## Prerequisites
- Docker

## Running the Demo
### Configuration
- To prevent data load on start-up, change the *demo-app* env var `LOAD_ON_STARTUP` to `"false"` in *.env*
- To edit the number of documents loaded into the database, change the *load-data* env var `NUM_ITEMS` to the desired count in *.env*

####Estimating Dataset Size
Adjust the number of documents loaded into the database with the `NUM_ITEMS` env var for the *load-data* service.
TODO - add table

### Running all demo containers
1. Start the containers with: `docker-compose up`
2. Load data by sending an HTTP request, e.g.
   - `curl localhost:8080/init` to load all data (first attempt will load from backend database)
   - **Note:** the application will attempt to fetch data upon startup, but the first attempt will reach an empty database if the _insert_data_ script is not complete
3. Repeat data load to load data from cache 

### To stop
1. `Crtl+C`
2. Stop any additional running containers attached to the network (e.g. `docker stop hibernatedemo_demo-app_2`)
3. `docker-compose down`

### Running another instance of the demo Spring Boot app
Once all containers are up and running from *docker-compose*, you can startup more instances of the Spring Boot application.
Each instance will attempt to immediately load data on startup if the `LOAD_DATA_ON_STARTUP` enviornment variable is set to "true".
To run:
1. `docker run --network hibernate-demo-network --env-file .env -p <host-port>:8080 --name <container-name> hibernatedemo_demo-app`
    - e.g. `docker run --network hibernate-demo-network --env-file .env -p 8081:8080 --name hibernatedemo_demo-app_2 hibernatedemo_demo-app`


   


