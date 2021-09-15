from selenium.webdriver import Firefox
from time import sleep


def find_by_text(browser, tag, text):
    """
    Encontrar o elemeto com o texto
    Argumentos:
        - browser = Instancia do browser [firefox, chrome, ...]
        - text = conteúdo que deve estar na tag
        - tag = tag onde o texto será procurado

    """
    elementos = browser.find_elements_by_tag_name(tag)  # lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento


browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_b.html')

nome_das_caixas = ['um', 'dois', 'tres', 'quatro']

for texto in nome_das_caixas:
    find_by_text(browser, 'div', texto).click()

for nome in nome_das_caixas:
    sleep(1)
    browser.back()

for nome in nome_das_caixas:
    sleep(1)
    browser.forward()

