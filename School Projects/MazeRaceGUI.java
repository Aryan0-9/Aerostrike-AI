
/*
 * Program header
 * Name: Aryan Juneja
 * Date: Tuesday May 26th, 2026
 * Course: ICS3U1 - 04 - Mr.Fernandes
 * Title: Aryan Juneja's Maze Race
 * Description: This program builds the maze frame and the core behind this game
 * Major skills: Importing methods, for loops, random functions, file reading
 * Added Features: Get player image to Face the Proper Direction as they move, Add more Accurate Timing (ex. tenths of seconds),
  Add a Menubar - with a number of options (New Game, Quit, etc.), Add a separate Opening Screen before the game starts, 
  Add a High Score label for the current game session, Add more Characters - user can select their character, Add Music and Sound Effects (ex. “Cha-ching” when you get a coin),
  Add Doorways/Portals, Add Power Ups (gives the player different special abilities)
  Add a Highscore with a player’s initials - save this information to an external text file; shows when the game is played and can get replaced by a new higher score, add a Highscore Table - saves the Top 5 scores to an external text file;this is able to be viewed (scores are sorted) and the information will get updated if a new Top 5 high score is achieved
 * Areas of concern: No validation of corrupted highscore.txt data, lags/game crashes and overlapping power ups
 * Sources: https://docs.oracle.com/javase/8/docs/api/java/util/Formatter.html - built knowledge for usage of formatter class, https://stackoverflow.com/questions/26305/how-can-i-play-sound-in-java - importing sound in java
 https://docs.oracle.com/javase/tutorial/uiswing/components/html.html - use for html 
 */



import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Formatter;
import java.util.Scanner;

import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.Timer;

public class MazeRaceGUI extends JFrame implements KeyListener, ActionListener {

	//Constants
	private final int CELL_SIZE = 25;
	private final int NUM_CELLS_WIDTH = 27;
	private final int NUM_CELLS_HEIGHT = 27;
	private final int NUM_COINS = 10;

	//Create panels for UI
	private JPanel mazePanel = new JPanel();
	private JPanel scoreboardPanel = new JPanel();
	
	//Create game grid
	private Cell[][] maze = new Cell[NUM_CELLS_HEIGHT][NUM_CELLS_WIDTH];

	//Menu system
	private JMenuBar menuBar = new JMenuBar();
	private JMenu gameMenu = new JMenu("Game");
	private JMenuItem newGameItem = new JMenuItem("New Game");
	private JMenuItem quitItem = new JMenuItem("Quit");
	private JMenuItem switchAccountItem = new JMenuItem("Switch Account");

	//Game images
	private final ImageIcon WALL = new ImageIcon("images/black square.png");
	private final ImageIcon OUT_OF_BOUNDS = new ImageIcon("images/red square.png");
	private final ImageIcon PATH = new ImageIcon("images/grey square.png");
	private final ImageIcon COIN = new ImageIcon("images/gold coin.gif");
	private final ImageIcon PORTAL = new ImageIcon("images/portal.jpg");
	private final ImageIcon SPEED_BOOST = new ImageIcon("images/speedboost.png");
	private final ImageIcon SHIELD = new ImageIcon("images/shield.png");
	private final ImageIcon COIN_MULTIPLIER = new ImageIcon("images/multiplier.png");
	
	//Character directions
	private final ImageIcon[] MARIO = {
			new ImageIcon("images/mario0.gif"),
			new ImageIcon("images/mario1.gif"),
			new ImageIcon("images/mario2.gif"),
			new ImageIcon("images/mario3.gif")
	};
	
	private final ImageIcon[] LUIGI = {
			 new ImageIcon("images/luigi0.gif"),
			 new ImageIcon("images/luigi1.gif"),
			 new ImageIcon("images/luigi2.gif"),
			 new ImageIcon("images/luigi3.gif")
	};
	
