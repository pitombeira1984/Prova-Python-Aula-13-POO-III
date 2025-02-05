
class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def cadastrar(self, titular, saldo):
        titular = input('Digite o nome do titular: ')
        saldo = float(input('Digite o saldo inicial: '))
        self.titular = titular
        self.saldo = saldo

    def deposito(self, valor):
        valor = float(input('Digite o valor do depósito: '))
        self.saldo += valor

    def saque(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor

    def exibir_saldo(self):
        return f'{self.titular}, seu saldo é de: R$ {self.saldo:.2f}'

