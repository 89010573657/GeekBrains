/* Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D
пространстве.
A (3,6,8); B (2,1,-7), -> 15.84
A (7,-5, 0); B (1,-1,9) -> 11.53
*/

int x1=0, y1=0, z1=0, x2=0, y2=0, z2=0; 
void distance_two_points_3d()
{
    try
    {
        Console.WriteLine("Введите значение координаты х первой точки: ");
        x1 = int.Parse(Console.ReadLine() ?? "");
        Console.WriteLine("Введите значение координаты y первой точки: ");
        y1 = int.Parse(Console.ReadLine() ?? "");
        Console.WriteLine("Введите значение координаты z первой точки: ");
        z1 = int.Parse(Console.ReadLine() ?? "");
        
        Console.WriteLine("Введите значение координаты х второй точки: ");
        x2 = int.Parse(Console.ReadLine() ?? "");
        Console.WriteLine("Введите значение координаты y второй точки: ");
        y2 = int.Parse(Console.ReadLine() ?? "");
        Console.WriteLine("Введите значение координаты z второй точки: ");
        z2 = int.Parse(Console.ReadLine() ?? "");

    }
    catch (Exception exp)
    {
        Console.WriteLine(exp.Message);
    }

    double distance = Math.Sqrt(Math.Pow((x2-x1), 2) + Math.Pow((y2-y1), 2) + Math.Pow((z2-z1), 2));
    Console.WriteLine(Math.Round(distance, 2));
}

 distance_two_points_3d();