#include <iostream>
using namespace std;

//Compiler version gcc  6.3.0

void printar(int*A, int n)
{
  for(int i =0; i<n; i++)
  {
    cout<<" "<<A[i];
  }
  cout<<"\n";
}

// 1 ,5,4,0,8
// first pass
// 0,1,5,4,8
// second pass
//0,1,5,4,8
// third pass
// 0,1,4,5,8
//fourth pass
// 0,1,4,5,8

void selection_sort(int* A, int n)
{ int indexOfMin , temp;

  cout<<"selection sort is running:\n";
  for (int i=0; i<n-1; i++)
  {
    indexOfMin = i;
    for (int j = i+1; j<n; j++)
    {
      if (A[j]< A[indexOfMin]){
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
  int A[] = {10,5,15,3,13};
  int n =5;
  printar(A,n);
  selection_sort(A,n);
  printar(A,n);
  return 0;
}