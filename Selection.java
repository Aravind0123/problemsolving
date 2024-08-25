public class Selection {
    public static void main(String[] args) {
        
        int nums[] = {6,5,4,3,2,1};
        int n = nums.length;
        int minindex = 0 ;
        int temp = 0;
        System.out.print("Before Sorting: ");
        for (int k : nums){
            System.out.print(k);
            System.out.print("");
        }
        System.out.println();
        for(int i=0; i<n-1;i++){
            minindex = i;
            for(int j=i;j<n;j++){
                if(nums[minindex]>nums[j]){
                    minindex = j;
                }
                temp = nums[minindex];
                nums[minindex]=nums[i];
                nums[i]=temp;


            }
            System.out.println();
            for(int  k : nums){
                System.out.print(k);
                System.out.print("");
            }
            System.out.print("");
        }
        System.out.println();
        System.out.println("After Sorting");
        for(int k : nums){
            System.out.print(k);
        }
    }
    
}
