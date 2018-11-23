//Call all functionalities in python 3 from a C code.

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>	


int main(){
	int x = 1;
	 
	do
	{
	int numb_int = 0;
	printf("------------------------------------\n");
	printf("Bem vindo ao reconhecimento facial !\n");
	printf("------------------------------------\n");
	printf("\n");
	printf("----------------------------------------------------------------------------\n");
	printf("1 -> Novo Cadastro; 2 -> Reconhecimento; 3 -> Modos de alterações; 4 -> Sair:\n");
	printf("----------------------------------------------------------------------------\n");
	scanf("%d", &numb_int);
	system("sudo modprobe bcm2835-v4l2");
	system("clear");

	/* main process */

	switch (numb_int)
        {
        case 1: //register and trainer
        	printf("\n");
        	system("python3 01_cadastro.py");
	 		system("python3 01_face_dataset.py");
			system("python3 02_face_training.py");
			//system("clear");
			printf("\n\n");
		break;

       	case 2: //recognition system
            printf("\n");
        	system("python3 03_facial.py");
        	//system("clear");
			printf("\n\n");
        break;

        case 3: //Editing database functions
            printf("\n");
        	system("python3 00_usuario.py");
        	//system("clear");
			printf("\n\n");
        break;

        case 4:
            printf("-----------------------\n");
			printf("Finalizando programa...\n");
			printf("-----------------------\n");
			//system("clear");
			printf("\n");
			x = 0;
        break;

        default:
           	printf ("\n\nError: Comando não encontrado.\n");
        }

}while(x == 1);
	
	return 0;
}
