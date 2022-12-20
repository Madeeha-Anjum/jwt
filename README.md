# Welcome to JWT 🚀🚀🚀

JWT is a basic todo app that will implement JSON web token authentication in FastAPI.

## Local development

1. Install [Docker](https://www.docker.com/products/docker-desktop)
2. Run `docker-compose up` to start the server
3. Open [http://localhost:8000](http://localhost:8000) to view it in the browser.
4. Open [http://localhost:8000/docs](http://localhost:8000/docs) to view the API documentation.
  
## Accessing the database

1. Run `docker exec -it <container_name> bash`
2. Run `sqlite3 todos.db`
3. Run `.schema` to see the tables
4. Run `.mode column` or `.mode table` or `.mode box` to see the columns
5. For example setup a row in the todo table:

  ```sql
   sqlite3 todos.db

   INSERT into todos (title, description, priority, complete, owner_id) VALUES ("Feed the dog", "He is hungary",5, false, 1);

   SELECT * FROM todos;

   ```

## Running Code

- `docker compose up` to start the app, postgress, and pgadmin
- open [http://localhost:8000](http://localhost:8000) to view pgadmin.
- Add the server with the following details:
  - Name: `postgres_container`
  - Host name/address: `postgres_container` # this is the IP address of the container
  - username: `${POSTGRES_USER}`
  - password: `${POSTGRES_PASSWORD}`

- `docker compose up -d` to start the app, postgress, and pgadmin
- to see the logs for the app `docker logs app_container -f -t`

# how to do production deployment
<!-- - `docker-compose -f docker-compose.prod.yml up -d --build` -->
- set ENVIROMENT to Production on server
- Create a network
- docker network create app-tier
- docker compose up --env-file ${ENV}.env --build
-  
<!-- EVVIROMENT=production deocker compose up --env fiel -${ENVIRONMENT}.env -->
-
