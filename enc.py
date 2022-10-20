class Professor:
    def __init__(self, nome, matricula, campus, salario) -> None:
        self.__nome = nome
        self.__matricula = matricula
        self.__campus = campus
        self.__salario = salario
    def __getNome(self):
        return self.__nome
    def __setNome(self,nome) -> None:
        self.__nome = nome

if __name__ == '__main__':
    print('Hello')