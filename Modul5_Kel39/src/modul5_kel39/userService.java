package modul5_kel39;

public class userService 
{
    private String[][] data = new String[2][3];
    private String email, password, roles = "",date = "";
    
   
    public userService(String emails, String passwords)
    {
        email = emails;
        password = passwords;
        String[][] data = 
        { 
            {"Mohamad_Iqbal_Amrullah_Kelompok39@gmail.com", "21120119140136", "Iqbal \nFisika Dasar \nDasar Komputer dan Pemrogaman", "23-04-2020"},
            {"Farrel_Ahmad_Yudithia_Kelompok39@gmail.com", "21120119130067", "Farrel \nDasar Komputer dan Pemrogaman \nKonsep Jaringan Komputer", "23-04-2020"} 
        };
        this.data = data;
    }

    public void login()
    {
        boolean status = checkCredential();
        if(status == true)
        { 
            System.out.println("\nWelcome \n" + roles);
            System.out.println("Tanggal Peminjaman : " + date);
            System.out.println("WELKAM BRADER " + email);
        }
        else
        {
            System.out.println("\nInvalid Login ");
        }
    }

    
    private boolean checkCredential()
    {
        for(int i = 0; i < data.length; i++ )
        {
            if(data[i][0].equals(email))
            {
                if(data[i][1].equals(password))
                {
                    roles = data[i][2];
                    date = data [i][3]
                    return true;
                }
            }
        }
        return false;
    }
}
    
 
