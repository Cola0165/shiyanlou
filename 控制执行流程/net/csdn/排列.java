package net.csdn;

import java.util.ArrayList;
import java.util.List;

public class 排列 {

    public static String drop(String token, int idx){
        if(idx==0){
            return token.substring(1);
        }
        if(idx>=token.length()-1){
            return token.substring(0, idx);
        }
        return token.substring(0, idx) + token.substring(idx+1);
    }

    public static List<String> permutation(String token){
        if(token.length() < 2){
            return List.of(token);
        }
        if(token.length()==2){
            String item = token.charAt(1) + String.valueOf(token.charAt(0));
            return List.of(token, item);
        }
        List<String> result = new ArrayList<>();
        for(int idx=0;idx<token.length();idx++){
            char chr = token.charAt(idx);
            String next = drop(token, idx);

            for(var rest: permutation(next)){
                result.add(chr +rest);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        String token = args[0];
        for(var item: permutation(token)){
            System.out.println(item);
        }
    }
}