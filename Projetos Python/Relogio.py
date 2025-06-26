import tkinter as tk
import time

def atualizar_relogio():
    # Obtém a hora atual
    hora_atual = time.strftime('%H:%M:%S')
    # Atualiza o rótulo com a hora atual
    rotulo_relogio.config(text=hora_atual)
    # Chama a função novamente após 1000 ms (1 segundo)
    rotulo_relogio.after(1000, atualizar_relogio)

# Cria a janela principal
janela = tk.Tk()
janela.title("Relógio Digital")
janela.configure(bg='black')  # Fundo preto

# Cria um rótulo para exibir a hora
rotulo_relogio = tk.Label(janela, font=('Arial', 50), bg='black', fg='white')
rotulo_relogio.pack(pady=20)  # Adiciona um espaço vertical

# Inicia a atualização do relógio
atualizar_relogio()

# Inicia o loop da interface gráfica
janela.mainloop()