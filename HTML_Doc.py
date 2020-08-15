class HtmlDocument:
    def __init__(self, tag, word):
        return "<%s>%s</%s>" % (tag, word, tag)


#initialize some HTML for a new document.