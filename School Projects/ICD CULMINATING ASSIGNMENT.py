#Aryan Juneja e-Reflection Platform on unit2B for ICD2O1 - P3 Digital Technology - Sunday June 8th, 2025
#This program is created as an e-Reflection platform to educate users on crtical concepts learned in Unit 2B of the ICD curriculum 

#Import libraries 
import tkinter
import tkinter.messagebox

#Create easy level questiom
Easy = {
    "Loops": [
         {'Question': 'Which is the correct syntax for a while loop?', 'answer': 'while i<=5:', 'options': ['while i<=5:', 'while (i <= 5) then:', 'while i <= 5 do:', 'loop while i <= 5:']},
    ], 

    "Modules": [
        {'Question': 'Which is the correct way of importing the math module?', 'answer': 'import math', 'options': ['import math.py', 'import math', 'import maths', 'add math.py']},
    ],

    "Value returning functions": [
        {'Question': 'Which is the correct way to return an expression?', 'answer': 'return expression', 'options': ['return(expression.py)', 'return expression.py', 'return expression', 'recall expression']},
    ],
}

#Create medium level difficulty questions
Medium = {
    "Loops": [
        {'Question': "How many times will this loop run: for i in range(5): \n print('hello')", 'answer': '5', 'options': ['6', '5', '3', '4']},
    ],

    "Sentinel values": [
        {'Question': 'Which is the correct syntax for not equal to', 'answer': '!=', 'options': ['!', '==', '!==', '!=']},
    ],

    "Running total": [
        {'Question': 'Which is the correct syntax to execute the following code: x = x+5', 'answer': 'x+=5', 'options': ['x+5', 'x*5', 'x++5', 'x+=5']},
    ],
}

#Create hard level questions
Hard = {
    "Loops": [
        {'Question': 'What is the output of following code:\n\nfor num in [1, 2, 3, 4, 5]\n print (num)\n main()', 'answer': '1, 2, 3, 4, 5', 'options': ['1, 2, 3, 4', '0, 1, 2, 3, 4', '0, 1, 2, 3, 4, 5', '1, 2, 3, 4, 5']},
    ],
    
    "Random numbers": [
        {'Question': 'One reason that lotteries don’t use computers to generate random numbers is:', 'answer': "Computers don't really generate random numbers, they generate pseudo-random numbers", 'options': ['There is no computer on the stage for the drawing', "Computers don't really generate random numbers, they generate pseudo-random numbers", 'They would just generate the same numbers over and over again', 'All of the above']},
    ],

    "Running total": [
        {'Question': 'Use augmented assignment operators that assign the remainder of x/4 to x', 'answer': 'x%=4', 'options': ['x/=4','x%4', 'x*=4', 'x%=4']},
    ],
}
     
#Create all level dictionary to store all the question data
all_levels = {
    'Easy': Easy,
    'Medium': Medium,
    'Hard': Hard
}

#Initialize score
score = 0
#Set the total number of questions
total_questions = 3
#Question data starts as none until the quiz is started
current_question_data = None
#Keeps track of which question user is on - start at 0 
current_question_index = 0
#A list that will hold all questions for a specific topic/level
questions_list = []

#Create intro window
Intro_window = tkinter.Tk()
Intro_window.title('Welcome to my eReflection platform!')
Intro_window.geometry('800x500')

#Create question window as a toplevel
Question_window = tkinter.Toplevel()
Question_window.geometry('600x400')
#Initally withdrawn
Question_window.withdraw()

#Create question label 
Question_label = tkinter.Label(Question_window, text="", font=("Arial", 14))
Question_label.pack(pady=20)

#Container to hold multiple choice options
options_frame = tkinter.Frame(Question_window)
options_frame.pack(pady=10)

#Define quiz start function
def Quiz_start():
    #Globalize these variables to later access and update them
    global level, current_question_index, questions_list, current_question_data
    #Withdraw the intro window to ensure only one window is shown
    Intro_window.withdraw()
    #Restore question window
    Question_window.deiconify()
    #Pulls the set of questions for the selected difficulty level
    level_questions = all_levels[level]
    questions_list = []
    #
    for topic_name, questions in level_questions.items():
        #Loop through each question in the current topic's list of questions
        for q in questions: 
            #Stores topic name inside each question - shows question and the coressponding topic
            q['topic'] = topic_name
            questions_list.append(q)
    
    #Sets the first question to display 
    current_question_data = questions_list[current_question_index]
    
    # Update question label 
    text_to_show = "Level: " + level + "\nTopic: " + current_question_data['topic'] + "\n\n" + current_question_data['Question']
    #Configurate the question label to show the updates 
    Question_label.config(text=text_to_show)
    display_question(current_question_data, level, current_question_data['topic'])

