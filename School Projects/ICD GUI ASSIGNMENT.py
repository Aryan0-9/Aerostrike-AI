#Import the libraries and random module  
import tkinter
import random
import tkinter.messagebox

#Create the question data, for each grade starting off at grade 1
#Create the questions using lists and dictionaries 
#Makes it easier to retrieve question data 
Grade_1_questions = { 
   #Create math questions
    "Math": [ 
        {'Question': "What is 3+5?", "answer": "8", "options": ['5', '2', '8', '9']},
        {'Question': "What is 15+6?", "answer": "21", "options": ['20', '21', '22', '23']},
        {'Question': "What is 11+9?", "answer": "20", "options": ['20', '19', '18', '21']}
    ], 
    #Create science questions
    "Science": [
        {'Question': "What do plants need to grow?", "answer": "Sunlight", "options": ['Sunlight', 'Milk', 'Juice', 'Fruits']}, 
        {'Question': "How many planets are in our solar system?", "answer": "8", "options": ['4', '5', '9', '8']},
        {'Question': "What do living things need to survive?", "answer": "All of the above", "options": ['Shelter', 'Food', 'Air', 'All of the above']},
    ],
    #Create english questions
    "English":[
        {'Question': "What is the opposite of hot?", "answer": "Cold", "options": ['Boiling', 'Cold', 'Warm', 'Hot']}, 
        {'Question': "What is the opposite of light?", "answer": "Dark", "options": ["Dark", "Light", "Bright", "Colorful"]},
        {'Question': 'The dog barked. Is this past, present or future tense?', 'answer': 'Past', 'options': ['Past', 'Present', 'Future', 'None of the above']},
    ]

}
#Create questions for grade 2 
Grade_2_questions = {
    "Math": [
        {'Question': "What is 17 + 32?", "answer": "49", "options": ['39', '59', '49', '50']},
        {'Question': "What is 58 - 33?", "answer": "25", "options": ["25", "24", "35", "31"]},
        {'Question': "What is 49+11?", "answer": "60", "options": ['50', '60', '70', '51']},

    ],
    
     "Science": [
        {'Question': 'What is the 4th planet in the solar system?', 'answer': 'Mars', 'options': ['Earth', 'Venus', 'Jupiter', 'Mars']}, 
        {'Question': 'Which of these animals is a carnivore?', 'answer': 'Lion', 'options': ['Elephants', 'Lion', 'Cows', 'Zebra']},
        {'Question': 'What do humans exhale?', 'answer': 'Carbon dioxide', 'options': ['Carbon monoxide', 'Carbon dioxide', 'Oxygen', 'Nitrogen']},
    ],

    "English": [
        {'Question': 'Which word is a noun?', 'answer': 'Dog', 'options': ['Dog', 'Run', 'Quickly', 'Under']},
        {'Question': 'What is the opposite of happy?', 'answer': 'Sad', 'options': ['Happy', 'Sad', 'Angry', 'Excited']},
        {'Question': 'What is the plural form for deer?', 'answer': 'Deer', 'options': ['Deers', 'Deered', 'Deering', 'Deer']},
    ],

}
#Create questions for grade 3
Grade_3_questions = {
    #Create grade 3 math questions
    "Math": [
        {'Question': 'What is 25 x 2?', 'answer': '50', 'options': ['27', '35', '40', '50']},
        {'Question': 'What is 5 x 3?', 'answer': '15', 'options': ['8', '10', '15', '20']},
        {'Question': 'How many sides are in a hexagon?', 'answer': '6', 'options': ['6', '8', '7', '9']},
    ],
    #Create grade 3 science qustions
    "Science": [
        {'Question': 'What planet is closest to the Sun?', 'answer': 'Mercury', 'options': ['Earth', 'Venus', 'Mars', 'Mercury']},
        {'Question': 'Which parts of a plant absorb water and nutrients?', 'answer': 'Roots', 'options': ['Leaves', 'Roots', 'Flowers', 'Stem']},
        {'Question': 'What do humans inhale?', 'answer': 'Oxygen', 'options': ['Carbon dioxide', 'Oxygen', 'Nitrogen', 'Carbon monoxide']},
    ],
    #Create english questions
    "English": [
        {'Question': 'Which of the following is a verb?', 'answer': 'Run', 'options': ['Run', 'Dog', 'Blue','Quick']},
        {'Question': 'What is the plural form of child?', 'answer': 'Children', 'options': ['Children', 'Child', 'Childs', 'Childrens']},
        {'Question': 'How many syllables are in the word, elephant', 'answer': '3', 'options':['1', '2', '3', '4']},
    ],

} 
#Create questions for grade 4
Grade_4_questions = {
    #Create math questions
    "Math": [
        {'Question': 'What is 7 x 9?', 'answer': '63', 'options': ['63', '72', '70', '54']},
        {'Question': 'What is the formula for the area of a triangle?', 'answer': '0.5 X base X height', 'options': ['L x L', 'L x W x W', '0.5 X base X height', 'W x W']},
        {'Question': 'What is the place value of the digit 5 in the number 4,582?', 'answer': 'Hundreds', 'options': ['Tens', 'Thousands', 'Hundreds', 'Ones']},
    ],
    #Create science questions
    "Science": [
        {'Question': 'What do we call animals that eat only plants?', 'answer': 'Herbivores', 'options': ['Herbivores', 'Carnivores', 'Omnivores', 'None of the above']},
        {'Question': 'What is the process by which plants make their own food?', 'answer': 'Photosynthesis', 'options': ['Photosynthesis', 'Breathing', 'Digestion', 'Absorption']},
        {'Question': 'What tool is used to measure temperature?', 'answer': 'Thermometer', 'options': ['Barometer', 'Scale', 'Ruler', 'Thermometer']},
    ],
    #Create english questions
    "English": [
        {'Question': 'What is the subject in this sentence: “The cat chased the mouse”?', 'answer': 'The cat', 'options': ['Chased', 'The cat', 'Mouse', 'The mouse']},
        {'Question': 'Which word is an adjective?', 'answer': 'Happy', 'options': ['Run', 'Yesterday', 'Sing', 'Happy']},
        {'Question': 'Which is past tense?', 'answer': 'She played outside', 'options': ['She played outside', 'She is playing outside', 'She plays outside']},
    ],

}
#Create questions for grade 5
Grade_5_questions = {
    #Create math questions
    "Math": [
        {'Question': 'When tossing a coin, what is the probability of landing heads', 'answer': '50%', 'options': ['50%', '40%', '100%', '60%']},
        {'Question': 'What transformation is responsible for moving an image up or down?', 'answer': 'Vertical translation', 'options': ['Vertical translation', 'Horizontal translation', 'Reflection', 'Rotation']},
        {'Question': 'What is the value of a dime?', 'answer': '$0.10', 'options': ['$0.05', '$0.25', '$0.10', '$0.50']},
    ],
    #Create science questions
    "Science": [
        {'Question': 'Which is a form of non renewable energy?', 'answer': 'Nuclear energy', 'options': ['Nuclear energy', 'Hydroelectric energy', 'Wind energy', 'Solar energy']},
        {'Question': 'What is a state of matter?', 'answer': 'Gas', 'options': ['Ice', 'Lava', 'Gas', 'Rock']},
        {'Question': 'Which of the following is a type of rock?', 'answer': 'Igneous', 'options': ['Igneous', 'Lake', 'Water', 'Plutonium']},
    ],
    #Create english questions
    "English": [
        {'Question': 'Which tense is the following sentence in: You have to work on Monday.', 'answer': 'Present tense', 'options': ['Present tense', 'Future tense', 'Past tense', 'None of the above']},
        {'Question': 'Which is an antonym to benefit?', 'answer': 'Detriment', 'options': ['Profit', 'Detriment', 'Asset', 'Welfare']},
        {'Question': 'Which of the following is a noun?', 'answer': 'Teacher', 'options': ['Beautiful', 'Fast', 'Teacher', 'Took']},
    ]
}
#Create questions for grade 6
Grade_6_questions = {
    #Create math questions
    "Math": [
        {'Question': 'What is the area of a rectangle with a length of 8 cm and width of 5 cm?', 'answer': '40 cm^2', 'options': ['40 cm^2', '40 m^2', '80 cm^2', '13 cm^2']},
        {'Question': 'What is 75 percent of 40?', 'answer': '30', 'options': ['20', '30', '40', '35']},
        {'Question': 'Select the number that is a prime number', 'answer': '13', 'options': ['6', '4', '9', '13']},
    ], 
    #Create science questions
    "Science": [
        {'Question': 'What is the main function of the heart?', 'answer': 'Pump blood', 'options': ['Pump air', 'Pump blood', 'Digest food', 'Filter waste']},
        {'Question': 'What form of energy comes from the sun?', 'answer': 'Light and heat', 'options': ['Electrical', 'Mechanical', 'Light and heat', 'Sound']},
        {'Question': 'Which planet is known as the "Red Planet"', 'answer': 'Mars', 'options': ['Earth', 'Venus', 'Jupiter', 'Mars']},
    ],
    #Create english questions
    "English": [
        {'Question': 'What is the prefix in the word “unfriendly”?', 'answer': 'un', 'options': ['friend', 'un', 'ly', 'friendly']},
        {'Question': 'Choose the correct homophone: I left my shoes over ___', 'answer': 'there', 'options': ['there', 'their', 'they', 'None of the above']},
        {'Question': 'Read the sentence: "The wind howled through the trees." What type of figurative language is used?', 'answer': 'Personification', 'options': ['Simile', 'Personification', 'Metaphor', 'Alliteration']},
    ]
}
#Create grade 7 questions
Grade_7_questions = {
    #Create questions for math
    "Math": [
        {'Question': 'Solve for x: 2(x+3) = 14', 'answer': '4', 'options': ['2', '4', '5', '7']},
        {'Question': 'What type of triangle has all equal sides?', 'answer': 'Equilateral', 'options': ['Equilateral', 'Isosceles', 'Scalene', 'All of the above']},
        {'Question': 'What is the volume of a cube with side length 3 cm?', 'answer': '27 cm^3', 'options': ['9cm^3', '18cm^3', '27cm^3', '81cm^3']},
    ],
    #Create questions for science
    "Science": [
        {'Question': 'Which part of a plant carries water?', 'answer': 'Stem', 'options': ['Leaves', 'Flowers', 'Seeds', 'Stems']},
        {'Question': 'Which is the standard unit of mass?', 'answer': 'Grams', 'options': ['Grams', 'AMU', 'Pounds', 'None of the above']},
        {'Question': 'Which of the following is a pure substance?', 'answer': 'None of the above', 'options': ['Cookie', 'Sand', 'Toothpaste', 'Soap']},
    ],
    #Create questions for english
    "English": [
        {'Question': 'What is the function of a conjunction?', 'answer': 'Join words or sentences', 'options': ['Join words or sentences', 'Show emotion', 'Describe nouns', 'Replace nouns']},
        {'Question': 'Which sentence is correct?', 'answer': 'She went to the mall', 'options': ['She wents to the mall', 'She whent to the mall', 'She went to the mall', 'She gone to the mall']}, 
        {'Question': 'Which is the noun?', 'answer': 'All of the above', 'options': ['Place', 'Animal', 'Human', 'All of the above']},
    ],
    #Create questions for geography
    "Geography": [
        {'Question': 'Which province has the most people in Canada?', 'answer': 'Ontario', 'options': ['Alberta', 'Quebec', 'Ontario', 'British Columbia']},
        {'Question': 'What is a topographic map?', 'answer': 'A map showing elevation and landforms', 'options': ['A map showing elevation and landforms', 'A political map', 'A weather map', 'A map of highways']},
        {'Question': 'How many continents are there?', 'answer': '7', 'options': ['6', '7', '8', '9']},
    ]
}
#Create grade 8 questions
Grade_8_questions = {
    #Create questions for math
    "Math": [ 
        {'Question': 'Solve for x: 3x - 7 = 11', 'answer': '6', 'options': ['6', '7', '8', '4']},
        {'Question': 'What is the slope of the line passing through the points (2, 3) and (4, 7)?', 'answer': '2', 'options': ['1', '2', '3','4']},
        {'Question': 'Which of the numbers is a rational number?', 'answer': '0.75', 'options': ['π', '√2', '0.75', '√3']}
    ],
    #Create questions for science
    "Science": [
        {'Question': 'Which law states that for every action, there is an equal and opposite reaction?', 'answer': 'Newton\'s third law', 'options': ['Newton\'s third law', 'Newton\'s second law', 'Newton\'s first law', 'None of the above']},
        {'Question': 'Which organelle is known as the "powerhouse" of the cell?', 'answer': 'Mitochondria', 'options': ['Golgi bodies', 'Mitochondria', 'Nucleus', 'Ribosomes']},
        {'Question': 'What is the chemical symbol for sodium?', 'answer': 'Na', 'options': ['S', 'Na', 'K', 'N']}, 
    ],
    #Create questions for english
    "English": [
        {'Question': 'What is the function of a thesis statement in an essay?', 'answer': 'To state the main argument or point', 'options': ['To state the main argument or point', ' To provide background information', 'To list all sources used', 'To summarize the conclusion']}, 
        {'Question': 'Choose the correct form of the word to complete the sentence: "She has always been _______ in her studies."', 'answer': 'diligent', 'options': ['dilate', 'diligent', 'diligency', 'diligence']},
        {'Question': 'Which word is a verb?', 'answer': 'Swim', 'options': ['Blue', 'Swim', 'Fast', 'Book']},
    ],
    #Create questions for geography
    "Geography": [
        {'Question': 'What is the capital city of Australia?', 'answer': 'Canberra', 'options': ['Sydney', 'Melbourne', 'Canberra', 'Brisbane']}, 
        {'Question': 'The Amazon River flows primarily through which country?', 'answer': 'Brazil', 'options': ['Brazil', 'Argentina', 'Peru', 'Colombia']},
        {'Question': 'Which is the largest continent by land area?', 'answer': 'Asia', 'options': ['Asia', 'Africa', 'Europe', 'North America']},
    ],
}
#Create questions for grade 9
Grade_9_questions = {
    #Create questions for math
    "Math": [
        {'Question': 'What is the answer to 5^4 x 5 ÷ 5^8?', 'answer': '1/125', 'options': ['1/5', '1/125', '1/625', '125']},
        {'Question': 'Solve for x: 3x+2=11', 'answer': '3', 'options': ['2', '3', '4', '5']},
        {'Question': 'What is the slope of the line: Y = 4x -2?', 'answer': '4', 'options': ['2', '-2', '4', '6']},
    ],
    #Create questions for chemistry
    "Chemistry": [
        {'Question': 'What part of the atom has a negative charge?', 'answer': 'Electron', 'options': ['Proton', 'Neutron', 'Electron', 'All of the above']},
        {'Question': 'What is the formula for water?', 'answer': 'H2O', 'options': ['Na', 'S', 'H2O', 'Ne']},
        {'Question': 'The number of protons in an atom can also be represented by _____', 'answer': 'Atomic number', 'options': ['Atomic mass', 'Atomic number', 'All of the abve', 'None of the above']},
    ],
    #Create questions for history
    "History": [
        {'Question': 'Who was the first Prime Minister of Canada?', 'answer': 'John A. Macdonald', 'options': ['John A. Macdonald', 'Pierre elliott trudeau', 'Brian Mulroney', 'Justin Trudeau']},
        {'Question': 'When did WW2 start?', 'answer': '1939', 'options': ['1939', '1945', '1917', '1919']}, 
        {'Question': 'When did WW1 start?', 'answer': '1914', 'options': ['1914', '1918', '1926', '1919']},
    ],
}
#Create grade 10 questions
Grade_10_questions = {
    #Create math questions
    "Math": [
        {'Question': 'What are the roots of x^2 - 9 = 0?', 'answer': '+-3', 'options': ['+-9', '+-3', '3, 9', '0']},
        {'Question': 'What is the vertex of the vertex of y = (x - 3)^2 + 2?', 'answer': '3,2', 'options': ['-3,2', '3,2', '2,3', '3, -2']},
        {'Question': 'What is the solution to 2x - 5 = 9?', 'answer': '7', 'options': ['2', '5', '6', '7']},
    ],
    #Create chemistry questions
    "Chemistry": [
        {'Question': 'What is the symbol for nitrogen?', 'answer': 'N', 'options': ['N', 'Ne', 'P', 'C']},
        {'Question': 'Which type of bonding involves the sharing of electrions', 'answer': 'Covalent', 'options': ['Covalent', 'Ionic', 'Rutherford', 'All of the above']},
        {'Question': 'Which is an example of a chemical change?', 'answer': 'Burning wood', 'options': ['Ripping paper', 'Cutting down trees', 'Burning wood', 'None of the above']},
    ],
    #Create biology questions
    "Biology": [
        {'Question': 'Which type of process is used for asexual reproduction?', 'answer': 'Mitosis', 'options': ['Meiosis', 'Mitosis', 'Binary divison', 'All of the above']},
        {'Question': 'Which of the following is an organ system?', 'answer': 'All of the above', 'options': ['Digestive system', 'Circulatory system', 'Respiratory system', 'All of the above']},
    ],
    #Create history questions
    "History": [
        {'Question': 'When did WW2 end?', 'answer': '1945', 'options': ['1939', '1945', '1940', '1919']},
        {'Question': 'When did WW1 end?', 'answer':  '1918', 'options': ['1918', '1919', '1940', '1917']},
        {'Question': 'When did the Cold War begin?', 'answer': '1947', 'options': ['1919', '1945', '1946', '1947']},
    ]
}
#Create master list containing data from all grades      
all_grades = {
    "Grade 1": Grade_1_questions, 
    "Grade 2": Grade_2_questions,
    "Grade 3": Grade_3_questions,
    "Grade 4": Grade_4_questions,
    "Grade 5": Grade_5_questions,
    "Grade 6": Grade_6_questions,
    "Grade 7": Grade_7_questions,
    "Grade 8": Grade_8_questions,
    "Grade 9": Grade_9_questions,
    "Grade 10":Grade_10_questions
}

