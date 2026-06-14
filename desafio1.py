import time
import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

navegador = Chrome(options=options)


navegador.get('https://books.toscrape.com')

# entra em Mystery
mystery = navegador.find_element(
    By.XPATH,
    '//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li[2]/a'
)
mystery.click()

listaMystery = []

while True:

    livros = navegador.find_elements(
        By.XPATH,
        '//*[@id="default"]/div/div/div/div/section/div[2]/ol/li'
    )

    for livro in livros:

        titulo = livro.find_element(
            By.XPATH,
            './/h3/a'
        ).get_attribute('title')

        valor = livro.find_element(
            By.XPATH,
            './/p[@class="price_color"]'
        ).text

        link = livro.find_element(
            By.XPATH,
            './/h3/a'
        ).get_attribute('href')

        # entra no detalhe

        navegador.get(link)

        estoque = navegador.find_element(
            By.XPATH,
            '//p[contains(@class,"instock")]'
        ).text

        estrelas = navegador.find_element(
            By.XPATH,
            '//p[contains(@class,"star-rating")]'
        ).get_attribute('class')

        # descrição
        try:
            descricao = navegador.find_element(
                By.XPATH,
                '//*[@id="product_description"]/following-sibling::p'
            ).text
        except:
            descricao = ""

        # UPC
        try:
            upc = navegador.find_element(
                By.XPATH,
                '//table[@class="table table-striped"]/tbody/tr[1]/td'
            ).text
        except:
            upc = ""

        listaMystery.append([
            titulo,
            valor,
            estoque,
            estrelas,
            descricao,
            upc
        ])

        navegador.back()
        time.sleep(0.5)


    # tenta achar próximo
    try:
        proxima = navegador.find_element(
            By.XPATH,
            '//*[@id="default"]/div/div/div/div/section/div[2]/div/ul/li[2]/a'
        )

        proxima.click()
        time.sleep(1)

    except:
        break


df = pd.DataFrame(
    listaMystery,
    columns=[
        'titulo',
        'valor',
        'estoque',
        'estrelas',
        'descricao',
        'upc'
    ]
)

df.to_excel("books.xlsx", index=False)
print("\nArquivo books.xlsx criado com sucesso")

# convertendo preço para número
df["valor_num"] = (
    df["valor"]
    .str.replace("£", "", regex=False)
    .astype(float)
)

# extraindo quantidade disponível do estoque
df["quantidade"] = (
    df["estoque"]
    .str.extract(r'(\d+)')
    .astype(int)
)

# resumo
total_livros = len(df)
preco_medio = df["valor_num"].mean()
quantidade_disponivel = df["quantidade"].sum()

print("\n===== RESUMO =====")
print(f"Total de livros: {total_livros}")
print(f"Preço médio: £{preco_medio:.2f}")
print(f"Quantidade disponível: {quantidade_disponivel}")
print("==================")
