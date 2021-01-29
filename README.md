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
1. Start the containers with: `docker-compose up`
2. Load data by sending an HTTP request, e.g.
   - `curl localhost:8080/init` to load all data (first attempt will load from backend database)
3. Repeat data load to load data from cache 

### Configuration
- To prevent data load on start-up, change the _demo_app_ environment variable `LOAD_ON_STARTUP` to `"false"` in _docker-compose.yaml_

### To stop
1. `Crtl+C`
2. `docker-compose down`