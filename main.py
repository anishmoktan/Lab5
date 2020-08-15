from HTML_Mngr import HtmlManager
from AWS_Mngr import AWSManager

print('Hello, let\'s test our AWS S3 skills by uploading an HTML to a bucket!')

manager = HtmlManager()
manager.create_html()
manager.save_html()

AWS= AWSManager()
AWS.save_to_s3()
AWS.load_from_s3()