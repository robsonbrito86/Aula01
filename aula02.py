class Conta:
    def __init__(self, titular, saldo, cpf, conta):
        self._titular=titular
        self._saldo=saldo
        self._cpf=cpf
        self._conta=conta
    
    
    def sacar(self,qtd):
        if (qtd <= self.saldo):
            self._saldo -= qtd
        else:
            ("saldo insuficiente")

    def depositar(self, qtd):
        self.saldo += qtd
    
    def ver_saldo(self):
        print(self._saldo)
            
minha_conta = Conta('Robson', 2000)
minha_conta.ver_saldo()
minha_conta.depositar(10)