import customtkinter as ct

ct.set_appearance_mode('dark')

janela = ct.CTk('#483D8B')

janela.geometry('500x300')

ct.CTkLabel(janela, text='Sistema de Login',font=('arial',50,'bold' ),text_color='red').pack(pady=15)

login = ct.CTkEntry(janela,placeholder_text='digite sua Login',width=450,height=50)

login.pack(pady=10)

senha = ct.CTkEntry(janela,placeholder_text='digite a sua senha',width=450,height=50,show='*',) 

senha.pack(pady=10)

botao = ct.CTkButton(janela,text='Acessar',font=('arial',30),fg_color='black',hover_color='darkred')
botao.pack(pady=5)



janela.mainloop()