#Define next question function
def next_question():
    #Gloablize these variables to later access them
    global current_question_data, current_question_index, questions_list, score
    #Create selected answer variable
    selected = selected_option.get()
    #Create correct answer variable
    correct_answer = current_question_data['answer']

    #If the selected answer is equal to the correct answer display a message saying the answer was correct
    if selected == correct_answer:
        tkinter.messagebox.showinfo('Correct', 'Correct!')
        #Update the score by 1
        score+=1
    
    #If selected answer is not equal to correct answer, display a message telling user their answer was incorrect
    else:
        tkinter.messagebox.showinfo('Incorrect', 'Oh no, you are incorrect!')
    
    #Increase the overall question index by 1
    current_question_index+=1

    #Checks if current question that user is on is less than total number of questions
    if current_question_index < len(questions_list):

        #Retrives question data from dictionary based on the question you are on 
        current_question_data = questions_list[current_question_index]
        #Displays question information
        display_question(current_question_data, level, current_question_data['topic'])
    

    else:
        #If the user completes the quiz, they will be informed by a message box
        tkinter.messagebox.showinfo("End of Quiz", "You have completed all questions for this topic")
        percentage = (score/total_questions) * 100
        
        #The message box will show user's score as a percentage
        tkinter.messagebox.showinfo("Quiz result", "You scored " + format(percentage, '.2f') +'%')
        Question_window.withdraw()
        Intro_window.deiconify()

#Create selected option - useful for tracking what the user selects    
selected_option = tkinter.StringVar()

#Option buttons stores radio buttons for updates 
option_buttons = []

#Loop 4 times to create 4 radio buttons
for i in range(4):
   
   #Create a label text for each option
   option_text = "Option " + str(i+1) 

   #Create the radio button
   rb = tkinter.Radiobutton(
      options_frame,
      text=option_text,
        variable=selected_option,
        value="",
        font=("Arial", 12),
        anchor='w',
        justify='left',
        wraplength=600,
        state='normal'
   )
   rb.pack(anchor='center', pady=5, fill='x')
   option_buttons.append(rb)

#Create the next button
next_button = tkinter.Button(
    Question_window,
    text="Next",
    font=("Arial", 12),
    bg='blue',
    fg='white',
    command=next_question
)
next_button.pack(pady=20)

#Define about program
def About_program():
    Intro_window.withdraw()
    About_window.deiconify()
    #Pack the all the frames
    Welcome_frame.pack()
    Message_frame.pack() 
    #Pack all the labels 
    Welcome_label.pack()
    Message_label.pack()
    Home_buttonframe.pack(anchor='se')
    Home_button.pack(anchor='se')
    #Pack the canvas 
    canvas2.pack(anchor='sw', pady=10)

#Define welcome game
def welcome_game():

    #Withdraw the opinion window, modules window, about window and content window
    #This is to ensure that when the user clicks back multiple windows aren't showing
    FAQ_window.withdraw()
    Opinion_window.withdraw()
    Modules_value_returning_functions_window.withdraw()
    About_window.withdraw()
    Content_window1.withdraw()

    #Restore/show the intro window 
    Intro_window.deiconify()
    Intro_frame.pack()
    Intro_label.pack(pady=10)
    Intro_buttonframe.pack()
    Instructions_button.grid(row=1, column=2)
    Content_button.grid(row=1, column=1)
    Quiz_button.grid(row=2, column=1)
    Quit_button.grid(row=2, column=2)
    
    #Configure the intro window to add a menu bar and background
    Intro_window.config(menu=menubar)
    Intro_window.config(bg='lavender')


def show_instructions():
    #Use message box to show instructions
    tkinter.messagebox.showinfo('Instructions','Welcome to my eReflection platform!\n\n 1.Use the unit content button to explore educational ' \
    'material\n\n 2.Once your done learning about the unit material, return to the home screen and take the quiz\n\n 3.Provide feedback or a rating' \
    'once your done with the quiz\n\n 4.You can exit the program')

#Define ask name function 
def ask_name():
    Intro_window.withdraw()
    name_window1.deiconify()
    nameframe1.pack()
    namelabel1.pack()
    
    #Pack the entry box
    name_entry.pack()
    #Use .focus set to activate it 
    name_entry.focus_set()
    #Bind the name entry box - when enter is clicked process name function is called
    name_entry.bind('<Return>', process_name)

#Define process name function 
def process_name(event):
    #Use player name variable to store name entry information
    player_name = name_entry.get()
    name_window1.withdraw()
    name_window2.deiconify()
    nameframe2.pack()
    namelabel2.pack()
    
    #Configure the name label 2, so that a hello message is displayed
    namelabel2.config(text='Hello ' + player_name + '\n\n Welcome to my e-Reflection platform!')
    #Delay the calling of the show content function for 1 second 
    name_window2.after(1000, show_content)

def show_content():
    name_window2.withdraw()
    #Call the first slide
    intro_slide()

#Define intro slide 
def intro_slide():
    Loops_window.withdraw()
    Content_window1.deiconify()
    
    #Pack all the frames and labels 
    Content_window1_titleframe.pack()
    Content_window1_titlelabel.pack()
    Content_window1_topicsframe.pack(anchor='nw', padx=10, pady=10)
    Content_window1_labelloops.pack(anchor='nw', padx=10, pady=10)
    Content_window1_labelrunningtotal.pack(anchor='nw', padx=10, pady=10)
    Content_window1_labelsentinel_inputvalidation.pack(anchor='nw', padx=10, pady=10)
    Content_window1_labelmoduels_generatingrandomnumbers.pack(anchor='nw', padx=10, pady=10)
    Content_window1_labelvalue_returning_functions.pack(anchor='nw', padx=10, pady=10)
    Content_window1_buttonframe.pack(anchor='se')
    Next_button1.grid(row=0, column=1)
    Back_button1.grid(row=0, column=0)
    canvas.pack(anchor='sw', pady=10)
    #Configure the content window to change background color
    Content_window1.config(bg='lavender')

