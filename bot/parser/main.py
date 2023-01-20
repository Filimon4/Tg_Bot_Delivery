import requests
from bs4 import BeautifulSoup
import json


def get_data(url):
    # headers = {
    #      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55'
    # }

    # src = requests.get(url).text

    with open('index.html', 'r', encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    set_list = soup.find_all(class_="product-items")

    dictionary = {}
    for set in set_list:

        image_string = ''

        name_set = set.find_all('li', class_='product-item set')
        for information in name_set:

            # gets set's name
            container = information.find_all('div', class_='product-title')
            for text_name_set_ in container:
                text_name_set = text_name_set_.text
                text_name_set = text_name_set.replace("  ", "")
                text_name_set = text_name_set.replace('\"', '')
                text_name_set = text_name_set.replace('\n', " ")
                dictionary[text_name_set] = {}

            # gets set's cost
            cost = information.find_all('span', class_='price new h3')
            for cost_ in cost:
                text_cost = cost_.text
                dictionary[text_name_set]['cost'] = text_cost

            # gets set's image
            image = information.find_all('a', class_='item-link')
            for image_text in image:
                image_ = image_text.find('img').get('src')
                image_string = 'yaponomaniya.com/' + image_
                dictionary[text_name_set]["img"] = image_string

            # gets set's description
            product_desc = information.find_all("div", class_='product-desc')
            for product_desc_ in product_desc:
                text_desc = product_desc_.text
                text_desc = text_desc.replace('  ', '').replace('\n', " ")
                dictionary[text_name_set]['desc'] = text_desc

    # inject the data into the json file
    # json_path = f"./data/parser/sessions/data_{}.json"
    json_object = json.dumps(dictionary, indent=4, ensure_ascii=False)
    with open('sample', "w", encoding='utf-8') as outfile:
        outfile.write(json_object)


get_data('https://yaponomaniya.com/assorty')