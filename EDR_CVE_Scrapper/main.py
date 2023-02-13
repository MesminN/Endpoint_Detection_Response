# This is a sample Python script.
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from edr_cve_graphs import gravite_moyenne_par_solution, jours_moyens_patch_par_solution, nombre_cves_par_solution
from ranking import get_rank_dictionary, display_ranking, plot_ranking


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
    print("1. Gravité moyenne par solution")
    print("2. Nombre de jours moyens avant patch par solution")
    print("3. Nombre de CVE par solution")
    print("4. Rank solutions")
    print("5. Quit!")
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

    for index, url in enumerate(urls):
        html_content = ""
        if index <= 1:
            html_content = browse_for_data(url)
        else:
            response = requests.get(url)
            if response.status_code == 200:
                html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        # print(soup.prettify())
        data = retrieve_data_from_table(soup, 'vulnslisttable', '', 'srrowns')
        vuln_dict[retrieve_product_name(soup)] = data

    print(vuln_dict)
    keep_going = True
    while keep_going:
        choix = display_menu()

        if choix == 1:
            gravite_moyenne_par_solution(vuln_dict)
        elif choix == 2:
            jours_moyens_patch_par_solution(vuln_dict)
        elif choix == 3:
            nombre_cves_par_solution(vuln_dict)
        elif choix == 4:
            ranking_data = get_rank_dictionary(vuln_dict)
            display_ranking(ranking_data)
            plot_ranking(ranking_data)
        elif choix == 5:
            keep_going = False
        else:
            print("Wrong Choice!")
