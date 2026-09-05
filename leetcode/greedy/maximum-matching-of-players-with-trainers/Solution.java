class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        
        Arrays.sort(players);
        Arrays.sort(trainers);

        int idx1 = players.length - 1;
        int idx2 = trainers.length - 1;
        int count = 0;

        while (idx1 >= 0 && idx2 >= 0) {

            if (players[idx1] <= trainers[idx2]) {
                count++;
                idx1--;
                idx2--;
            } else {
                idx1--;
            }

        }

        return count;

    }
}