import java.util.Scanner;

class Game{

    public static void main(String args) {
        Scanner input= new Scanner(System.in);

               System.out.println("You awaken to find yourself in a Barren Moor...Type Look...");
               String look=input.nextLine();

            if (look == "look"){
                System.out.println("Try north,south,east,or west");

            }
            else{
            System.out.println("Game Over");
           
               }
            }
    }