	private final ImageIcon[] BOWSER = {
			new ImageIcon("images/bowser0.gif"),
            new ImageIcon("images/bowser1.gif"),
            new ImageIcon("images/bowser2.gif"),
            new ImageIcon("images/bowser3.gif")
	};
	
	//Images for selected player 
	private ImageIcon[] PLAYER;

	//Player object
	private Player player;
	
	//Game states
	private int numCoinsCollected = 0;	
	private double time = 0;
	private final int MAX_SCORES = 5;
	private String[] topNames = new String[MAX_SCORES];
	private int[] topScores = new int[MAX_SCORES];
	private double[] topTimes = new double[MAX_SCORES];
	private String currentUser = null;
	private int currentUserScore;
	
	//Create 2 portals
	private Cell portalA;
	private Cell portalB;
	
	//Initialize power ups to false --> power ups are currently inactive 
	private boolean speedActive = false;
	private boolean shieldActive = false;
	private boolean multiplierActive = false;

	//Initialize time to 0 that power ups are active 
	private int speedTimer = 0;
	private int shieldTimer = 0;
	private int multiplierTimer = 0;

	//Time that power ups should be active 
	private final int SPEED_DURATION = 30;
	private final int SHIELD_DURATION = 50;
	private final int MULTIPLIER_DURATION = 50;

	//Active gameplay modifiers applied when a power-up is active
	private int coinMultiplier = 1;
	private int speedMoves = 1;
	
	//Total number of power-ups available or spawned in the game/level
	private final int NUM_SPEED = 3;
	private final int NUM_SHIELD = 2;
	private final int NUM_MULTIPLIER = 2;
    
	//Labels
	private JLabel scoreLabel = new JLabel("0");
	private JLabel timeLabel = new JLabel("0.0");
	private JLabel highScoreLabel = new JLabel("0");

	//Timer(Incremented by 100ms)
	private Timer gameTimer = new Timer(100, this);

	//Constructor
	public MazeRaceGUI() {

		createHighScoreFile();
		loadCharacter();
		loadHighScores();
		loginUser();
		menuSetup();
		scoreboardPanelSetup();
		mazePanelSetup();
		frameSetup();

	}
	
	//This method creates the high score file
	private void createHighScoreFile() {

	    try {

	    	//File for storing the leaderboard data
	        File file = new File("highscore.txt");
	        
	        //Check if the file is missing before attempting initialization
	        if (!file.exists()) {

	        	//Use formatter class
	            Formatter outputFile = new Formatter(file);

	            //Populate the file with default rows
	            for (int i = 0; i < MAX_SCORES; i++) {
	                outputFile.format("--- 0 9999.0%n");
	            }

	            //Close the formatter
	            outputFile.close();
	            
	        }
	        
	     // Log the error if the file cannot be created or written to
	    } catch (IOException e) {
	        System.out.println("File creation error.");
	    }
	}
	
	//This method focuses on loading the appropriate character based on users selection  
	private void loadCharacter() {

		//If user doesn't click anything character is Mario
	    if (Cell.selectedCharacter == null) {
	        Cell.selectedCharacter = "Mario";
	    }

	    //If user selects Mario, save Mario as the character 
	    if (Cell.selectedCharacter.equals("Mario")) {
	        PLAYER = MARIO;
	    }

	    //If user selects Luigi, save Luigi as the character 
	    else if (Cell.selectedCharacter.equals("Luigi")) {
	        PLAYER = LUIGI;
	    }

	    //If user selects Bowser, save Bowser as the character
	    else if (Cell.selectedCharacter.equals("Bowser")) {
	        PLAYER = BOWSER;
	    }
	    
	    //Spawn the player with the selected character's settings
	    player = new Player(PLAYER[1]);
	}
	
	//This method focuses on setting up the method
	private void menuSetup() {

		//Add items to the menu
		gameMenu.add(newGameItem);
		gameMenu.add(quitItem);
		gameMenu.add(switchAccountItem);
		switchAccountItem.addActionListener(this);

		//Add Game menu to menu bar
		menuBar.add(gameMenu);
		setJMenuBar(menuBar);

		//Attach menu bar to the frame
		newGameItem.addActionListener(this);
		quitItem.addActionListener(this);
	}