#Define loops slide 
def loops_slide():
    Content_window1.withdraw()
    Runningtotal_window.withdraw()
    Loops_window.deiconify()
    
    #Pack all the frames, buttons and labels
    Loops_window_titleframe.pack()
    Loops_window_titlelabel.pack()
    Loops_window_topicframe.pack(anchor='nw', padx=10, pady=10)
    Loops_window_topiclabel.pack(anchor='nw', padx=10, pady=10)
    Loops_window_nestedloopframe.pack(anchor='nw', padx=5, pady=5)
    Loops_window_nestedlooplabel.pack(anchor='nw', padx=5, pady=5)
    Loops_window_whileloopframe.pack(anchor='nw', padx=5, pady=5)
    Loops_window_whilelooplabel.pack(anchor='nw', padx=5, pady=5)
    Loops_window_forloopfame.pack(anchor='nw', padx=5, pady=5)
    Loops_window_forlooplabel.pack(anchor='nw', padx=5, pady=5) 
    Loops_window_buttonframe.pack(anchor='se')
    Next_button2.grid(row=0, column=1)
    Back_button2.grid(row=0, column=0)
    Loops_window.config(bg='lavender')

#Define running total slide
def runningtotal():
    sentinel_value_inputvalidation_window.withdraw()
    Loops_window.withdraw()
    Runningtotal_window.deiconify()

    #Pack all the frames, labels and buttons
    Runningtotal_titleframe.pack()
    Runningtotal_detailframe.pack(anchor='nw', padx=10, pady=10)
    Runningtotal_titlelabel.pack(anchor='nw', padx=10, pady=10)
    Runningtotal_detaillabel.pack(anchor='nw', padx=10, pady=10)
    Runningtotal_syntaxlabel.pack(anchor='nw', padx=10, pady=10)
    Runningtotal_buttonframe.pack(anchor='se')
    Next_button3.grid(row=0, column=1)
    Back_button3.grid(row=0, column=0)
    Runningtotal_window.config(bg='lavender')

#Define sentinel value and input validation slide
def sentinel_value_inputvalidation():
    Runningtotal_window.withdraw()
    gen_randomnumbers_window.withdraw()
    sentinel_value_inputvalidation_window.deiconify()

    #Pack all the frames, labels and buttons
    sentinel_value_inputvalidation_titleframe.pack()
    sentinel_value_inputvalidation_titlelabel.pack(anchor='nw', padx=10, pady=10)
    sentinel_valueframe.pack(anchor='nw', padx=10, pady=10)
    sentinel_valuelabel.pack(anchor='nw', padx=10, pady=10)
    input_validationframe.pack(anchor='nw', padx=10, pady=10)
    input_validationlabel.pack(anchor='nw', padx=10, pady=10)
    sentinel_value_inputvalidation_buttonframe.pack(anchor='se')
    Next_button4.grid(row=0, column=1)
    Back_button4.grid(row=0, column=0)
    sentinel_value_inputvalidation_window.config(bg='lavender')

#Define random number slides
def gen_randomnumbers():
    sentinel_value_inputvalidation_window.withdraw()
    Modules_value_returning_functions_window.withdraw()
    gen_randomnumbers_window.deiconify()
    
    #Pack all the frames, labels and buttons
    gen_randomnumbers_titleframe.pack()
    gen_randomnumbers_titlelabel.pack(anchor='nw', padx=10, pady=10)
    gen_randomnumbers_detailframe.pack(anchor='nw', padx=10, pady=10)
    gen_randomnumbers_detaillabel.pack(anchor='nw', padx=10, pady=10)
    gen_randomnumbers_applicationlabel.pack(anchor='nw', padx=10, pady=10)
    gen_randomnumbers_buttonframe.pack(anchor='se')
    Next_button5.grid(row=0, column=1)
    Back_button5.grid(row=0, column=0)
    gen_randomnumbers_window.config(bg='lavender')

#Define modules and value returning functions slide
def Modules_value_returning_functions():
    gen_randomnumbers_window.withdraw()
    Modules_value_returning_functions_window.deiconify()
    
    #Pack all the frames, labels and buttons
    Modules_value_returning_functions_titleframe.pack()
    Modules_value_returning_functions_titlelabel.pack(anchor='nw', padx=10, pady=10)
    Modules_detailframe.pack(anchor='nw', padx=10, pady=10)
    Modules_detaillabel.pack(anchor='nw', padx=10, pady=10)
    Value_returning_functions_detailframe.pack(anchor='nw', padx=10, pady=10)
    Value_returning_functions_detaillabel.pack(anchor='nw', padx=10, pady=10)

    #Pack a home button to return back to home screen
    Home_buttonframe2.pack(anchor='se')
    Home_button2.pack(anchor='se')
    Modules_value_returning_functions_window.config(bg='lavender')

