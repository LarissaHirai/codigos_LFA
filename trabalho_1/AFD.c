#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "AFD.h"

int transicao_estendida(int estado,char* palavra){
    char* novaPalavra;
    novaPalavra= strlen(palavra)-1;
    if(strlen(palavra)==0){
        return estado;
    }else{
        for (int i = 0; i < strlen(palavra) - 1; i++) {
            palavra[i] = novaPalavra[i];
        }
        novaPalavra[strlen(palavra) - 1] = '\0';
        return transicao_estendida(transicao_estendida(estado,novaPalavra),palavra[(strlen(palavra)-1)]);
    }

}