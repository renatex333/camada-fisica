# PROJETO 8 - MODULAÇÃO AM
Nesse projeto, seu objetivo é transmitir um áudio que ocupe bandas de baixas frequências (entre 20 Hz e 2.500 Hz) através de um canal de transmissão em que você possa utilizar apenas as bandas entre 10.500 Hz e 15.500 Hz. Após a transmissão via sinal acústico, o receptor, que gravou o sinal transmitido, deverá demodular o sinal e reproduzí-lo de maneira audível novamente. 

### Gráfico 1: Sinal de áudio original normalizado – domínio do tempo.
![Gráfico 1](https://github.com/renatex333/CAMFIS/blob/main/Projeto%208%20-%20Modula%C3%A7%C3%A3o%20AM/Client/Gr%C3%A1fico1.png)
### Gráfico 2: Sinal de áudio filtrado – domínio do tempo. (repare que não se nota diferença).
![Gráfico 2](https://github.com/renatex333/CAMFIS/blob/main/Projeto%208%20-%20Modula%C3%A7%C3%A3o%20AM/Client/Gr%C3%A1fico2.png)
### Gráfico 3: Sinal de áudio filtrado – domínio da frequência.
![Gráfico 3](https://github.com/renatex333/CAMFIS/blob/main/Projeto%208%20-%20Modula%C3%A7%C3%A3o%20AM/Client/Gr%C3%A1fico3.png)
### Gráfico 4: sinal de áudio modulado – domínio do tempo (mais uma vez, não se nota diferença).
![Gráfico 4](https://github.com/renatex333/CAMFIS/blob/main/Projeto%208%20-%20Modula%C3%A7%C3%A3o%20AM/Client/Gr%C3%A1fico4.png)
### Gráfico 5: sinal de áudio modulado – domínio da frequência. (verifique que você não ocupa mais bandas não permitidas!)
![Gráfico 5](https://github.com/renatex333/CAMFIS/blob/main/Projeto%208%20-%20Modula%C3%A7%C3%A3o%20AM/Client/Gr%C3%A1fico5.png)


## DEMOD REALIDADE
### Sinal de áudio demodulado – domínio da frequência.
![Fourier Demodulado](https://github.com/renatex333/CAMFIS/blob/main/Projeto%208%20-%20Modula%C3%A7%C3%A3o%20AM/Server/fourierDemoduladoGravado.png)
### Sinal de áudio demodulado e filtrado – domínio da frequência.
![Sinal Demodulado](https://github.com/renatex333/CAMFIS/blob/main/Projeto%208%20-%20Modula%C3%A7%C3%A3o%20AM/Server/fourierFiltradoGravado.png)

## DEMOD MUNDO IDEAL
### Sinal de áudio demodulado – domínio da frequência.
![Fourier Demodulado](https://github.com/renatex333/CAMFIS/blob/main/Projeto%208%20-%20Modula%C3%A7%C3%A3o%20AM/Server/fourierDemoduladoArquivo.png)
### Sinal de áudio demodulado e filtrado – domínio da frequência.
![Sinal Demodulado](https://github.com/renatex333/CAMFIS/blob/main/Projeto%208%20-%20Modula%C3%A7%C3%A3o%20AM/Server/fourierFiltradoArquivo.png)

