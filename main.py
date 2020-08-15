from HTML_Mngr import HtmlManager

print('Hello, let us test our S3 skills by uploading an HTML file to AWS S3')
text= input('What would you like to write on the HTML file?')
HtmlManager(text)
