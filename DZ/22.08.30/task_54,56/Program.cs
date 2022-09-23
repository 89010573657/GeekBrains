/*
Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой 
строки двумерного массива.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
В итоге получается вот такой массив:
7 4 2 1
9 5 3 2
8 4 4 2
*/

int[] random_size_array() // передает рандомные размеры массива
{
    int [] array = new int [] {new Random().Next(1,10), new Random().Next(1,10)};
    return array;
}

double[,] new_array(int [] array_size) // создает и передаёт двумерный массив
{
    double[,] new_array = new double [array_size[0], array_size[1]];
    return new_array;
}

double[,] fill_array(double[,] array) // заполняет двумерный массив случайными числами, выводи в консоль, передаёт
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i,j] = new Random().NextDouble()*new Random().Next(0, 11);
            Console.Write(string.Format("{0:F1}", array[i,j]) + " ");
        }
        Console.WriteLine();
    }
    return array;
}

double [,] ordering_rows_array(double [,] array) // Упорядочивает строк массива пузырьковым методом
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int k = j+1; k < array.GetLength(1); k++)
            {
                if (array[i,k] > array[i,j])
                {
                    double swap = array[i,k];
                    array[i,k] = array[i,j];
                    array[i,j] = swap;
                }
            }
            Console.Write(string.Format("{0:F1}", array[i,j]) + " ");
        }
        Console.WriteLine();
    
    }
    return array;
}
//////////////////////////////////////////////////////////////////////////////////
int[] size_array = random_size_array();
double[,] n_array = new_array(size_array);
double[,] array= fill_array(n_array);
////////////////////////////////////////////////////////////////////////////////
Console.WriteLine("Решение задачи №54:");
double[,] end_array_54 = ordering_rows_array(array);

/*Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку
с наименьшей суммой элементов.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
5 2 6 7
Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей суммой элементов: 1 строка
*/

void search_minimal_sum_el_rows_array(double [,] array) // Поиск минимальной суммы элементов в строках
{
    double min_sum = 99999;
    int numbers_rows = 0;

    for (int i = 0; i < array.GetLength(0); i++)
    {
        double sum = 0;
        for(int j = 0; j < array.GetLength(1); j++)
        {
            sum += array[i,j];
        }
        if(sum < min_sum)
        {
            min_sum = sum;
            numbers_rows = i;
        }
    }
    Console.WriteLine($"Минимальная сумма элементов находится в строке №:{numbers_rows} и равна: {Math.Round(min_sum,2)}");
}

Console.WriteLine("Решение задачи №56:");
search_minimal_sum_el_rows_array(array);



