/*
Задача 66: Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов 
в промежутке от M до N.
M = 1; N = 15 -> 120
M = 4; N = 8. -> 30
*/

int sum_element_range( int start, int end)
{
    int sum = 0;
    if (start <= end ) 
    {
        return sum +=start + sum_element_range(start+1,end);
    }
    else
        return 0;
}
Console.Write(sum_element_range(1,15));
