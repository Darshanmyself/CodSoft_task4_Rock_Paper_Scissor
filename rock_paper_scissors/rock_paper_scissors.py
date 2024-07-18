from tkinter import *
from PIL import Image,ImageTk
from random import randint

root=Tk()
root.title('Rock Paper Scissor')
root.configure(background='#3BACF2')
root.geometry('730x600+400+100')
root.resizable(False,False)

#resize
def resize_image(image_path, size):
    # Open the image file
    image = Image.open(image_path)
    # Resize the image
    resized_image = image.resize(size, Image.LANCZOS)
    return resized_image

# update choices

choices = ['rock','paper','scissor']

def update_choices(x):
    #for computer
    comp_choice = choices[randint(0,2)]
    if comp_choice=='rock':
        comp_label.configure(image=rock_comp)
    elif comp_choice=='paper':
        comp_label.configure(image=paper_comp)
    else:
        comp_label.configure(image=scissor_comp)
    #for user
    if x=='rock':
        user_label.configure(image=rock_user)
    elif x=='paper':
        user_label.configure(image=paper_user)
    else:
        user_label.configure(image=scissor_user)
        
    check_winner(x,comp_choice)
    
#update messages

def update_message(text):
    msg['text']=text

# update user score
def update_user_score():
    score=int(user_score['text'])
    score+=1
    user_score['text']=str(score)

#update comp score
def update_comp_score():
    score=int(comp_score['text'])
    score+=1
    comp_score['text']=str(score)


# checking winner
def check_winner(user,comp):
    if user == comp:
        update_message('          Tie !      ')
    elif user == 'rock':
        if comp=='paper':
            update_message('   You Loose !   ')
            update_comp_score()
        else:
            update_message('    You Win !    ')
            update_user_score()
    elif user=='paper':
        if comp=='scissor':
            update_message('   You Loose !   ')
            update_comp_score()
        else:
            update_message('    You Win !    ')
            update_user_score()
    elif user=='scissor':
        if comp=='rock':
            update_message('   You Loose !   ')
            update_comp_score()
        else:
            update_message('    You Win !    ')
            update_user_score()
    else:
        pass
            
#Creating Icon
image_icon=PhotoImage(file=r'images/icon.png')
root.iconphoto(False,image_icon)

#Top bar
top_image=PhotoImage(file=r"images/bg.png")
Label(root,image=top_image,bg='#3BACF2').place(x=0,y=0)

#images
new_size=(150,150)
rock_user=ImageTk.PhotoImage(resize_image(r'images/rock_user.png',new_size))
paper_user=ImageTk.PhotoImage(resize_image(r'images/paper_user.png',new_size))
scissor_user=ImageTk.PhotoImage(resize_image(r'images/scissor_user.png',new_size))
rock_comp=ImageTk.PhotoImage(resize_image(r'images/rock_comp.png',new_size))
paper_comp=ImageTk.PhotoImage(resize_image(r'images/paper_comp.png',new_size))
scissor_comp=ImageTk.PhotoImage(resize_image(r'images/scissor_comp.png',new_size))

#inserting images
user_label = Label(root,image=scissor_user,bg='#3BACF2')
comp_label = Label(root,image=scissor_comp,bg='#3BACF2')

user_label.place(x=30,y=350)
comp_label.place(x=550,y=350)

#Scores
user_score = Label(root, text=0, font='times 20',bg='#3BACF2',fg='black')
comp_score = Label(root, text=0, font='times 20',bg='#3BACF2',fg='black')
user_score.place(x= 240,y=405)
comp_score.place(x=470,y=405)

#buttons
but_size=(80,80)
rock = ImageTk.PhotoImage(resize_image(r'images/rock.png',but_size))
paper = ImageTk.PhotoImage(resize_image(r'images/paper.png',but_size))
scissor =ImageTk.PhotoImage(resize_image(r'images/scissor.png',but_size))
Button(root,image=rock,bg='#3BACF2',bd=0,command = lambda:update_choices('rock')).place(x=210,y=490)
Button(root,image=paper,bg='#3BACF2',bd=0,command = lambda:update_choices('paper')).place(x=330,y=490)
Button(root,image=scissor,bg='#3BACF2',bd=0,command = lambda:update_choices('scissor')).place(x=450,y=490)

#Indicators
user_ind = Label(root,text='USER',font='times 17 bold italic',bg='#3BACF2',fg='black')
comp_ind = Label(root,text='COMPUTER',font='times 17 bold italic',bg='#3BACF2',fg='black')
user_ind.place(x=50,y=300)
comp_ind.place(x=570,y=300)

#message
msg = Label(root,font='times 25 bold italic', bd=5,bg='#3BACF2', fg='black')
msg.place(x=255,y=300)

root.mainloop()
