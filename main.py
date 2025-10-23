import logging
import time

def configurando_logger():

    tempo_atual = time.strftime("%d-%m-%Y %H:%M:%S",time.localtime())

    logger = logging.getLogger("Estudo 3")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(fr"%(message)s - %(asctime)s",datefmt="%H:%M:%S"))
    stream_handler.addFilter(MaxFilter(logging.ERROR))

    file_handler = logging.FileHandler(f"Error {tempo_atual}.log")
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(logging.Formatter(fr"%(message)s - %(levelname)s - %(asctime)s", datefmt="%H:%M:%S"))

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

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