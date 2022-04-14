#include <stdio.h>

void printArray(int *A, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", A[i]);
    }
    printf("\n");
}



void insetion_sort(int *A, int n)
{
    int key, j;

    // Number of pass
    for (int i = 1; i <= n - 1; i++)  // i start with 1 index because we are compare second index number 
    // key = those value that you  compare all the alimants in the list
    //j = j is the index of i-1 number and j is creat only for swap a j and key value

    {
         key = A[i];
        j = i - 1;

        while (j >= 0 && A[j] > key)  // compare key value to all privious values
        // j>0 , 0 is a index of j 
        {
            A[j+1] = A[j];  // swapping 
           
            j--;
        }
        // this line is add last number to the first mnuber mtlb
        // agr hmara j -1 tk chla gya h to hm j+1 means first injex pe key value ko rkh dege

        A[j + 1] = key;
    }
}
// 3, |5, 9, 1, 6  <<< i=1, key=5, j=0
// 3, 5, |9, 1, 6  <<< i=2, key=9, j=1  first pass complete
// 3, 5, 9, |1 ,6  <<< i=3 , key=1, j=2 second pass start
// 3, 5, 1, 9, 6
// 3, 1, 5, 9, 6
// 1, 3, 5, 9, 6  <<< third pass complete

// 1, 3, 5, 9, |6 <<< i=4 , key=6, j=3
// 1, 3, 5, 6, 9 <<<<<< forth pass

int main()
{
    int A[] = {3, 5, 9, 1,6 };
    int n = 5;
 
    printArray(A, n);
    insetion_sort(A, n);
    printArray(A, n);
  
}
