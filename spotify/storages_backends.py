from storages.backends.s3boto3 import S3Boto3Storage

class CustomS3Boto3Storage(S3Boto3Storage):
    default_acl = None
    object_parameters = {
        'ACL': None,
    }