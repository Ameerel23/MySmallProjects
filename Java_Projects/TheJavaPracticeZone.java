class TheJavaPracticeZone{
	
	public static void oddOrEven(int a) {
		if (a % 2 == 0) {
			System.out.println("Even");
		}
		else {
			System.out.println("Odd");
		}
	}
	
	public static void main (String[] args) {
		oddOrEven(2);
		System.out.println("Open");
	}
}