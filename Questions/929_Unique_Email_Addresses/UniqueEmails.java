import java.util.HashSet;

public class UniqueEmails{
    public int numUniqueEmails(String[] emails) {
        int eLength = emails.length;
        int index;
        int ampersand;
        
        HashSet<String> hset = new HashSet<String>();
        for (int i = 0; i < eLength; i++) {
            ampersand = emails[i].indexOf("@");
            String helper = emails[i].substring(ampersand, emails[i].length()-1);
            emails[i] = emails[i].substring(0,ampersand-1);
            index = emails[i].indexOf("+");
            if (index != -1) {
                emails[i] = emails[i].substring(0, index);
            }
            for (int k = 0; k < emails[i].length(); k++) {
                index = emails[i].indexOf(".");
                if (index == -1) {
                    break;
                } else {
                    StringBuilder sb = new StringBuilder(emails[i]);
                    sb.deleteCharAt(index);
                    emails[i] = sb.toString();
                }        
                k = index;
            }
            hset.add(emails[i] + helper);
        }     
        return hset.size();
    }
}