#Initialize current grade variable to 1, representing the grade level the user will start at
current_grade = 1


#Create list for radio button questions/data
radio_buttons = []

#Define game background function - can be seen in the menu(file)
def Game_background():
    #Withdraw the welcome window and restore the game background window 
    #This ensures only one window is open 
    Welcome_window.withdraw()
    Game_backgroundwindow.deiconify()
    #Pack the background frame, history message label and background label 
    Backgroundframe.pack()
    Historymessage.pack()
    Backgroundlabel.pack()
    #Pack homebutton frame and the button itself
    Home_buttonframe.pack(anchor='se')
    Home_button.pack()
    #Pack the canvas to the left direction, using anchor 
    canvas.pack(anchor='w')

#Define the pregame function 
def pregame():
    #Withdraw the gamebackground window, while restoring the welcome window
    Game_backgroundwindow.withdraw()  
    Welcome_window.deiconify()     
#Pack the welcome, detail and intro button frame 
    Welcome_frame.pack()
    Detail_frame.pack()
    Intro_buttonframe.pack()
#Pack the welcome, detail and instructions label
    Welcome_label.pack()
    Detail_label.pack()
    Instructions_button.pack()
#Pack the startgame and quit button
    startgame_button.pack()
    quit_button.pack()
    #Configurate the welcome window, to change background color
    Welcome_window.config(bg='lavender', highlightbackground='white')
    #Configurate the welcome window to add the menubar 
    Welcome_window.config(menu=menubar)
    #Pack the other canvas 
    canvas3.pack()

