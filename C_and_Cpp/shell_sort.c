#include <stdio.h>

void printArray(int A[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", A[i]);
    }
    printf("\n");
}

void sell_sort(int A[], int n)
{
    int gap = n / 2;
    int i;
    int temp;
    while (gap > 0)
    {
        i = gap;
        while (i < n)
        {
            if (A[i - gap] > A[i])
            {
                temp = A[i - gap];
                A[i - gap] = A[i];
                A[i] = temp;
            }
            i++;
        }
        gap /= 2;
    }
}

int main()
{
    int A[] = {3, 5, 9, 1, 6};
    int n = 5;
    printArray(A, n);
    sell_sort(A, n);
    printArray(A, n);
}