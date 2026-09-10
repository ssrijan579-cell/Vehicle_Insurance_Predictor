import boto3
from dotenv import load_dotenv

from src.constants import REGION_NAME

# Load environment variables from .env
load_dotenv(override=True)


class S3Client:

    s3_client = None
    s3_resource = None

    def __init__(self, region_name=REGION_NAME):
        """
        Creates a connection with the S3 bucket.

        AWS credentials are automatically picked up by boto3.
        On EC2, boto3 uses the attached IAM role.
        """

        if S3Client.s3_resource is None or S3Client.s3_client is None:

            S3Client.s3_resource = boto3.resource(
                "s3",
                region_name=region_name
            )

            S3Client.s3_client = boto3.client(
                "s3",
                region_name=region_name
            )

        self.s3_resource = S3Client.s3_resource
        self.s3_client = S3Client.s3_client
