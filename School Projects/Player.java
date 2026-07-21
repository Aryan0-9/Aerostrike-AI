import javax.swing.ImageIcon;

public class Player extends Cell{
	
	//NO EXTRA FIELDS
	public Player(ImageIcon image) {
		
		setIcon(image);
		
	}
	
	//dRow and dColumn - will be -1, 0, or 1
	public void move(int dRow, int dColumn) {
		
		setRow(getRow() + dRow);
		setColumn(getColumn() +dColumn);
		
	}
	
	
	
}
