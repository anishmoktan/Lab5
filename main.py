from HTML_Mngr import HtmlManager

print('Hello, let\'s test our AWS S3 skills by uploading an HTML to a bucket!')

manager = HtmlManager()
manager.create_html()
manager.save_html()
