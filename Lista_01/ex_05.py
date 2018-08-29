# Bank account class
class ContaCorrente ():

    # Instance generator
    def __init__ (self, numeroConta, nomeCorrentista, saldo = 0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo
    
    # Changes name
    def alterarNome (self, novoNome):
        self.nome = novoNome
    
    # Deposits cash
    def depositar (self, valor):
        if (valor < 0):
            print ("Você não pode depositar um valor negativo!")
        else:
            self.saldo += valor

    # Withdraw cash
    def sacar (self, valor):
        if (valor > self.saldo):
            print ("Saldo indisponível!")
        else:
            self.saldo -= valor

conta = ContaCorrente("70416-7053X", "Gabriel Gazola Milan", 0.05)
print ("Os dados da conta são: \n - Nome: {}\n - Número da conta: {}\n - Saldo: {}". format(conta.nomeCorrentista, conta.numeroConta, conta.saldo))

print ("Alterando o nome para \"Buda\"")
conta.alterarNome("Buda")
print ("Os dados da conta são: \n - Nome: {}\n - Número da conta: {}\n - Saldo: {}". format(conta.nomeCorrentista, conta.numeroConta, conta.saldo))

print ("Depositando 50 reais")
conta.depositar(50)
print ("Os dados da conta são: \n - Nome: {}\n - Número da conta: {}\n - Saldo: {}". format(conta.nomeCorrentista, conta.numeroConta, conta.saldo))

print ("Retirando 30 reais")
conta.sacar(30)
print ("Os dados da conta são: \n - Nome: {}\n - Número da conta: {}\n - Saldo: {}". format(conta.nomeCorrentista, conta.numeroConta, conta.saldo))
