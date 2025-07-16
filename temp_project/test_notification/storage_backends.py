# test_notification/storage_backends.py
from storages.backends.s3boto3 import S3Boto3Storage

class SupabaseStorage(S3Boto3Storage):
    bucket_name = 'your-supabase-bucket-name'
    default_acl = 'public-read'
