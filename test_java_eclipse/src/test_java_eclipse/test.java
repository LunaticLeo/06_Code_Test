package test_java_eclipse;
public class test {
	//  error: non-static variable this cannot be referenced from a static context
//    class test1{
//        public static int i = 1;
//    }
    
    // static inner class
	static class test2 { 
		public static int i = 0;
	}
	public static void main(String[] args) {
		class test3 {
			public static int i = 1;
		}
		test2 t2 = new test2();
		test3 t3 = new test3();
		System.out.println(t2.i + " " + t3.i);
	}
}