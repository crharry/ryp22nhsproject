from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        tag.replace(" ", "")
        if tag in containsdata:
            print('{"',tag, '"')
        else:
            print('"',tag, '" : [')

    def handle_endtag(self, tag):
        print("]")

    def handle_data(self, data):
        print(':"', data, '"}')
containsdata = ["title","h1"]
parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
