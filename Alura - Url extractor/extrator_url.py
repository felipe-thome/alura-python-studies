import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f'URL: {self.url}\nURL Base: {self.base}\nParâmetros: {self.parametros}'

    def __eq__(self, other):
        return self.url == other.url

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)

        if not match:
            raise ValueError('A URL não é válida')


    @property
    def base(self):
        indice_inter = url.find('?')
        url_base = url[:indice_inter]
        return url_base

    @property
    def parametros(self):
        indice_inter = url.find('?')
        url_parametros = url[indice_inter + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.parametros.find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.parametros.find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.parametros[indice_valor:]
        else:
            valor = self.parametros[indice_valor:indice_e_comercial]
        return valor


url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
extrator_url = ExtratorURL(url)

valor_dolar = 5.5
moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
quantidade = extrator_url.get_valor_parametro('quantidade')

if moeda_origem == 'real' and moeda_destino == 'dolar':
    valor_convertido = int(quantidade) / valor_dolar
    print(f'O valor de R${quantidade} reais é igual a ${str(valor_convertido)} dolares')
elif moeda_origem == 'dolar' and moeda_destino == 'real':
    valor_convertido = int(quantidade) * valor_dolar
    print(f'O valor de ${quantidade} dolares é igual a ${str(valor_convertido)} reais')
