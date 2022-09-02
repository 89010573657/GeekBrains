/*
Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
Например, даны 2 матрицы:
2 4 | 3 4
3 2 | 3 3
Результирующая матрица будет:
18 20
15 18
*/

double[,]a = new double[2,2];
double[,]b = new double[2,2];
a[0,0] = 2;
a[0,1] = 4;
a[1,0] =3;
a[1,1] = 2;
b[0,0] = 3;
b[0,1] = 4;
b[1,0] =3;
b[1,1] = 3;    

void multiplication_array(double[,]a , double[,] b)
{
    double[,] result_array = new double [a.GetLength(0), a.GetLength(1)];
    for(int i = 0; i < a.GetLength(0); i++)
    {
        for(int j = 0; j < b.GetLength(1); j++)
        {
            result_array[i,j] = 0;
            for (int k = 0; k < a.GetLength(0); k++)
            {
                result_array[i,j] += a[i,k] * b[k,j];
                
            }
            Console.Write($"{result_array[i,j]} ");
        } 
        Console.WriteLine();
    }
} 
multiplication_array(a,b);