#Define the show instructions function     
def show_instructions():
    #Use tkinter.messagebox to use the dialogue box to show the instructions as a dialoge box 
    tkinter.messagebox.showinfo('instructions', "1.When you click start game, you will be taken to another window, where you will need to enter your name.\n\n"
    "2.After entering your name, you will then be taken to a question window, where you will have to answer questions from different subjects. You will start at grade 1. \n\n"
    "3. If you answer the first question successfully, you will progress to grade 2, where you will have to answer another randomized question.\n\n"
    "4. If you continue to answer the questions successfully, this process repeats until you pass grade 10, where you will then, be deemed to be smarter than a 10th grader.\n\n"
    "5. If you answer the question unsuccessfully, you must restart the quiz. \n\n"
    "6. Best of luck!")

#Define the startgame function
def startgame(): 
    #Withdraw the welcome window to ensure that only the name window shows 
    Welcome_window.withdraw()
    #Use .decionify to restore the name window, which was initally hidden 
    name_window.deiconify()
    #Call the ask name function to get the users name 
    ask_name()

#Define the ask name function 
def ask_name():
    #Pack the name frame, namelabel1 and the name entry 
    nameframe1.pack()
    namelabel1.pack()
    name_entry.pack()
    name_entry.focus_set()
    #Bind the name entry function to the enter key, while calling the process name function 
    name_entry.bind('<Return>', process_name)

