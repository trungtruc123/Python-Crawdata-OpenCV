import urllib.request
import re
import urllib.parse

url='https://pythonprogramming.net/python-3-tkinter-basics-tutorial/'
value ={'s':'basic',
        'submit':'search'}
data = urllib.parse.urlencode(value)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraph =re.findall(r'<p>(.*?)</p>',str(respData))
for each in paragraph:
       print(each)
