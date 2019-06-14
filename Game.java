import java.util.Scanner;

class Game{

    public static void main (String[] args) {
        Scanner input= new Scanner(System.in);

            int Distance=15;

               System.out.println("You awaken to find yourself in a Barren Moor.");
               System.out.println("You have nothing but a magical compass that displays the number 15");
                System.out.println("Type 1 to go North, 2 to go East, 3 to go South and 4 to go West");
               int no1=input.nextInt();

           int R=(Distance-(no1));

               System.out.println("You take a few steps");
               System.out.print(R);
               System.out.println(" is shown on the compass");
               System.out.println("Type 1 for north,2 for east,3 for south or 4 for west");
               int no2=input.nextInt();

            int T=(R-(no2-5));

            System.out.println("You take a few steps");
               System.out.print(T);
               System.out.println(" is shown on the compass, maybe it is broken...");
               System.out.println("Type 1 for north,2 for east,3 for south or 4 for west");
               int no3=input.nextInt();

            int M=(T-(no3));
            
            System.out.println("You take a few steps");
               System.out.print(M);
               System.out.println(" is shown on the compass");
               System.out.println("Type 1 for north,2 for east,3 for south or 4 for west");
               int no4=input.nextInt();

            int L=(M-(no4*2));

            if(L < 2){
                System.out.println("You Stumble across a Treasure Chest, Congratulations you're still lost");
               
            }
            
            else{

            System.out.println("You take a few steps but see nothing new");
                System.out.print(L);
                System.out.println(" is shown on the compass");
                System.out.println("Type 1 for north,2 for east,3 for south or 4 for west");
                int no5=input.nextInt();

            int S=(L-(no5+2));

            if(S < 2){
                System.out.println("You Stumble across a Treasure Chest, Congratulations you're still lost");
                
            }
            
            else{

            System.out.println("You take a few steps but see nothing new... you're struck by lightning and die GAME OVER");
           
                

    }
}
}
}
