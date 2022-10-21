class Conta():
    
    def __init__(self, titular: str, numConta: int, agencia: int, saldo: float):
        self.setTitular(titular)
        self.setAgencia(agencia)
        self.setNumConta(numConta)
        self.setSaldo(saldo)
        
    def getTitular(self) -> str:
        return self.__titular
    def setTitular(self, name: str):
        self.__titular = name
    
    def getNumConta(self) -> int:
        return self.__numConta
    def setNumConta(self, numConta: int):
        self.__numConta = numConta
    
    def getAgencia(self) -> int:
        return self.__agencia
    def setAgencia(self, agencia: int):
        self.__agencia = agencia
    
    def getSaldo(self) -> float:
        return self.__saldo
    def setSaldo(self, saldo: float):
        self.__saldo = saldo
    
    def depositar(self, value: float):
        self.setSaldo(self.getSaldo() + value)
        
    def sacar(self, value: float):
        self.setSaldo(self.getSaldo() - value)
    
    def print(self):
        print('Titular: ', self.getTitular(),'\nNúmero da Conta: ', self.getNumConta(), '\nAgência: ', self.getAgencia(), '\nSaldo: ', self.getSaldo())


def tranferencia(conta1, conta2, value: float):
    conta1.sacar(value)
    conta2.depositar(value)

if __name__ == '__main__':
    
    c1 = Conta('Marcos', 123, 202, 100.0) 
    c2 = Conta('João', 321, 203, 0.0)
    
    tranferencia(c1, c2, 50.0)
    
    c1.print()
    c2.print()