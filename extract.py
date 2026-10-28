import re, sys
path = sys.argv[1]
data = open(path, encoding='utf-8').read()
titles = re.findall(r'"title":"(.*?)"', data)
urls = re.findall(r'"contentUrl":"(.*?)"', data)
for t, u in zip(titles, urls):
    print(t, '|', u)
