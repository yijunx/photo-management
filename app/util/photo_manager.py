# some boto3 stuff goes here
from boto3 import client
from botocore.client import Config
from botocore.exceptions import ClientError
from werkzeug.datastructures import FileStorage
from app.config.app_config import conf


class PhotoManager:
    def __init__(self):
        print("Connecting to S3")
        self.client = client(
            service_name="s3",
            endpoint_url=conf.S3_HOST,
            aws_access_key_id=conf.S3_ACCESS,
            aws_secret_access_key=conf.S3_SECRET,
            config=Config(signature_version="s3v4"),
            # verify=conf.CA_CERT_PATH  # if TLS is needed
        )
        print("Creating bucket")
        try:
            self.client.create_bucket(Bucket=conf.S3_BUCKET)
        except ClientError as e:
            print(e)

    def download_file(self, key: str) -> FileStorage:
        f = self.client.get_object(Bucket=conf.S3_BUCKET, Key=key)
        print(f"Type of f['Body'] is {type(f['Body'])}")
        return f["Body"]

    def delete_file(self, key: str) -> None:
        self.client.delete_object(Bucket=conf.S3_BUCKET, Key=key)

    def upload_file(self, file: FileStorage, key: str):
        self.client.put_object(Body=file, Bucket=conf.S3_BUCKET, Key=key)
