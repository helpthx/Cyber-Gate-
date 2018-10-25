#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>	


int main(){
	int x = 1;
	while(x){
	int inteiro = 0;
	printf("Bem vindo ao reconhecimento facial !\n");
	printf("Digite: 1 - Novo Cadastro, 2 - Reconhecimento, 3 - Modo de alteração e 4 - Sair: ");
	scanf("%d", &inteiro);

	/* processos principal */

	if (inteiro == 1) //Cadastro e treinamento
	{		
		system("python3 01_cadastro.py");	
		system("python3 01_face_dataset.py");
		system("python3 02_face_training.py");
	}
	else if (inteiro == 2) // Reconhecimento 
	{
		system("python3 03_facial.py");
	}
	else if (inteiro == 3) // Reconhecimento 
	{
		system("python3 00_usuario.py");
	}

	else if(inteiro == 4){ // sair 
		printf("Finalizando programa...\n");
		x = 0;
	}


}
	
	return 0;
}