import re


class Telefone:
    def __init__(self, numero):
        if self.valida_telefone(numero):
            self.numero = numero
            print(self.numero)
        else:
            raise ValueError('Numero de telefone inválido')

    def __str__(self):
        return self.format_telefone()

    def valida_telefone(self, numero):
        padrao_telefone = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        busca = re.findall(padrao_telefone, numero)
        if busca:
            return True
        else:
            return False

    def format_telefone(self):
        padrao_telefone = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        busca = re.search(padrao_telefone, self.numero)
        numero_formatado = "+{}({}){}-{}".format(
            busca.group(1),
            busca.group(2),
            busca.group(3),
            busca.group(4)
        )
        return numero_formatado
