class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def sacar(self, qtd):
        if(qtd <= self.saldo):
            self.saldo -= qtd
        else:
            print('Saldo insuficiente')

    def depositar(self, qtd):
        self.saldo += qtd

    def consultar_saldo(self):
        print(self.saldo)

minha_conta = Conta("Robson")

minha_conta.consultar_saldo()
minha_conta.sacar(200)


minha_conta.depositar(300)
minha_conta.sacar(200)
minha_conta.consultar_saldo()




    