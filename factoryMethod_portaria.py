from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def ingressar(seft, nome):
        pass

class Diretor(Pessoa):
    def ingressar(self, nome):
        return f"Olá {nome}, você tem vinculo com a Fatec como: Diretor"

class Coordenador(Pessoa):
    def ingressar(self, nome):
        return f"Olá {nome}, você tem vinculo com a Fatec como: Coordenador"

class Professor(Pessoa):
    def ingressar(self, nome):
        return f"Olá {nome}, você tem vinculo com a Fatec como: Professor"

class Adiministrativo(Pessoa):
    def ingressar(self, nome):
        return f"Olá {nome}, você tem vinculo com a Fatec como: Adiministrativo" 

class Aluno(Pessoa):
    def ingressar(self, nome):
        return f"Olá {nome}, você tem vinculo com a Fatec como: Aluno"

class Vestibulando(Pessoa):
    def ingressar(self,nome):
        return f"Olá {nome}, você tem vinculo com a Fatec como: Vestibulando"

class AnalizaPessoa:
    def criar_acesso(self, tipo_acesso):
        if tipo_acesso == "1":
            return Diretor() 
        elif tipo_acesso == "2": 
            return Coordenador() 
        elif tipo_acesso == "3": 
            return Professor() 
        elif tipo_acesso == "4": 
            return Adiministrativo() 
        elif tipo_acesso == "5": 
            return Aluno() 
        elif tipo_acesso == "6": 
            return Vestibulando() 
        else: 
            raise ValueError("Pessoa não tem nenhum vinculo com a instituição, acompanhar até a secretaria")
analiza_pessoa = AnalizaPessoa()
while True:
    print("\nSeja Bem-vindo a Portaria FATEC!\nPara liberar acesso informe seu vinculo com a instituição")
    print("""Vinculo código ---------------------------- 
     Diretor:         1 
     Coordenador:     2 
     Professor:       3 
     Adiministrativo: 4 
     Aluno:           5 
     Vestibulando:    6 
     Outro:           0 """)

    cod = input("Código da opção de vinculo: ")
    if cod not in ("1","2","3","4","5","6"):
        print("Você não possue Vinculo com a instituição! \nPorfavor se dirija a secretaria")
    else:
        pessoa = analiza_pessoa.criar_acesso(cod)
        print(pessoa.ingressar(input("informe seu nome:")))
    if input("Deseja reiniciar (S/N)?" ) not in ("S", "s"):
        break