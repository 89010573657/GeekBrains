string [] search_array(string [] array)
{
    int count = 0;
    foreach(string i in array) // Перебор массива для понимания какой длины массив создать
    {
        if (i.ToString().Length <= 3) count++;
    }
    string [] result_array = new string [count];

    int j = 0;
    foreach(string i in array) // вывод на экран
    {
        if (i.ToString().Length <= 3)
        {
            result_array[j]=i;
            Console.Write($"{result_array[j]} ");
            j++;
        }
    }
    return result_array;
}

string[] array = {"hello", "world", ":-)", "1234", "-2", };
string[] result = search_array(array);

