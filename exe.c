//Call all functionalities in python 3 from a C code.

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>	


int main(){
	int x = 1, y = 1;
	printf("------------------------------------\n");
	printf("Para acessar remotamente o servidor!\n");
	printf("Esse é o endereço de ip acessável\n");
	system("hostname -I");
	printf("Use:\n");
	printf("https//xxx.xxx.xxx.xxx/index/index/.html\n");
	printf("ou\n");
	printf("https//xxx.xxx.xxx.xxx/index\n");
	printf("------------------------------------\n");
	printf("Ativando a camera pi\n");
	//system("sudo modprobe bcm2835-v4l2");
	printf("------------------------------------\n");
		 
	 
	do
	{
	int numb_int = 0, numb_ref = 0;
	
	printf("------------------------------------\n");
	printf("Bem vindo ao reconhecimento facial !\n");
	printf("------------------------------------\n");
	printf("\n");
	printf("-------------------------------------------------------------------------------\n");
	printf("1 -> Novo Cadastro; 2 -> Iniciar refeição; 3 -> Modos de alterações; 4 -> Sair:\n");
	printf("-------------------------------------------------------------------------------\n");
	scanf("%d", &numb_int);
	
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
       	do{
       		printf("-----------------------------------------------------\n");
			printf("Selecione uma refeição para inicar o reconhecimento !\n");
			printf("-----------------------------------------------------\n\n");
			printf("--------------------------------\n");
			printf("1 - Para iniciar: Café da manhã.\n");
			printf("2 - Para iniciar: Almoço.\n");
			printf("3 - Para iniciar: Janta.\n");
			printf("4 - Para voltar ao menu inicial.\n");
			printf("--------------------------------\n\n");
			scanf("%d", &numb_ref);
			
			switch (numb_ref){
				case 1:
					printf("-----------------------------------\n");
					system("echo  Café da manhã foi iniciado às:");
					system("date");
					printf("-----------------------------------\n\n");
					//escrita no log
					system("echo  >> log_refeicoes.txt");
					system("echo --------------------------------- >> log_refeicoes.txt");
					system("echo O Café da manhã foi iniciado às: >> log_refeicoes.txt");
					system("date  >> log_refeicoes.txt");
					system("echo --------------------------------- >> log_refeicoes.txt");
					
					sleep(5);
					//system("python3 03_facial.py");
			       	

			       	printf("-----------------------------------\n");
					system("echo  Café da manhã foi terminado às:");
					system("date");
					printf("-----------------------------------\n\n");
					
					system("echo  >> log_refeicoes.txt");
					system("echo --------------------------------- >> log_refeicoes.txt");
					system("echo O Café da manhã foi terminado às: >> log_refeicoes.txt");
					system("date  >> log_refeicoes.txt");
					system("echo --------------------------------- >> log_refeicoes.txt");
			       	y = 0;
		       	break;

		       	case 2:
			       	
			       	printf("-----------------------------------\n");
					system("echo O Almoço foi iniciado às:");
					system("date");
					printf("-----------------------------------\n\n");
					//escrita no log
					system("echo  >> log_refeicoes.txt");
					system("echo --------------------------------- >> log_refeicoes.txt");
					system("echo O Almoço foi iniciado às: >> log_refeicoes.txt");
					system("date  >> log_refeicoes.txt");
					system("echo --------------------------------- >> log_refeicoes.txt");
					
					sleep(5);
					//system("python3 03_facial.py");
			       	

			       	printf("-----------------------------------\n");
					system("echo O Almoço foi terminado às:");
					system("date");
					printf("-----------------------------------\n\n");
					
					system("echo  >> log_refeicoes.txt");
					system("echo --------------------------------- >> log_refeicoes.txt");
					system("echo O Almoço foi terminado às: >> log_refeicoes.txt");
					system("date  >> log_refeicoes.txt");
					system("echo --------------------------------- >> log_refeicoes.txt");

			       	y = 0;
		       	break;

		       	case 3:
			      
			       	printf("-----------------------------------\n");
					system("echo O Jantar foi iniciado às:");
					system("date");
					printf("-----------------------------------\n\n");
					//escrita no log
					system("echo  >> log_refeicoes.txt");
					system("echo --------------------------------- >> log_refeicoes.txt");
					system("echo O Jantar foi iniciado às: >> log_refeicoes.txt");
					system("date  >> log_refeicoes.txt");
					system("echo --------------------------------- >> log_refeicoes.txt");
					
					sleep(5);
					//system("python3 03_facial.py");
			       	

			       	printf("-----------------------------------\n");
					system("echo O Jantar foi terminado às:");
					system("date");
					printf("-----------------------------------\n\n");
					
					system("echo  >> log_refeicoes.txt");
					system("echo --------------------------------- >> log_refeicoes.txt");
					system("echo O Jantar foi terminado às: >> log_refeicoes.txt");
					system("date  >> log_refeicoes.txt");
					system("echo --------------------------------- >> log_refeicoes.txt");

			       	y = 0;
			       	break;

		       	case 4:
		            printf("---------------------------\n");
					printf("Voltando para menu inicial.\n");
					printf("---------------------------\n");
					//system("clear");
					printf("\n");
					y = 0;
					break;

				default:
           		printf ("\n\nError: Comando não encontrado.\n");
			}
       


		}while(y == 1);
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
