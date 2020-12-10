# Ready-TKinter-Windows
Hello there! This code is based on a program I made for college, since I noted
there aren't any "Ready-to-go" codes out there for fast use of the Tkinter library
for small projects and programs. Here I will explain how to properly use the code to your favor,
and feel free to optimize it to your liking! I'm not an expert on Python programming, just 
a student that's trying to make other people's jobs easier. It's also my first attempt 
on a free to use code and tutorial, so if there are any incorrect use of terms, as well
hard to understand explanations, please send your feedback so I can update these files! 
Here we go!

# 1 - GETTING THE CODE TO WORK
This part is easy: Have Python 3.* installed on your machine (don't know if there any problems on having only 2.* installed,
so better go for both for maximum compatibility XD). Normally it already has the Tkinter library with it, but in case
it doesn't, download it through Pip (you can find more information through other tutorials). 

# 2 - HOW IT WORKS 
After several search for answers on some points to better use of the Tkinter 
library through the college project, I found some pieces of code from other users of
StackOverflow to optimize some parts like: creating a UNIQUE screen without creating 
unnecessary Toplevels (Tkinter's way to create new screens besides the MAIN one for the start
of the project; in this code, it's the Clear function), how to solve some basic problems 
on Entry's GET function (the IntEntry class), and how to make Buttons work properly when press
them (the lambda before the actual event that happens when the button is pressed; Ex:
command=lambda: _event_). Thanks to these users, I could create this code, 
so a big thanks to these guys! 

The code uses 3 main global variables for fast creation and destruction of Tkinter's Widgets
on the screen (root, Frame and Canvas), making their creation faster and more intuitive (I hope \[T]/).

- This part:

global root     
root = tk.Tk()
startScreen(root)

- Makes ROOT be a global variable for further use, makes it the main screen for Tkinter to work,
and gets called by the function startScreen so it can be initialized. From here, the magic starts:

def startScreen(root):
    global canvas
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    global frame
    frame = tk.Frame(root, bg="gray", bd=10)
    frame.place(relheight=1, relwidth=1)

    root.mainloop()

- ROOT is now working as TK, and the Frame and Canvas are now set. The Canvas is useful for the 
desired size of the screen, by using HEIGHT and WIDTH as its parameters (they are a CONSTANT 
of your choice), and using ROOT as its main screen. The loop is set on the end, and the Frame is where the fun happens.

- From now on, the widgets that you will create will use FRAME as its substitute for ROOT; Instead of
creating widgets on ROOT, the Frame allows the use of widget.destroy() command, making the use of 
the function Clear to delete widgets on Frame whenever you want to create a "new"
screen without the need for Toplevels, and thus a single screen is being used (ROOT), but being rewritten in Frame. 

- Each "new" screen can be created inside funtions, so if you use a button to go to a "new" screen,
for example, you can use the function Clear(frame, _userFunction_) as the Button Command 
to clear the actual screen of its widgets and create new ones inside the _userFunction_ call. Ex:

button = tk.Button(frame, command=lambda: clear(frame, _newScreen_))
                                    ^ The lambda makes sure its command happens only when you press it.

- You can create widgets on the startScreen already, just use Frame for them, and clear them out with
Clear funtion after an event.

This makes it for the basics, when you open the code, more explaining is done with an interactive example, just run the code on
your editor of preference.

# 3 - ADJUSTMENTS AND OPTIMIZATIONS
I made the code based on a college project, and took me about 1 week to finish it; I'm not that
expert on Python programming, so if you think that you make it better and adapt it to your needs, 
go for it! And if possible, tell me how you did it, so I can update the project itself! XD

Based on this, you're free to use your imagination to use this code, from a college project like mine,
or a quick solution for an idea you just had; Any questions or problems, talk to me through my GitHub
and I will do my best to help you out. 

-Yours sincerely, the project Author: gabrielalextx
