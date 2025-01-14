public class Quick{
    public static void quicksort(int []arr,int low,int high){
        if(low<high){
            int pi=partition(arr,low,high);
            quicksort(arr,low,pi-1);
            quicksort(arr,pi+1, high);
        }
    }
    private static int partition(int[]arr, int low,int high){
        int pivot = arr[high];
        int i = low-1;
        for(int j=low;j<high;j++){
            if(arr[j]<pivot){
                i++;
                int temp =arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
        int temp =arr[i+1];
        arr[i+1]=arr[high];
        arr[high]=temp;
        return i+1;
        
    }
    public static void main(String[] args) {
        int arr[ ] = {5,6,2,1,3,8}; 
        System.out.println("Before Sorting:");
        for(int k:arr){
            System.out.print(k);
            System.out.print(" ");
        }

        quicksort(arr,0,arr.length-1); 

        System.out.println(" ");
        System.out.println("After Sorting: ");
        for(int n : arr){
            System.out.print(n);
            System.out.print(" ");
        }
    }
    
}
