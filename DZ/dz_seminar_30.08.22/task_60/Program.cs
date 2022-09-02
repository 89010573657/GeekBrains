/*Задача 60. ...Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу,
которая будет построчно выводить массив, добавляя индексы каждого элемента.
Массив размером 2 x 2 x 2
66(0,0,0) 25(0,1,0)
34(1,0,0) 41(1,1,0)
27(0,0,1) 90(0,1,1)
26(1,0,1) 55(1,1,1)
*/

int [,,] get_new_array()  // Создаёт 3х мерный массив
{
    int[,,] array = new int [2,2,2];
    return array;
}

int[,,] get_fill_array(int [,,] array) // Заполняет массив двухзначными числами
{
    List <int> check_list = new List<int>();
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int k = 0; k < array.GetLength(2); k++)
            {
                int new_element;

                while(true)
                {
                    new_element = new Random().Next(10, 18);
                    if (check_list.Contains(new_element))
                    {
                        continue;
                    }
                    break;
                }

                array[i,j,k] = new_element;
                check_list.Add(new_element);
                Console.Write($"{array[i,j,k]}({i},{j},{k}) ");
            }
            Console.WriteLine();
        }
    }
    return array;
}

int [,,] result_array = get_fill_array(get_new_array());

