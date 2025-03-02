package test_java_eclipse;

import java.util.Comparator;
import java.io.IOException;

@Deprecated // Use your custom annotation here
public class test<T extends Number & Comparable<T>> extends Number implements Comparable<test<T>> {

    // Fields
    private T x;
    public final String name;
    
    // Constructor
    public test(int x, String name) {
        this.x = (T) Integer.valueOf(x);  // Cast to T (assuming T is a subtype of Number like Integer)
        this.name = name;
    }
    
    // Methods
    public void myMethod() throws IOException {
        if (x.doubleValue() < 0) {
            throw new IOException("Negative number");
        }
        System.out.println("Method executed with x = " + x);
    }

    public static void staticMethod() {
        System.out.println("This is a static method");
    }

    public void defaultMethod() {
        System.out.println("This is a default method");
    }

    // imolement Comparable interface
    public int compareTo(test<T> other) {
        return x.compareTo(other.x);  // Comparing the 'x' field of the class
    }

    @Override 
    public int intValue() {
        return x.intValue();  // Implementation of abstract method from Number class
    }
    
    // Inner class implementing method from Comparable
    public class InnerClass implements Comparable<test<T>> {
        @Override
        public int compareTo(test<T> o) {
            return x.compareTo(o.x);
        }
    }
    
    public static void main(String[] args)
    {
        System.out.println("test");
    }
}