#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <iomanip>
#include <gsl/gsl_linalg.h>
#include <gsl/gsl_blas.h>

using namespace std;

void print_mat(double *data,size_t a, size_t b) {
    
    int i,j;
    
    for(i=0;i<a*b;i++)
    {
        cout << data[i] << " ";
        if((i+1)%3 == 0)
            cout << endl;
    }
}

int main() {
    
    int n = 3;
    double A_mat[n*n] = {1,0.67,0.33,0.45,1,0.55,0.67,0.33,1};
    gsl_matrix *A = gsl_matrix_alloc(n,n);
    A->data = A_mat;
    
    int signum=0;
    gsl_permutation *p = gsl_permutation_alloc(n);
    gsl_linalg_LU_decomp(A,p,&signum);
    
    gsl_matrix *L = gsl_matrix_alloc(n,n);
    gsl_matrix *U = gsl_matrix_alloc(n,n);
    gsl_matrix_set_identity(L);
    gsl_matrix_set_identity(L);
    
    
    int i,j;
    double temp;
    
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {   
            temp = gsl_matrix_get(A,i,j);
            if(i>j) {
                gsl_matrix_set(L,i,j,temp);
            }
            
            else gsl_matrix_set(U,i,j,temp);
        }
    }
    
    gsl_matrix *B = gsl_matrix_alloc(n,n);
    gsl_blas_dgemm(CblasNoTrans,CblasNoTrans,1.0,L,U,0.0,B);
    
    cout << "The original matrix:" << endl;
    print_mat(A->data,A->size1,A->size2);
    cout << endl;
    cout << "The matrix L:" << endl;
    print_mat(L->data,L->size1,L->size2);
    cout << endl;
    cout << "The matrix U:" << endl;
    print_mat(U->data,U->size1,U->size2);
    cout << endl;
    cout << "The product of L and U:" << endl;
    print_mat(B->data,B->size1,B->size2);
    
    gsl_matrix_free(A);
    gsl_matrix_free(L);
    gsl_matrix_free(U);
    gsl_matrix_free(B);
    gsl_permutation_free(p);
    
    return 0;
}

