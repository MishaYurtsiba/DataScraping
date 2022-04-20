from requests import get
from bs4 import BeautifulSoup

BASE_URL = "http://www.univ.kiev.ua"
URL = f"{BASE_URL}/ua/departments"
ADM_URL = "http://www.univ.kiev.ua/ua/geninf/adm/"

page = get(URL)
soup = BeautifulSoup(page.content,  "html.parser")

with open("univ_kiev.txt", "w", encoding="UTF=8") as file:
    fac_list = soup.find(class_="b-references__holder")
    for li in fac_list.find_all("li"):
        
        a = li.find("a")
        link = a.get("href")
        fac_name = a.find(text=True, recursive=False)
        link = BASE_URL+ a.get("href")
        file.write(f"{fac_name} - {link}\n")
        print(fac_name)
        print(link)

        fac_page = get(link)
        fac_soup = BeautifulSoup(fac_page.content, "html.parser")
        dep_list = fac_soup.find(class_="b-body__holder")
        for dep_ol in dep_list.find_all("ol"):
            for dep_li in dep_ol.find_all("li"):
                dep_name = dep_li.find(text=True, recursive=False)
                if dep_name == None:
                    a = dep_li.find("a")
                    dep_name = a.find(text=True, recursive=False)
                file.write(f"   {dep_name}\n")
                print(dep_name)

    adm_page = get(ADM_URL)
    adm_soup = BeautifulSoup(adm_page.content, "html.parser")
    adm_list = adm_soup.find(class_="b-body__holder")
    h1 = adm_list.find("h1")
    adm_title = h1.find(text=True, recursive=False)
    file.write(f"\n\n{adm_title}\n")
    print(adm_title)
    for adm_div in adm_list.find_all("div"):
        adm_position = adm_div.find("h3", text=True, recursive=False)
        file.write(f"\n{adm_position}\n")
        print(adm_position)
        for adm_ul in adm_div.find_all("ul"):
            adm_name = adm_ul.find("a", text=True, recursive=False)
            file.write(f"    {adm_name}\n")
            print(adm_name)
            for adm_li in adm_ul.find_all("li"):
                adm_info = adm_li.find(text=True, recursive=False)
                if adm_info == None:
                    a = adm_li.find("a")
                    adm_info = a.find(text=True, recursive=False)
                file.write(f"    {adm_info}\n")
                print(adm_info)