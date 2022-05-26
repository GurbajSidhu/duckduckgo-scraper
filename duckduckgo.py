from bs4 import BeautifulSoup
import requests

url = 'https://duckduckgo.com/?q=hello+world&atb=v187-1&ia=web'
response = requests.get(url)

print(response)                          #duckduckgo gives 418 response instead of 200
data = response.text
#print(data)
soup = BeautifulSoup(data, "html.parser")
#print(soup)

jobs= soup.find_all('h2',{'class':'result__title'})
for job in jobs:
    print(job.text)
    #title= job.find('a',{'class':'result__a'}).text
   # print(title)


