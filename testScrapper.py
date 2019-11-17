from lxml import html
import requests

page = requests.get('https://www.earningswhispers.com/calendar')
tree = html.fromstring(page.content)

companyNames = tree.cssselect('div.company')

print 'Company: ', companyNames