#Define process name function
def process_name(event):
    #Use player name variable to store users name 
    player_name = name_entry.get()
    #Withdraw the name window function and restore the name window 2 function, to ensure only one window is showing 
    name_window.withdraw()
    name_window2.deiconify()
    #Pack the nameframe2 and namelabel2
    nameframe2.pack()
    namelabel2.pack()
    #Configurate namelabel2 to have a different text, which address the players name with a hello message
    namelabel2.config(text='Hello ' + player_name + '\n\n Welcome to the game!')
    #Delay the quiz start function for 1 second using .after function
    name_window2.after(1000, Quiz_start)

#Define quiz start function 
def Quiz_start():
    #Globalize current answer 
    global current_answer 
    #Withdraw name window2 window and restore question window, to ensure only one window is showing 
    name_window2.withdraw()
    Question_window.deiconify()
    #Pack the question frame, button frame and label
    Question_frame.pack()
    Question_Buttonsframe.pack()    
    Question_label.pack()
    #Concatenating the grade level with the actual grade itself
    grade_key = "Grade " + str(current_grade)
    #Use .keys() to help retrieve data from the dictionaries above
    subjects = list(all_grades[grade_key].keys())
    #Use random.choice to randomize the subjects 
    subject = random.choice(subjects) 
    #Use random.choice to randomize the questions
    current_question = random.choice(all_grades[grade_key][subject])
    #Retrieve answer data from dictionaries
    current_answer = current_question['answer']
    #Configurate/change the question label into showing the question
    Question_label.config(text="Grade " + str(current_grade) + " - " + subject + "\n\n" + current_question['Question'])
    #Set the answer variable to nothing
    answer_var.set(None)
    #Clear potential previous radio buttons/multiple choice options
    for rb in radio_buttons:
        rb.destroy()
    radio_buttons.clear()
    for option in current_question['options']:
        rb = tkinter.Radiobutton(Question_Buttonsframe, text=option, variable=answer_var, value=option, font=("Arial", 14))
        #Pack the radiobuttons 
        rb.pack(anchor='w', padx=20, pady=5)
        #Used to modify the list 
        radio_buttons.append(rb)
        #Pack the next button frame and button itself
    next_buttonframe.pack(side='right')
    next_button.pack()
    #Pack the quit button and it's frame
    Quit_buttonframe.pack(side='right')
    quit_button2.pack()

