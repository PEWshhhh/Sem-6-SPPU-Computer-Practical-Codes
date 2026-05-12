import java.io.*;

public class WeatherAvg {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new FileReader("sample_weather.txt"));

        String line;

        double tempSum = 0;
        double dewSum = 0;
        double windSum = 0;

        int count = 0;

        while ((line = br.readLine()) != null) {

            String[] parts = line.split(" ");

            double temp = Double.parseDouble(parts[1]);
            double dew = Double.parseDouble(parts[2]);
            double wind = Double.parseDouble(parts[3]);

            tempSum += temp;
            dewSum += dew;
            windSum += wind;

            count++;
        }

        br.close();

        System.out.println("Average Temperature: " + (tempSum / count));
        System.out.println("Average Dew Point: " + (dewSum / count));
        System.out.println("Average Wind Speed: " + (windSum / count));
    }
}