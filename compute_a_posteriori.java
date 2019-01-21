import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.Arrays;
import java.util.List;

public class compute_a_posteriori {


	public static void main(String[] args) {

		List<Double> prior = Arrays.asList(0.1,0.2,0.4,0.2,0.1);
		List<Double> c_prob = Arrays.asList(1.0,0.75,0.50,0.25,0.0);
		List<Double> l_prob = Arrays.asList(0.0,0.25,0.50,0.75,1.0);

		String Q="";
		Integer siz = 0;
		String result = "";

		List<Double> b_prob=prior;
		Double c_sum=0.0;
		Double l_sum=0.0;

		Q=args[0];
		siz=Q.length();

		result = "Observed sequence: "+Q;
		result += "\nLength of Q: "+siz;

		for(int j=0;j<=4;j++) {
			c_sum+= (b_prob.get(j)) * c_prob.get(j);
			l_sum+=(b_prob.get(j)) * l_prob.get(j);
		}

		for(int i=1;i<=siz;i++) {
			result+="\nAfter Observation: "+i + " = "+ Q.charAt(i-1);		
			if(Q.charAt(i-1)!='C') {
				for(int j=0;j<=4;j++) {
					Double t=((b_prob.get(j)) * l_prob.get(j))/l_sum;
					b_prob.set(j, t);
					result+="\nP(h"+(j+1)+" | Q) = "+String.format("%.10f", t);

				}
			}
			else {				
				for(int j=0;j<=4;j++) {
					Double t=((b_prob.get(j)) * c_prob.get(j))/c_sum;
					b_prob.set(j, t);
					result+="\nP(h"+(j+1)+" | Q) = "+String.format("%.10f", t);
				}
			}
			c_sum=0.0;
			l_sum=0.0;
			for(int j=0;j<=4;j++) {
				c_sum+= (b_prob.get(j)) * c_prob.get(j);
				l_sum+=(b_prob.get(j)) * l_prob.get(j);
			}

			result+="\nProbability that the next candy we pick will be C, given Q:"+String.format("%.10f", c_sum);
			result+="\nProbability that the next candy we pick will be L, given Q:"+String.format("%.10f", l_sum);
		}
		System.out.println(result);
        try{
			
			FileWriter f = new FileWriter("result.txt",false);
			BufferedWriter output = new BufferedWriter(f);
			output.write(result);
			output.close();
			f.close();
		}
		catch (Exception e){
			e.printStackTrace();
		}


	}
}







