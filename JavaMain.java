import java.util.ArrayList;
import java.util.List;

public class JavaMain {
    public static void main(String[] args) {
        List<Double> numbers = parseArguments(args);

        if (numbers.isEmpty()) {
            numbers = List.of(1.5, 2.0, 3.5, 4.0);
            System.out.println("No numeric args provided. Using default numbers.");
        }

        double total = sum(numbers);
        System.out.println("Numbers: " + numbers);
        System.out.println("Sum = " + total);
    }

    public static double sum(List<Double> numbers) {
        return numbers.stream().mapToDouble(Double::doubleValue).sum();
    }

    private static List<Double> parseArguments(String[] args) {
        List<Double> numbers = new ArrayList<>();
        for (String arg : args) {
            try {
                numbers.add(Double.parseDouble(arg));
            } catch (NumberFormatException ignored) {
                System.err.println("Skipping invalid number: " + arg);
            }
        }
        return numbers;
    }
}