	//This method focuses on setting up the scoreboard panel
	private void scoreboardPanelSetup() {

	    //Position and size scoreboard panel at top of screen
	    scoreboardPanel.setBounds(0, 0, CELL_SIZE * NUM_CELLS_WIDTH, 80);
	    
	    //Use absolute positioning for labels
	    scoreboardPanel.setLayout(null);

	    //Labels
	    JLabel scoreTitle = new JLabel("COINS");
	    JLabel timeTitle = new JLabel("TIME");
	    JLabel leaderboardTitle = new JLabel("TOP PLAYERS");

	    //Customize title
	    scoreTitle.setFont(new Font("Arial", Font.BOLD, 16));
	    timeTitle.setFont(new Font("Arial", Font.BOLD, 16));
	    leaderboardTitle.setFont(new Font("Arial", Font.BOLD, 16));

	    //Customize labels
	    scoreLabel.setFont(new Font("Arial", Font.BOLD, 22));
	    timeLabel.setFont(new Font("Arial", Font.BOLD, 22));
	    highScoreLabel.setFont(new Font("Monospaced", Font.PLAIN, 12));

	    //Position score elements
	    scoreTitle.setBounds(40, 5, 100, 20);
	    scoreLabel.setBounds(50, 30, 100, 30);

	    //Position time elements
	    timeTitle.setBounds(210, 5, 100, 20);
	    timeLabel.setBounds(220, 30, 100, 30);

	    //Position leaderboard 
	    leaderboardTitle.setBounds(420, 2, 200, 20);
	    highScoreLabel.setBounds(420, 24, 260, 90);

	    //Add all components to panel
	    scoreboardPanel.add(scoreTitle);
	    scoreboardPanel.add(scoreLabel);
	    scoreboardPanel.add(timeTitle);
	    scoreboardPanel.add(timeLabel);
	    scoreboardPanel.add(leaderboardTitle);
	    scoreboardPanel.add(highScoreLabel);
	}

	//This method focuses on setting up the maze 
	private void mazePanelSetup() {

		//Set maze panel size and position
		mazePanel.setBounds(0, 65, CELL_SIZE * NUM_CELLS_WIDTH, CELL_SIZE * NUM_CELLS_HEIGHT);

		//Create grid layout for maze cells
		mazePanel.setLayout(new GridLayout(NUM_CELLS_HEIGHT, NUM_CELLS_WIDTH, 0, 0));

		//Call methods
		loadMaze();
		placeCoins();	
		placePortals();
		placePowerUps();
		placePlayer();
	}

	//This method focuses on placing the power ups 
	private void placePowerUps() {
		
		//Place speed boosts
		for (int count = 0; count < NUM_SPEED; count++) {
			Cell c = findEmptyCell();
			maze[c.getRow()][c.getColumn()].setIcon(SPEED_BOOST);
	    }
		
		//Place shields
		for (int count = 0; count < NUM_SHIELD; count++) {
			Cell c = findEmptyCell();
			maze[c.getRow()][c.getColumn()].setIcon(SHIELD);
	    }
		
		//Place coin multipliers
		for (int count = 0; count < NUM_MULTIPLIER; count++) {
			Cell c = findEmptyCell();
			maze[c.getRow()][c.getColumn()].setIcon(COIN_MULTIPLIER); 
		}
		
	}
	
	//Loads maze layout external text file
	private void loadMaze() {

		int row = 0;

		
		try {

			//Open the maze text file for reading
			Scanner inputFile = new Scanner(new File("images/maze.txt"));

			while (inputFile.hasNext()) {

				char[] line = inputFile.nextLine().toCharArray();

				for (int col = 0; col < line.length; col++) {
					fillCell(line[col], row, col);
				}

				row++;
			}

			//Close the scanner to free up system resources
			inputFile.close();

		} catch (FileNotFoundException e) {
			
			//Print the error details if the maze file is missing or cannot be opened
			System.out.println("File error: " + e);
		}
	}

