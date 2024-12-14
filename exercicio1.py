class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.__saldo}")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.__saldo}")

    def get_saldo(self):
        return self.__saldo

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo=0):
        return super().__init__(titular, saldo)

    def render_juros(self):
        juros = self.get_saldo() * 0.005
        self.depositar(juros)
        print(f"Juros de R${juros:.2f} aplicados com sucesso.")

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo=0, limite=500):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        saldo_total = self.get_saldo() + self.limite
        if valor > saldo_total:
            print("Saldo insuficiente (considerando o limite).")
        else:
            saldo_disponivel = self.get_saldo()
            if valor > saldo_disponivel:
                restante = valor - saldo_disponivel
                super().sacar(saldo_disponivel)
                self.limite -= restante
            else:
                super().sacar(valor)

pop = ContaPoupanca('Davi', 1000)
pop.render_juros()
pop.get_saldo()


   
        