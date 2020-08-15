import boto3
class AWSManager:
    def __init__(self):
        s3_client = boto3.client('s3')
    def save_to_s3(self):
        boto3.client('s3').upload_file('anish.html', 'lmtd-class', 'anish.html')

    def load_from_s3(self):
        boto3.client('s3').download_file('lmtd-class', 'anish.html', 'anishtamang.html')

    def read_from_s3(self):
        obj = boto3.resource('s3').Object('lmtd-class', 'heyshafan.json')
        print(type(obj))
        data = json.load(obj.get()['Body']) 
        print(data)


#defines the connections to boto3 and some functions that let you save your file to S3.