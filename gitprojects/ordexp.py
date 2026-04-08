import re
text='''ORD-12345 | Name: Ramesh Kumar | Phone: 9876543210 | Email: ramesh@gmail.com
ORD-54321 | Name: Sita Devi | Phone: 9123456780 | Email: sita@yahoo.com
ORD-00001 | Name: Arjun Reddy | Phone: 9988776655 | Email: arjun@outlook.com
ORD-1234  | Name: Ravi Teja | Phone: 98765ABCD | Email: ravi@gmail
ORD-ABCDE | Name: Meena Sharma | Phone: 9123456789 | Email: meena@gmail.com
ORD-99999 | Name: John Paul | Phone: 9000011111 | Email: john@mail.com
ORD_11111 | Name: Anjali Singh | Phone: 8888888888 | Email: anjali@gmail.com
ORD-22222 | Name: Kiran Rao | Phone: 7777777777 | Email: kiran@yahoo.com
ORD-12A45 | Name: Priya Das | Phone: 9999999999 | Email: priya@gmail.com
ORD-33333 | Name: Rohit Verma | Phone: 6666666666 | Email: rohit@company.com'''
pettern=re.compile(r'ORD-[A-Za-z0-9]*')
result=pettern.findall(text)
print(result)