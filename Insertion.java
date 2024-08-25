public class Insertion {
    public static void main(String[] args) {
        int nums[]={6,5,3,4,1,2};
        int n = nums.length;
        int j=0;
        int key = 0;
        System.out.println("Before Sorting : ");
        for(int k : nums){
            System.out.print(k);
            System.out.print(" ");
        }
        for(int i=1;i<n;i++){
            key = nums[i];
            j = i-1 ;
            while(j>=0 && nums[j]>key){
                nums[j+1]=nums[j];
                j=j-1;
            }
            
            nums[j+1]=key;
            System.out.println();
            for(int k : nums ){
                System.out.print(k);
                System.out.print(" ");
            }
        }
        System.out.println("");
        System.out.println("After Sorting: ");
        for(int k : nums){
            System.out.print(k);
            System.out.print(" ");
        }
    }
}
