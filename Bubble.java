public class Bubble{
    public static void main (String[] args) {
        int nums[] = {9,5,3,2,1,6,11,15,66,99,12,33,45,98,75,101};
        System.out.print("Before Sorting : ");
        int steps=0;
        for(int n : nums){
            System.out.print(n);
            System.out.print(" ");
        }
        int n  = nums.length;
        int temp =0;
        for (int i =0;i<n-1;i++){
            for(int j=0;j<n-i-1;j++){
                if(nums[j]>nums[j+1]){
                    temp = nums[j];
                    nums[j]=nums[j+1];
                    nums[j+1]=temp;
                    steps++;

                }
            }
            System.out.println();
            System.out.println("Sorting at " + i + ": ");
            for(int k : nums){
                System.out.print(k);
                System.out.print(" ");
        }
    }
        System.out.println();
        System.out.print("After Sorting : ");
        for(int k : nums){
            System.out.print(k);
            System.out.print(" ");
        }
        System.out.println(" ");
        System.out.println("Sorted in " + steps + " Steps");
    }
    
}
