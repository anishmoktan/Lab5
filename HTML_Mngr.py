class HtmlManager:

    def __init__(self, input):
        f = open('anish.html','w')
        message = """<html>
            <head></head>
            body><p>"""+input+"""</p></body>
            </html>"""

        f.write(message)
        f.close()

#defines functions that let you create a new HTML document, and save the document to your files.

