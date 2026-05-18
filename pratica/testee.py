import tkinter as tk

def calcular():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        operacao = operator.get()

        if operacao == '+':
            resultado.set(n1 + n2)
        elif operacao == '-':
            resultado.set(n1 - n2)
        elif operacao == '*':
            resultado.set(n1 * n2)
        elif operacao == '/':
            resultado.set(n1 / n2)
    except:
        resultado.set('Erro! apenas números')

janela = tk.Tk()
janela.title('Calculadora Simples')
janela.geometry('500x200')

operator = tk.StringVar(janela)
operator.set('+') # Valor padrão
resultado = tk.StringVar()

# Componentes da Interface (Widgets)
entrada1 = tk.Entry(janela)
entrada1.pack(pady=5)

# Menu de Opções para operação
seletor = tk.OptionMenu(janela, operator, '+', '-', '*', '/')
seletor.pack(pady=5)

entrada2 = tk.Entry(janela)
entrada2.pack(pady=5)

botao = tk.Button(janela, text="Calcular", command=calcular)
botao.pack(pady=10)

label_resultado = tk.Label(janela, textvariable=resultado, font=("Arial", 12, "bold"))
label_resultado.pack(pady=5)

# Iniciar a aplicação
janela.mainloop()