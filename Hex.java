/**************************************************************************    
Cindy Zheng                                                                    
Cybersecurity                                                                  
XOR Strings                                                                   
                                                                               
Given three strings mode, text, and key: it will produce an output string by x\
r'ing corresponding values together.                                           
 *************************************************************************/
import java.nio.file.*;
public class Hex{

    public static void main(String[]args){
	String mode;
	String keyfile;
	String inpfile;
	String key;
	String inp;
	boolean debug = true;
	try{
	    mode = args[0];
	    keyfile = args[1];
	    inpfile = args[2];
	    key = Files.readString(Path.of(keyfile));
	    key = key.substring(0, key.length());
	    inp = Files.readString(Path.of(inpfile));
	    inp = inp.substring(0, inp.length());
	    if(debug){
		System.out.println("mode:"+mode);
		System.out.println("key: "+key);
		System.out.println("inp: "+inp);
	    }
	}catch(Exception e){
	    e.printStackTrace();
	    System.exit(1);
	}
       
    }
}
