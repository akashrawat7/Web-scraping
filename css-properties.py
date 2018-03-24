import requests
from lxml import html	
if __name__ == '__main__':
	print('Please Wait...')
url = 'http://www.blooberry.com/indexdot/css/propindex/all.htm'
a = requests.get(url)
b = a.content
htmlElements = html.fromstring(b)
tree = htmlElements.xpath('/html/body')
print(tree[0].text_content())