#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação
####################################################


#esta é a camada superior, de aplicação do seu software de comunicação serial UART.
#para acompanhar a execução e identificar erros, construa prints ao longo do código! 


from enlace import *
import time
import numpy as np
from random import randint

comando_1 = b'\x00\xFF\x00\xFF'
comando_2 = b'\x00\xFF\xFF\x00'
comando_3 = b'\xFF'
comando_4 = b'\x00'
comando_5 = b'\xFF\x00'
comando_6 = b'\x00\xFF'

lista_bytes = [comando_1,comando_2,comando_3,comando_4,comando_5,comando_6]

# Funções para sortear um número de bytes que serão enviados
def quantidade_de_comandos():
    n = randint(10,30)
    return n

# Função que cria uma lista com N comandos e adicionados de forma aleatória
def cria_lista_comandos(n):
    lista_envio = []
    for i in range(n):
        j = randint(0,5)
        lista_envio.append(lista_bytes[j])
    
    return lista_envio

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM4"                  # Windows(variacao de)


def main():
    try:
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com1 = enlace(serialName)
        
    
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        com1.enable()
        #Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        print(com1)
        
        #aqui você deverá gerar os dados a serem transmitidos. 
        #seus dados a serem transmitidos são uma lista de bytes a serem transmitidos. Gere esta lista com o 
        #nome de txBuffer. Esla sempre irá armazenar os dados a serem enviados.
        print("-"*30)
        print("Carregando comandos para transmissão:")
        print("-"*30)
        
        txBuffer = b''
        # Estamos usando o valor 5 em hexadecimal para representar quando um novo comando começa
        # para que o Server consiga identificar o começo de um comando.
        identificador = b'\x05' 
        n = quantidade_de_comandos()
        lista_comandos = cria_lista_comandos(n)
        for c in lista_comandos:
            n_bytes_comando = bytes([len(c)])
            # Envia mensagem composta por: Identificador + Número de bytes no comando + Comando
            txBuffer += identificador + n_bytes_comando + c # Concatena sequência de bytes
        
        # print("txBuffer = {}".format(txBuffer)) # Print para identificar possíveis erros na montagem do txBuffer
        print("txBufferLen = {}".format(len(txBuffer)))
        print("-"*30)

        #finalmente vamos transmitir os dados. Para isso usamos a funçao sendData que é um método da camada enlace.
        #faça um print para avisar que a transmissão vai começar.
        #tente entender como o método send funciona!
        #Cuidado! Apenas trasmitimos arrays de bytes! Nao listas!
          
        print("A transmissão vai começar")   
        print("-"*30)
        time.sleep(1)
        
        # Instituímos um sinal que indica para o Server que a comunicação vai começar. Esse sinal é 
        # chamado "Handshake" e será, neste caso, um array com 1 byte, cujo valor será o tamanho do próximo array a ser enviado
        txBufferLen = bytes([len(txBuffer)])
        print("Handshake = {}".format(txBufferLen))
        print("-"*30)
        print("Transmitindo handshake")
        print("-"*30)
        com1.sendData(np.asarray(txBufferLen))
        # Faz uma pequena pausa para deixar o outro computador receber e processar a mensagem e se preparar para as próximas.
        time.sleep(1)
        print("Transmitindo mensagem")
        print("-"*30)
        # Transmitindo a mensagem que desejamos
        com1.sendData(np.asarray(txBuffer))


        # Agora recebe do Server a quantidade de comandos que foram enviados para garantir que tudo chegou como deveria.      
        print("A Recepção vai comecar")
        print("-"*30)
        #acesso aos bytes recebidos
        rxBuffer, nRx = com1.getData(1)
        
        if nRx == 0:
            print("Timeout de 10 segundos")
            print("-"*30)
            com1.disable()
        
        else:
            print("Recebeu RxBuffer")
            print("-"*30)
            
            # Transformando byte recebido no rxBuffer para int
            n_rxBuffer = int.from_bytes(rxBuffer, byteorder='big')
            print("Quantidade de bytes recebidos pelo Server = {}".format(n_rxBuffer))
            print("-"*30)
            print("Quantidade de bytes enviados pelo Client = {}".format(n))
            print("-"*30)
            
            if n_rxBuffer == n:
                print("Sucesso! O servidor recebeu os comandos enviados")
                print("-"*30)
            else:
                print("Falhou")
                print("-"*30)
            # Encerra comunicação
            print("Comunicação encerrada")
            print("-"*30)
            com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
