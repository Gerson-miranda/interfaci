import customtkinter as ct
import os

# -------Funções--------

def shutdown():
    os.system('shutdown -s 0')
    
def restart():
    os.system('shutdown /r /t 0')
    
def logoff():
    os.system('shutdown -l ')
    

# ------------------------

ct.set_appearance_mode('dark')

janela = ct.CTk()

janela.maxsize(300,400) 

janela.minsize(300,400)

janela.title('Power Patch V 1.0')

janela.iconbitmap('409bomb_100833.ico')


ct.CTkLabel(janela, text= ' Power Patch V1.0',font= ('verdana', 28 , 'bold'),text_color= 'yellow').pack(pady=10)

desligar = ct.CTkButton(janela,
                        text='desligar',
                        width=250,height=20,
                        fg_color='yellow',
                        text_color='black',
                        font=('verdana',18,'bold'),
                        hover_color='gold',
                        cursor = 'pirate',
                        command= shutdown)

desligar.pack(pady=30)

reniciar = ct.CTkButton(janela,
                        text='reniciar',
                        width= 250,
                        height=20,
                        fg_color='yellow',
                        text_color='black',
                        font=('verdan',18,'bold'),
                        hover_color='gold',
                        cursor = 'pirate',
                        command= restart)

reniciar.pack(pady=30)

bloquear = ct.CTkButton(janela,
                        text='bloquear',
                        width= 250,
                        height=20,
                        fg_color='yellow',
                        text_color='black',
                        font=('verdan',18,'bold'),
                        hover_color='gold',
                        cursor = 'pirate',
                        command= logoff)

bloquear.pack(pady=30)



janela.mainloop()