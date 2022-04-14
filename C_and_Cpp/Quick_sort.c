#include <stdio.h>

void printArray(int *A, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", A[i]);
    }
    printf("\n");
}
int  partition(int *A, int low, int high)
{
    int pivot = A[low];
    int i = low + 1;
    int j = high;
    int temp;

    do
    {
        while (A[i] <= pivot)
        {
            i++;
        }

        while (A[j] > pivot)
        {
            j--;
        }
        if (i < j)
        {
            temp = A[i];
            A[i] = A[j];
            A[j] = temp;
        }
    } while (i < j); //this loop for swapping index of i is leaser index of j so we swap a low and j

temp = A[low];
A[low] = A[j];
A[j] = temp;
return j;
}

void sort(int A[], int low, int high)
{
    int partitionIndex;
    if (low < high)
    {
        partitionIndex = partition(A, low, high);   //Index of pivat 
         sort(A, low, partitionIndex - 1); // sort left subarray
        sort(A, partitionIndex + 1, high);    // sort right subarray
    }
}
int main()
{   
    // 3 pivot, 5i, 7, 8, 2, 13, 12, 1, 2j    OUr ARRAY IS 
    // 3 pivot, 2i, 7, 8, 2, 13, 12, 1, 5j    swap i and j
    // 3, 2, 7i, 8, 2, 13, 12, 1j, 5          we get i and j value 
    // 3, 2, 1i, 8, 2, 13, 12, 7j, 5          swap i and j
    // 3, 2, 1, 8i, 2j, 13, 12, 7, 5          we get i and j value 
    // 3, 2, 1, 2i, 8j, 13, 12, 7, 5          swap i and j
    // 3, 2, 1, 2j, 8i, 13, 12, 7, 5          we get i and j value  ut i cros a j
    // 2, 2, 1, 3 pivot, 8 ,13, 12, 7, 5      finally we swap a j and pivot number

    // and than we repeat the following staps agian for pivot left side array and pivot right side array

    int A[] = {3, 5, 7, 8, 2, 13, 12, 1, 2 };
    int n = 9;
    printArray(A, n);
    sort(A, 0, n-1);
    printArray(A, n);
    return 0;
}