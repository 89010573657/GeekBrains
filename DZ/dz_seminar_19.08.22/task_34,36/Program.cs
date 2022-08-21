/*
Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. 
Напишите программу, которая покажет количество чётных чисел в массиве.
[345, 897, 568, 234] -> 2
*/

int get_random_length_array() // Возвращает рандомную длину массива
{
    int random_length_array = new Random().Next(1, 1000);
    return random_length_array;
}

int [] get_new_array(int lengt_array) // Возвращает новый массив с указанной длинной
{
    int [] new_array = new int [lengt_array];
    return new_array;
}

int [] get_fill_array(int [] array) // Заполняет массив случайными 3х значными числами и передаёт его
{
    for(int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(100, 1000);
    }
    return array;
}

int get_count_even_numbers(int [] array) // Считает количество чётных чисел и возвращает
{
    int count = 0;
    foreach (int element in array)
    {
        if (element % 2 == 0)
        {
            count++;
        }
    }
    return count;
}

List<int> get_array_even_numbers(int [] array) // Отдельное сохранение списка чётных чисел
{
    List<int> array_even_numbers = new List<int>();
    foreach (int element in array)
    {
        if (element % 2 == 0)
        {
            array_even_numbers.Add(element);
        }
    }
    return array_even_numbers;
}

int [] array = get_fill_array(get_new_array(get_random_length_array()));
List<int> array_even_numbers = get_array_even_numbers(array);
Console.WriteLine($"Сформированный массив:\n[{String.Join(", ", array)}]");
Console.WriteLine($"Отредактированный массив с чётными числами:\n[{String.Join(", ", array_even_numbers)}]");
Console.WriteLine($"Количество четных чисел в массиве равняется: {get_count_even_numbers(array)}");

/*Задача 36: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих
на нечётных позициях.
[3, 7, 23, 12] -> 19
[-4, -6, 89, 6] -> 0
*/

int get_sum_no_even_numbers(int [] array) // Возвращает сумму нечётных элементов
{
    int sum = 0;
    foreach(int element in array)
    {
        if (element % 2 != 0)
        {
            sum += element;
        }
    }
    return sum;
}

Console.WriteLine($"Сумма нечётных элементов массива составляет: {get_sum_no_even_numbers(array)}");