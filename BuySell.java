public class BuySell {

    public static void main(String[] args) {
        int nums[] = {2,5,1,2,5,1};
        int n = nums.length;
        int profit=0;
        int buy = 0;
        int sell =0;
        int max=0;
        for(int i=0;i<n;i++){
            for (int j=i+1;j<n;j++){

                if (nums[i]<nums[j]){
                    profit = nums[j]-nums[i];
                    if (profit>max){
                        buy=i;
                        sell = j ;
                        max=profit;
                    }

                }
            }

            }
        System.out.println("Max profit: "+ max + " Buy at " + buy + " sell at " + sell );
        }

    }
