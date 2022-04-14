#include<stdio.h>

void Print_array(int *arr,int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
    
}

void Bubble_sort(int *arr,int n)
{
    int temp;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n-1-i; j++)
        {
            if (arr[j] > arr[j+1])
            {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main()
{
    int arr[] = {3,43,4,1};
    int n = 4;
    Print_array(arr,n);
    Bubble_sort(arr,n);
    Print_array(arr,n);

}