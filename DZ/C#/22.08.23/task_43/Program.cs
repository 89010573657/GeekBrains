/* 
Задача 43: Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями
 y = k1 * x + b1
 y = k2 * x + b2
значения b1, k1, b2 и k2 задаются пользователем.
b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5)
*/

double[] input_value()
{
    double[] array = new double[4];
    while (true)
    {
        try
        {
            Console.Write("Введие значение к1: ");
            array[0] = double.Parse(Console.ReadLine() ?? "");

            Console.Write("Введие значение к2: ");
            array[1] = double.Parse(Console.ReadLine() ?? "");

            Console.Write("Введие значение b1: ");
            array[2] = double.Parse(Console.ReadLine() ?? "");

            Console.Write("Введие значение b2: ");
            array[3] = double.Parse(Console.ReadLine() ?? "");
            return array;
        }
        catch (Exception)
        {
            Console.WriteLine("Вводите вещественные числа!");
        }
    }
}

void result(double[] array)
{
    double x = (array[3] - array[2]) / (array[0] - array[1]);
    double y = array[0] * x + array[2];
    Console.WriteLine($"{(x, y)}");
}

result(input_value());