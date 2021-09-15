from selenium.webdriver import Firefox


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


def find_by_href(browser, link):
    """Encontrar o elemento 'a' com o link 'link'
    Argumentos:
        - browser = Instância do browser [firefox, chrome, ...]
        - link = link que será procurado em todos as tags 'a'
    """

    elementos = browser.find_elements_by_tag_name('a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento


browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')

# elemento_ddg = find_by_text(browser, 'li', 'DuckDuckGo')

elemento_ddg = find_by_href(browser, 'ddg')

"""
1. buscamos ul
2. buscamos todos 'li'
3. No primeiro 'li', buscamos 'a' e pegamos o seu texto

ul
   li
    a
      texto

  li
    a
      texto

"""
