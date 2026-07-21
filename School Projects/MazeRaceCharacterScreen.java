
/*
 * Name: Aryan Juneja
 * Date: Tuesday, May 26th, 2026
 * Course: ICS3U1 - 04 - Mr.Fernandes
 * Title: Character selection
 * Description: This frame models the character selection process for my game
 * Major skills: Importing methods, if/else statements, importing images
 * Areas of concern: Increase button size to maximize space, more vibrant colors and images
 * 
 */

import java.awt.Font;
import java.awt.GridLayout;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;

public class MazeRaceCharacterScreen extends JFrame implements ActionListener {

	//Create menu bar items 
	private JMenuBar menuBar = new JMenuBar();
	private JMenu gameMenu = new JMenu("Game");
	private JMenuItem quitItem = new JMenuItem("Quit");
	
	//Create label for background
	private JLabel background = new JLabel();
	
	//Create 3 pillars/panels
	private JPanel marioPanel = new JPanel();
	private JPanel luigiPanel = new JPanel();
	private JPanel bowserPanel = new JPanel();

	//Create buttons
	private JButton marioButton = new JButton("Select");
	private JButton luigiButton = new JButton("Select");
	private JButton bowserButton = new JButton("Select");
	
	//Constructor 
	public MazeRaceCharacterScreen() {

		//Call methods
		menuSetup();
		backgroundSetup();
		panelSetup();
		frameSetup();
		
	}
	
	//This method focuses on setting up the menubar
	private void menuSetup() {
		
		//Adding items to menubar
		gameMenu.add(quitItem);
		menuBar.add(gameMenu);
		setJMenuBar(menuBar);
		quitItem.addActionListener(this);
		
	}

	//This method focuses on setting up the background
	private void backgroundSetup() {
		
		//Fit background completely 
		background.setBounds(0, 0, 1000, 600);
		ImageIcon back_ground = new ImageIcon("images/Characters.png");
		
		//Smoothly scale image
		Image image = back_ground.getImage().getScaledInstance(
				1000,
				600,
				Image.SCALE_SMOOTH);
		background.setIcon(new ImageIcon(image));
		background.setLayout(new GridLayout(1, 3, 50, 80));
		
	}

	//Three character column cards onto the background layout
	private void panelSetup() {
		
		//Setup configuration for Mario's card 
		setupCharacterPanel(marioPanel, "Mario", "images/mario.png", marioButton);
		
		//Setup configuration for Luigi's card
		setupCharacterPanel(luigiPanel, "Luigi", "images/luigi.png", luigiButton);
		
		//Setup configuration for Bowser's card
		setupCharacterPanel(bowserPanel,"Bowser", "images/bowser.png", bowserButton);
		
		//Add the cards to the background
		background.add(marioPanel);
		background.add(luigiPanel);
		background.add(bowserPanel);
		
	}

	//This method focuses on setting up the panels
	private void setupCharacterPanel(JPanel panel, String name, String imagePath, JButton button) {
		
		//Divide the card into 3 sections 
		panel.setLayout(new GridLayout(3, 1, 0, 10));
		panel.setBorder(BorderFactory.createLineBorder(java.awt.Color.BLACK));
		JLabel imageLabel = new JLabel();
		
		//Align images in the center 
		imageLabel.setHorizontalAlignment(JLabel.CENTER);
		ImageIcon icon = new ImageIcon(imagePath);
		Image image = icon.getImage().getScaledInstance(200, 200, Image.SCALE_SMOOTH);
		imageLabel.setIcon(new ImageIcon(image));
		
		//Establish centered label displaying name text
		JLabel nameLabel = new JLabel(name, JLabel.CENTER);
		nameLabel.setFont(new Font("Arial", Font.BOLD, 25));
		button.addActionListener(this);
		
		//Add the image, name and button to the panel 
		panel.add(imageLabel);
		panel.add(nameLabel);
		panel.add(button);
		
	}
	
	//This method focuses on setting up the frame
	private void frameSetup() {
		
		setTitle("Character Selection");
		setSize(1000, 600);
		setLayout(null);
		add(background);
		setResizable(false);
		setDefaultCloseOperation(DISPOSE_ON_CLOSE);
		setVisible(true);

	}

	//This method listens for clicks on buttons and menu items
	public void actionPerformed(ActionEvent event) {
		
		//Process input if user chooses Mario profile options
		if (event.getSource() == marioButton) {
			
			Cell.selectedCharacter = "Mario";
			dispose();
		}
		
		//Process input if user chooses Luigi profile options
		else if (event.getSource() == luigiButton) {

			Cell.selectedCharacter = "Luigi";
			dispose();
		}
		
		//Process input if user chooses Bowser profile options
		else if (event.getSource() == bowserButton) {

			Cell.selectedCharacter = "Bowser";
			dispose();
		}
		
		//Handle system shutdown trigger actions requests
		else if (event.getSource() == quitItem) {
			
			System.exit(0);
		}
		
	}

}
