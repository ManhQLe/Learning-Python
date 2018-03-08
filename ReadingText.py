import urllib

def read_text():
    file = open("Files\\Text.txt")
    content = file.read()
    print(content)
    check_profanity(content)
    file.close()


def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    out = connection.read()
    print(out)
    connection.close()

read_text()