def choose_level():
    Intro_window.withdraw()
    Level_window.deiconify()

    #Pack the level select widget to display level selection options
    level_select.pack()

    #Retrive list of available levels from all levels dictionary keys
    levels = list(all_levels.keys())

    #Define a start easy function with the easy level when the easy button is clicked 
    def start_easy():
        start_quiz_with_level("Easy")
    
    #Define a start medium function with the medium level when the medium button is clicked 
    def start_medium():
        start_quiz_with_level("Medium")
    
    #Define a start hard function with the hard level when the hard button is clicked 
    def start_hard():
        start_quiz_with_level("Hard")
    
    #Create the buttons for the easy, medium and hard level
    btn_easy = tkinter.Button(Level_window, text="Easy", font=("Arial", 12), width=20, height=2, command=start_easy)
    btn_medium = tkinter.Button(Level_window, text="Medium", font=("Arial", 12), width=20, height=2, command=start_medium)
    btn_hard = tkinter.Button(Level_window, text="Hard", font=("Arial", 12), width=20, height=2, command=start_hard)

    #Pack the buttons 
    btn_easy.pack(pady=5)
    btn_medium.pack(pady=5)
    btn_hard.pack(pady=5)


def start_quiz_with_level(chosen_level):
    #Globalize level to access it again
    global level
    #Assign the selected level to global variable
    level = chosen_level

    #Destroy the level window 
    Level_window.destroy()

    #Call quiz start function
    Quiz_start()

def display_question(question_data, level, topic):
    # Create the question text by joining pieces
    question_text = "Level: " + level + "\n" + "Topic: " + topic + "\n\n" + question_data['Question']
    
    # Set the question label to show the question text
    Question_label.config(text=question_text)
    
    # Clear any previously selected answer with an empty string
    selected_option.set("")
    
    # Update the text of each radio button with the options
    for i in range(4):
        option_buttons[i].config(
            text=question_data['options'][i],
            value=question_data['options'][i]
        )

#Define FAQ function  
def FAQ_question():
    Intro_window.withdraw()
    FAQ_window.deiconify()
    FAQ_introlabel.pack()

    #Pack the question labels
    Q1_label.pack(padx=10, pady=10)
    Q2_label.pack(padx=10, pady=10)
    Q3_label.pack(padx=10, pady=10)

    #When enter is clicked, the FAQ answer function is called
    FAQ_window.bind('<Return>', FAQ_answer)

    Home_buttonframe3.pack(anchor='se')
    Home_button3.pack(anchor='se')
   
def FAQ_answer(event):
    #When enter is clicked the answers are shown 
    A1_label.pack(padx=10, pady=10)
    A2_label.pack(padx=10, pady=10)
    A3_label.pack(padx=10, pady=10)

def ratings():
    Intro_window.withdraw()
    Ratings_window.deiconify()
    Ratings_window.config(bg='white', highlightbackground='white')
    #Pack the ratings frame, label and canvas 
    Rating_frame.pack()
    Rating_label.pack()
    canvas3.pack()
    Rating_buttonframe.pack(anchor='se')
    Rating_buttonframe2.pack(anchor='center')
    Rating_button.pack()
    
    #Set the variable to 0 
    Rating_var.set(0)

    #Create the radio buttons to represent the user ratings
    rb1 = tkinter.Radiobutton( Rating_buttonframe2, text='★', variable=Rating_var, value=1, font=('Arial', 12), fg='gold')
    rb1.pack(side='left', padx=5)
    rb2 = tkinter.Radiobutton( Rating_buttonframe2, text='★★', variable=Rating_var, value=2, font=('Arial', 12), fg='gold')
    rb2.pack(side='left',padx=5)
    rb3 = tkinter.Radiobutton( Rating_buttonframe2, text='★★★', variable=Rating_var, value=3, font=('Arial', 12), fg='gold')
    rb3.pack(side='left',padx=5)
    rb4 = tkinter.Radiobutton( Rating_buttonframe2, text='★★★★', variable=Rating_var, value=4, font=('Arial', 12), fg='gold')
    rb4.pack(side='left',padx=5)
    rb5 = tkinter.Radiobutton( Rating_buttonframe2, text='★★★★★', variable=Rating_var, value=5, font=('Arial', 12), fg='gold')
    rb5.pack(side='left',padx=5)

def thank_rate():
    tkinter.messagebox.showinfo('Rating', 'Thank you for rating, this application will shortly close')
    #Delay the application ending for 1 second
    Ratings_window.after(1000, Intro_window.destroy)

def opinion():
    Intro_window.withdraw()
    Opinion_window.deiconify()
    
    #Pack all the labels and frames
    Opinion_titleframe.pack()
    Opinion_titlelabel.pack()

    #Pack the entry box
    entry_box.pack()

    #Use .focus set so that the entry box is activated
    entry_box.focus_set()
    opinion_buttonframe.pack(anchor='se')
    opinion_submitbutton.pack(anchor='se')

#Define submit button response 
def submit_button_response():
    opinion = entry_box.get()

    #When the user submits their response they will be asked a question
    User_response = tkinter.messagebox.askquestion("Congratulations!", "Thank you for your opinion, would you like to provide another one?")

    #If the user respondes yes, the user can provide another opinion
    if User_response == 'yes':
        opinion()
    else:
    #If the user respondes with no, welcome game function will be called 
        welcome_game()
    
#---------------------------------------------------------GUI DRIVER-------------------------------------------------------------------#
#Create rating var 
Rating_var = tkinter.IntVar()

#Create about window
About_window = tkinter.Toplevel()
About_window.title('About')
About_window.geometry('900x620')
#Ensure window is withdrawn
About_window.withdraw()

