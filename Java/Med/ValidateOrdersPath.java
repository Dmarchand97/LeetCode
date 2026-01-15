import javax.swing.*;
import java.util.HashSet;
import java.util.Set;

public class ValidateOrdersPath {
    public boolean isValidPath(String[] path) {
        Set<Integer> pickups = new HashSet<>();
        Set<Integer> deliveries = new HashSet<>();

        for (String step : path) {
            char type = step.charAt(0);
            int orderid = Integer.parseInt(step, 1);

            if (type == 'P') {
                if (pickups.contains(orderid)) {
                    return false;
                } else {
                    pickups.add(orderid);
                }
            } else {
                if (!pickups.contains(orderid)) {
                    return false;
                }
                if (deliveries.contains(orderid)) {
                    return false;
                }
                deliveries.add(orderid);
            }
        }
        return pickups.equals(deliveries);
    }
}
