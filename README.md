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

### 4. Como funcionará a instalação do sistema?


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
Analisar os dados levantados. Demonstrar que as Guiding Questions foram respondidas e que a equipe tem a base necessária para propor a solução.
</p>

## Solution
<p align="justify">
Muitas vezes é possível propor várias propostas de solução. Isso é bom para ajudar na discussão sobre que idéia melhor resolve o problema, quais as vantagens e desvantagens de cada uma delas.
Como neste exemplo é um aplicativo móvel, é interessante ter um protótipo de suas telas. Assim, é possível ter uma noção de como o aplicativo vai ficar, auxiliando enormemente na hora de discutir com especialistas.
</p>
