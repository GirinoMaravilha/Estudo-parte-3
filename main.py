class PrincipalClasse:

    def __init__(self,msg):

        self.mensagem = msg
    
    def mostrando_mensagem(self):

        return self.mensagem


def main():

    p = PrincipalClasse("Ola eu sou um teste")
    p.mostrando_mensagem()


if __name__ == "__main__":

    main()