#Define submit answer function
def submit_answer():
    global current_grade
    selected = answer_var.get()
    #If the user's selected option is correct, a message box will be displayed telling them that they are correct
    if selected == current_answer: 
        tkinter.messagebox.showinfo('Correct', 'Correct, Great job!')
        #Increase grade by 1 to move onto the next grade
        current_grade+=1
        #If the grade is greater than 10, call the endgame function
        if current_grade > 10:
            endgame()
          
        else: 
            #If not return to the quiz start function
            Quiz_start()
            
    else: 
        #If the answer is wrong a message box will be displayed telling the user that
        tkinter.messagebox.showerror("Incorrect", "Oops that's the wrong answer!")
        #The restart game function will then be called
        restart_game()

#Define restart game function, used to restart the game
def restart_game():
    global current_grade
    current_grade = 1
    answer_var.set(None)
    tkinter.messagebox.showinfo("Restarting", "Let's try again from Grade 1!")
    Quiz_start()

#Define endgame function, called when the user completes the game
def endgame():
    User_response = tkinter.messagebox.askquestion("Congratulations!", "You've completed all grades!\n\nDo you want to rate our game?")

    #If the user respondes yes, the question window will be withdrawn and the ratings function will be called
    if User_response == 'yes':
        Question_window.withdraw()
        ratings()
    else:
        tkinter.messagebox('Final message', 'Thank you for playing!')
    
    
