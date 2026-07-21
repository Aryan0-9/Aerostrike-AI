
/*
 * Program header
 * Name: Aryan Juneja
 * Date: May 26th, 2026
 * Course: ICS3U1 - 04 - Mr.Fernandes
 * Title: MazeRace
 * Description: This program acts as the opening screen for the entire application
 * Major skills: Importing methods, call and create methods, importing images, creating message boxes
 * Areas of concern: Image scaling, panel size, layout positioning 
 * 
 */

import java.awt.Font;
import java.awt.GridLayout;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;


public class MazeRaceOpeningScreen extends JFrame implements ActionListener{

	//Create menu bar items
	private JMenuBar menuBar = new JMenuBar();
	private JMenu gameMenu = new JMenu("Game");
	private JMenuItem quitItem = new JMenuItem("Quit");
	
	//Create visual labels for the window layout 
	private JLabel background = new JLabel();
	private JLabel titleLabel = new JLabel("MazeRace");
	
	//Create main menu navigation buttons
	private JButton playButton = new JButton("Play");
	private JButton backgroundButton = new JButton("Background Info");
	private JButton characterButton = new JButton("Characters");
	private JButton instructionButton = new JButton("Instructions");
	
	//Create button panel
	private JPanel buttonPanel = new JPanel();
	
	//Constructor
	public MazeRaceOpeningScreen() {

		//Call methods
		menuSetup();
		backgroundSetup();
		titleSetup();
		buttonPanelSetup();
		frameSetup();
	}
	
	//This method allows for the setup of menu
	private void menuSetup() {
		
		//Add items to the background
		gameMenu.add(quitItem);
		menuBar.add(gameMenu);
		setJMenuBar(menuBar);
		quitItem.addActionListener(this);
		
	}

	//This method allows for the setup of the background
	private void backgroundSetup() {
		
		//Size the background
		background.setBounds(0, 0, 800, 800);
		ImageIcon back_ground = new ImageIcon("images/MazeBackground.png");
		Image image = back_ground.getImage().getScaledInstance(
				800,
				800,
				Image.SCALE_SMOOTH);
		background.setIcon(new ImageIcon(image));
		background.setLayout(null);
		
	}

	//This method focuses on setting up the title
	private void titleSetup() {
		
		//Positions the title
		titleLabel.setBounds(310, 40, 300, 60);
		titleLabel.setFont(new Font("Arial", Font.BOLD, 40));
		background.add(titleLabel);
		
	}

	//This method sets up the button panel
	private void buttonPanelSetup() {
		
		//Position the button panel
		buttonPanel.setBounds(250, 180, 300, 300);
		buttonPanel.setLayout(new GridLayout(4, 1, 15, 15));
		buttonPanel.setOpaque(false);

		//Make the buttons clickable
		playButton.addActionListener(this);
		backgroundButton.addActionListener(this);
		characterButton.addActionListener(this);
		instructionButton.addActionListener(this);

		//Add the buttons to the button panel
		buttonPanel.add(playButton);
		buttonPanel.add(backgroundButton);
		buttonPanel.add(characterButton);
		buttonPanel.add(instructionButton);
		background.add(buttonPanel);
		
	}

	//This method focuses on setting up the frame
	private void frameSetup() {
		
		setTitle("MazeRace");
		setSize(800, 800);
		setLayout(null);
		add(background);
		setResizable(false);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
		
	}

	
	//Listens for button clicks 
	public void actionPerformed(ActionEvent event) {
		
		//If user selects 'Play' option pathway
		if(event.getSource() == playButton) {
			
			new MazeRaceGUI();
			dispose();
			
		}
		
		//If user selects 'Background Info' button panel
		else if(event.getSource() == backgroundButton) {
			
			JOptionPane.showMessageDialog(
					this,
					"This game was created on May 26th, 2026 and was founded by Aryan Juneja. This is currently version 1 of the game. The game was inspired by Super Mario"
			);
			
		}
		
		//If user selects 'Characters' configuration option panel
		else if(event.getSource() == characterButton) {
			
			new MazeRaceCharacterScreen();
			
		}
		
		//If user selects 'Instructions' button pathway step items
		else if(event.getSource() == instructionButton) {
			
			JOptionPane.showMessageDialog(
					this,
					"Once you select your character and click 'Play', your objective is to collect all the coins in the least amount of time. There are various powerups that can boost your chances. Good luck!"
			);
			
		}
		
		//Handle system shutdown actions request
		else if(event.getSource() == quitItem) {
			
			System.exit(0);
			
		}
		
	}
	
	

}
