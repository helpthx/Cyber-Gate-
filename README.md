# Cyber Gate

<p align="center">
	<img src="/Imagens/40637444_262471647930542_3437316980447641600_n.jpg" alt="Smiley face" height="300" width="300"></p>

# Desenvolvimento de Software - CBL - 2/2018 

## Resumo
<p align="justify">
É cada vez mais importante o uso de controles de acesso aos mais diferentes ambiente, seja para garantir maior segurança, para restringir acesso a informações sigilosas, para assegurar a integridade de bens ou para simples controle de tempo dos usuários do sistema, tornando-se fundamental a utilização de meios eficientes para a realização desta gestão.
A partir disso foi observado uma grande ineficiência no sistema de controle do Restaurante Universitário da Faculdade do Gama, em que se observa constantes falhas no sistema e filas enormes. Tornando o objetivo do projeto propor uma solução de controle mais eficiente, que gere um sistema capaz de promover maior comodidade aos usuários do restaurante.</p>

## Equipe
João Vitor Rodrigues Baptista 	15/0013329

Igor Sousa		  	              15/0011971

Matheus Pereira		              15/0018304

Nilo Mendonça		                16/0037522

Marcos Cabeceira                15/0051816

Vinicius Porto                  15/0065515


## Tutores
Inclua o nome de profissionais, especialistas, ou outras pessoas que colaboraram no levantamento de informações relevantes para o trabalho.

## Big Idea
Controle de acesso ao Restaurante Universitário da Faculdade do Gama.

## Essential Questions

### 1. O que é controle de acesso?
<p align="justify">
Em termos de segurança, a expressão controle de acesso e utilizada para referenciar a prática de limitar o acesso a determinado ambiente exclusivamente para um grupo de pessoas que possuam autorização para tal.
</p>

### 2. Como são feitos os controles de acesso?
<p align="justify">
Os controles de acesso geralmente são feitos através de pessoas (recepcionistas, guardas, seguranças, …), através de meios mecânicos (portões, cancelas, ...) ou por meios eletrónicos (cartões de acesso, biometria, reconhecimento facial, ...). </p>

### 3. Como é o modelo atual de controle de acesso do objeto de estudo?
<p align="justify">
É extremamente visível que a adoção de métodos de controle de acesso ao qual se faz necessário o uso de filas, possuem como consequência a obstrução do fluxo de pessoas, acarretando por sua vez um sistema gradativamente mais lento. Tendo como objeto de estudo as filas do Restaurante Universitário (RU) da Faculdade do Gama, onde aliado ao modelo de controle de acesso bastante ineficiente, se somam problemas estruturais como a constante queda do sistema, em que torna necessário o uso de sistema de controle manual, necessitando através de um funcionário a verificação individual da identidade de cada usuário.
</p>

### 4. Como funciona o controle de acesso por reconhecimento facial?
<p align="justify">
O rosto é composto por medidas únicas, como o comprimento da linha da mandíbula, a distância entre os olhos, o tamanho do crânio, a largura do nariz, etc. Basicamente o sistema de reconhecimento facial realiza o reconhecimento de tais medidas e através de um banco de dados com as informações dos usuários cadastrados é feito o reconhecimento e autenticação. O sistema é composto principalmente por uma câmera (responsável pela captura da imagem do usuário), um microcontrolador (que possui um algoritmo que realizará o processamento e comparação da imagem capturada pela câmera com imagens do banco de dados), um display (utilizado para exibir informações a respeito do funcionamento do dispositivo) e o banco de dados (onde serão armazenadas as informações a respeito dos usuário).
</p>

### 5. Quais os principais requisitos para o controle de acesso do Restaurante Universitário?
<p align="justify"> Segurança 
Um dos principais requisitos para o sistema, sendo de caráter fundamental a correta identificação do usuário.
Disponibilidade 
O sistema deve permanecer sempre disponível, em caso de haver alguma interrupção ele deve ser restaurado o mais rápido possível.
Viabilidade 
O sistema deve ser viável fisicamente e economicamente.
</p>

## Challenge
<p align="justify">
Obter um sistema de controle de acesso mais eficiente para o Restaurante Universitário da Faculdade do Gama utilizando um sistema de reconhecimento facial.
</p>

## Guiding Questions

