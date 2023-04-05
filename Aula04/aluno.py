class Aluno:
    def __init__(self,codigo,nome,matricula):
        self.cod = codigo 
        self.name = nome 
        self.matricula = matricula

    def imprimir(self):
        print(" Aluno: ")
        print(" Nome ",self.name)
        print(" Matricula ",self.matricula)


class AlunoEM(Aluno):
    def __init__(self,codigo,nome,matricula,ano):
        Aluno.__init__(self,codigo,nome,matricula)
        self.ano = ano


    def imprimir(self):
        print(" Aluno: ")
        print(" Nome ",self.name)
        print(" Matricula ",self.matricula)
        print(" Ano ",self.ano)


x  = AlunoEM(None,"Pietro","771800405","2º ano")
x.imprimir()