	//Creates and assigns each maze cell type
	private void fillCell(char c, int row, int col) {

		//Create new cell object
		maze[row][col] = new Cell(row, col);

		//Assign title type based on character 
		if (c == 'W')
			maze[row][col].setIcon(WALL);
		else if (c == 'X')
			maze[row][col].setIcon(OUT_OF_BOUNDS);
		else
			maze[row][col].setIcon(PATH);

		//Add cell to maze panel
		mazePanel.add(maze[row][col]);
	}

	//This method finds a random empty path cell
	private Cell findEmptyCell() {

		Cell cell;

		//Keep picking random coordinates until an empty path is found
		do {
			cell = new Cell();
			
			//Generate a random row and column between index 2 and 25
			cell.setRow((int) (Math.random() * 24 + 2));
			cell.setColumn((int) (Math.random() * 24 + 2));

		} while (maze[cell.getRow()][cell.getColumn()].getIcon() != PATH);

		return cell;
	}

	// Places coins in random valid positions
	private void placeCoins() {

		//Loop through the total number of coins to be placed
		for (int i = 0; i < NUM_COINS; i++) {

			//Finds empty spot 
			Cell c = findEmptyCell();
			maze[c.getRow()][c.getColumn()].setIcon(COIN);
		}
	}
	
	//Places paired teleport portals
	private void placePortals() {
		
		//Find first portal
		do {
			portalA = findEmptyCell();
		}
		while (maze[portalA.getRow()][portalA.getColumn()].getIcon() != PATH);

		maze[portalA.getRow()][portalA.getColumn()].setIcon(PORTAL);

		//Find second portal
		do {
			portalB = findEmptyCell();
		}
		while (
			maze[portalB.getRow()][portalB.getColumn()].getIcon() != PATH ||
			(portalB.getRow() == portalA.getRow() && portalB.getColumn() == portalA.getColumn())
		);

		maze[portalB.getRow()][portalB.getColumn()].setIcon(PORTAL);
		
	}

	//Places player at a random valid starting position
	private void placePlayer() {

		//Find a random empty spot for the player
		Cell c = findEmptyCell();

		//Set the player's initial grid position
		player.setRow(c.getRow());
		player.setColumn(c.getColumn());

		//Draw the player icon on the maze grid
		maze[player.getRow()][player.getColumn()].setIcon(player.getIcon());
		
		mazePanel.revalidate();
		mazePanel.repaint();
	}

	//This method initializes main game window
	private void frameSetup() {

		setTitle("Maze Race");
		
		//Size the window to perfectly fit the maze, scoreboard, and borders
		setSize(mazePanel.getWidth() + 15,
		        mazePanel.getHeight() + scoreboardPanel.getHeight()+40);

		//Positioning for layout components
		setLayout(null);

		//Add game components to the main window
		add(scoreboardPanel);
		add(mazePanel);

		//Listen for player keyboard inputs
		addKeyListener(this);

		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setResizable(false);
		setVisible(true);

		gameTimer.start();
	}
	
	//This method plays sound effects from file path
	private void playSound(String filePath) {

		try {
			File soundFile = new File(filePath);
			Clip clip = AudioSystem.getClip();
			clip.open(AudioSystem.getAudioInputStream(soundFile));
			clip.start();

		} catch (Exception e) {
			System.out.println("Sound error: " + e);
		}
	}
	
