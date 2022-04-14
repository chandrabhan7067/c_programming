#include <stdio.h>

void printArray(int *A, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", A[i]);
    }
    printf("\n");
}

void bubble_sort(int *A, int n)
{
    int temp;
    for (int i = 0; i < n - 1; i++) //number of pass
    {
        for (int j = 0; j < n - 1 - i; j++) //number of comparision
        {
            if (A[j] > A[j + 1])
            {
                temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
            }
        }
    }
}
int main()
{
    int A[] = {3, 14, 2, 60, 1};
    int n = 5;
    printArray(A, n);
    bubble_sort(A, n);
    printArray(A, n);
    return 0;
}