import java.util.HashSet;
import java.util.Set;

public class ContainsDuplicate {
    public static boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)){
                return true;


            }
            seen.add(num);
        }
        return false;

    }


    public static void main(String[] args) {
   int[][] testCases = {
            {1, 2, 3, 1},
            {1, 2, 3, 4},
            {1, 1, 1, 3, 3, 4, 3, 2, 4, 2}
    };
    boolean[] expected = {true, false, true};

    for (int i = 0; i < testCases.length; i++) {
        boolean result = containsDuplicate(testCases[i]);
        System.out.println("nums=" + java.util.Arrays.toString(testCases[i]) +
                " -> result=" + result +
                ", expected=" + expected[i]);
    }

}
}