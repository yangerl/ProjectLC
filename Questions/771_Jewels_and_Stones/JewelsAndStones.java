public class JewelsAndStones {
    public int numJewelsInStones(String J, String S) {
        int SLength = S.length();
        int counter = 0;
        for (int i = 0; i < SLength; i++) {
            if (J.contains(Character.toString(S.charAt(i)))) {
                counter++;
            }
        }
        return counter;
    }
}
