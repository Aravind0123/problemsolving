import java.util.Scanner;

public class patternprogam {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int n = s.length();
        int m = (int)(n/2);
        for (int i=0;i<n+1;i++){
            for(int j=0;j<n-i;j++){
                System.out.print(" ");
            }
            for(int k=m;k<=m+i;k++){
                if(k>=n){
                    int z=k-n;
                    System.out.print(s.charAt(z));
                }
                else{
                    System.out.print(s.charAt(k));
                }

            }
            System.out.println( " ");
            }

        }
    }
    
