import boto3
import os

# Constants
MODEL_PUSHER_S3_KEY = "model-registry"

# Retrieve AWS credentials from environment variables
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID_ENV_KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY_ENV_KEY")

# Initialize the S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name="eu-central-1"  # Specify the desired region
)

try:
    # Fetch the list of all buckets
    buckets = s3.list_buckets()
    print(f"Total Buckets Found: {len(buckets['Buckets'])}")
    
    # Display detailed information for each bucket
    print("\nBucket Information:")
    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        creation_date = bucket['CreationDate']
        
        # Fetch region of the bucket
        region = s3.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
        
        # Display bucket information
        print(f"Bucket Name: {bucket_name}")
        print(f"  - Creation Date: {creation_date}")
        print(f"  - Region: {region}")
        
        # Check for model registry key existence
        model_key_path = f"{MODEL_PUSHER_S3_KEY}/"
        print(f"  - Checking for Model Registry Key: {model_key_path}")
        
        # List objects with the specified key prefix
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=model_key_path)
        if 'Contents' in response:
            print(f"  - Model Registry Key Exists: Yes")
            for obj in response['Contents']:
                print(f"    - Object: {obj['Key']} | Size: {obj['Size']} bytes")
        else:
            print(f"  - Model Registry Key Exists: No")
        
        print("-" * 30)

except Exception as e:
    print(f"An error occurred: {str(e)}")
