import boto3
import pandas as pd
from trp import Document
from storing_output import excel_data

class textract_connect:

    def __init__(self):
        #s3 connecting
        self.s3 = boto3.resource(
            service_name='s3',
            region_name='us-east-1',
            aws_access_key_id='', # Give your keys which u created in AWS IAM
            aws_secret_access_key='' # Give your keys which u created in AWS IAM
        )
        # Amazon Textract client connecting
        self.textract = boto3.client('textract', region_name='us-east-1'
                                , aws_access_key_id='' # Give your keys which u created in AWS IAM
                                , aws_secret_access_key='') # Give your keys which u created in AWS IAM

    def print_files(self):
        #  Print out bucket names
        for bucket in self.s3.buckets.all():
            # print(bucket.name)
            pass

    def upload_s3(self):
        # Upload files to S3 bucket
        self.s3.Bucket('bucketname').upload_file(Filename= 'file_name', Key= 'key_name') # give bucket name, filename with path that u want to upload and key name


    def files_display(self):
        # TO see all files/folders in particualr bucket
        for obj in self.s3.Bucket('bucketname').objects.all():
            # print(obj)
            pass


    def ocr(self, filename):
        # Call Amazon Textract and extract like table
        self.response = self.textract.analyze_document(
            Document={
                'S3Object': {
                    'Bucket': 'bucketname', # bucket name
                    'Name': filename  # key name of file present in S3
                }}, FeatureTypes=["TABLES"]) # table format
        return self.response


tex_connect_obj= textract_connect()
tex_connect_obj.upload_s3()
response= tex_connect_obj.ocr('keyname')

doc = Document(response) #after extracting, making it as document

for page in doc.pages:
#     print(type(page))
    for table in page.tables:
#         print(table.rows)
        for r, row in enumerate(table.rows):
#         for row in table.rows:
#             print(row)
            for c, cell1 in enumerate(row.cells):
#                 print(cell)
                print("Table[{}][{}] = {}".format(r, c, cell1.text))
