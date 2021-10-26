#include <stdio.h>
#include <stdlib.h>
#include <time.h>

time_t t;

typedef struct nodo{
    int row;
    int column;
    int data;
    struct nodo * nextRow;
    struct nodo * nextCol;

}*circleList;

circleList extra;
circleList one;
circleList two;
circleList three;

circleList new(void){
    return NULL;
}

int is_new(circleList c){
    return c == NULL;
}

int first(circleList c){

    return c -> nextCol->data;
    
}

circleList toForm(circleList c , int dato){

    circleList t = (circleList)malloc(sizeof(struct nodo));
    t -> data  = dato;

    if(is_new(c)){
        c = t;
        c -> nextCol = c;
    }

    else{
        t -> nextCol = c -> nextCol;
        c->nextCol =  t;
    }

    return t;
}

void fillMatrix(int **matrix, int n, int m)
{
    
    int i = 0;
    int j = 0;
    for (i = 0; i < n + 1; i++)
    {  
        for (j = 0; j < m + 1; j++)
        {

            if(i == 0){
                matrix[i][j] = 0;
            }
            else{
                if(j == 0){
                    matrix[i][j] = 0;
                }
                else{
                    matrix[i][j] = rand()%10;
                }
            }
           
        }
    }
}

void printMatrix(int **matrix, int n, int m)
{

    int i = 0;
    int j = 0;
    for (i = 0; i < n+1; i++)
    {
        for (j = 0; j < m+1; j++)
        {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
}

//functions in file
int **createMatrix(int n, int m)
{
    
    int i = 0;
    int **matrix = (int **)malloc((n+1) * sizeof(int *));
    for (i = 0; i < n+1; i++)
    {
        matrix[i] = (int *)malloc((m+1) * sizeof(int));
    }

    return matrix;
}

void insert(int ** matrix,int row , int col){
    if(row >=4 || col >= 4){
        printf("El numero de filas y columnas es mayor\n");
    }

    else{

    int dataMatrix = matrix[row][col];

    switch(row){
        case 0: extra = toForm(extra,dataMatrix);break;
        case 1: one = toForm(one,dataMatrix);break;
        case 2: two = toForm(two,dataMatrix);break;
        case 3: three = toForm(three,dataMatrix);break;

    }

    }
  
}

int main(void){

    extra = new();
    one = new();
    two = new();
    three = new();

    int **mat = createMatrix(3, 3);
    fillMatrix(mat,3,3);
    printMatrix(mat,3,3);
    int i = 0;
    //toForm(circleList c , int dato)
    int row = 0;
    int col = 0;

    printf("Value of row :\n");
    scanf("%d",&row);
    printf("Value of col :\n");
    scanf("%d",&col);
    insert(mat,row,col);
    printf("%d\n",three -> data);
   
    return 0;
}