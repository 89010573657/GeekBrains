/* Задача 41: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл 
пользователь.
0, 7, 8, -2, -2 -> 2
1, -7, 567, 89, 223-> 3
*/

int count_numbers() // Ввод длины массива(количество чисел для проверки)
{
    while(true)
    {
        try
        {  
       
            Console.WriteLine("Введите количество чисел которые вы хотите проверить:");
            int count_numbers = int.Parse(Console.ReadLine() ?? "");
            if (count_numbers < 0)
            {
                Console.WriteLine("Необходимо целое положительное число");
                continue;
            }
            return count_numbers;
        }

        catch (Exception)
        {
            Console.WriteLine("Необходимо ввести целое число");
        }
    }
}

int [] creating_array(int length) // Создание массива
{
    int [] creating_array = new int [length];
    return creating_array;
}

int [] fill_array(int [] array) // Заполнение массива
{
    int i = 0;
    while (i < array.Length)
    {
        try
        {
            Console.Write($"Введите число №{i+1}: ");
            array[i] = int.Parse(Console.ReadLine() ?? "");
            i++;
        }
        catch (Exception)
        {
            Console.WriteLine("Необходимо ввести целое число");
            i = 0;
        }
    }
    return array;
}
 
int count_positive_numbers(int [] array) // Подсчёт положительных элементов
{
    int count = 0;
    foreach (int element in array)
    {
        if (element > 0)
            count++;
    }
    return count;
}

int [] array = fill_array(creating_array(count_numbers()));
int result = count_positive_numbers(array);
Console.WriteLine($"Количество положительных чисел равно: {result}");

