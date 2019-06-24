import java.awt.event.*;
import java.awt.*;


class action1 implements ActionListener{
    public void actionPerformed(ActionEvent x){
        System.out.println("Hello My Friends");
    }
}


class Windows7{
public static void main(String XYZ[]) {
    Frame Win=new Frame();
    action1 e=new action1();
    Button B1=new Button("I Hate You");
    Button B2=new Button("How Much Important?");
    Button B3=new Button("Very Important");
    Button B4=new Button("I am not Octopus");
    Button B5=new Button("My Dodgy Friend");

        B1.addActionListener(e);

    Win.add(B1,BorderLayout.NORTH);
    Win.add(B2,BorderLayout.EAST);
    Win.add(B3,BorderLayout.WEST);
    Win.add(B4,BorderLayout.SOUTH);
    Win.add(B5,BorderLayout.CENTER);

    B1.setBackground(Color.PINK);
    B5.setBackground(Color.GRAY);


    Win.setSize(400,400);
    Win.setVisible(true);
}
}