#Define ratings function
def ratings():
    rating_window.deiconify()
    rating_window.config(bg='white', highlightbackground='white')
    #Pack the ratings frame, label and canvas 
    rating_frame.pack()
    rating_label.pack()
    canvas2.pack()
    Rating_buttonframe.pack(anchor='se')
    Rating_buttonframe2.pack(anchor='center')
    Rating_button.pack()
    
    #Set the variable to 0 
    rating_var.set(0)

    #Create the radio buttons to represent the user ratings
    rb1 = tkinter.Radiobutton( Rating_buttonframe2, text='★', variable=rating_var, value=1, font=('Arial', 12), fg='gold')
    rb1.pack(side='left', padx=5)
    rb2 = tkinter.Radiobutton( Rating_buttonframe2, text='★★', variable=rating_var, value=2, font=('Arial', 12), fg='gold')
    rb2.pack(side='left',padx=5)
    rb3 = tkinter.Radiobutton( Rating_buttonframe2, text='★★★', variable=rating_var, value=3, font=('Arial', 12), fg='gold')
    rb3.pack(side='left',padx=5)
    rb4 = tkinter.Radiobutton( Rating_buttonframe2, text='★★★★', variable=rating_var, value=4, font=('Arial', 12), fg='gold')
    rb4.pack(side='left',padx=5)
    rb5 = tkinter.Radiobutton( Rating_buttonframe2, text='★★★★★', variable=rating_var, value=5, font=('Arial', 12), fg='gold')
    rb5.pack(side='left',padx=5)

