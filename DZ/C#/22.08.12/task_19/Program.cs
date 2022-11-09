/*
Задача 19
Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
14212 -> нет
12821 -> да
23432 -> да
*/
void palindrome_check()
{
    int num = 0;
    try
    {
        Console.Write("Введи число для проверки на палиндромность:");
        num = int.Parse(Console.ReadLine() ?? "");
    }
    catch (Exception exp)
    {
        Console.WriteLine($"Ошибка: {exp.Message}");
        return;
    }

    if (num >= 10000 && num <= 99999)
    {
        if (num.ToString()[0] == num.ToString()[4] && num.ToString()[1] == num.ToString()[3])
            Console.WriteLine($"Число {num} является палиндромом.");
        else
            Console.WriteLine($"Число {num} не является палиндромом.");
    }
    else
        Console.WriteLine("Вы ввели не 5-значное число");
}
while(true)
{
    int input = 0;
    Console.WriteLine("Нажми 1 - для проверки числа на палиндромность, 0 - завершения программы");
    if (int.TryParse(Console.ReadLine(), out input))
    {
        if (input == 1)
            palindrome_check();
        else if(input ==0)
        {
            Console.WriteLine("Всего хорошего");
            break;
        } 
        else
        {
            Console.WriteLine("Неверный ввод");
            continue;
        }
    }
    else
    {
        Console.WriteLine("Error");
        continue;
    }
}