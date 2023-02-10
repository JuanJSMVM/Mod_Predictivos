import boto3


# Retrieve the list of existing buckets
s3 = boto3.client('s3')
res_s3 = boto3.resource('s3')
response = s3.list_buckets()
# Output the bucket names
print('\nExisting buckets:')
for bucket in response['Buckets']:
    print(f' {bucket["Name"]}')
response_objs = s3.list_objects(Bucket='bucketzilla218238',MaxKeys=2)


print("\n\nList objects of bucketzilla218238:")
for obj in response_objs['Contents']:
    print(f' {obj["Key"]}')


print("\nUpload file bucket.txt in bucketzilla218238...\n\n")
res_s3.meta.client.upload_file("C:\\Users\\Administrador\\Downloads\\a.txt", 'bucketzilla218238', 'a.txt')




