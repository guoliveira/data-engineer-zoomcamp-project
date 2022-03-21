## Step for building a Google Cloud Platform Infrastruture
# Advanced steps to configure GCP locally

1. After the creation of the GCP project we went into **IAM & Admin** and built a new service account:
![role](https://user-images.githubusercontent.com/12693788/159322475-6297d894-b368-4cb6-8e4c-cb34c1adcf1c.png)

2. At this new service account it was built a KEY in JSON format:

![image](https://user-images.githubusercontent.com/12693788/159325350-23e8ccbd-a1ed-4ba7-b393-7e84a338204d.png)


3. This key was downloaded locally. And then it was set the variable GOOGLE_APPLICATION_CREDENTIALS 


4.In the IAM section of [IAM & Admin](https://console.cloud.google.com/iam-admin/iam)
It was added the following roles to the service account: 
Storage Admin + Storage Object Admin + BigQuery Admin

5. API were enabled : https://console.cloud.google.com/apis/library/iam.googleapis.com
https://console.cloud.google.com/apis/library/iamcredentials.googleapis.com
