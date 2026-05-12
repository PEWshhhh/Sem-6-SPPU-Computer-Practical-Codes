import java.io.*;
import java.util.*;

public class MapReduce {

    public static void main(String[] args) throws Exception {

        // Open log file
        File file = new File("log.txt");

        Scanner sc = new Scanner(file);

        // HashMap for storing word counts
        HashMap<String, Integer> map = new HashMap<>();

        // Read words one by one
        while(sc.hasNext()) {

            String word = sc.next();

            // Check if word already exists
            if(map.containsKey(word)) {

                // Increase count
                map.put(word, map.get(word) + 1);

            } else {

                // Add new word with count 1
                map.put(word, 1);
            }
        }

        // Print final output
        System.out.println("Reducer Output:");

        for(String key : map.keySet()) {

            System.out.println(key + " " + map.get(key));
        }

        sc.close();
    }
}