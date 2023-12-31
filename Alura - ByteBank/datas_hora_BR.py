from datetime import datetime, timedelta


class Data:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_momento()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março", "abril", "junho", "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro - 1]

    def dia_semana(self):
        dias_da_semana = [
            "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira",
            "sexta-feira", "sábado", "domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_da_semana[dia_semana]

    def format_momento(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro
