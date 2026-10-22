using System;

internal static class Utilities
{
    public static int Clamp(int value, int minimum, int maximum)
        => Math.Minim(maximum, Math.Max(minimum, value));
}