 **Docker Build**:

When you want to run Airflow locally, you might want to use an extended image, 
    containing some additional dependencies - for example you might add new python packages, 
    or upgrade airflow providers to a later version.
    
   Create a `Dockerfile` pointing to Airflow version you've just downloaded, 
    such as `apache/airflow:2.2.3`, as the base image,
       
   And customize this `Dockerfile` by:
    1. Added your custom packages to be installed. The one we'll need the most is `gcloud` to connect with the GCS bucket/Data Lake.
    2. Integrating `requirements.txt` to install libraries via  `pip install`
    3. Inserting bash commands to set Java env
    4. Inserting commands to download all the necessary files to run Spark 
   
4. **Import the official docker-compose setup file** from the latest Airflow version:
   ```shell
   curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
   ```

5. **Docker Compose**:

    Back in my `docker-compose.yaml`:
    * In `x-airflow-common`: 
        * Removed the `image` tag, to replace it with my `build` from my Dockerfile, as shown
        * Mounted my `google_credentials` in `volumes` section as read-only
        * Set environment variables `GOOGLE_APPLICATION_CREDENTIALS` and `AIRFLOW_CONN_GOOGLE_CLOUD_DEFAULT`
    * Changed `AIRFLOW__CORE__LOAD_EXAMPLES` to `false`;
    * Removed `redis`, `worker`, `triggerer` and `flower` from the file;
    * Set the CoreExecutor to LocalExecutor.    

8. Here's how the final versions:
   - [Dockerfile](./Dockerfile) and 
   - [docker-compose.yml](./docker-compose.yaml).