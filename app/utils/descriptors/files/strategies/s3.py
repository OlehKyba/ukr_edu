import boto3


class S3Strategy():

    def __init__(self, bucket_name):

        s3 = boto3.resource('s3')

        self.bucket_name = bucket_name
        self.bucket = s3.Bucket(bucket_name)

        self.location = boto3.client('s3').get_bucket_location(
            Bucket=bucket_name)['LocationConstraint']

    def get_file_link(self, filename):

        url = "https://s3.{}.amazonaws.com/{}/{}".format(
            self.location,
            self.bucket_name,
            filename,
        )

        return url

    def save_file(self, file, filename):
        response = self.bucket.put_object(Key=filename, Body=file)
        return response

    def delete_file(self, filename):
        response = self.bucket.Object(filename).delete()
        return response
