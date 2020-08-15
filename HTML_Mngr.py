from HTML_Doc import HtmlDocument
class HtmlManager:

    def __init__(self):
        self.document= None #object but not right now

    def create_html(self):
        message2 = """<html>
            <head></head>
            <body><p> Buddha Blessed 🙏 </p></body>
            </html>"""
        message = """<img src="https://images.homedepot-static.com/productImages/3aaa74d2-7f2c-4b16-8b24-f369f2af8c1d/svn/alpine-corporation-garden-statues-gem170-64_1000.jpg"
            alt="The Buddha"
            width="300"
            height="300"
            title="The Buddha">"""
        new_doc=HtmlDocument(message +message2)
        self.document=new_doc
    
    def save_html(self):
         f = open('anish.html','w')
         f.write(self.document.content)
         f.close()

#defines functions that let you create a new HTML document, and save the document to your files.