#Create FAQ window
FAQ_window = tkinter.Toplevel()
FAQ_window.title('FAQS')
FAQ_window.geometry('900x620')
#Ensure window is withdrawn 
FAQ_window.withdraw()

#Create content window
Content_window1 = tkinter.Toplevel()
Content_window1.title('Unit content')
Content_window1.geometry('1000x625')
Content_window1.withdraw()

#Create loops window
Loops_window = tkinter.Toplevel()
Loops_window.title('All about loops!')
Loops_window.geometry('1000x625')
Loops_window.withdraw()

#Create runningtotal window
Runningtotal_window = tkinter.Toplevel()
Runningtotal_window.title('Running totals!')
Runningtotal_window.geometry('1000x625')
Runningtotal_window.withdraw()

#Create sentinel value and input validation window
sentinel_value_inputvalidation_window = tkinter.Toplevel()
sentinel_value_inputvalidation_window.title('Sentinel values and input validation')
sentinel_value_inputvalidation_window.geometry('1000x625')
sentinel_value_inputvalidation_window.withdraw()

#Create random number window
gen_randomnumbers_window = tkinter.Toplevel()
gen_randomnumbers_window.title('Generating random numbers')
gen_randomnumbers_window.geometry('1000x625')
gen_randomnumbers_window.withdraw()

#Create modules and value returning functions window
Modules_value_returning_functions_window = tkinter.Toplevel()
Modules_value_returning_functions_window.title('Modules and Value returning functions')
Modules_value_returning_functions_window.geometry('1000x625')
Modules_value_returning_functions_window.withdraw()

#Create level window
Level_window = tkinter.Toplevel()
Level_window.title('Level selection')
Level_window.geometry('1000x625')
Level_window.withdraw()

#Create name window1
name_window1 = tkinter.Toplevel()
name_window1.title("Please enter your name")
name_window1.geometry('500x450')
name_window1.withdraw()

#Create name window2
name_window2 = tkinter.Toplevel()
name_window2.title('Hello')
name_window2.geometry('500x500')
name_window2.withdraw()

#Create ratings window
Ratings_window = tkinter.Toplevel()
Ratings_window.title('Ratings')
Ratings_window.geometry('800x500')
Ratings_window.withdraw()

#Create opinion window
Opinion_window = tkinter.Toplevel()
Opinion_window.title('Opinion')
Opinion_window.geometry('800x500')
Opinion_window.withdraw()

#Create frames
Welcome_frame = tkinter.Frame(About_window)
Message_frame = tkinter.Frame(About_window)
Home_buttonframe = tkinter.Frame(About_window)

Intro_frame = tkinter.Frame(Intro_window)
Intro_buttonframe = tkinter.Frame(Intro_window)

Content_window1_buttonframe = tkinter.Frame(Content_window1)
Content_window1_titleframe = tkinter.Frame(Content_window1)
Content_window1_topicsframe = tkinter.Frame(Content_window1)

nameframe1 = tkinter.Frame(name_window1)
nameframe2 = tkinter.Frame(name_window2)

Whileloops_frame = tkinter.Frame(Loops_window)
Loops_window_titleframe = tkinter.Frame(Loops_window)
Loops_window_topicframe = tkinter.Frame(Loops_window)
Loops_window_nestedloopframe = tkinter.Frame(Loops_window)
Loops_window_whileloopframe = tkinter.Frame(Loops_window)
Loops_window_forloopfame = tkinter.Frame(Loops_window)
Loops_window_buttonframe = tkinter.Frame(Loops_window)

Runningtotal_titleframe = tkinter.Frame(Runningtotal_window)
Runningtotal_detailframe = tkinter.Frame(Runningtotal_window)
Runningtotal_buttonframe = tkinter.Frame(Runningtotal_window)

sentinel_value_inputvalidation_titleframe = tkinter.Frame(sentinel_value_inputvalidation_window)
sentinel_valueframe = tkinter.Frame(sentinel_value_inputvalidation_window)
input_validationframe = tkinter.Frame(sentinel_value_inputvalidation_window)
sentinel_value_inputvalidation_buttonframe = tkinter.Frame(sentinel_value_inputvalidation_window)

gen_randomnumbers_titleframe = tkinter.Frame(gen_randomnumbers_window)
gen_randomnumbers_detailframe = tkinter.Frame(gen_randomnumbers_window)
gen_randomnumbers_buttonframe = tkinter.Frame(gen_randomnumbers_window)

Modules_value_returning_functions_titleframe = tkinter.Frame(Modules_value_returning_functions_window)
Modules_detailframe = tkinter.Frame(Modules_value_returning_functions_window)
Value_returning_functions_detailframe = tkinter.Frame(Modules_value_returning_functions_window)
Home_buttonframe2 = tkinter.Frame(Modules_value_returning_functions_window)

Home_buttonframe3 = tkinter.Frame(FAQ_window)

Rating_frame = tkinter.Frame(Ratings_window)
Rating_buttonframe = tkinter.Frame(Ratings_window)
Rating_buttonframe2 = tkinter.Frame(Ratings_window)
Opinion_titleframe = tkinter.Frame(Opinion_window)
opinion_buttonframe = tkinter.Frame(Opinion_window)

