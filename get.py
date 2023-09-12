import boto3

def get_csv_from_s3(bucket_name, s3_key, file_name):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name,s3_key,file_name)
        print("File dowload successfully to s3")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

bucket_name = 'yashchauhan7990916474'
file_name = 'yash3.csv'
s3_key = 'y@shchauhan.83_accessKeys.csv'

get_csv_from_s3(bucket_name,s3_key,file_name)