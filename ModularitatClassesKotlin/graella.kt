class Coordenada
{
		var x: Int
		var y: Int

		constructor()
		{
			// Coordenada inicial
			x = 0
			y = 0
		}

		fun moure_dreta()
		{
			x += 1
		}

		fun moure_esquerra()
		{
			x -= 1
		}

		fun moure_amunt()
		{
			y += 1
		}

		fun moure_avall()
		{
			y -= 1
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
			println("Nova coordenada després de moure a la dreta: (${coordenada.x}, ${coordenada.y})")

			coordenada.moure_amunt()
			println("Nova coordenada després de moure amunt: (${coordenada.x}, ${coordenada.y})")
		}
	}

	fun main()
	{
		Main()
	}
