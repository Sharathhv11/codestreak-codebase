class Solution {

    List<String> result = new ArrayList<>();

    private void backtrack(ArrayList<String> ipSeg,String s){

        if( ipSeg.size() == 3 ){
            if( s.length()<=3 && Integer.parseInt(s) <= 255  )
            {
                if( s.length()>1 && s.charAt(0) == '0') return;
                StringBuilder validIp = new StringBuilder();
                for(String i : ipSeg )
                    validIp.append(i+".");
                validIp.append(s);
                result.add(validIp.toString());
            }
            return;
        }


        for( int i=1; i<s.length(); i++ ){

            String sub = s.substring(0,i);
            if( sub.length()<=3 && Integer.parseInt(sub) <= 255 ){

                if( sub.length()>1 && sub.charAt(0) == '0') continue;
                ipSeg.add(sub);
                backtrack(ipSeg,s.substring(i,s.length()));
                ipSeg.remove(ipSeg.size()-1);
            }

        }
    }

    public List<String> restoreIpAddresses(String s) {
        backtrack(new ArrayList<>(),s);
        return result;
    }
}