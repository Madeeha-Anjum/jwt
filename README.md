# JWT

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

   INSERT into todos (title, description, priority, complete) VALUES ("Feed the dog", "He is hungary",5, false);

   SELECT * FROM todos;

   ```
