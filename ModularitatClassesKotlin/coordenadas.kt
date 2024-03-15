class Coordenada
{
	var x: Int
	var y: Int
	constructor()
	{
		// Coordenada inicial
		this.x = 0
		this.y = 0
	}

  fun moure_dreta()
	{
		this.x += 1
	}
    
	fun moure_esquerra()
	{
		this.x -= 1
	}

	fun moure_amunt()
	{
		this.y += 1
	}

	fun moure_avall()
	{
		this.y -= 1
	}
}

class Main
{
    // Programa principal
		constructor()
		{
        // Executar moviments
        var coordenada: Coordenada = Coordenada()
        coordenada.moure_dreta()
        println("Nova coordenada despres de moure a la dreta: (${coordenada.x}, ${coordenada.y})")

        coordenada.moure_amunt()
        println("Nova coordenada despres de moure amunt: (${coordenada.x}, ${coordenada.y})")
		}
}

fun main()
{
	Main()
}
