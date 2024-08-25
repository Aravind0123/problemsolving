public class Binarysearch
{
    public static void main(String[] args) {
        int nums [] = new int[5];
        nums[0]=1;
        nums[1]=3;
        nums[2]=5;
        nums[3]=6;
        nums[4]=9;
        
        int l=0;
        int n=9;
        int u= nums.length;
        int pos=0;
        while (l<=u) {
            int mid = (int) (l+u)/2 ;
            if(nums[mid]==n){
                pos = mid;
                System.out.println(pos);
                break;
            }
            else{
                if(n<mid){
                    u=mid-1;
                }
                else{
                    l=mid+1;
                }
            }
            
        }

    }
}
