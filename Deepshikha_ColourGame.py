#This Game is made by Deepshikha - Enjoy it.
import tkinter
import random
  

colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']
score = 0
  
# this is for the game time left, initially I took 40 seconds.
timeleft = 40
  

def startGame(event):
      
    if timeleft == 40:
          
        # start the countdown timer.
        countdown()
          
    # run the function to
    # choose the next colour.
    nextColour()
  
# Function to choose and
# display the next colour.
def nextColour():
  
    # use the globally declared 'score'
    # and 'play' variables above.
    global score
    global timeleft
  
    
    if timeleft > 0:
  
        
        e.focus_set()
  
        
        if e.get().lower() == colours[1].lower():
              
            score += 1
  
        
        e.delete(0, tkinter.END)
          
        random.shuffle(colours)
          
      
        label.config(fg = str(colours[1]), text = str(colours[0]))
          
        
        scoreLabel.config(text = "Score: " + str(score))
  
  
# Countdown timer function 
def countdown():
  
    global timeleft
  
    
    if timeleft > 0:
  
        
        timeleft -= 1
          
        
        timeLabel.config(text = "Time left: "
                               + str(timeleft))
                                 
        
        timeLabel.after(1000, countdown)
  
  

  
# creating a GUI window
root = tkinter.Tk()
  
# setting the title
root.title("COLOR GAME - Deepshikha")
  
# setting the size
root.geometry("450x300")
  
instructions = tkinter.Label(root, text = "This Game is made by Deepshikha - Enjoy!!",
                                      font = ('Bernard MT Condensed', 15))

instructions.pack()

instructions = tkinter.Label(root, text = "Type in the colour"
                        " of the words, and not the word text!",
                                      font = ('Helvetica', 12))
instructions.pack() 
  

scoreLabel = tkinter.Label(root, text = "Press enter to start",
                                      font = ('Helvetica', 12))
scoreLabel.pack()
  

timeLabel = tkinter.Label(root, text = "Time left: " +
              str(timeleft), font = ('Algerian', 15))
                
timeLabel.pack()
  

label = tkinter.Label(root, font = ('Algerian', 60))
label.pack()
  

e = tkinter.Entry(root)
  
# run the 'startGame' function 
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()
  

e.focus_set()
  
# starting the GUI
root.mainloop()
