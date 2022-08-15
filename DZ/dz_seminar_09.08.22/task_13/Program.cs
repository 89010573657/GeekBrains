/*
Задача 13: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что 
третьей цифры нет.
645 -> 5
78 -> третьей цифры нет
32679 -> 6
*/
int num = new Random().Next(1, 999999);
Console.WriteLine(num);
if (num < 100) 
    Console.WriteLine("Третьей цифры нет");
else
    Console.WriteLine(num.ToString()[2]);