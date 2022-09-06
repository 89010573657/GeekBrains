/*
Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два 
неотрицательных числа m и n.
m = 2, n = 3 -> A(m,n) = 29 ////в условии опечатка//// не 29 а 9
*/

 int ackerman_function(int m, int n)
 {
    if (m == 0)
        return n+1;
    else if (m > 0 && n ==0)
    {
        return ackerman_function(m-1, 1);
    }
    return ackerman_function(m-1, ackerman_function(m, n-1));
 }
 Console.Write(ackerman_function(2,3));