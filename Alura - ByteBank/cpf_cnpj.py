from validate_docbr import CPF
from validate_docbr import CNPJ


# Factory
class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError('Qauntidade de caracteres inválida!')


class Cpf:
    def __init__(self, numero):
        if self.cpf_eh_valido(numero):
            self.cpf = numero
        else:
            raise ValueError('CPF invalido !!!')

    def __str__(self):
        return self.format_cpf()

    def cpf_eh_valido(self, numero):
        validador = CPF()
        return validador.validate(numero)

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class Cnpj:
    def __init__(self, numero):
        if self.cnpj_eh_valido(numero):
            self.cnpj = numero
        else:
            raise ValueError('CNPJ inválido!!!')

    def __str__(self):
        return self.format_cnpj()

    def cnpj_eh_valido(self,numero):
        validador = CNPJ()
        return validador.validate(numero)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

