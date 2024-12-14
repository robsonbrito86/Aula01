class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if(self.saldo >= valor):
            self.saldo -= valor
        else:
            print('Impossivel realizar a operação')

    def verficar_saldo(self):
        return f'O saldo atual é de {self.saldo}'