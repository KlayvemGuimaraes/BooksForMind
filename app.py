import tkinter as tk
import random

recomendacoes = {
    "programação": ["Clean Code", "Python Crash Course", "The Pragmatic Programmer"],
    "ficção científica": ["1984", "Fahrenheit 451", "Duna"],
    "autoajuda": ["O Poder do Hábito", "Como Fazer Amigos e Influenciar Pessoas", "Mindset", "Hábitos Atômicos"],
    "romance": ["É assim que acaba", "Um romance fora de época", "Eu e esse meu coração", "Como eu era antes de você"],
    "fantasia": ["É assim que acaba", "Um romance fora de época", "Eu e esse meu coração", "Como eu era antes de você"],
    "comédia": ["Diário de um banana", "Perdido em Marte", "Cadê você Bernadette?"]
}

def gerar_recomendacao(topico):
    if topico in recomendacoes:
        livros = recomendacoes[topico]
        recomendacao = random.choice(livros)
        return recomendacao
    else:
        return "Desculpe, não tenho recomendações para esse tópico."

def mostrar_recomendacao():
    topico = entrada.get()
    recomendacao = gerar_recomendacao(topico)
    resultado.configure(text=recomendacao)

janela = tk.Tk()
janela.title("Recomendação de Livros")

rotulo = tk.Label(janela, text="Digite um tópico:")
rotulo.pack()

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Gerar Recomendação", command=mostrar_recomendacao)
botao.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

# Loop principal da interface gráfica
janela.mainloop()
