import java.util.HashMap;
import java.util.Map;

public class AuthData {

    public static final String LOG = "login2",
    public static final String PASS = "password2",
    public static final String FAKE_LOG = "log2in",
    public static final String FAKE_PASS = "pass2word"
}

public class NewsData {
    public static Map<String, String> data;

    static {
      data = new HashMap<>();
        data.put("category", "Профсоюз");
        data.put("title", "Внимание!!!");
        data.put("date", "10.10.1910");
        data.put("time", "17:10");
        data.put("description", "Hello!");
