# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("Corentin")

    # Utilisation de la bibliothèque requests pour réaliser la requête HTTP sur le site web gartner.com
    response = requests.get("https://www.gartner.com/reviews/market/endpoint-detection-and-response-solutions")

    # Vérification de la réponse HTTP
    if response.status_code == 200:
        # Si la réponse est OK, parsing du corps de la réponse avec BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())
    else:
        # Si la réponse n'est pas OK, affichage d'un message d'erreur
        print("Error: Response code {}".format(response.status_code))

    # Utilisation de Selenium pour naviguer sur le site web cvedetails.com
    driver = webdriver.Edge()
    driver.get("https://www.cvedetails.com/")

    # Recherche de la chaîne "Test" sur le site web cvedetails.com
    search_box = driver.find_element_by_name("CVE")
    search_box.send_keys("Test")
    search_box.send_keys(Keys.RETURN)

    # Affichage du corps HTML de la page résultante
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())

    # Fermeture du navigateur
    driver.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
