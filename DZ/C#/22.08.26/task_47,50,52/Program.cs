/*
Задача 47. Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
m = 3, n = 4.
0,5 7 -2 -0,2
1 -3,3 8 -9,9
8 7,8 -7,1 9
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
            // Console.Write($"{array[i,j]} ");
            Console.Write(string.Format("{0:F1}", array[i,j]) + " ");
        }
        Console.WriteLine();
    }
    return array;
}

int[] size_array = random_size_array();
double[,] n_array = new_array(size_array);
Console.WriteLine($"Вывод в консоль решения задачи №47");
double[,] array= fill_array(n_array);

/*Задача 52. Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом
столбце.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.
*/

double [] average_value(double [,] array)
{
    double [] result = new double[array.GetLength(1)];
    for (int i = 0; i < array.GetLength(1); i++)
    {
        double sum = 0;
        for (int j = 0; j < array.GetLength(0); j++)
        {
            sum += array[j,i];
        }
        result[i] = Math.Round(sum/array.GetLength(0), 1);
       
    }
    return result;
}

Console.WriteLine($"Вывод в консоль решения задачи №50\n{String.Join(" ", average_value(array))}");


/*Задача 50. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве,
и возвращает значение этого элемента или же указание, что такого элемента нет.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
17 -> такого числа в массиве нет
*/

while(true)
{
    Console.WriteLine("Введите двухзначное число: ");
    string pos = Console.ReadLine() ?? "";
    // bool is_i = int.TryParse(pos[0].ToString(), out int i);
    // bool is_j = int.TryParse(pos[1].ToString(), out int j);
    int i = 0, j = 0;
    if (pos.Length !=2 || (!int.TryParse(pos[0].ToString(), out i)) && (!int.TryParse(pos[1].ToString(), out j)))
    {
        Console.WriteLine("Ошибка ввода");
        continue;
    }
    else if (i < array.GetLength(0) && j < array.GetLength(1))
    {
        Console.WriteLine($"В указанной позиции находится число: {Math.Round(array[i,j], 1)}");
        break;
    }
    else
        Console.WriteLine("Указанная позиция выходит за пределы массива!");
}

