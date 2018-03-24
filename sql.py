import requests
from lxml import html	
if __name__ == '__main__':
	print('Please Wait...')
	print('Enter the (sql) word below')
first = input('enter:')
url = 'https://www.w3schools.com/' + first +'/sql_syntax.asp'
a = requests.get(url)
b = a.content
htmlElements = html.fromstring(b)
tree = htmlElements.xpath('//*[@id="main"]/ul[2]')
if first == 'sql':
	print(tree[0].text_content())
else:
    print('Enter the word correctly!!!')