/*
Задача 25: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A
 в натуральную степень B.
2, 4 -> 16
*/

int [] get_input_numbers()
{
int [] input_numbers = new int [2];
while(true)
    {
        try
        {
            Console.WriteLine("Введите число 'A', которое будет возводиться в степень: ");
            input_numbers[0] = int.Parse(Console.ReadLine() ?? "");

            Console.WriteLine("Введите число 'B', степень в которую возведём число А: ");
            input_numbers[1] = int.Parse(Console.ReadLine() ?? "");
        
            return input_numbers;
        }
        
        catch( Exception error )
        {
            Console.WriteLine($"{error.Message}, введите целые числа");
            continue;
        }
    }
}

double get_exponentiation(int [] array)
{
    double result = 1;
    if (array[1] == 0)
        return result;
    else if (array[1] > 0)
    {
        while (array[1] > 0)
        {
            result *= array[0];
            array[1]--;
        }
        return result;
    }
    else
    {
        int i = Math.Abs(array[1]);
        int denominator = 1;
        while (i > 0)
        {
            denominator *= array[0];
            i--;
        }
        result = result/denominator;
        return result;
    }
} 

int [] input_numbers = get_input_numbers();
Console.WriteLine($"Число A = {input_numbers[0]} в степени B = {input_numbers[1]}, равняется: {get_exponentiation(input_numbers)}");