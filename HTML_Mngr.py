from HTML_Doc import HtmlDocument
class HtmlManager:

    def __init__(self):
        self.document= None #object but not right now

    def create_html(self):
        message = """<html>
            <head></head>
            <body><p> Yo It's Woke Anish </p></body>
            </html>"""
        new_doc=HtmlDocument(message)
        self.document=new_doc
    
    def save_html(self):
         f = open('anish.html','w')
         f.write(self.document.content)
         f.close()

#defines functions that let you create a new HTML document, and save the document to your files.

