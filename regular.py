import re
string ='''
I am Tran Trung Truc .I live Quang Nam
I am 24 years old, 15 , 97, 102
'''
age =re.findall(r'\d{1,3}',string)
name =re.findall(r'[A-Z][a-z]*',string)
print(age)
print(name)