### Concepts
 [Airflow Concepts and Architecture](1_concepts.md)

### Official Version
 (For the section on the Custom/Lightweight setup, scroll down)

 #### Setup
  [Airflow Setup with Docker, through official guidelines](MainSETUP.md)

 #### Execution
 
  1. The image was built but only on the first time (it was necessary to rebuilt in case of changes of DockerFile):
     ```shell
     docker-compose build
     ```

 2. I initialized the Airflow scheduler, DB, and other config
    ```shell
    docker-compose up airflow-init
    ```

 3. Kick up the all the services from the container:
    ```shell
    docker-compose up
    ```

 4. Login to Airflow web UI on `localhost:8080` with default creds: `airflow/airflow`

 5. Run your DAG on the Web Console.

 7. On finishing your run or to shut down the container/s:
    ```shell
    docker-compose down
    ```

    To stop and delete containers, delete volumes with database data, and download images, run:
    ```
    docker-compose down --volumes --rmi all
    ```