	//Loads high score data from file
	private void loadHighScores() {

	    try {

	    	//Highscore text file 
	        File file = new File("highscore.txt");

	        //If the file is missing, create a blank default one
	        if (!file.exists()) {
	            createHighScoreFile();
	        }

	        Scanner inputFile = new Scanner(file);

	        //Tracks the current leaderboard rank being loaded
	        int rank = 0;

	        //Read data until the end of the file or the leaderboard slots are full
	        while (inputFile.hasNext() && rank < MAX_SCORES) {

	            topNames[rank] = inputFile.next();
	            topScores[rank] = inputFile.nextInt();
	            topTimes[rank] = inputFile.nextDouble();

	            rank++;
	        }

	        //Close the file reader
	        inputFile.close();
	        
	    }

	    catch (Exception e) {

	    	//Handle any file reading or data formatting errors
	        System.out.println("Error loading highscores.");
	    }

	    updateHighScoreLabel();
	}
	
	//This method handles login input
	private void loginUser() {

		 String name = JOptionPane.showInputDialog(this, "Enter your name:");

		    if (name == null || name.isEmpty()) {name = "Player";}

		    //Convert the user's name to uppercase for consistent leaderboard display
		    currentUser = name.toUpperCase();

		    currentUserScore = 0;

		    addHighScore(currentUser, 0, 9999);
	}
	
	//This method involves saving leaderboard to file
	private void saveHighScores() {
		
		    try {
		    	
		    	//Open the high score file for writing
		        Formatter outputFile = new Formatter("highscore.txt");

		        //Loop through each entry on the leaderboard
		        for (int entry = 0; entry < MAX_SCORES; entry++) {

		        	//Fill in default placeholder data if an entry is empty
		            if (topNames[entry] == null) {
		                topNames[entry] = "---";
		                topScores[entry] = 0;
		                topTimes[entry] = 9999;
		            }

		            outputFile.format(
		                    "%s %d %.1f%n",
		                    topNames[entry],
		                    topScores[entry],
		                    topTimes[entry]
		            );
		        }

		        //Close the file
		        outputFile.close();
		    }

		    catch (IOException e) {

		        System.out.println("Save error.");
		    }
		}
	
	//This method updates leaderboard entry
	private void addHighScore(String name, int score, double completionTime) {

	    boolean found = false;

	    //Fill empty slots
	    for (int slots = 0; slots < MAX_SCORES; slots++) {

	        if (topNames[slots] == null) {

	            topNames[slots] = "---";
	            topScores[slots] = 0;
	            topTimes[slots] = 9999;
	        }
	    }

	    //Check if player already exists
	    for (int rank = 0; rank < MAX_SCORES; rank++) {

	        if (topNames[rank].equalsIgnoreCase(name)) {

	            found = true;

	            //Update record if the new score is higher
	            if (score > topScores[rank]) {

	                topScores[rank] = score;
	                topTimes[rank] = completionTime;
	            }

	            //Same score but faster time
	            else if (score == topScores[rank] && completionTime < topTimes[rank]) {

	                topTimes[rank] = completionTime;
	            }

	            break;
	        }
	    }

	    //Add new player if not found
	    if (!found) {

	        //Find empty slot first
	        boolean added = false;

	        for (int slot = 0; slot < MAX_SCORES; slot++) {

	            if (topNames[slot].equals("---")) {

	                topNames[slot] = name;
	                topScores[slot] = score;
	                topTimes[slot] = completionTime;

	                added = true;
	                break;
	            }
	        }

	        //If the leaderboard is full replace worst player
	        if (!added) {

	            int worstIndex = 0;

	            for (int rank = 1; rank < MAX_SCORES; rank++) {

	                //Lower score is worse
	                if (topScores[rank] < topScores[worstIndex]) {

	                    worstIndex = rank;
	                }

	                // same score but slower time is worse
	                else if (topScores[rank] == topScores[worstIndex]
	                        && topTimes[rank] > topTimes[worstIndex]) {

	                    worstIndex = rank;
	                }
	            }

	            // replace if new score better
	            if (score > topScores[worstIndex]
	                    || (score == topScores[worstIndex]
	                    && completionTime < topTimes[worstIndex])) {

	                topNames[worstIndex] = name;
	                topScores[worstIndex] = score;
	                topTimes[worstIndex] = completionTime;
	            }
	        }
	    }

	    //Sort leaderboard
	    for (int current = 1; current < MAX_SCORES; current++) {

	        int compare = current;

	        while (compare > 0 &&
	              (topScores[compare] > topScores[compare - 1] ||
	              (topScores[compare] == topScores[compare - 1] &&
	               topTimes[compare] < topTimes[compare - 1]))) {

	            //Swap score
	            int tempScore = topScores[compare];
	            topScores[compare] = topScores[compare - 1];
	            topScores[compare - 1] = tempScore;

	            //Swap time
	            double tempTime = topTimes[compare];
	            topTimes[compare] = topTimes[compare - 1];
	            topTimes[compare - 1] = tempTime;

	            //Swap name
	            String tempName = topNames[compare];
	            topNames[compare] = topNames[compare - 1];
	            topNames[compare - 1] = tempName;

	            compare--;
	        }
	    }

	    saveHighScores();
	    updateHighScoreLabel();
	}