#Define thank rate function
#The program will delivery a message saying thank you for rating the game
def thank_rate():
    tkinter.messagebox.showinfo('Rating', 'Thank you for rating, this application will shortly close')
    #Delay the application ending for 1 second
    rating_window.after(1000, Welcome_window.destroy)


#--------------------------------------------------------GUI DRIVER-----------------------------------------------------#
#The gui driver will involve the creation of windows, frames, buttons and labels 

#Create the welcome window, which will act as the main window of this application 
Welcome_window = tkinter.Tk()
Welcome_window.title("Welcome to the game")
Welcome_window.geometry("900x600")

#Create the answer and rating variable 
answer_var = tkinter.StringVar()
rating_var = tkinter.IntVar()

#Create teh game background window
#This will be a toplevel window
#This will remain withdrawn until called upon
Game_backgroundwindow = tkinter.Toplevel()
Game_backgroundwindow.title('The thought behind the game')
Game_backgroundwindow.geometry('900x600')
Game_backgroundwindow.withdraw()

#Create the name window, which will be a toplevel window and will ask the user to enter their name
name_window = tkinter.Toplevel()
name_window.title("Please enter your name")
name_window.geometry('900x600')
#Keep this window initally hidden 
name_window.withdraw()

#Create the second name window, which will also be a toplevel window and will address the user 
name_window2 = tkinter.Toplevel()
name_window2.title("Hello")
name_window2.geometry('500x500')
#Similarly, this window will also be initally hidden 
name_window2.withdraw()

#Create the question window, which will be a toplevel window, showing the user the questions 
Question_window = tkinter.Toplevel()
Question_window.title("Questions")
Question_window.geometry('900x600')
#This window will be initally hidden 
Question_window.withdraw()

#Create a rating window, which will be a toplevel window, providing the user the opportunity to place their ratings
rating_window = tkinter.Toplevel()
rating_window.title('Rate our game')
rating_window.geometry('900x600')
#Keep this initally withdrawn
rating_window.withdraw()

#Create the welcome, detail and introbutton frame which will correspond to the first/main window(Welcome window)
Backgroundframe = tkinter.Frame(Game_backgroundwindow)
Home_buttonframe = tkinter.Frame(Game_backgroundwindow)
Welcome_frame = tkinter.Frame(Welcome_window)
Detail_frame = tkinter.Frame(Welcome_window)
Intro_buttonframe = tkinter.Frame(Welcome_window)

