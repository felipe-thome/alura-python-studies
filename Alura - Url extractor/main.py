
url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'

# Sanitização da URL
url = url.replace(' ', '')

if url == '':
    raise ValueError('A URL está vazia')


indice_inter = url.find('?')
url_base = url[:indice_inter]
print(url_base)

url_parametros = url[indice_inter + 1:]
print(url_parametros)

parametro_busca = ''
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)


