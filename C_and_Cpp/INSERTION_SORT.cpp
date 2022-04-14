#include<iostream>
using namespace std;
void printArray(int *A, int n)
{
    for (int i = 0; i < n; i++)
    {
        cout<< " "<<A[i];
    }
        cout<< "\n";
}
void insetion_sort(int *A, int n)
{   int key , j;
    for (int i = 1; i < n-1; i++)
    { 
         key = A[i];
         j = i-1;
        while (j>=0 && A[j]>key)
        {
            A[j+1] = A[j];
            j--;
        }
        A[j+1] =  key;
    }
    
        // this line is add last number to the first mnuber mtlb
// agr hmara j -1 tk chla gya h to hm j+1 means first injex pe key value ko rkh dege

        A[j + 1] = key;
    }

// 3, |5, 9, 1, 6  <<< i=1, key=5, j=0
// 3, 5, |9, 1, 6  <<< i=2, key=9, j=1  first pass complete
// 3, 5, 9, |1 ,6 <<< i=3 , key=1, j=2 second pass start
// 3, 5, 1, 9, 6
// 3, 1, 5, 9, 6
// 1, 3, 5, 9, 6 <<<<<<<<<< third pass complete

// 1, 3, 5, 9, |6 <<< i=4 , key=6, j=3
// 1, 3, 5, 6, 9 <<<<<< forth pass

int main()
{
    int A[] = {3, 5, 9, 1, 6};
    int n = 5;
    printArray(A, n);
    insetion_sort(A, n);
    printArray(A, n);
}
