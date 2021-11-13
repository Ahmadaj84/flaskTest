import bs4


with open ("about.html",'r') as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt)

# create new link
new_link = soup.new_tag("link", rel="icon", type="image/png", href="img/tor.png", attrs = {"id":"linkss","class":"xyz"})
# insert it into the document
soup.body.insert(3,new_link)
arr = {'x':'This is X', 'y':'This is Y', 'z':'This is Z', 'l':'This is L'}

for k, v in arr.items():
    nTag = soup.new_tag("li" , attrs = {'id':k, 'class':'xyz' })

    soup.body.insert(new_child,nTag)

# save the file again
with open("about.html", "w") as outf:
    outf.write(str(soup))
