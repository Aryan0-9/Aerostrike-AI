import javax.swing.ImageIcon;
import javax.swing.JLabel;

public class Cell extends JLabel{
	
	//A global variable to store the chosen character name across all screens
	public static String selectedCharacter;
	
	private int row;
	private int column;
	private ImageIcon icon;
	
	//Empty constructor - no row and column
	public Cell() {
		
	}
	
	//Regular constructor - we know the position
	public Cell(int row, int column) {
		super();
		this.row = row;
		this.column = column;
	}
	
	//Getter and setter methods below 
	
	public int getRow() {
		return row;
	}

	public void setRow(int row) {
		this.row = row;
	}

	public int getColumn() {
		return column;
	}

	public void setColumn(int column) {
		this.column = column;
	}
	
	public ImageIcon getIcon() {
		
		return icon;
		
	}
	
	public void setIcon(ImageIcon icon) {
		
		this.icon = icon;
		super.setIcon(icon);
		
	}
	

	//To string method 
	public String toString() {
		return "Cell [row=" + row + ", column=" + column + "]";
	} 
	
	
	
	
	
}