#Create all the labels
Intro_label = tkinter.Label(Intro_frame, text='Aryan Juneja e-Reflection platform - ICD Unit 2B', font=('arial', 20, 'bold'))
namelabel1 = tkinter.Label(nameframe1, text='Please enter your name below and click enter to proceed')
namelabel2 = tkinter.Label(nameframe2, text='', font=('arial', 20))
Content_window1_titlelabel = tkinter.Label(Content_window1_titleframe, text='Overview', font=('arial', 30, 'bold'))
Runningtotal_titlelabel = tkinter.Label(Runningtotal_titleframe, text='Running totals', font=('arial', 20, 'bold'))
sentinel_value_inputvalidation_titlelabel = tkinter.Label(sentinel_value_inputvalidation_titleframe, text='Sentinel values and input validation', font=('arial', 20, 'bold'))
gen_randomnumbers_titlelabel = tkinter.Label(gen_randomnumbers_titleframe, text='Generating Random Numbers', font=('arial', 20, 'bold'))
Modules_value_returning_functions_titlelabel = tkinter.Label(Modules_value_returning_functions_titleframe, text='Modules and Value returning functions', font=('arial', 20, 'bold'))
level_select = tkinter.Label(Level_window, text='Please select a level to start at')
Rating_label = tkinter.Label(Rating_frame, text='Rate the e-Reflection Platform', font=('Arial', 20))
Opinion_titlelabel = tkinter.Label(Opinion_titleframe, text='Please provide your opinion about the unit below', font=('Arial', 20, 'bold'))
Welcome_label = tkinter.Label(Welcome_frame, text='Welcome to my e-Reflection platform', font=('arial', 20, 'bold'))

#Create labels used in the slides
Message_label = tkinter.Label(Message_frame, text='This platform will educate users on content covered in Unit 2B of the computer science course.'
'This e-Reflection platform\nwill cover content regarding loops, calculating a running total, sentinel values, input validation,'
'generating random numbers,\nmoduels and value returning functions.', justify='left')

Content_window1_labelloops = tkinter.Label(Content_window1_topicsframe, text='Loops are an essential concept in this unit.' 
' Having a clear and solid\nunderstanding of loops is the key to success in this particular unit.\n' 
'In particular, you will be learning about while loops, for loops and nested loops.', justify='left')

Content_window1_labelrunningtotal = tkinter.Label(Content_window1_topicsframe, text='In this unit you will also learn how' 
' to calculate a running total\nthrough learning about augmented assignment operators.', justify='left', wraplength=900)

Content_window1_labelsentinel_inputvalidation = tkinter.Label(Content_window1_topicsframe, text='Additionally, this course' 
' will teach you about special values, used to signal the end of a program.\nFurthermore, you will learn about designing programs'
' which ensure bad input is not accepted.', justify='left', wraplength=900)

Content_window1_labelmoduels_generatingrandomnumbers = tkinter.Label(Content_window1_topicsframe, text='This unit will also provide you'
' insight into how to import and use various moduels to organize our code.\nAdditionally, you will learn how to generate random numbers and'
' the application is has in the real world.', justify='left', wraplength=900)

Content_window1_labelvalue_returning_functions = tkinter.Label(Content_window1_topicsframe, text='Moreover, you will learn about value'
' returning functions and how returned values are used throughout a code.', justify='left', wraplength=900)

Loops_window_titlelabel = tkinter.Label(Loops_window_titleframe, text='Loops', font=('arial', 20, 'bold'))

Loops_window_topiclabel = tkinter.Label(Loops_window_topicframe, text='The specific loops covered in unit 2B of the computer science course is:\n'
'Nested loops, While loops and For loops', justify='left')

Loops_window_nestedlooplabel = tkinter.Label(Loops_window_nestedloopframe, text='Nested loops are an essential concept to learn'
'if you want to be successful in this course.\nNested loops are essentially when an inner loop goes through all of its iterations' 
' for every\nsingle iteration of an outer loop. Inner loops tend to complete their iteratations faster than\nouterloops.' 
'To get the total number of iterations for a nested loop multiply the number of\niterations of all loops. In this course you will'
' use nested loop to print various patterns and\nsequences. To effectivly understand nested loops, you must understand for and while loops.', justify='left', wraplength=900)

Loops_window_whilelooplabel = tkinter.Label(Loops_window_whileloopframe, text='While loops are also an integral part of the course '
'and involve creating conditions, which when satisified, repeat statements.\nIt essentially involves a task being accomplished while a statement is true.' 
' It works in two parts, 1) the condition is tested\n2) the statements are repeated if the condition is true.' 
'If the condition is false, the program exists. This classifies the while\nloop as a condition controlled loop.' 
'It is also important to consider that loops need a way of stopping, in which something\ninside the loop must eventually make the test condition false.'
'If the loop does not have a way of stopping, it is called an\ninfinite loop.The program continues to run until the program' \
'is interrupted. This usually occurs when the programmer\nforgets to write code inside the loop that makes the test condition false.', justify='left', wraplength=900 )

