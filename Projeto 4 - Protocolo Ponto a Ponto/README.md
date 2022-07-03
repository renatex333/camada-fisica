# PROJETO 4 – PROTOCOLO DE COMUNICAÇÃO UART PONTO-A-PONTO
Ano de 2026. Agora você é um(a) engenheiro(a) de computação recém-contratado(a) para desenvolver a comunicação entre 
sensores de campo (que enviam dados periodicamente) e aplicações locais que armazenam os dados em um banco SQL. Os 
sensores não têm a funcionalidade de envio de dados via protocolo TCP-IP, porém têm um processador que pode rodar uma 
aplicação Python e também possui um chip UART, podendo comunicar-se serialmente.
Você então tem a tarefa de implementar uma aplicação para os sensores se comunicarem serialmente com padrão UART de 
maneira segura, sem perda de dados. A comunicação deve ser feita para envio de arquivos para os servidores, sendo uma rotina 
de envio executada pelo sensor toda vez que este tem um arquivo a ser enviado.
