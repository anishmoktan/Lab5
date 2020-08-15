class HtmlDocument:
    def __init__(self, content):
        self.content = content


    def __str__(self):
        return (f'{self.content}')


#initialize some HTML for a new document.