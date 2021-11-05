package try_java;

import java.util.concurrent.Semaphore;

public class try_thread extends Thread {

	public static volatile int counter = 0;
	public static Semaphore mutex = new Semaphore(1,true);
	
	public String id;
	
	try_thread(String id){
		this.id=id;
	}
	
	public void run() {
		// TODO Auto-generated method stub
		for (int i = 0; i < 50; i++) {
			try {
				mutex.acquire();
				counter++;
				System.out.println(counter + " comes from " + id);
				mutex.release();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Thread P = new try_thread("P");
		Thread Q = new try_thread("Q");
		P.start();
		Q.start();
		System.out.println("Final counter=" + counter);
	}

}
