import java.awt.*;
import java.awt.event.*;

class Operations implements ActionListener{
    TextField T1;
    int FirstNumber;
    String opt;
    String Math;
    public Operations(TextField A){
        T1=A;
    }
    public void actionPerformed(ActionEvent e){
                Button btn= (Button) e.getSource();
        opt=btn.getLabel();
        if(opt.equals("c")){
            T1.setText("");
        }
        else if(opt.equals("=")){
                if (Math.equals("+")){
                    T1.setText (Integer.toString(FirstNumber+Integer.parseInt(T1.getText())));
                }
                    if (Math.equals("-")){
                        T1.setText (Integer.toString(FirstNumber-Integer.parseInt(T1.getText())));
                    }
                        if (Math.equals("x")){
                            T1.setText (Integer.toString(FirstNumber*Integer.parseInt(T1.getText())));
                        }
                            if (Math.equals("/")){
                                T1.setText (Integer.toString(FirstNumber/Integer.parseInt(T1.getText())));
                            }
                }
        else{
                 FirstNumber=Integer.parseInt(T1.getText());
                 Math=opt;
                 T1.setText("");       
        }

}
}

class Digits implements ActionListener{
    TextField T1;
    public Digits(TextField A){
        T1=A;
    }

    public void actionPerformed(ActionEvent E){
        Button btn= (Button) E.getSource();
        T1.setText(T1.getText() + btn.getLabel());
    }
    
}
class calculator{
    public static void main(String XYZ[]) {
        Frame F=new Frame();
        Panel P1=new Panel();
        Panel P2=new Panel();
        F.setVisible(true);
        F.setSize(300,200);
        TextField T=new TextField(18);

        Button B0,B1,B2,B3,B4,B5,B6,B7,B8,B9;

        Button B_Add,B_Mul,B_Sub,B_Div;

        Button B_Eql,B_Clr;



        Digits Digit_event=new Digits(T);
        Operations Operations_event=new Operations(T);

        B0=new Button("0");
            B0.addActionListener(Digit_event);
        B1=new Button("1");
            B1.addActionListener(Digit_event);
        B2=new Button("2");
            B2.addActionListener(Digit_event);
        B3=new Button("3");
            B3.addActionListener(Digit_event);
        B4=new Button("4");
            B4.addActionListener(Digit_event);
        B5=new Button("5");
            B5.addActionListener(Digit_event);
        B6=new Button("6");
            B6.addActionListener(Digit_event);
        B7=new Button("7");
            B7.addActionListener(Digit_event);
        B8=new Button("8");
            B8.addActionListener(Digit_event);
        B9=new Button("9");
            B9.addActionListener(Digit_event);
        
        B_Add=new Button("+");
            B_Add.addActionListener(Operations_event);
        B_Mul=new Button("x");
            B_Mul.addActionListener(Operations_event);
        B_Sub=new Button("-");
            B_Sub .addActionListener(Operations_event);
        B_Div=new Button("/");
            B_Div.addActionListener(Operations_event);
        B_Eql=new Button("=");
            B_Eql.addActionListener(Operations_event);
        B_Clr=new Button("C");
            B_Clr.addActionListener(Operations_event);

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

        B_Clr.setBackground(Color.RED);
        B0.setBackground(Color.lightGray);
        B1.setBackground(Color.lightGray);
        B2.setBackground(Color.lightGray);
        B3.setBackground(Color.lightGray);
        B4.setBackground(Color.lightGray);
        B5.setBackground(Color.lightGray);
        B6.setBackground(Color.lightGray);
        B7.setBackground(Color.lightGray);
        B8.setBackground(Color.lightGray);
        B9.setBackground(Color.lightGray);

        B_Eql.setBackground(Color.GREEN);
        B_Div.setBackground(Color.GRAY);
        B_Mul.setBackground(Color.GRAY);
        B_Sub.setBackground(Color.GRAY);
        B_Add.setBackground(Color.GRAY);

        P1.setBackground(Color.BLACK);
    }
}

