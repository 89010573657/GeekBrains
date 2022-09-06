/*
Задача 64: Задайте значения M и N. Напишите программу, которая выведет все натуральные числа 
в промежутке от M до N.
M = 1; N = 5. -> ""1, 2, 3, 4, 5""
M = 4; N = 8. -> ""4, 6, 7, 8""
*/

string output_numbers_range(int m, int n)
{
    string result = string.Empty;
    if ( m <= n)
    {
        return $"{result + m.ToString()}, " + output_numbers_range(m+1, n);
    }
    else 
    {
        return string.Empty;
    }
}
string result = output_numbers_range(5,8);
Console.Write(result.Substring(0,result.Length-2));