#include<stdio.h>

void Bubble_sort(int arr[], int n)
{
    int temp;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n-1-i; j++)
        {
            if (arr[j] > arr[j+1])
            {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

void Alternative_sort(int *arr,int n)
{
    Bubble_sort(arr,n);
    int i = 0;
    int j = n-1;

    while (i<j)
    {
        printf("%d ",arr[i]);
        i++;
        printf("%d ",arr[j]);
        j--;
    }
    if (n%2 != 0)
    {
        printf("%d ",arr[i]);
    }
}

int main()
{
 int a[] = {3,1,5,7,2,8};
 int n = 6;
 Alternative_sort(a,n);   
}