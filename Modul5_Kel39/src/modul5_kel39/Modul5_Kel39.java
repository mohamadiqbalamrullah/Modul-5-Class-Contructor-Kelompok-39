
package modul5_kel39;

import java.util.Scanner;

public class Modul5_Kel39 {

    public static void main(String[] args) {
        
        String email, password;
        
        Scanner input = new Scanner(System.in);
        System.out.print("Nama : ");
        email = input.nextLine();
        System.out.print("NIM : ");
        password = input.nextLine();
        
        userService satu = new userService( email, password );
        satu.login();
    }
    
}
