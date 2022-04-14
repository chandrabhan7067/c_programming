#include <stdio.h>

void printArray(int *A, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", A[i]);
    }
    printf("\n");
}

void merge(int A[], int mid, int low, int high)
{
    int i, j, k, B[10];
     i = low;
    j = mid + 1;
    k = low;
    while (i <= mid && j <= high)
    // while loop for jb tk mid se phle vala array khtm n ho jaye ya mid+1 se high tk ka array khtm na ho jaye
    {
        if (A[i] < A[j])
        {
            B[k] = A[i];

            i++;
            k++;
        }
        else
        {
            B[k] = A[j];
            j++;
            k++;
        }
    }
    while (i <= mid)  // agr mid se phle vale array ke element khtm ho jate h to pure eliments b array me copy kr lege
    {
        B[k] = A[i];
        i++;
        k++;
    }
    while (j <= high)  // agr mid+1 se high vale array ke elements khtm ho jate h to pure elements b array me copy kr dege 
    {
        B[k] = A[j];
        j++;
        k++;
    }
    for (i = low; i <= high; i++)
    {
        A[i] = B[i];
    }
}

void merge_sort(int A[], int low, int high)
{
    int mid;
    if (low < high)
    {
        mid = (low + high) / 2;
        merge_sort(A, low, mid);
        merge_sort(A, mid + 1, high);
        merge(A, mid, low, high);
    }
}
int main()
{
    int A[] = {3,2,10,9,6};
    int n = 5;

    printArray(A, n);
    merge_sort(A, 0, 4);
    printArray(A, n);
    return 0;
}