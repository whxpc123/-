import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

for index in range(3000000, 3158700, 1):

    response = requests.get(f"https://www.douguo.com/cookbook/{index}.html", headers=headers)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    all_titles = soup.findAll("h1", attrs={"class": "title text-lips"})
    all_item = soup.findAll("td", attrs={"class": "lirre"})

    for title in all_titles:
        print("菜名:",end=" ")
        if "/" not in title.string:
            print(title.string)
    for item in all_item:
        itemName = item.find("span", attrs={"class": "scname"})
        print("材料:"+itemName.string,end="  ")
        itemValue = item.find("span", attrs={"class": "right scnum"})
        print(itemValue.string)
    time.sleep(1)

    print("\n\n\n")


