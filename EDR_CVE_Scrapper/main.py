# This is a sample Python script.

from bs4 import BeautifulSoup
from selenium import webdriver
from firstgraph import first_graph
from secondgraph import second_graph
from thirdgraph import third_graph


def browse_for_data(url):
    driver = webdriver.Edge()
    driver.get(url)

    html = driver.page_source

    driver.quit()
    return html


def retrieve_product_name(b_soup):
    content_div = b_soup.find('div', attrs={'id': 'contentdiv'})
    a_tags = content_div.find('h1').find_all('a')

    name = ''
    for ele in a_tags:
        name += ' '
        name += ele.text.strip()

    return name.strip()


def retrieve_data_from_table(b_soup, table_id, table_class, tr_class):
    data = []
    table_attrs = {}
    if table_id:
        table_attrs['id'] = table_id

    if table_class:
        table_attrs['class'] = table_class

    table = b_soup.find('table', attrs=table_attrs)

    tr_attrs = {}
    if tr_class:
        tr_attrs['class'] = tr_class

    # Read headers

    # Read values
    rows = table.find_all('tr', attrs=tr_attrs)
    for row in rows:
        cols = row.find_all('td')
        selected_cols = []
        for index, ele in enumerate(cols):
            if index >= 8:
                break
            elif index != 2 and index != 3:
                selected_cols.append(ele.text.strip())

        data.append([ele for ele in selected_cols])
    return data


def display_menu():
    print("Bienvenu sur EDR CVE Ranking! Choisissez le diagramme souhaité: \n")
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. Quit!")
    return int(input())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    urls = ["https://www.cvedetails.com/vulnerability-list/vendor_id-76/product_id-34197/year-2017/"
            "Symantec-Advanced-Threat-Protection.html",
            "https://www.cvedetails.com/vulnerability-list/vendor_id-29474/product_id-132532/year-2023/"
            "Cybereason-Endpoint-Detection-And-Response.html",
            "https://www.cvedetails.com/vulnerability-list/vendor_id-16/product_id-114009/year-2022/"
            "Cisco-Secure-Endpoint.html",
            "https://www.cvedetails.com/vulnerability-list/vendor_id-2032/year-2021/Opentext.html"]

    vuln_dict = {}

    for url in urls:
        html_content = browse_for_data(url)

        soup = BeautifulSoup(html_content, 'html.parser')

        # print(soup.prettify())
        data = retrieve_data_from_table(soup, 'vulnslisttable', '', 'srrowns')
        vuln_dict[retrieve_product_name(soup)] = data

    print(vuln_dict)
    keep_going = True
    while keep_going:
        choix = display_menu()

        if choix == 1:
            first_graph(vuln_dict)
        elif choix == 2:
            second_graph(vuln_dict)
        elif choix == 3:
            third_graph(vuln_dict)
        elif choix == 4:
            keep_going = False
        else:
            print("Wrong Choice!")

