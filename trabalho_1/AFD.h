#ifndef AFD_H
#define AFD_H

typedef struct regras{
   int Einicial;
   char* palavra;
   int* Efinal;
}Transicao;

typedef struct automato{
    char* alfabeto;
    int* estados;
    Transicao funcao;
    int inicial;
    int* final;

}AFD;

// recebe estado inicial e palavra, retorna conjunto de estados finais
int transicao_estendida(int,char*); 


#endif