Loops_window_forlooplabel = tkinter.Label(Loops_window_forloopfame, text='For loops are count controlled loops, which involve a statement'
' iterating a specific number of times. For loops follow a\nformat where the variable represents the name of the variable and inside' 
' the brackets a sequence of values appears\nwith a comma separator to create a list. The next statements are executed each time the loop iterates.'
' Step value is a\nimportant concept to learn and is associated with the range function. Step value tells the loop how much to increase or\ndecrease the variable'
' each time it repeats.When you pass a third argument to the range function that is used as the step value.\nThe format for this involves' 
' the first argument representing the starting value, the second argument representing the ending value\nand the third argument representing the step value.' 
' Instead of increasing by 1, each successive number in the sequence will increase\nby the step value. Target variables are also associated with for loops.' 
' The purpose of a target variable is to reference each item in a\nsequence of items as the loop iterates. An example of this includes creating' 
'a table shows the values 1 to 10 on one column and the square\nof each number on the other column.', wraplength=900, justify='left')

Runningtotal_detaillabel = tkinter.Label(Runningtotal_detailframe, text='You will learn about the concept of keeping a running total and'
' the two major elements involved.\nThese two major elements involve learning about how a loop reads each number in a series and'
'\nhow a variable accumulates the total of the numbers that they read.An accumulator is the variable\nthat is used to accumulate' 
' the total of the numbers. A lot of programs in this unit will have assignment\nstatements where the variable that is on the'
' left side of the variable also appears on the right side - looking like this: X = X+1.\nHowever there is a more efficient way of writing'
' this, which involves an augmented assignment operator: x+=1. An augmented\nassignment operator is a shortcut, which allows you to'
' update the value of a variable by performing an operation on it and assigning\nthe result back to the same variable.', justify='left', wraplength=900)

Runningtotal_syntaxlabel = tkinter.Label(Runningtotal_detailframe, text='To be successful in effectivly learning this concept' 
'it is important to learn the syntax.\nx+=5 is equivalent to x = x+5.\nx-=2 is equivalent to x = x-2.\nx*=3 is equivalent to x = x*3.' \
'\nx/=y is equivalent to x = x/y.\nx%=3 is equivalent to x = x%3.', justify='left')

sentinel_valuelabel = tkinter.Label(sentinel_valueframe, text='A sentinel value is a special value that marks the end of a sequence of values.' 
' When a program reads a sentinel value, the loop terminates.\nOne example of using a sentinel value involves creating a program to calculate the' 
' average weight of patients and when the sentinel\nvalue is hit, no more weights are recorded, the loop terminates and the program displays the ' 
' average weight. In this case a reasonable\nsentinel value to set might be <=0. This suggests that the loop will terminate when the program reads'
' a weight less than or equal to 0.\nNote: The syntax for not equal to is: !=', justify='left', wraplength='900')

input_validationlabel = tkinter.Label(input_validationframe, text='Input validation loops are used to ensure our program does not accept bad input.' 
' These validation loops, inspect the input\nbefore it is processed, in which if the input is invalid, the program discards it and' 
' prompts the user to enter correct data.\nIf the input is bad, the loop will display an error message to inform the user of the bad input and then' 
' it reads the new input.\nThis loop will repeat as long as the input is deemed to be invalid. One such example, involves dealing with a businesses' 
' wholesales\nand setting the input validation to display an error message when wholesalve < 0, displaying the cost cannot be negative.', justify='left', wraplength=900)

gen_randomnumbers_detaillabel = tkinter.Label(gen_randomnumbers_detailframe, text='Python has several library functions to work with random numbers'
' stored in the random module in the standard library.\nTo use the random module, you will need to first write an import statement at the top of your program(import random).\n'
'In writing this import statement we are able to load the contents of the random module into memory and available to the program.\nFor functions inside a module we need to use dot notation' 
' to refer to it - the name of the module is on the left and the name of\nthe function is on the right. The random function returns a floating point number, in which you do not'
' pass any arguments to the\nrandom function. In this unit, you will learn about the randint function which allows two arguments to pass through it to ask for a\nrandom integer'
' inside of this specific range. For example, random.randint(1, 100) will generate a random number between 1 and 100.\nYou will also learn about the random.randrange function.'
' This function takes the same arguments as the range function, however it\ninstead returns a randomly selected value from the sequence of values. For instance, random.randrange(10)'
' will generate a random\nnumber from 1 - 10. There are also uniform functions, which return random floating-point number, but allows you to specify the range\nof values to select from.' 
' For example, random.uniform(1.0, 10.0) will return a floating-point number in the range of 1.0 through 10.0.', justify='left', wraplength=900)

gen_randomnumbers_applicationlabel = tkinter.Label(gen_randomnumbers_detailframe, text='Generating random numbers has various applications such as:\n'
'Creating games\nSimulation programs\nStatistical programs\nEncrypting sensitive data\nIn this unit you will use generating random numbers for coin toss'
' programs, rock paper scissors programs and much more.', justify='left')

Modules_detaillabel = tkinter.Label(Modules_detailframe, text='As our programs grow bigger, it may contain more lines, in which to make our code more organized' 
' and easier to maintain, we can\nuse modules to seperate codes in seperate file. Modules act as a code libary, with their simplicity and reusability. A module is' 
' essentially\na file that contains python code, which should contain functions that perform a similar task. Modules make it easier to reuse the same code\nin more than' 
' one program. If you write a set of functions that are needed in different programs, you can place those in a module and import it in each program that needs to call ' 
" one of the functions. A module's name should end in .py so that it can be imported into other python programs. To import other modules we must write an import statement" 
' above (example: import math, import random, import calculation).', justify='left', wraplength=900)

