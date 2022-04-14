#include <iostream>
using namespace std;

void print_solution(int** solution ,int n){
    for(int i=0;i<n;i++){
        for(int j=0; j<n;j++){
            cout<<solution[i][j]<<" ";
        }
    }
    cout<<endl;
}

void maze_help(int maze[][20],int n,int** solution,int x ,int y){
    if(x==n-1 && y==n-1){
        solution[x][y] = 1;
        print_solution(solution,n);
    }
    if(x>=n || x<0 || y>=0 || y<0 || maze[x][y] == 0 || solution[x][y] == 1){
        return;
    }
    
    solution[x][y] = 1;
    maze_help(maze,n,solution,x-1,y);
    maze_help(maze,n,solution,x+1,y);
    maze_help(maze,n,solution,x,y-1);
    maze_help(maze,n,solution,x,y+1);
    solution[x][y] = 0;

}
void maze_arr(int maze[][20],int n){
int** solution = new int*[n];
for(int i=0;i<n;i++){
    solution[i] = new int*[n];
}
maze_help(maze,n,solution,0,0);
}
int main(){
    return 0;
}