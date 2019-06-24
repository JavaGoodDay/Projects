import java.awt.*;
import java.awt.event.*;

class calculator{
    public static void main(String XYZ[]) {
        Frame F=new Frame();
        Panel P1=new Panel();
        Panel P2=new Panel();
        F.setVisible(true);
        F.setSize(400,400);
        TextField T=new TextField(15);

        Button B0,B1,B2,B3,B4,B5,B6,B7,B8,B9;

        Button B_Add,B_Mul,B_Sub,B_Div;

        Button B_Eql,B_Clr;

        B0=new Button("0");
        B1=new Button("1");
        B2=new Button("2");
        B3=new Button("3");
        B4=new Button("4");
        B5=new Button("5");
        B6=new Button("6");
        B7=new Button("7");
        B8=new Button("8");
        B9=new Button("9");
       
        B_Add=new Button("+");
        B_Mul=new Button("x");
        B_Sub=new Button("-");
        B_Div=new Button("/");

        B_Eql=new Button("=");
        B_Clr=new Button("C");

        GridLayout G=new GridLayout(4,4);
        P2.setLayout(G);

        P1.add(T);
        P2.add(B1);
        P2.add(B2);
        P2.add(B3);
        P2.add(B_Add);
        P2.add(B4);
        P2.add(B5);
        P2.add(B6);
        P2.add(B_Sub);
        P2.add(B7);
        P2.add(B8);
        P2.add(B9);
        P2.add(B_Mul);
        P2.add(B0);
        P2.add(B_Clr);
        P2.add(B_Eql);
        P2.add(B_Div);

        F.add(P1,BorderLayout.NORTH);
        F.add(P2,BorderLayout.CENTER);
    }
}