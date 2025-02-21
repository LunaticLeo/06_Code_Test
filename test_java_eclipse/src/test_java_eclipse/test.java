package test_java_eclipse;

public class test {

	public static void main(String[] args) throws InterruptedException {

        StringBuffer stringBuffer = new StringBuffer();
        StringBuilder stringBuilder = new StringBuilder();

        for (int i = 0; i < 100; i++) {
            new Thread(new Runnable() {
                public void run() {
                	stringBuilder.append(1);
                	stringBuffer.append(1);
                }
            }).start();
        }
        Thread.sleep(100);
        System.out.println("stringBuilder:" + stringBuilder.length() + " stringBuffer:" + stringBuffer.length());

    }

}
