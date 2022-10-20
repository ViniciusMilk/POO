#include <stdio.h>
#include <stdlib.h>

typedef struct avl{
    int info; //informação do nó
    int altura; //distância até a folha
    struct avl *esq;
    struct avl *dir;
}RootAVL;

RootAVL * rotacaoDireita( RootAVL * K2 ){
    RootAVL * K1;
    K1 = K2->esq;
    K2->esq = K1->dir;
    K1->dir = K2;
    K2->altura = maior( altura( K2->esq ), altura( K2->dir ) ) + 1;
    K1->altura = maior( altura( K1->esq ), K2->altura ) + 1;
    return K1; //nova raiz
}

RootAVL * rotacaoEsquerda( RootAVL * K1 ){
    RootAVL * K2;
    K2 = K1->dir;
    K1->dir = K2->esq;
    K2->esq = K1;
    K1->altura = maior( altura( K1->esq ), altura( K1->dir ) ) + 1;
    K2->altura = maior( altura( K2->dir ), K1->altura ) + 1;
    return K2; //nova raiz
}

RootAVL * rotacaoEsquerdaDireita( RootAVL * K3 ){
    K3->esq = rotacaoEsquerda( K3->esq );
    return rotacaoDireita( K3 );
}

RootAVL * rotacaoDireitaEsquerda( RootAVL * K1 ){
    K1->dir = rotacaoDireita( K1->dir);
    return rotacaoEsquerda( K1 );
}

RootAVL * insere( int info, RootAVL * arv ){
    if( arv == NULL ){
        arv = aloca(info);
    }
    else if( info < arv->info ){
        arv->esq = insere( info, arv->esq );
    if( altura( arv->esq ) - altura( arv->dir ) == 2 ){
        if( info < arv->esq->info )
        arv = rotacaoDireita( arv );
        else
        arv = rotacaoEsquerdaDireita( arv );
        }
    }

    else if( info > arv->info )
    {
    arv->dir = insere( info, arv->dir );
    if( altura( arv->dir ) - altura( arv->esq ) == 2 )
    {
    if( info > arv->dir->info )
    arv = rotacaoEsquerda( arv );
    else
    arv = rotacaoDireitaEsquerda( arv );
    }
    }
    arv->altura = maior( altura( arv->esq ), altura( arv->dir ) ) + 1;
    return arv;
}
int main(int argc, char const *argv[])
{
    printf("Hello\n");
    return 0;
}
