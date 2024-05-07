class Aux
{
	private static int num_instances = 0;

	public Aux() {
		num_instances++;
	}

	public  int getNumInstances() {
		return num_instances;
	}
}

class Main
{
	public static void main(String[] args) {
		Aux x = new Aux();
		System.out.println("Numero de instancias: " + x.getNumInstances());
		Aux y = new Aux();
		System.out.println("Numero de instancias: " + x.getNumInstances());
	}
}
