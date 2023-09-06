
public class Problem {

    public static void main(String[] args) {
        long primeSum = 0;
        for(int i = 2; i < 2000000; i++){
            if(isPrime(i)){
                primeSum += i;
            }
        }
        
        System.out.println(primeSum);
        
    }
    
    public static boolean isPrime(int num){
        for(int i = 2; i * i <= num; i++){
            if(num % i == 0){
                return false;
            }
        }
        return true;
    }

}
