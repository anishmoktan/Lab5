from HTML_Mngr import HtmlManager
from HTML_Doc import HtmlDocument

print('Hello, let\'s test our AWS S3 skills by uploading an HTML to a bucket!')

tag= input('Please enter the tag you would like to add')
word = input('Please enter the name you would like to add')
comb= HtmlDocument(tag,word)
print("This is what will be stored on the anish.html file: ")
print(word)



text= input('What would you like to write on the HTML file?: ')
HtmlManager(text)

