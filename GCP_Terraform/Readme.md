## Step for building a Google Cloud Platform Infrastructure
# Advanced steps to configure GCP

1. After the creation of the GCP project we went into **IAM & Admin** and built a new service account called **developer** and with a Basic Role of Viewer :
![role](https://user-images.githubusercontent.com/12693788/159322475-6297d894-b368-4cb6-8e4c-cb34c1adcf1c.png)

2. At this new service account it was built a KEY in JSON format:

![image](https://user-images.githubusercontent.com/12693788/159325350-23e8ccbd-a1ed-4ba7-b393-7e84a338204d.png)


3. This key was downloaded locally and set as the variable GOOGLE_APPLICATION_CREDENTIALS; 


4. In the IAM section of [IAM & Admin](https://console.cloud.google.com/iam-admin/iam)
It was added the following roles to the service account: Storage Admin + Storage Object Admin + BigQuery Admin


5. The following API were enabled : https://console.cloud.google.com/apis/library/iam.googleapis.com
https://console.cloud.google.com/apis/library/iamcredentials.googleapis.com
   
# Creation of a GCP Infrastructure

1. First it was copy the Terraform files (`main.tf` and `variables.tf`) for the infrastructure creation 
   (For this step it was used the [default files from the Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_1_basics_n_setup/1_terraform_gcp/terraform))

2. At the file `variables.tf` it was changed variable "BQ_DATASET" to have the default value "weather_historical_data";

3. It was applied the following commands to plan the creation of the GCP Infrastructure:
```shell
# Initialize state file (.tfstate)
terraform init

# Check changes to new infra plan
terraform plan -var="project=capstone-luis-oliveira"
```

4. It was applied the following command to create the GCP Infrastructure.
```shell
terraform apply -var="project=capstone-luis-oliveira"
```

It is possible to see below in the GCP console that the Infrastructure was correctly created:
![BiG Query](https://user-images.githubusercontent.com/12693788/159502520-c0f3f7a2-a7eb-467e-b594-8b7ddaf8f769.png)

![image](https://user-images.githubusercontent.com/12693788/159502713-8ba0d753-862d-4578-b450-f0f47b413015.png)

