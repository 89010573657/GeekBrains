/*
Задача 15: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
является ли этот день выходным.
6 -> да
7 -> да
1 -> нет
*/
while(true)
{
    Console.WriteLine("Введите число от 1 до 7 для проверки дня недели, или Enter для завершения программы: ");
    string? input = Console.ReadLine();
    if (input == "")
    {
        Console.WriteLine("Всего хорошего");
        break;
    }
    if (int.TryParse(input, out int input_int))
    {
        if ( input_int >=1 && input_int <= 5 )
        {   
            Console.WriteLine("Это будний день");
            continue;
        }
        if (input_int >=5 && input_int <= 7 )
            Console.WriteLine("Это выходной день");
        else
            Console.WriteLine("Ошибка ввода, число не входит диапазон от 1 до 7");
    }
    else
        Console.WriteLine("Error");
}