	//Refreshes and updates text displayed on continuous GUI panel layout
	private void updateHighScoreLabel() {

		//Begin building structured HTML string context
	    String text = "<html>";

	    //Initialize counter variable track visible slots populated
	    int shown = 0;

	    //Loop systematically through all leaderboard items
	    for (int slot = 0; slot < MAX_SCORES; slot++) {

	        if (topNames[slot] != null
	                && !topNames[slot].equals("---")) {

	            shown++;

	            String line =
	                    shown + ". " + topNames[slot] + " - "
	                    + topScores[slot]
	                    + " coins";

	            //Check if slot record matches active current player
	            if (topNames[slot].equalsIgnoreCase(currentUser)) {

	                text += "<font color='blue'><b>" + line + "</b></font><br>";}

	            else {

	                text += line + "<br>";
	            }
	        }
	    }

	    text += "</html>";
	    highScoreLabel.setText(text);
	}
	
	//Handles actions like timer ticks and menu clicks
	public void actionPerformed(ActionEvent event) {
		
		//Run this block if the game timer triggered the action (every 100ms)
		if (event.getSource() == gameTimer) {

			// Add 0.1 seconds to the clock
		    time += 0.1;
		    timeLabel.setText(String.format("%.1f", time));

		    //Speed boost countdown
		    if (speedActive) {

		        speedTimer--;
		        
		        //Accounts for if time ran out
		        if (speedTimer <= 0) {

		            speedActive = false;
		            speedMoves = 1;
		        }
		    }

		    //Shield countdown
		    if (shieldActive) {

		        shieldTimer--;

		        if (shieldTimer <= 0) {

		            shieldActive = false;
		        }
		    }

		    //Multiplier countdown
		    if (multiplierActive) {

		        multiplierTimer--;

		        if (multiplierTimer <= 0) {

		            multiplierActive = false;
		            coinMultiplier = 1;
		            
		        }
		    }
		}

		//Run this block if the user clicks "New Game" in the menu
		else if (event.getSource() == newGameItem) {

			//Close the current window
			dispose();
			new MazeRaceGUI();
		}

		//Run this block if the user clicks "Quit" in the menu
		else if (event.getSource() == quitItem) {
			
			showFinalHighScores();
			System.exit(0);
		}
		
		//Run this block if the user clicks "Switch Account"
		else if (event.getSource() == switchAccountItem) {

		    int choice = JOptionPane.showConfirmDialog(
		            this,
		            "Switch account? Progress will be saved.",
		            "Warning",
		            JOptionPane.YES_NO_OPTION
		    );

		    if (choice == JOptionPane.YES_OPTION) {

		        loginUser();
		        resetGame();
		    }
		}
		
	}

