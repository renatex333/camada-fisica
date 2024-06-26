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

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM5"                  # Windows(variacao de)


def main():
    try:
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com1 = enlace(serialName)
        
    
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        com1.enable()
        #Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        print("Eba! Comunicação aberta com sucesso!")
        print("--------------------------")
        #aqui você deverá gerar os dados a serem transmitidos. 
        #seus dados a serem transmitidos são uma lista de bytes a serem transmitidos. Gere esta lista com o 
        #nome de txBuffer. Esla sempre irá armazenar os dados a serem enviados.
        
        #txBuffer = imagem em bytes!
        #Endereço da imagem a ser transmitida
        imageR = "./imgs/rickroll.jpg"
        #Endereço da imagem a ser salva
        imageW = "./imgs/recebidaCopia.jpg"       
            
        #finalmente vamos transmitir os tados. Para isso usamos a funçao sendData que é um método da camada enlace.
        #faça um print para avisar que a transmissão vai começar.
        #tente entender como o método send funciona!
        #Cuidado! Apenas trasmitimos arrays de bytes! Nao listas!
          
        print("Carregando a imagem para transmissão:")
        print(" - {}".format(imageR))
        print("--------------------------")
        txBuffer = open(imageR, 'rb').read()
        start_transmission = time.perf_counter()
        com1.sendData(np.asarray(txBuffer))
        end_transmission = time.perf_counter()
       
        # A camada enlace possui uma camada inferior, TX possui um método para conhecermos o status da transmissão
        # Tente entender como esse método funciona e o que ele retorna
        txSize = com1.tx.getStatus()
        #Agora vamos iniciar a recepção dos dados. Se algo chegou ao RX, deve estar automaticamente guardado
        #Observe o que faz a rotina dentro do thread RX
        #print um aviso de que a recepção vai começar.
        
        print("A recepção dos bytes vai começar!")
        print("--------------------------")
        #acesso aos bytes recebidos
        txLen = len(txBuffer)
        start_reception = time.perf_counter()
        rxBuffer, rxLen = com1.getData(txLen)
        # rxLen = len(rxBuffer)
        end_reception = time.perf_counter()

        #Será que todos os bytes enviados estão realmente guardadas? Será que conseguimos verificar?
        #Veja o que faz a funcao do enlaceRX  getBufferLen

        #print("RxBuffer len = {}".format(rxLen))
        #print("TxBuffer len = {}".format(txLen))

        if txLen == rxLen:
            print("Todos os bytes estão sendo guardados.")
        else:
            print("Algo está errado, os bytes não estão sendo guardados corretamente.")

        
        print("--------------------------")
        print("Salvando dados no arquivo")
        print(" - {}".format(imageW))
        f = open(imageW, 'wb')
        f.write(rxBuffer)

        #Fecha arquivo de imagem
        f.close()
        
        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com1.disable()
        
        print("Tempo de transmissão = {} segundos".format(end_transmission - start_transmission))
        print("Tempo de recepção = {} segundos".format(end_reception - start_reception))
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
