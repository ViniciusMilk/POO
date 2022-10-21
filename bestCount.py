from itertools import count

from random import sample

class Conta():
    
    def __init__(self, titular: str, numConta: int, agencia: int):
        self.__setTitular(titular)
        self.__setAgencia(agencia)
        self.__setNumConta(numConta)
        self.__setSaldo(2)
        
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
        print('Titular: ', self.__getTitular(),'\nNúmero da Conta: ', self.__getNumConta(), '\nAgência: ', self.__getAgencia(), '\nSaldo: ', self.__getSaldo())


def tranferencia(conta1, conta2, value: float):
    conta1.sacar(value)
    conta2.depositar(value)
    
def createCount() -> Conta:
    count = Conta(str(input('Nome do titular da conta: ')), sample(range(10000, 99999)), 101)
    return count

# Variável de controle do switch para opção no menu
opc = 1
    
if __name__ == '__main__':
    
    listCount = list()
    
    c1 = Conta('Marcos', 123, 202, 100.0)
    c2 = Conta('João', 321, 203, 0.0)
    
    tranferencia(c1, c2, 50.0)
    
    c1.print()
    c2.print()
    
    while (opc != 0):
        
        print('----------Funcionários----------')
        print('1 - Criar Conta')
        print('2 - Consultar saldo')
        print('3 - depositar')
        print('4 - Sacar')
        print('5 - Transferir')
        print('0 - Sair')
        
        opc = int(input('Opc: '))
        
        switch = {
        1: listCount.append(createCount()),
        2: (
            num = int(input('Digite o número da conta: '));
            for i in listCount:
                if(i.__getNumConta() == num):
                    a
            ),
        3: func.registerPhone,
        4: func.editUser,
        5: func.deleteUser,
        6: func.printList,
        0: exit
        }
        
        case = switch.get(opc, default)
        case()