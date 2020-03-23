#/usr/bin/pyhton3

from requests import get
from bs4 import BeautifulSoup, element, NavigableString
import re
#html = "https://tasty.co/recipe/apple-pie-from-scratch"
#response = get(html).text
print("Gotten response")

f = open("/home/marc/Documents/python/waterrecipe/pages/tasty.co.html")

print("Finished parsing")

def tag_visible(elem):
	if elem.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]', 'article']:
		return 0 
	if isinstance(elem, element.Comment):
		return 0
	if elem == "\n" or elem.strip() == "":
		return 0
	return 1

def applyFormatting(elem):
	# formatting
	elem = re.sub(" +", " ", elem)
	return elem

def text_from_html(body):
	soup = BeautifulSoup(body, 'html.parser')
	texts = soup.findAll(text=True)
	visible_texts = map(applyFormatting, filter(tag_visible, texts)) 
	return [t.strip() for t in visible_texts]

print(text_from_html(f))

#	for found in founds:
#	if type(found) is element.Tag and "ingredient" in str(found.attrs):
##		print(found)
#		for child in found.descendants:
#			if type(child) is NavigableString and child != "\n":
#				print(child)
