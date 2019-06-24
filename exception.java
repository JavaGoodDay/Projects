class exception{
    public static void main(String xyz[]) {
        int A,B,C;

        A=B=C=0;

        try{
            A=4;
            B=0;
            C=A/B;
            System.out.println(C);
        }
        catch(ArithmeticException exp1) {
            System.out.println("cannot divide by zero");
    }
    }
}