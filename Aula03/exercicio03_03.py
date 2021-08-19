from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html#'

navegador = Firefox()
navegador.get(url)

sleep(2)

p = navegador.find_elements_by_tag_name('p')
a = navegador.find_element_by_tag_name('a')

ps_text = p[-1].text.split()[-1]

a.click()

num_gerado= p[-1].text.split()[-1]


while num_gerado != ps_text:
    a.click()
    num_gerado = p[-1].text[-1]
    num_gerado
