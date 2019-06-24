import java.awt.*;
import java.awt.event.*;

class WindowXP{

public static void main(String xyz[]) {
    Frame F=new Frame ("Calculations");
    TextField T1,T2,T3;
    Label L1,L2,L3;
    Button B1=new Button("=");
    L1=new Label("First No:");
    L2=new Label("Second No:");
    L3=new Label("Result:");
    T1=new TextField(10);

    T2=new TextField(10);
    T3=new TextField(10);
    FlowLayout FL=new FlowLayout();

    F.setLayout(FL);

    Ehandler E=new Ehandler(T1,T2,T3);
    B1.addActionListener(E);
    F.add(L1);
    F.add(T1);
    F.add(L2);
    F.add(T2);
    F.add(B1);
    F.add(L3);
    F.add(T3);

    F.setSize(400,400);
    F.setVisible(true);
    } 
    }


class Ehandler implements ActionListener{
    TextField NO1,NO2,Result;

    public Ehandler(TextField A,TextField B,TextField C){
        NO1=A;
        NO2=B;
        Result=C;}

        public void actionPerformed(ActionEvent X){
            int A,B,C;
            A=Integer.parseInt(NO1.getText());
            B=Integer.parseInt(NO2.getText());

            C=A+B;

            Result.setText(Integer.toString(C));
            
        }
    }