### 1. Como será o funcionamento do sistema?
<p align="justify">Os usuários usarão seus rostos para acessar o sistema do RU. Atualmente esse processo é feito através de diferenciamento de código de barras. O que torna o processo bem arcaico e lento.</p>


### 2. Quais os requisitos para funcionamento do sistema?
* Um microcontrolador (a escolha da equipe para o projeto é o Raspberry pi 3B);
* Um modulo de camera para a Raspberry;
* Um display para se mostrar as informações necessárias;
* Uma estrutura para proteger o sistema (case);
* Um software para identificação de faces
* Um banco de dados e dataset de imagens.
* Cabo HDMI;
* Módulo relé 12V;
* Fonte de tensão;
* Conexão com a internet;
* Um ambiente onde se possa manter registro de pessoas e de horários de entrada e saıda da mesma para monitoração (servidor);

### 3. Quais os custo do sistema?
<p align="justify">
Os custos vem da parte de hardware do sistema, como o reconhecimento facial depende muito de uma câmera de qualidade, este componente segue a lógica de quanto melhor a câmera melhor a confiabilidade do sistema e aumenta o preço devido ao fato de boas câmeras serem caras. O resto dos componentes tem um preço mais constante já que são específicos e razoavelmente baratos, levando em consideração a implementação do sistema pela Sanoli, responsável pelo RU da UnB, uma empresa bem estabelecida no mercado.


| Raspberry Pi 3B | Câmera p/ Raspberry Pi 3B | Display LCD | Módulo Relé | Cabo HDM |   Total  |
|:---------------:|:-------------------------:|:-----------:|:-----------:|:--------:|:--------:|
|    R$200-300    |          R$40-300         |   R$89,00   |   R$10,00   |  R$30,00 | R$539,00 |</p>


### 4. Como funcionará a instalação do sistema?
A princípio será desenvolvido um protótipo do projeto que tem o objetivo de demonstrar todas as funcionalidades porém com um número reduzido de usuários cadastrados. 


## Guiding Activities
	

## Guiding Resources
<p align="justify">
TIWARI, Shantnu Face Detection in Python Using a Webcam., Disponivel em: https://realpython.com/face-detection-in-python-using-a-webcam/ i ,Acesso em: 01 set.2018.

MJROBOT, MJRoBot. Real-Time Face Recognition: An End-to-End Project., Disponivel em: https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826 i .,Acesso em: 01 set. 2018.

VICENTIN, TISSIANE. Projeto usa Raspberry e reconhecimento facial para medir produtividade., Disponivel em: https://www.tecmundo.com.br/software/126916-projeto-usa-raspberry-reconhecimento-facial-medir-produtividade.htm i ,Acesso em: 01 set. 2018.

CASSITA, DANIELLE. Reconhecimento facial ajuda polı́cia a identificar suspeito em festival. 2018.,Disponivel em: https://www.tecmundo.com.br/software/133803-reconhecimento-facial-ajuda-policia-identificar-suspeito-festival.htm i .,Acesso em: 01 set. 2018.

CHOWDHURY, Nasimuzzaman. Access Control of Door and Home Security by Raspberry Pi Through Internet. 2018., Disponivel em: https://www.ijser.org/researchpaper/access-control-of-door-and-home-security-by-raspberry-pi-through-internet.pdf i .,Acesso em: 01 set. 2018.
</p>

## Analysis
<p align="justify">
Após estudar o tema proposto e entender melhor o problema levantado, e diversas questões relacionadas existiu uma melhor visão do problema, o que fez existir diversas opiniões de pontos que poderiam ser observados ou mesmo trabalhados para a solução do mesmo, desde formas de identificação tal como servidores e a eletrônica vinculada em hardware para o sistema.
</p>

## Solution
<p align="justify">
Como foco principal de solução é de fato a implementação de um sistema de reconhecimento facial, com um servidor online para a verificação de usuários e registro de créditos. Porém as soluções de contorno foram feitas em torno de um mesmo problema de controle de acesso, por tanto existiu-se o debate sobre a melhor forma de reconhecimento(Facial, código de barras(meio usado atualmente), RFID, QR codes entre outros.).
A criação de servidores foi também de fato trabalhada sobre qual melhor jeito para se armazenar informações seja em memoria interna do dispositivo, ou em um servidor online. Questões essas que levaram a escolha da solução abordada para o desenvolvimento da solução escolhida para a prototipagem e desenvolvimento: O uso do reconhecimento facial 

</p>
