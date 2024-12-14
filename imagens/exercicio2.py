class ContaBancaria:
    def __init__(self, titular, saldo = 0):
        self._titular = titular
        self.__saldo = saldo
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if(self.__saldo >= valor):
            self.__saldo -= valor
        else:
            print('Impossivel realizar a operação')

    def verficar_saldo(self):
        return f'O saldo atual é de {self.__saldo}'
    
    def set_saldo(self, valor):
        self.__saldo = valor
    

minhaConta = ContaBancaria('Davi')
minhaConta.depositar(1000)
print(minhaConta.verficar_saldo())