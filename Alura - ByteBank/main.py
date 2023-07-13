from acesso_cep import BuscaEndereco

cep = 13331690
objeto_cep = BuscaEndereco(cep)

rua, bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(rua, bairro, cidade, uf)

