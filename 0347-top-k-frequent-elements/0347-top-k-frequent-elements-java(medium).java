class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int c : nums){
            map.put(c,map.getOrDefault(c,0)+1);
        } 

     ArrayList<Map.Entry<Integer,Integer>> arr = new ArrayList<>(map.entrySet());

        arr.sort((a,b) -> b.getValue() - a.getValue());

        int[] res = new int[k];
        for(int i =0; i < k; i++){
            res[i] = arr.get(i).getKey();
        }
        return res;
    }
}