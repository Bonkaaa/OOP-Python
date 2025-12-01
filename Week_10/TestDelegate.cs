using System;

class TestDelegate
{
    public delegate void IntAction(int x);


    public static void PrintInt(int x)
    {
        Console.WriteLine(x);
    }

    public static void Perform(IntAction act, int[] arr)
    {
        foreach (var v in arr)
        {
            act(v);
        }
    }

    static void Main()
    {
        IntAction act = PrintInt;

        act(42);

        int[] arr = { 1, 2, 3, 4, 5};
        Perform(PrintInt, arr);
    }
}