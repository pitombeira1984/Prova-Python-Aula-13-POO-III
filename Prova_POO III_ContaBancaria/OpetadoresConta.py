
class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor

    def exibir_saldo(self):
        return f'{self.titular}, seu saldo é de: R$ {self.saldo:.2f}'

# conta = ContaBancaria('João', 0)
# print(conta.exibir_saldo())
# deposito = float(input('Digite o valor do depósito: '))
# saque = float(input('Digite o valor do saque: '))
# conta.deposito(deposito)
# conta.saque(saque)
# print(conta.exibir_saldo())


