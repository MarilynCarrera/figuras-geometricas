// Clase base Figura (opcional, para herencia)
public abstract class Figura
{
    // Propiedades abstractas para área y perímetro
    public abstract double Area { get; }
    public abstract double Perimetro { get; }
}

// Clase Circulo
public class Circulo : Figura
{
    private double radio;

    public Circulo(double radio)
    {
        this.radio = radio;
    }

    // Implementando las propiedades abstractas de Figura
    public override double Area
    {
        get { return Math.PI * radio * radio; }
    }

    public override double Perimetro
    {
        get { return 2 * Math.PI * radio; }
    }
}

// Clase Cuadrado
public class Cuadrado : Figura
{
    private double lado;

    public Cuadrado(double lado)
    {
        this.lado = lado;
    }

    // Implementando las propiedades abstractas de Figura
    public override double Area
    {
        get { return lado * lado; }
    }

    public override double Perimetro
    {
        get { return 4 * lado; }
    }
}

// ... y así sucesivamente para Rectángulo, Triángulo, etc.