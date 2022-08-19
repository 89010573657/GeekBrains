/*
Задача 29: Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран.
1, 2, 5, 7, 19 -> [1, 2, 5, 7, 19]
6, 1, 33 -> [6, 1, 33]
*/

int [] input_elements_array()
{
    int [] array = new int [8];
    while(true)
    {
        try
        {
            for (int i = 0; i < array.Length; i++)
            {
                Console.Write($"Введиnt элемент массива №{i}: ");
                array[i] = int.Parse(Console.ReadLine() ?? "");
            }
            return array;
        }
        catch (Exception)
        {
            Console.WriteLine("Ошибка ввода. Введите целые числа");
        }
    }

}

void output_elements_array(int [] array)
{
    Console.WriteLine(array);
    for(int i = 0; i < array.Length; i++)
    {
        Console.WriteLine($"Элемент массива №{i} равняется {array[i]}");
    }
}
output_elements_array(input_elements_array());
