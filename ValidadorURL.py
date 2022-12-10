import re

url = "https://www.bytebank.com.br/cambio"
padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?(/cambio)?")

padrao_e_url_match = padrao_url.match(url)

if not padrao_e_url_match:
    raise ValueError("URL não existe")
else:
    print("URL Válida")
