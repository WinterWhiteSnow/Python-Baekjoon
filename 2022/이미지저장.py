import urllib.request
from bs4 import BeautifulSoup
import requests
header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}

url = #주소
r = requests.get(url,headers=header)
soup = BeautifulSoup(r.text,"html.parser")
# parent_tag = soup.find("div",{"class":"post-body entry-content"}).find_all("div",{"class":"separator"})
parent_tag = soup.find("div",{"class":"write_div"}).find_all("img")
index = 0
for i in parent_tag:
    # link = i["onclick"][19:202]
    link = i["src"]
    print(link)
    # link = i.find("a")["href"]
    urllib.request.urlretrieve(link,f"파일경로 백슬, 그냥 슬래시 다됨!")
    index+=1
    
    
    
