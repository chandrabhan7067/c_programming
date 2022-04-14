// #include <stdio.h>
// void printArray(int *A, int n)
// {
//     for (int i = 0; i < n - 1; i++)
//     {
//         printf("%d ", A[i]);
//     }
//     printf("\n");
// }

// void merge(int A[], int mid, int low, int high)
// {
//     int i, j, k, B[10];
//     i = low;
//     j = mid + 1;

//     while (i <= mid && j <= high)
//     {
//         if (A[i] < A[j])
//         {
//             B[k] = A[i];
//             i++;
//             k++;
//         }
//         else
//         {
//             B[k] = A[j];
//             i++;
//             k++;
//         }
//     }
//     while (i <= mid)
//     {
//         B[k] = A[i];
//     }
//     while (j <= high)
//     {
//         B[k] = A[j];
//     }
// }
// void merge_sort(int A[], int low, int high)
// {
//     int mid;
//     if (low < high)
//     {
//         mid = low + high / 2;
//         merge_sort(A, low, mid);
//         merge_sort(A, mid + 1, high);
//         merge(A, mid, low, high);
//     }
// }
// int main()
// {
//     int A[] = {4, 7, 10, 14, 3, 1};
//     int n = 6;
//     printArray(A, n);
//     merge_sort(A, 0, 5);
//     printArray(A, n);
// }




