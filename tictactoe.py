from tkinter import *
from tkinter import messagebox as msg
import random
root = Tk()
root.title('Tic Tac Toe-codevision')
# X starts so true

clicked = True
count = 0

#disable  buttonS
def disable_button():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
#check winner or game
def showinfo():
    global winner
    winner = False
    #horizontal checking
    if b1['text']== 'X' and b2['text']== 'X'and b3['text']== 'X':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','X is WINNER')
    elif b4['text']== 'X' and b5['text']== 'X'and b6['text']== 'X':
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','X is WINNER')

    elif b7['text']== 'X' and b8['text']== 'X'and b9['text']== 'X':
        b7.config(bg='green')
        b8.config(bg='green')
        b9.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','X is WINNER')
    #verticaly checking
    elif b1['text']== 'X' and b4['text']== 'X'and b7['text']== 'X':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','X is WINNER')
    elif b2['text']== 'X' and b5['text']== 'X'and b8['text']== 'X':
        b2.config(bg='green')
        b5.config(bg='green')
        b8.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','X is WINNER')
    elif b3['text']== 'X' and b6['text']== 'X'and b9['text']== 'X':
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','X is WINNER')
    #checking diagonal
    elif b1['text']== 'X' and b5['text']== 'X'and b9['text']== 'X':
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','X is WINNER')
    elif b3['text']== 'X' and b5['text']== 'X'and b7['text']== 'X':
        b3.config(bg='green')
        b5.config(bg='green')
        b7.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','X is WINNER')
#checking for O 
    #horizontal checking
    elif b1['text']== 'O' and b2['text']== 'O'and b3['text']== 'O':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','O is WINNER')
    elif b4['text']== 'O' and b5['text']== 'O'and b6['text']== 'O':
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','O is WINNER')
    elif b7['text']== 'O' and b8['text']== 'O'and b9['text']== 'O':
        b7.config(bg='green')
        b8.config(bg='green')
        b9.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','O is WINNER')
    #verticaly checking
    elif b1['text']== 'O' and b4['text']== 'O'and b7['text']== 'O':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','O is WINNER')
    elif b2['text']== 'O' and b5['text']== 'O'and b8['text']== 'O':
        b2.config(bg='green')
        b5.config(bg='green')
        b8.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','O is WINNER')
    elif b3['text']== 'O' and b6['text']== 'O'and b9['text']== 'O':
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','O is WINNER')
    #checking diagonal
    elif b1['text']== 'O' and b5['text']== 'O'and b9['text']== 'O':
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','O is WINNER')
    elif b3['text']== 'O' and b5['text']== 'O'and b7['text']== 'O':
        b3.config(bg='green')
        b5.config(bg='green')
        b7.config(bg='green')
        winner = True
        disable_button()
        msg.showinfo('Tic Tac Toe','O is WINNER')
    #check if tie
    if count==9 and winner== False:
        msg.showinfo('Tic Tac Toe','No one winner play game again')
#button clicked
def b_click(b):
    global clicked,count
    if b['text']==' ' and clicked==True:
        b['text'] = 'X'
        count +=1
        clicked = False
        showinfo()
    elif b['text']==' ' and clicked==False:
        b['text'] = 'O'
        count +=1
        clicked = True
        showinfo()
    else:
        msg.showerror('Tic Tac Toe-codevision','You are not Allowed to click a button Twice!!')




def main():
    
        

    global b1,b2,b3,b4,b5,b6,b7,b8,b9
   
    
    #GAME Button 
    b1 = Button(root,text=' ',font=('lucida',30),bg='SystemButtonFace',height=3,width=6,command=lambda:b_click(b1))
    b2 = Button(root,text=' ',font=('lucida',30),bg='SystemButtonFace',height=3,width=6,command=lambda:b_click(b2))
    b3 = Button(root,text=' ',font=('lucida',30),bg='SystemButtonFace',height=3,width=6,command=lambda:b_click(b3))

    b4 = Button(root,text=' ',font=('lucida',30),bg='SystemButtonFace',height=3,width=6,command=lambda:b_click(b4))
    b5 = Button(root,text=' ',font=('lucida',30),bg='SystemButtonFace',height=3,width=6,command=lambda:b_click(b5))
    b6 = Button(root,text=' ',font=('lucida',30),bg='SystemButtonFace',height=3,width=6,command=lambda:b_click(b6))

    b7 = Button(root,text=' ',font=('lucida',30),bg='SystemButtonFace',height=3,width=6,command=lambda:b_click(b7))
    b8 = Button(root,text=' ',font=('lucida',30),bg='SystemButtonFace',height=3,width=6,command=lambda:b_click(b8))
    b9 = Button(root,text=' ',font=('lucida',30),bg='SystemButtonFace',height=3,width=6,command=lambda:b_click(b9))
    #Grid our Button in our window screen
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)
#create a menu
yourmenue = Menu(root)
m1 = Menu(yourmenue,tearoff=0)
m1.add_command(label='Refresh',command=main)

root.config(menu= yourmenue)
yourmenue.add_cascade(label='Setting',menu=m1)
main()
root.mainloop()