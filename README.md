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

**Environment Variables**
Note that all environment variables have default values that can be found in `resources/application.properties` and `resources/redisson.yaml` for demo-app and in `setup/insert_data.py` for insert-data

- APP_HOST_PORT      --> the port for demo-app that is exposed from the host machine (demo-app)
- APP_CONTAINER_PORT --> the port for the demo-app that is exposed from the container (demo-app) (this should **not** change)
- SCRIPT_NAME        --> the name of the data loading script (only needed for docker-compose)
- NUM_ITEMS          --> the number of items/documents to for insert-data script to load into MySQL (insert-data)
- MYSQL_HOST         --> the MySQL host string or IP (demo-app and insert-data)
- MYSQL_PORT         --> the MySQL port (demo-app and insert-data)
- MYSQL_DB           --> the MySQL database name (demo-app and insert-data)
- MYSQL_USER         --> the MySQL username (demo-app and insert-data)
- MYSQL_PASS         --> the MySQL password (demo-app and insert-data)
- REDIS_HOST         --> the Redis host string or IP (demo-app)
- REDIS_PORT         --> the Redis port (demo-app and insert-data)
- REDIS_PASS         --> the Redis password (demo-app and insert-data) (note: if set, the field must be uncommented in `resources/redisson.yaml`!)

**Estimating Dataset Size**
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


   


