import requests
from  lxml import html

if __name__=='__main__':
 print('please wait....')
print('Enter the (tags) word below')
first = input('enter:')
url = 'https://www.w3schools.com/' + first +'/default.asp'
getr = requests.get(url)
srccode = getr.content
htmlElements = html.fromstring(srccode)
tree = htmlElements.xpath('//*[@id="htmltags"]')
if first == 'tags':
	print(tree[0].text_content())
else:
    print('Nothing to show')