#Create the first and second name frames, as well as the question frame
nameframe1 = tkinter.Frame(name_window)
nameframe2 = tkinter.Frame(name_window2)
Question_frame = tkinter.Frame(Question_window)
Question_Buttonsframe = tkinter.Frame(Question_window)
Quit_buttonframe = tkinter.Frame(Question_window)

#Create button frames for the next and quit button
next_buttonframe = tkinter.Frame(Question_window)
rating_frame = tkinter.Frame(rating_window)
Rating_buttonframe = tkinter.Frame(rating_window)
Rating_buttonframe2 = tkinter.Frame(rating_window)

#Create the instructions, startgame and quit button
#When clicked the instructions button will show the instructions
Home_button = tkinter.Button(Home_buttonframe, text='Home', command=pregame)
Instructions_button = tkinter.Button(Intro_buttonframe, text="Instructions", command=show_instructions)
#When clicked, the startgame button will call and execute the startgame functions 
startgame_button = tkinter.Button(Intro_buttonframe, text='Start', command=startgame)
#When clicked, the quit button will simply exit the progame/application
quit_button = tkinter.Button(Intro_buttonframe, text='Quit', command=Welcome_window.destroy)
quit_button2 = tkinter.Button(Quit_buttonframe, text='Quit', command=Welcome_window.destroy)
next_button = tkinter.Button(next_buttonframe, text='Next', command=submit_answer)
Rating_button= tkinter.Button(Rating_buttonframe, text='Submit', command=thank_rate)


#Create all the labels - welcome, detail, namelabel1, namelabel2 and question label
Historymessage = tkinter.Label(Backgroundframe, text= 'This application was established on May 15th, 2025 and is still in the beta phase of development.\n'
'As an early access user, you can provide key feedback to help better our game.\n')
Backgroundlabel = tkinter.Label(Backgroundframe, text = 'This game is based off the popular game show, Are You Smarter Than A 6th Grader.\n'
'In this game, you will be tested on various different subjects to determine if you truely are smarter than a 6th grader.\n'
'As the player, this game will help you understand the true extent of our knowledge and the impact education has had on it.\n'
'Good luck!')
Welcome_label = tkinter.Label(Welcome_frame, text='Welcome to the Are You Smarter Than A 10th Grader Quiz!', font=('Arial', 15))
Detail_label = tkinter.Label(Detail_frame, text='To view instructions click instructions.\n' 
'If you just want to start the game without viewing the instructions, click the start game.\n'
'To close the application click quit.', font=('Arial', 12))
namelabel1 = tkinter.Label(nameframe1, text='Please enter your name below and click enter to continue', font=('Arial', 20))
namelabel2 = tkinter.Label(nameframe2, text='', font=('Arial', 20))
Question_label = tkinter.Label(Question_frame, text='', font=('Arial', 20))
rating_label = tkinter.Label(rating_frame, text='Rate our game!', font=('Arial', 20))

#Create the name entry, which will be key for acquiring the users name 
name_entry = tkinter.Entry(nameframe1)

#Create the menubar 
menubar = tkinter.Menu(Welcome_window)

#Add the a background, exit and rate option in the menubar
file_menu = tkinter.Menu(menubar)
file_menu.add_command(label='Background', command=Game_background)
file_menu.add_command(label='Exit', command=Welcome_window.destroy)
file_menu.add_command(label='Rate', command=ratings)
menubar.add_cascade(label = 'File', menu=file_menu)

#Create the canvas for 3 different images

canvas = tkinter.Canvas(Game_backgroundwindow, width=500, height=500)
Gameshow_host= tkinter.PhotoImage(file='Gameshowhost.PNG')
canvas.create_image(0,450, anchor='sw', image=Gameshow_host)

canvas2 = tkinter.Canvas(rating_window, width=500, height=300)
Five_stars_rating = tkinter.PhotoImage(file='5_stars.svg.png')
Five_stars_rating = Five_stars_rating.subsample(7)
canvas2.create_image(250,200, anchor = 'center', image=Five_stars_rating)

canvas3 = tkinter.Canvas(Welcome_window, width=500, height=300)
Gameshow = tkinter.PhotoImage(file='gameimage2.png')
canvas3.create_image(-20,150, anchor='w', image=Gameshow)

#Call the pregame/first function
pregame()

#Loop the welcome/main window
Welcome_window.mainloop()
