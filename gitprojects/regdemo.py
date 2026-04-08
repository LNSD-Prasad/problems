import re 
text='''John Doe, 25
Jane Smith, 30
email: user123@gmail.com
email: test.user@yahoo.com
phone: 9876543210
phone: 91234-56789
date: 12-05-2024
date: 2024/05/12
IP: 192.168.1.1
URL: https://example.com '''
pattern=re.compile(r'\d{10}|\d{5}-\d{5}|[a-z0-9A-Z_.]+@[a-z0-9A-Z]+\.[a-zA-Z]+')

result=pattern.findall(text)
print(result)