	//Handles keyboard arrow keys when pressed
	public void keyPressed(KeyEvent key) {
		
	    int dRow = 0;// How many rows to move (-1 for up, 1 for down)
	    int dCol = 0;// How many columns to move (-1 for left, 1 for right)

	    // Check which key was pressed, update the player sprite direction, and set movement values
	    if (key.getKeyCode() == KeyEvent.VK_UP) {

	        player.setIcon(PLAYER[0]);
	        dRow = -1;
	    }

	    else if (key.getKeyCode() == KeyEvent.VK_RIGHT) {

	        player.setIcon(PLAYER[1]);
	        dCol = 1;
	    }

	    else if (key.getKeyCode() == KeyEvent.VK_DOWN) {

	        player.setIcon(PLAYER[2]);
	        dRow = 1;
	    }

	    else if (key.getKeyCode() == KeyEvent.VK_LEFT) {

	        player.setIcon(PLAYER[3]);
	        dCol = -1;
	    }

	 // Move the player (loops multiple times if a speed boost is active)
	    for (int count = 0; count < speedMoves; count++) {

	        int nextRow = player.getRow() + dRow;
	        int nextCol = player.getColumn() + dCol;

	     //Stop moving if the target cell is outside the maze borders
	        if (nextRow < 0
	                || nextRow >= NUM_CELLS_HEIGHT
	                || nextCol < 0
	                || nextCol >= NUM_CELLS_WIDTH) {

	            break;
	        }

	     //Handle wall collisions
	        if (maze[nextRow][nextCol].getIcon() == WALL) {

	            //Shield allows for the player to pass through 
	            if (shieldActive) {

	            	 playSound("sounds/shieldblock.wav");

	                 //Reduce shield duration faster
	                 shieldTimer -= 5;
	                		 
	            }

	            else {

	                break;
	            }
	        }

	        movePlayer(dRow, dCol);
	    }
	}
	
	// Updates the player's position on the grid and triggers game item pickups
	private void movePlayer(int dRow, int dCol) {

		//Store old position
		int oldRow = player.getRow();
		int oldCol = player.getColumn();

		//Restore old tile properly
		if (isPortal(oldRow, oldCol)) {
			maze[oldRow][oldCol].setIcon(PORTAL);
			
		}
		
		
		else {
			maze[oldRow][oldCol].setIcon(PATH);
			
		}

		// Move player
		player.move(dRow, dCol);

		//Current tile
		ImageIcon current =
		        (ImageIcon) maze[player.getRow()][player.getColumn()].getIcon();

		
		//Coin collection
		if (current == COIN) {

		    //Remove collected coin
		    maze[player.getRow()][player.getColumn()].setIcon(PATH);

		    numCoinsCollected += coinMultiplier;

		    currentUserScore = numCoinsCollected;

		    //Update score label
		    scoreLabel.setText(Integer.toString(numCoinsCollected));

		    playSound("sounds/coin.wav");
		}	    

		//Speed boost
		if (current == SPEED_BOOST) {

		    speedActive = true;

		    speedTimer = SPEED_DURATION;

		    speedMoves = 3;

		    playSound("sounds/powerup.wav");
		    
		}

		//Shield
		if (current == SHIELD) {

		    shieldActive = true;

		    shieldTimer = SHIELD_DURATION;

		    playSound("sounds/powerup.wav");
		    
		}

		//Coin Multiplier
		if (current == COIN_MULTIPLIER) {

		    multiplierActive = true;

		    multiplierTimer = MULTIPLIER_DURATION;

		    coinMultiplier = 2;

		    playSound("sounds/powerup.wav");
		    
		}
		
		//Teleport from portal A to portal B
		if (player.getRow() == portalA.getRow()
				&& player.getColumn() == portalA.getColumn()) {

			maze[portalA.getRow()][portalA.getColumn()].setIcon(PORTAL);

			player.setRow(portalB.getRow());
			player.setColumn(portalB.getColumn());
		}

		//Teleport from portal B to portal A
		else if (player.getRow() == portalB.getRow()
				&& player.getColumn() == portalB.getColumn()) {

			maze[portalB.getRow()][portalB.getColumn()].setIcon(PORTAL);

			player.setRow(portalA.getRow());
			player.setColumn(portalA.getColumn());
		}

		//Draw player
		maze[player.getRow()][player.getColumn()].setIcon(player.getIcon());

		//Win condition
		if (numCoinsCollected >= NUM_COINS) {

			//Stop the gameplay timer clock 
		    gameTimer.stop();

		    //Add this run to the high scores list 
		    addHighScore(currentUser, numCoinsCollected, time);

		    playSound("sounds/win.wav");
		    showFinalHighScores();

		    //Ask the player if they want to play again 
		    int choice = JOptionPane.showConfirmDialog(
		            this,
		            "WINNER!\nPlay again?",
		            "Game Over",
		            JOptionPane.YES_NO_OPTION
		    );

		    
		    if (choice == JOptionPane.YES_OPTION) {
		    	
		    	//Ask if they want to keep using the same account name
		        int accountChoice = JOptionPane.showConfirmDialog(
		                this,
		                "Continue with current account?",
		                "Account",
		                JOptionPane.YES_NO_OPTION
		        );

		        //If they select no, prompt for a new account name input and update leaderboard
		        if (accountChoice == JOptionPane.NO_OPTION) {
		            loginUser();
		            showFinalHighScores();
		
		        }

		        resetGame();
		    }

		    else {

		        showFinalHighScores();
		        System.exit(0);
		    }
		}
	}
	
