url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"

# Limpeza da URL(Primeiro Parametro = O que será substituido e o segundo é o que entrará no lugar)
url = url.replace(" ", "")

# Validação da Url
if url == "":
    raise ValueError("Url Inválida")  # Imprime a String no terminal

# Separa a URL dos Parâmetros:
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1:]

# Busca os Parâmetros
parametro_busca = "moedaDestino"

indice_parametro = url_parametros.find(parametro_busca)
indice_valor_do_parametro = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find("&", indice_valor_do_parametro)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor_do_parametro:]
else:
    valor = url_parametros[indice_valor_do_parametro: indice_e_comercial]

print(valor)
