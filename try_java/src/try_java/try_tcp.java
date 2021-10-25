package try_java;

import java.util.concurrent.*;

import java.net.*;

public class try_tcp {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Semaphore arr= new Semaphore(1);
		System.out.println(arr.availablePermits());
	}
}
