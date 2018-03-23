import requests
from lxml import html	
if __name__ == '__main__':
	print('Please Wait...')
username = input('enter the valid username:')
url = 'https://www.codechef.com/users/' + username
a = requests.get(url)
b = a.content
htmlElements = html.fromstring(b)
tree = htmlElements.xpath('/html/body/main/div/div/div/div/div/section[1]/ul/li[6]/span')
if len(tree) == 0:
 print('not a username')
else:
 print(tree[0].text_content())