// selection sort in not stable !
// selection sort is not abaptive !
// sorting in minimum in swap

#include <stdio.h>

void printar(int *A, int n)
{
  for (int i = 0; i < n; i++)
  {
    printf("%d ", A[i]);
  }
  printf("\n");
}

void selection_sort(int *A, int n)
{
  int indexOfMin, temp;

  printf("selection sort is running:\n");
  for (int i = 0; i < n - 1; i++)  // number of pass 
  {
    indexOfMin = i;
    for (int j = i + 1; j < n; j++)  //this for for comparison we compae first number to compare all the number in the list
    {
      if (A[j] < A[indexOfMin])
      {
        indexOfMin = j;
      }
      
    }
    temp = A[i];
    A[i] = A[indexOfMin];
    A[indexOfMin] = temp;
  }
}
int main()
{
  // 1, 5, 4, 6, 0  <<< in first pass minimun aliment is 1 and we are compare 1 to all the numbers
  // 0,1,5,4,6  <<< first pass is complete
  // 0,1,5,4,6  <<< in the second pass value of indexOfMin in 1
  // 0,1,5,4,6  <<< second pass complete
  // 0,1,5,4,6  <<< in the therd pass indexOfMin value is 5
  // 0,1,4,5,6  <<< third pass is complete
  // 0,1,4,5,6  <<< fourth pass indexOfMin value is 5
  // 0,1,4,5,6  <<< fourth pass complete 

  int A[] = {13, 5, 10, 6, 4};
  int n = 5;
  printar(A, n);
  selection_sort(A, n);
  printar(A, n);
  return 0;
}