import customtkinter as ct

def calcular():
    d= int(distancia.get())
    g = int(gasolina.get())
    p = float(preco.get())
    
    calculo = (d/g)*p
    
    resultado.configure(text=f'o valor total para a viagem sera de R${calculo:.2f}')

ct.set_appearance_mode('dark')

janela = ct.CTk()

janela.geometry('500x500')

ct.CTkLabel(janela, text='Calcular consumo de Gasolina',font=('arial',30,'bold' ),text_color='red').pack(pady=15)

distancia = ct.CTkEntry(janela,placeholder_text='digite a distancia ',width=450,height=50)

distancia.pack(pady=10)

gasolina = ct.CTkEntry(janela,placeholder_text='digite o consumo do veiculo',width=450,height=50,) 

gasolina.pack(pady=10)

preco = ct.CTkEntry(janela,placeholder_text='digite o preço',width=450,height=50,) 

preco.pack(pady=10)


botao = ct.CTkButton(janela,text='calcular',font=('arial',30),fg_color='black',hover_color='darkred',command=calcular)
botao.pack(pady=5)

resultado = ct.CTkLabel(janela,text='',font=('arial',18))

resultado.pack(pady=5)

janela.mainloop()