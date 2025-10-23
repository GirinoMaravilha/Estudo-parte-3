import logging
import time

def configurando_logger():

    ### Variáveis ###

    #Instancia do Logger
    logger = None

    #Handlers
    console_handler = None
    file_handler = None

    #Variavel que armazena a string do horario/data atual
    tempo_atual = ""

    ### Código ###

    #Capturando o valor do tempo atual
    tempo_atual = time.strftime(fr"%H:%M:%S %d-%m-%Y", time.localtime())

    #Configurando o Logger
    logger = logging.getLogger("Bot de Vendas")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    #Criando handler para console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.addFilter(MaxFilter(logging.ERROR))
    console_handler.setFormatter(logging.Formatter(fr"%(message)s - %(asctime)s", datefmt=fr"%H:%M:%S"))

    #Criando handler para logs de erro
    file_handler = logging.FileHandler(f"Error {tempo_atual}.log",delay=True)
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(logging.Formatter(fr"%(message)s - %(levelname)s - %(asctime)s",datefmt=fr"%d-%m-%Y %H:%M:%S"))

    #Adicionando handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    #Retornamos a instancia do Logger
    return logger

class MaxFilter(logging.Filter):

    def __init__(self,level):

        self.level = level
    
    def filter(self,record):

        return record.levelno < self.level


class PrincipalClasse:

    def __init__(self,msg,logger:logging.Logger):

        self.mensagem = msg
        self.logger = logger
    
    def mostrando_mensagem(self):

        self.logger.info("Testando Logger")
        return self.mensagem


def main():

    p = PrincipalClasse("Ola eu sou um teste",configurando_logger())
    p.mostrando_mensagem()


if __name__ == "__main__":

    main()