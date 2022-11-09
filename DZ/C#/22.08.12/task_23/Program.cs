/*Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
3 -> 1, 8, 27
5 -> 1, 8, 27, 64, 125
*/

string result = "";
int i = 1;
Console.WriteLine("Введите целое положительнное число, больше нуля: ");
if (int.TryParse(Console.ReadLine(), out int n))
{
    if (n < 1)
    {
        Console.WriteLine("Ошибка ввода");
    }
    else
    {
        while(i <= n)
        {
            result += Math.Pow(i, 3).ToString() + ", ";
            i++;
        }
        result = result.Substring(0, result.Length-2);
        Console.WriteLine(result);
    }
}
else
{
    Console.WriteLine("Error");
}