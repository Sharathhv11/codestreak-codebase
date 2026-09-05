class Solution {
    public int binaryGap(int n) {
        
        while ((n & 1) == 0) n >>= 1;
        n >>= 1;

        int res = 0;
        int idx = 1;

        while (n > 0) {

            if ((n & 1) != 0) {
                res = Math.max(idx, res);
                idx = 1;
            } else {
                idx++;
            }

            n >>= 1;

        }

        return res; 

    }
}