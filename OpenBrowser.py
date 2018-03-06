import webbrowser
import time
count = 0

print("This program started on " + time.ctime())

while (count < 5):
    time.sleep(100)
    webbrowser.open("https://www.youtube.com/watch?v=izGwDsrQ1eQ")
    count=count+1
