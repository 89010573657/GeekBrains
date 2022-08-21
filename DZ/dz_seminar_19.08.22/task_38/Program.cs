/*
Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
[3 7 22 2 78] -> 76
*/

int get_random_length_array() // Возвращает рандомную длину массива
{
    int random_length_array = new Random().Next(1, 1000);
    return random_length_array;
}

double [] get_new_array(int lengt_array) // Возвращает новый массив с указанной длинной
{
    double [] new_array = new double [lengt_array];
    return new_array;
}

int get_coefficient () // Возвращает коэффициент для перемножения рандомных чисел double
{
    int coefficient = new Random().Next(-999, 1000);
    return coefficient;
}

double [] get_fill_array(double [] array, int coefficient)  // Заполняет массив вещественными числами и передаёт его
{
    for(int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().NextDouble()*coefficient;
    }
    return array;
}

double get_delta_max_min (double [] array) // Возвращает разницу между максимальным и минимальным элементом массива
{
    double max = array[0], min = array[0];
    for (int i = 1; i < array.Length; i++)
    {
        if (array[i] > max)
            max = array[i];
        else if (array[i] < min)
            min = array[i];
    }
    double delta_max_min = max - min;
    return delta_max_min;
}

double [] array = get_fill_array(get_new_array(get_random_length_array()), get_coefficient());
Console.WriteLine($"Разница между max и min значением составляет: {get_delta_max_min(array)}");