import re 
text='''Musk in 2025
Born	Elon Reeve Musk
June 28, 1971 (age 54)
Pretoria, South Africa
Citizenship	
South Africa
Canada
United States (since 2002)
Education	University of Pennsylvania (BA, BS)
Occupations	
CEO and product architect of Tesla
Founder, CEO, and chief engineer of SpaceX
Founder and CEO of xAI
Founder and CTO of X Corp.
Co-founder of Neuralink, the Boring Company, OpenAI, Zip2, and X.com (part of PayPal)
President of the Musk Foundation
Political party	Independent
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Children	14[a] (publicly known), including Vivian Wilson
Parents	
Errol Musk (father)
Maye Musk (mother)
Relatives	Musk family
Awards	Full list'''
find=re.compile(r'age (\d+)')
result=find.findall(text)
print(result)