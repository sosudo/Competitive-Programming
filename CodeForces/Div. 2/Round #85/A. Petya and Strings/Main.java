import java.io.*;
import java.util.StringTokenizer;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter pw = new PrintWriter(System.out);
		String a = r.readLine();
		String b = r.readLine();
		a = a.toLowerCase();
		b = b.toLowerCase();
		int z = a.compareTo(b);
		z = z > 0 ? 1 : z < 0 ? -1 : 0;
		pw.println(z);
		pw.flush();
		pw.close();
	}
}
