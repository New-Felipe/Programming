import tkinter as tk
import time

# Função para atualizar o relógio
def atualizar_relogio():
    tempo_atual = time.strftime('%H:%M:%S')
    label_relogio.config(text=tempo_atual)
    label_relogio.after(1000, atualizar_relogio)

# Criação da janela principal
janela = tk.Tk()
janela.title("Relógio Digital")
janela.configure(bg='black')

# Configuração do rótulo do relógio
label_relogio = tk.Label(janela, font=('Digital-7', 60), background='black', foreground='white')
label_relogio.pack(pady=20)

# Inicia a atualização do relógio
atualizar_relogio()

# Inicia o loop da interface gráfica
janela.mainloop()