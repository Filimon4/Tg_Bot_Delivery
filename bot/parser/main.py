import requests
from bs4 import BeautifulSoup
import json
import os.path


def get_data(url):
    src = requests.get(url).content

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
    json_path = None
    json_name = 'eat_data.json'
    json_object = json.dumps(dictionary, indent=4, ensure_ascii=False)

    with open(json_name, "w", encoding='utf-8') as outfile:
        outfile.write(json_object)

    json_path = os.path.abspath(json_name)
    return json_path



# get_data()