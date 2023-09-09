import requests
from bs4 import BeautifulSoup

l=[]
n=[]
nl={}

URL = "https://news.google.com/search?q=Delhi&hl=en-IN&gl=IN&ceid=IN%3Aen"
page = requests.get(URL)

#print(page)

soup = BeautifulSoup(page.content, "html.parser")

#print(soup)

#im = soup.find_all(class_="wsLqz RD0gLb")
name = soup.find_all(class_="DY5T1d RZIKme")

time=soup.find_all(class_="WW6dff uQIVzc Sksgp slhocf")

# ti = soup.find_all(class_="QmrVtf RD0gLb kybdz")

#print("IM",im)
print("Name",name)      

print("Time:",time)

print(len(time))

# print(ti)

#print("F=",f)

for abc in range(0,11):
    c=str(name[abc]).split('" target="_blank">')
    r1=c[1].replace("</a>","")
    datetime=str(time[abc]).split('<time class="WW6dff uQIVzc Sksgp slhocf" datetime="')
    datetime2=datetime[1].split('">')
    print(datetime2[0])
    r2=c[0].replace('<a class="DY5T1d RZIKme" href="',"")
    n.append(r1)
    l.append(r2)
    id_=r2.split('./articles/')
    link = ("https://news.google.com/"+r2)
    id2=id_[1].replace("?hl=en-IN&amp;gl=IN&amp;ceid=IN%3Aen","")
    nl[id2]={"title":r1,"updated_on":{"time":datetime2[0].split("T")[1].replace('Z',''),"date":datetime2[0].split("T")[0]},"link":link}
    
    #print("C=",c)

#print("N=",n)
#print("L=",l)

print(nl)
print(len(nl))