	//Completely clears current level progress stats and re-generates a fresh maze map
	private void resetGame() {

	    //Stop timer first
	    gameTimer.stop();

	    //Reset variables
	    numCoinsCollected = 0;
	    time = 0;

	    //Reset timers
	    speedActive = false;
	    shieldActive = false;
	    multiplierActive = false;

	    speedMoves = 1;
	    coinMultiplier = 1;

	    //Reset countdown clocks back to zero
	    speedTimer = 0;
	    shieldTimer = 0;
	    multiplierTimer = 0;

	    //Reset labels
	    scoreLabel.setText("0");
	    timeLabel.setText("0.0");

	    //Reset existing maze
	    mazePanel.removeAll();

	    //Rebuild maze data only
	    maze = new Cell[NUM_CELLS_HEIGHT][NUM_CELLS_WIDTH];

	    loadMaze();
	    placeCoins();
	    placePortals();
	    placePowerUps();
	    placePlayer();

	    //Refresh
	    mazePanel.revalidate();
	    mazePanel.repaint();
	    
	    //requestFocusInWindow();

	    gameTimer.start();
	}
	
	//Validates whether coordinates match any of the portal positions
	private boolean isPortal(int row, int col) {

		return (portalA != null && portalB != null && ((row == portalA.getRow() && col == portalA.getColumn()) ||
				(row == portalB.getRow() && col == portalB.getColumn() )));
	}
	
	//Converts double-precision seconds into human-readable MM:SS format
	private String formatTime(double seconds) {

	    int minutes = (int) seconds / 60;
	    int remainingSeconds = (int) seconds % 60;

	    return minutes + ":" +
	            String.format("%02d", remainingSeconds);
	}
	
	//Displays a standard popup message box displaying the leaderboard high scores
	private void showFinalHighScores() {

	    String text = "TOP 5 HIGH SCORES\n\n";

	    for (int entry = 0; entry < MAX_SCORES; entry++) {

	        if (topNames[entry] != null) {

	            text +=
	                    (entry + 1) + ". "
	                    + topNames[entry]
	                    + ": "
	                    + topScores[entry]
	                    + ", "
	                    + formatTime(topTimes[entry])
	                    + "\n";
	        }
	    }

	    JOptionPane.showMessageDialog(this, text);
	}

	public void keyTyped(KeyEvent e) {
		
		
	}
	
	public void keyReleased(KeyEvent e) {
		
	}

	
}