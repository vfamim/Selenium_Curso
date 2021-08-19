from selenium.webdriver import Firefox


# vaoms chamar o URL
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

# navegador
browser = Firefox()
browser.get(url)

h1 = browser.find_element_by_tag_name('h1')
ps = browser.find_elements_by_tag_name('p')

list1 = []
list2 = []

for keys in range(3):
    valor = ps[keys].get_attribute('atributo')
    list1.append(valor)
    chaves = ps[keys]
    list2.append(chaves.text)

dictionary = dict(zip(list1, list2))

print(dictionary)

browser.quit()
