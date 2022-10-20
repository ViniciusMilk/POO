
from operator import le
import os

# Classe Funcionário
class Funcionario:

    # * Inicia a lista de funcionários
    def __init__(self):
        self.lista = []

    # Registra um dicionário de funcionário na lista
    def registerUser(self):
        
        func = {'nome': input('Nome do funcionário: '), 'cpf': int(input('CPF: ')), 'cargo': input("Cargo: "), 'salario': float(input("Salário: ")), 'phone': []}
        func['phone'].append(int(input('Telefone: ')))
        self.lista.append(func)

    # Pesquisa um funcionário dentro da lista
    def searchUser(self):
        if(len(self.lista) == 0):
            print("Impossivel pesquisar funcionário.\tLista vazia.")
            return
        else:
            cpf = int(input("Digite o cpf do funcionário: "))

            for i in self.lista:
                if (cpf  in i.values()):
                    print(i)

    # Registra um novo telefone para um funcionário específico da lista
    def registerPhone(self):
        if(len(self.lista) == 0):
            print("Impossivel registrar telefone para um funcionário.\tLista vazia.")
            return
        else:
            cpfFunc = int(input('Digite o cpf do funcionário que deseja cadastrar o telefone: '))
            tel = int(input('Digite o telefone: '))
            for i in self.lista:
                if (cpfFunc  in i.values()):
                    i['phone'].append(tel)

    # Edita as informações de um funcionário específico da lista
    def editUser(self):
        if(len(self.lista) == 0):
            print("Impossivel editar funcionário.\tLista vazia.")
            return
        else:
            cpfFunc = int(input('Digite o cpf do funcionário que deseja editar: '))
            for i in self.lista:
                if (cpfFunc in i.values()):
                    i['nome'] =  input('Nome do funcionário: ')
                    i['cpf'] =   int(input('CPF: '))
                    i['cargo'] =  input(" Cargo: ")
                    i['salario'] = float(input("Salário: "))
                    i['phone'] = int(input('Telefone: '))

    # Deleta um funcionário da lista
    def deleteUser(self):
        if(len(self.lista) == 0):
            print("Impossivel excluir Funcionário.\tLista vazia.")
            return
        else:
            cpfFunc = int(input('Digite o cpf do funcionário que deseja editar: '))
            for i in range(len(self.lista)):
                if (cpfFunc in self.lista[i].values()):
                    self.lista.pop(i)
    # Imprimi a lista de funcionários
    def printList(self):
        for i in self.lista:
            print(i)
# Variável de controle do switch para opção no menu
opc = 1
# 
def default():
        print("Opção inválida")

# Função que muda o valor da variável de controle do switch para sair do menu   
def exit():
    opc = 0

if __name__ == '__main__':
    
    func = Funcionario() 
    
    while (opc != 0):
        
        print('----------Funcionários----------')
        print('1 - Cadastrar Funcionário')
        print('2 - Pesquisar Funcionário')
        print('3 - Cadastrar Novo telefone')
        print('4 - Editar dados do funcionário')
        print('5 - Deletar Funcionário')
        print('6 - Exibir lista de funcionários')
        print('0 - Sair')
        
        opc = int(input('Opc: '))
        
        switch = {
        1: func.registerUser,
        2: func.searchUser,
        3: func.registerPhone,
        4: func.editUser,
        5: func.deleteUser,
        6: func.printList,
        0: exit
        }
        
        case = switch.get(opc, default)
        case()

    