Value_returning_functions_detaillabel = tkinter.Label(Value_returning_functions_detailframe, text='This unit will teach you about the implementation of a return statement.' \
' Return statements work by exiting the\nfunction and sending a value back to the main program, which is read throughout your code. Return is commonly\nused to use a functions' \
' output in other parts of your code and as a result it is important to note that it is different\nthan print. The return statement follows a simple format of: return expression.' \
' Expression can be a value that will\nbe sent back to the part of the program that called the function. Expression can act as a variable or value. You can\nalso write functions,' \
' which return strings, boolean values(true or false) and multiple values.', justify='left', wraplength=900)

FAQ_introlabel = tkinter.Label(FAQ_window, text='These are frequently asked questions regarding the unit material. Click enter to see the answers.')

#Create question and answer labels for frequently asked questions 
Q1_label = tkinter.Label(FAQ_window, text='Question 1: What exactly is a loop?')
A1_label = tkinter.Label(FAQ_window, text='Answer 1:  A loop is a control structure that repeats actions')
Q2_label = tkinter.Label(FAQ_window, text='Question 2: What is a sentinel value?')
A2_label = tkinter.Label(FAQ_window, text="Answer 2: It's a special value that signals the end of input.")
Q3_label = tkinter.Label(FAQ_window, text='Question 3: What does import do?')
A3_label = tkinter.Label(FAQ_window, text='Answer 3: It loads external code libraries or modules.')

#Create all the buttons
Instructions_button = tkinter.Button(Intro_buttonframe, text='Instructions', width=20, height=2, command=show_instructions)
Content_button = tkinter.Button(Intro_buttonframe, text='Unit content', width=20, height=2, command=ask_name)
Quiz_button = tkinter.Button(Intro_buttonframe, text='Quiz', width=20, height=2, command=choose_level)
Quit_button = tkinter.Button(Intro_buttonframe, text='Quit', width=20, height=2, command=Intro_window.destroy)
Next_button1 = tkinter.Button(Content_window1_buttonframe, text='Next', command=loops_slide)
Back_button1 = tkinter.Button(Content_window1_buttonframe, text='Back', command=welcome_game)
Home_button = tkinter.Button(About_window, text='Home', command=welcome_game)
Next_button2 = tkinter.Button(Loops_window_buttonframe, text='Next', command=runningtotal)
Back_button2 = tkinter.Button(Loops_window_buttonframe, text='Back', command=intro_slide)
Next_button3 = tkinter.Button(Runningtotal_buttonframe, text='Next', command=sentinel_value_inputvalidation)
Back_button3 = tkinter.Button(Runningtotal_buttonframe, text='Back', command=loops_slide)
Next_button4 = tkinter.Button(sentinel_value_inputvalidation_buttonframe, text='Next', command=gen_randomnumbers)
Back_button4 = tkinter.Button(sentinel_value_inputvalidation_buttonframe, text='Back', command=runningtotal)
Next_button5 = tkinter.Button(gen_randomnumbers_buttonframe, text='Next', command=Modules_value_returning_functions)
Back_button5 = tkinter.Button(gen_randomnumbers_buttonframe, text='Back', command=sentinel_value_inputvalidation)
Home_button2 = tkinter.Button(Home_buttonframe2, text='Home', command=welcome_game)
Home_button3 = tkinter.Button(Home_buttonframe3, text='Home', command=welcome_game)
Rating_button= tkinter.Button(Rating_buttonframe, text='Submit', command=thank_rate)
opinion_submitbutton = tkinter.Button(opinion_buttonframe, text='Submit', command=submit_button_response)
 
#Create the entry boxes
name_entry = tkinter.Entry(nameframe1)
entry_box = tkinter.Entry(Opinion_window, width=50)

#Create all the canvases 
canvas = tkinter.Canvas(Content_window1, width=1180, height=500)
Computer_science1 = tkinter.PhotoImage(file='Computer_science.png')
Computer_science1 = Computer_science1.subsample(3)
canvas.create_image(5, 250, anchor='sw', image=Computer_science1)

canvas2 = tkinter.Canvas(About_window, width=1000, height=500)
Computer_science2 = tkinter.PhotoImage(file='Computer_science about.png')
canvas2.create_image(870, 250, anchor='se', image=Computer_science2)

canvas3 = tkinter.Canvas(Ratings_window, width=500, height=300)
Five_stars_rating = tkinter.PhotoImage(file='5_stars.svg.png')
Five_stars_rating = Five_stars_rating.subsample(7)
canvas3.create_image(250,200, anchor = 'center', image=Five_stars_rating)

#Create the menu bar 
menubar = tkinter.Menu(Intro_window)
file_menu = tkinter.Menu(menubar)
#Add an about program section
file_menu.add_command(label='About', command=About_program)
#Add an FAQ question section
file_menu.add_command(label='FAQS', command=FAQ_question)
#Add a ratings section
file_menu.add_command(label='Ratings', command=ratings)
#Add an opinion section
file_menu.add_command(label='Opinion', command=opinion)
#Add an exit option
file_menu.add_command(label='Exit', command=Intro_window.destroy)
menubar.add_cascade(label = 'File', menu=file_menu)

#Call the welcome game function
welcome_game()

#Mainloop the intro window
Intro_window.mainloop()