import re


class ExtratorURL:

    def __init__(self, url):
        self._url = self.sanitiza_url(url)
        self.validar_url()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f"URL: {self.url}\n" \
               f"URL Base: {self.get_url_base()}\n" \
               f"Paramêtros da URL: {self.get_url_parametros()}"

    def __eq__(self, other):
        return self.url == other.url

    @staticmethod
    def sanitiza_url(url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validar_url(self):
        if not self.url:
            raise ValueError("URL está Vazia")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        padrao_e_url_match = padrao_url.match(self.url)
        if not padrao_e_url_match:
            raise ValueError("URL não existe")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[: indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor_do_parametro = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor_do_parametro)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor_do_parametro:]
        else:
            valor = self.get_url_parametros()[indice_valor_do_parametro: indice_e_comercial]
        return valor

    def conversao_dolar_real(self):
        moeda_destino = self.get_valor_parametro("moedaDestino")
        moeda_origem = self.get_valor_parametro("moedaOrigem")
        quantidade = int(self.get_valor_parametro("quantidade"))

        real_para_dolar = quantidade * 5.5
        return f"O valor de R${quantidade} convertido para {moeda_destino} é U${real_para_dolar:.0f}"

    @property
    def url(self):
        return self._url


extrator_url = ExtratorURL("bytebank.com.br/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real")
extrator_url_2 = ExtratorURL("bytebank.com.br/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real")

valor_quantidade = extrator_url.get_valor_parametro("quantidade")

print(f"Tamanho da URL é: {len(extrator_url)}")
print(extrator_url)
print(f"Extrator_URL == Extrator_URL_2? {extrator_url == extrator_url_2}")

print(f"Valor do paramêtro quantidade: {valor_quantidade}")
print(f"{extrator_url.conversao_dolar_real()}")
