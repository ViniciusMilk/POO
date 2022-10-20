class Conta():
    
    def __init__(self, titular: str, numConta: int, agencia: int, saldo: float):
        self.__setTitular(titular)
        self.__setAgencia(agencia)
        self.__setNumConta(numConta)
        self.__setSaldo(saldo)
        
    def __getTitular(self) -> str:
        return self.__titular
    def __setTitular(self, name: str):
        self.__titular = name
    
    def __getNumConta(self) -> int:
        return self.__numConta
    def __setNumConta(self, numConta: int):
        self.__numConta = numConta
    
    def __getAgencia(self) -> int:
        return self.__agencia
    def __setAgencia(self, agencia: int):
        self.__agencia = agencia
    
    def __getSaldo(self) -> float:
        return self.__saldo
    def __setSaldo(self, saldo: float):
        self.__saldo = saldo
    
    def depositar(self, value: float):
        self.__setSaldo(self.__getSaldo() + value)
        
    def sacar(self, value: float):
        self.__setSaldo(self.__getSaldo() - value)
    
    def print(self):
        print('Titular: ', self.__getTitular(),'\nNúmero da Conta: ', self.__getNumConta(), '\nAgência: ', self.__getAgencia, '\nSaldo: ', self.__getSaldo())

c1 = Conta('Marcos', 123, 202, 100.0)
c2 = Conta('João', 321, 203, 0.0)

def tranferencia(conta1, conta2, value: float):
    conta1.sacar(value)
    conta2.depositar(value)
    
tranferencia(c1, c2, 50.0)

c1.print()
c2.print()