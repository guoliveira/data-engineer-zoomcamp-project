## Setup

### Pre-Reqs

1. For the sake of standardization across this config I renamed my gcp-service-accounts-credentials 
   file to `google_credentials.json` & store it in my `$HOME` directory
    ``` bash
        cd ~ && mkdir -p ~/.google/credentials/
        mv /mnt/c/Users/LuisSousaOliveira/Documents/Pessoal/Formação/Capstonecapstone-luis-oliveira-347008-f7e05ab98b8b.json ~/.google/credentials/google_credentials.json
    ```

Created a new sub-directory called `Airflow` in mine `project` dir 

Set the Airflow user using the following commands:

    ```bash
    mkdir -p ./dags ./logs ./plugins
    echo -e "AIRFLOW_UID=$(id -u)" > .env
    ```