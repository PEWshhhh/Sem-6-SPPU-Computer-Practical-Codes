import java.io.*;
import java.util.*;

public class WeatherData {

    public static void main(String[] args) throws Exception {

        double tempSum = 0;
        double dewSum = 0;
        double windSum = 0;

        int count = 0;

        File file = new File("weather.txt");

        Scanner sc = new Scanner(file);

        while(sc.hasNextLine()) {

            String line = sc.nextLine();

            // Skip empty lines
            if(line.trim().isEmpty()) {
                continue;
            }

            // Split values using spaces
            String values[] = line.split("\\s+");

            // Add values
            tempSum += Double.parseDouble(values[0]);

            dewSum += Double.parseDouble(values[1]);

            windSum += Double.parseDouble(values[2]);

            count++;
        }

        // Calculate averages
        double avgTemp = tempSum / count;

        double avgDew = dewSum / count;

        double avgWind = windSum / count;

        // Print output
        System.out.println("Average Temperature: " + avgTemp);

        System.out.println("Average Dew Point: " + avgDew);

        System.out.println("Average Wind Speed: " + avgWind);

        sc.close();
    }
}