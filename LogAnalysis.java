import java.io.*;
import java.util.*;

public class LogAnalysis {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new FileReader("log.txt"));

        HashMap<String, Integer> map = new HashMap<>();

        String line;

        while ((line = br.readLine()) != null) {

            String[] words = line.split(" ");

            String logType = words[0];

            if (map.containsKey(logType)) {
                map.put(logType, map.get(logType) + 1);
            } else {
                map.put(logType, 1);
            }
        }

        br.close();

        System.out.println("Log Count:");

        for (String key : map.keySet()) {
            System.out.println(key + " : " + map.get(key));
        }
    }
}