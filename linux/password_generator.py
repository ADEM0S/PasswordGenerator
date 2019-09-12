import string
from random import randint, choice
from tkinter import *

def generate_password():
    #determiner max et min de car
    password_min = 6
    password_max = 20
    #determiner quels caracteres sont acceptés
    all_chars = string.ascii_letters + "@#._" + string.digits
    #generer le mdp random
    password = "".join(choice(all_chars) for x in range (randint(password_min, password_max)))
    #afficher dans l'espace d'input
    password_entry.delete(0, END)
    password_entry.insert(0, password)

        


#cration fenetre
window= Tk()
window.title("Password Generator")
window.geometry('1080x720')
window.iconbitmap('@icon.xbm')
window.config(bg= '#663366')

#creer la frame
frame = Frame(window, bg= '#663366')

#creation d'imagine
width = 300
height= 300
image = PhotoImage(file = "login.png").subsample(2)
canvas = Canvas(frame, width=width, height= height, bg='#663366', bd=0, highlightthickness=0 )
canvas.create_image(width/2, height/2, image = image)
canvas.grid(row=0, column= 0, sticky=W)

#creer une sous boite
right_frame = Frame(frame, bg= '#663366', )

#creer un titre
label_title = Label(right_frame, text="Mot de passe:", font=('Helvetica', 30), bg= '#663366', fg= 'white')
label_title.pack()

#creer un champ/entree/input
password_entry = Entry(right_frame, font=('Helvetica', 20), bg= '#663366', fg= 'white')
password_entry.pack()

#creer un boutton
password_generate_button = Button(right_frame, text="Générer", font=('Helvetica', 20), bg= '#663366', fg= 'white', command= generate_password)
password_generate_button.pack(pady= 10, fill= X)

#on place la sous boite a droite de la frame
right_frame.grid(row=0, column=1, sticky = E)

#AFFICHER LA FRAME
frame.pack(expand= YES)

#creer une barre de menu
menu_bar = Menu(window)

#creer menu 1
file_menu = Menu(menu_bar, tearoff= 0)
file_menu.add_command(label='Nouveau', command= generate_password)
file_menu.add_command(label='Quitter', command= window.quit)
menu_bar.add_cascade(label='Fichier', menu= file_menu)

#configurer pour rentrer le menu
window.config(menu= menu_bar)

#AFFICHER WINDOW
window.mainloop()
