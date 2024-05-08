"""
Criação de uma arvore binaria de busca do dicionario aurélia, utilizando python

Criadores:
    JhonHR
    Ayalon Dutra
    Matheus Moreira
    Hiago Ribeiro
"""
# Importando a biblioteca Tkinter do python para criar a vizualização da árvore
import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
from ttkthemes import ThemedTk
import json
import graphviz
from PIL import Image, ImageTk
import random
from customtkinter import *

class No:
    """
    Representa um nó em uma árvore de pesquisa binária.

    Atributos:
        chave: A chave do nó.
        valor: O valor associado à chave.
        esquerdo: Uma referência ao nó filho esquerdo.
        direito: Uma referência ao nó filho certo.
    """

    def __init__(self, chave, valor):
        """
        Inicializa uma nova instância da classe No.

        Argumentos:
            chave: A chave do nó.
            valor: O valor associado à chave.
        """
        self.chave = chave
        self.valor = valor
        self.esquerdo = None
        self.direito = None


def inserir(raiz, chave, valor):  # Define uma função chamada inserir que recebe a raiz da árvore, uma chave e um valor como argumentos
    if raiz is None:  # Se a raiz for None, significa que estamos inserindo na raiz da árvore
        return No(chave, valor)  # Retorna um novo nó com a chave e o valor fornecidos
    else:  # Se a raiz não for None, significa que estamos inserindo em uma árvore já existente
        if chave < raiz.chave:  # Se a chave a ser inserida for menor que a chave do nó atual
            raiz.esquerdo = inserir(raiz.esquerdo, chave, valor)  # Insere o novo nó no filho à esquerda do nó atual
        else:  # Se a chave a ser inserida for maior ou igual que a chave do nó atual
            raiz.direito = inserir(raiz.direito, chave, valor)  # Insere o novo nó no filho à direita do nó atual
    return raiz  # Retorna a raiz da árvore após a inserção


def buscar(raiz, chave):  # Define uma função chamada buscar que recebe a raiz da árvore e uma chave como argumentos
    if raiz is None or raiz.chave == chave:  # Se a raiz for None ou se a chave for igual à chave do nó atual
        return raiz.valor if raiz else None  # Retorna o valor do nó atual se a raiz não for None, caso contrário, retorna None
    if chave < raiz.chave:  # Se a chave procurada for menor que a chave do nó atual
        return buscar(raiz.esquerdo, chave)  # Realiza a busca recursivamente no filho à esquerda do nó atual
    return buscar(raiz.direito, chave)  # Caso contrário, realiza a busca recursivamente no filho à direita do nó atual


def minimo(raiz):  # Define uma função chamada minimo que recebe a raiz da árvore como argumento
    atual = raiz  # Inicializa a variável 'atual' com a raiz da árvore
    while atual.esquerdo is not None:  # Enquanto o nó atual tiver um filho à esquerda
        atual = atual.esquerdo  # Atualiza o nó atual para ser o filho à esquerda do nó atual
    return atual  # Retorna o valor do nó atual, que é o nó com o menor valor na árvore


def remover(raiz, chave):  # Define uma função chamada remover que recebe a raiz da árvore e uma chave como argumentos
    if raiz is None:  # Se a raiz for None, significa que a chave não está presente na árvore
        return raiz  # Retorna None, indicando que a chave não foi encontrada
    if chave < raiz.chave:  # Se a chave procurada for menor que a chave do nó atual
        raiz.esquerdo = remover(raiz.esquerdo, chave)  # Realiza a remoção recursivamente no filho à esquerda do nó atual
    elif chave > raiz.chave:  # Se a chave procurada for maior que a chave do nó atual
        raiz.direito = remover(raiz.direito, chave)  # Realiza a remoção recursivamente no filho à direita do nó atual
    else:  # Se a chave procurada for igual à chave do nó atual
        if raiz.esquerdo is None and raiz.direito is None:  # Se o nó atual não tem filhos
            raiz = None  # Remove o nó atual
        elif raiz.esquerdo is None:  # Se o nó atual tem apenas um filho à direita
            raiz = raiz.direito  # Substitui o nó atual pelo seu filho à direita
        elif raiz.direito is None:  # Se o nó atual tem apenas um filho à esquerda
            raiz = raiz.esquerdo  # Substitui o nó atual pelo seu filho à esquerda
        else:  # Se o nó atual tem dois filhos
            sucessor = minimo(raiz.direito)  # Encontra o nó com o menor valor no subárvore à direita
            raiz.chave = sucessor.chave  # Substitui a chave do nó atual pela chave do sucessor
            raiz.valor = sucessor.valor  # Substitui o valor do nó atual pelo valor do sucessor
            raiz.direito = remover(raiz.direito, sucessor.chave)  # Remove o sucessor da árvore
    return raiz  # Retorna a raiz da árvore após a remoção


def preordenacao(raiz, dot):  # Define uma função chamada preordenacao que recebe a raiz da árvore e um objeto dot (presumivelmente do módulo graphviz) como argumentos
    if raiz is not None:  # Se a raiz não for None, significa que há um nó para processar
        dot.node(str(id(raiz)), label=f'{raiz.chave} ({raiz.valor})')  # Cria um nó no gráfico com a chave e o valor do nó atual
        if raiz.esquerdo:  # Se o nó atual tem um filho à esquerda
            dot.edge(str(id(raiz)), str(id(raiz.esquerdo)), label="")  # Cria uma aresta entre o nó atual e seu filho à esquerda
        if raiz.direito:  # Se o nó atual tem um filho à direita
            dot.edge(str(id(raiz)), str(id(raiz.direito)), label="")  # Cria uma aresta entre o nó atual e seu filho à direita
        preordenacao(raiz.esquerdo, dot)  # Realiza a preordenação recursivamente no filho à esquerda do nó atual
        preordenacao(raiz.direito, dot)  # Realiza a preordenação recursivamente no filho à direita do nó atual


raiz = None #Inicializando a raiz da arvore como None

def inserir_palavra():  # Define uma função chamada inserir_palavra
    global raiz  # Declara que a variável raiz é global, permitindo que seja acessada dentro da função
    chave = entrada_palavra.get()  # Obtém o texto da entrada de palavra
    valor = entrada_descricao.get()  # Obtém o texto da entrada de descrição
    raiz = inserir(raiz, chave, valor)  # Chama a função inserir para adicionar a palavra e sua descrição à árvore
    entrada_palavra.delete(0, tk.END)  # Limpa o campo de entrada de palavra
    entrada_descricao.delete(0, tk.END)  # Limpa o campo de entrada de descrição

    
def buscar_palavra():  # Define uma função chamada buscar_palavra
    global raiz  # Declara que a variável raiz é global, permitindo que seja acessada dentro da função
    chave = entrada_palavra.get()  # Obtém o texto da entrada de palavra
    valor = buscar(raiz, chave)  # Chama a função buscar para encontrar a palavra na árvore
    if valor:  # Se a função buscar retornou um valor (indicando que a palavra foi encontrada)
        messagebox.showinfo("Resultado", f"{chave} - {valor}")  # Mostra uma caixa de mensagem informando o resultado da busca
    else:  # Se a função buscar não retornou um valor (indicando que a palavra não foi encontrada)
        messagebox.showinfo("Resultado", f"Palavra '{chave}' não encontrada!")  # Mostra uma caixa de mensagem informando que a palavra não foi encontrada


def remover_palavra():  # Define uma função chamada remover_palavra
    global raiz  # Declara que a variável raiz é global, permitindo que seja acessada dentro da função
    chave = entrada_palavra.get()  # Obtém o texto da entrada de palavra
    raiz = remover(raiz, chave)  # Chama a função remover para remover a palavra da árvore
    entrada_palavra.delete(0, tk.END)  # Limpa o campo de entrada de palavra
    messagebox.showinfo("Sucesso", f"Palavra '{chave}' removida com sucesso.")  # Mostra uma caixa de mensagem informando que a palavra foi removida com sucesso


def ler_arquivo_json():  # Define uma função chamada ler_arquivo_json
    global raiz  # Declara que a variável raiz é global, permitindo que seja acessada dentro da função
    try:  # Começa um bloco try para capturar exceções
        with open('palavras.json', 'r', encoding='utf-8') as arquivo:  # Abre o arquivo 'palavras.json' para leitura
            dados = json.load(arquivo)  # Carrega o conteúdo do arquivo JSON em uma estrutura de dados Python
            pares_chave_valor = list(dados.items())  # Converte os dados em uma lista de pares chave-valor
            random.shuffle(pares_chave_valor)  # Embaralha os pares chave-valor
            for chave, valor in pares_chave_valor:  # Itera sobre cada par chave-valor
                raiz = inserir(raiz, chave, valor)  # Insere o par chave-valor na árvore
        messagebox.showinfo("Sucesso", "Arquivo JSON lido e dados adicionados à árvore.")  # Exibe uma mensagem de sucesso
    except FileNotFoundError:  # Captura a exceção FileNotFoundError
        messagebox.showerror("Erro", "Arquivo 'palavras.json' não encontrado.")  # Exibe uma mensagem de erro
    except json.JSONDecodeError:  # Captura a exceção json.JSONDecodeError
        messagebox.showerror("Erro", "Erro ao decodificar o arquivo JSON.")  # Exibe uma mensagem de erro

        
def apresentar_pre_ordem(raiz, apresentacao_arvore):
    if raiz is not None:
        print(raiz.chave, raiz.valor)  # Visita o nó atual, e imprime
        apresentacao_arvore.insert("",tk.END, text="1", values=(f"{raiz.chave}",f"{raiz.valor}")) # Insere o valor atual no campo treeview do tkinter
        apresentar_pre_ordem(raiz.esquerdo, apresentacao_arvore)  # Visita o filho à esquerda
        apresentar_pre_ordem(raiz.direito, apresentacao_arvore)  # Visita o filho à direita

def apresentar_em_ordem(raiz, apresentacao_arvore):
    if raiz is not None:
        apresentar_em_ordem(raiz.esquerdo, apresentacao_arvore)  # Visita o filho à esquerda
        print(raiz.chave, raiz.valor)  # Visita o nó atual, e imprime
        apresentacao_arvore.insert("",tk.END, text="1", values=(f"{raiz.chave}",f"{raiz.valor}")) # Insere o valor atual no campo treeview do tkinter
        apresentar_em_ordem(raiz.direito, apresentacao_arvore)  # Visita o filho à direita

def apresentar_pos_ordem(raiz, apresentacao_arvore):
    if raiz is not None:
        apresentar_pos_ordem(raiz.esquerdo, apresentacao_arvore)  # Visita o filho à esquerda
        apresentar_pos_ordem(raiz.direito, apresentacao_arvore)  # Visita o filho à direita
        apresentacao_arvore.insert("",tk.END, text="1", values=(f"{raiz.chave}",f"{raiz.valor}")) # Insere o valor atual no campo treeview do tkinter
        print(raiz.chave, "-", raiz.valor)  # Visita o nó atual, e imprime
        
def in_ordem():
    clear_treeview()
    apresentar_em_ordem(raiz, tree)

def post_ordem():
    clear_treeview()
    apresentar_pos_ordem(raiz, tree)
    
def pre_ordem():
    clear_treeview()
    apresentar_pre_ordem(raiz, tree)
    
def clear_treeview():
    for item in tree.get_children():
        tree.delete(item)
  
# Função para exibir a imagem da árvore na janela
def exibir_imagem_arvore():
    imagem = Image.open("arvore.png")  # Abre a imagem da árvore
    imagem = imagem.resize((300, 300), Image.ANTIALIAS)  # Redimensiona a imagem para 300x300 pixels
    imagem = ImageTk.PhotoImage(imagem)  # Converte a imagem para um formato compatível com Tkinter
    # label_imagem.config(image=imagem)  # Configura o widget label_imagem para exibir a imagem
    # label_imagem.image = imagem  # Armazena a imagem para evitar que ela seja descartada


# Função para criar a imagem da árvore
def criar_imagem_arvore(raiz, nome_arquivo):
    dot = graphviz.Digraph(comment='Árvore Binária de Busca')  # Cria um novo objeto Digraph
    preordenacao(raiz, dot)  # Adiciona os nós e arestas à árvore usando a função preordenacao
    dot.render(nome_arquivo, view=True)  # Renderiza a árvore como uma imagem e abre a imagem no visualizador padrão

    
# Função para exibir a árvore quando o botão "Mostrar Árvore" for clicado
def mostrar_arvore():
    criar_imagem_arvore(raiz, "arvore.png")  # Cria uma imagem da árvore e salva como "arvore.png"
    exibir_imagem_arvore()  # Exibe a imagem da árvore na GUI


# Cria uma janela com um tema moderno
janela = ThemedTk(theme="winxpblue")  # "arc" é um tema moderno disponível no ttkthemes

# Define o título da janela
janela.title("Busca em Árvore Binária")

# Define o tamanho inicial da janela
janela.geometry("1200x720")
janela.state('zoomed')
janela.configure(background='#ece9d8')


# Cria um widget Label com um título e o adiciona à janela
label_titulo = ttk.Label(janela, text="Busca em Árvore Binária", font=("Helvetica", 16))
label_titulo.pack(pady=10)

# Cria um botão para mostrar a árvore e o adiciona à janela
botao_mostrar_arvore = ttk.Button(janela, text="Mostrar Árvore", command=mostrar_arvore)
botao_mostrar_arvore.pack(pady=20)

# Cria um widget Label para o rodapé da janela com informações de crédito
label_rodape = ttk.Label(janela, text="Desenvolvido por JhonHR, Ayalon Dutra, Hiago Ribeiro e Matheus Moreira", foreground="#666", font=("Helvetica", 8))
label_rodape.pack(side=tk.BOTTOM, pady=10)

# Titulo do widgt de Entradas de Valores
label_titulo_entradas = ttk.Label(janela, text="Inserção de Valores", font=("Helvetica", 12))
label_titulo_entradas.pack(pady=10)

# Cria um widget para separar os campos de inserção de valores
frame_entradas = ttk.Frame(janela)
frame_entradas.pack(pady=20)

# Cria um widget Label para a entrada de palavras e o adiciona à janela
tk.Label(frame_entradas, text="Palavra", background='#ece9d8').grid(row=0, column=0, padx=5, pady=5, sticky="w")
entrada_palavra = tk.Entry(frame_entradas)
entrada_palavra.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Cria um widget Label para a entrada de descrições e o adiciona à janela
tk.Label(frame_entradas, text="Descrição", background='#ece9d8').grid(row=1, column=0, padx=5, pady=5, sticky="w")
entrada_descricao = tk.Entry(frame_entradas)
entrada_descricao.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Titulo do widgt de botões de ações
label_titulo_botoes = ttk.Label(janela, text="Ações", font=("Helvetica", 12))
label_titulo_botoes.pack(pady=10)

# Cria um widget para separar os botões de ações da janela
frame_botao = ttk.Frame(janela)
frame_botao.pack(pady=20)

# Cria um botão para inserir palavras na árvore e o adiciona à janela
botao_inserir = ttk.Button(frame_botao, text="Inserir", command=inserir_palavra)
botao_inserir.grid(row=0, column=0, padx=5, pady=5)

# Cria um botão para buscar palavras na árvore e o adiciona à janela
botao_buscar = ttk.Button(frame_botao, text="Buscar", command=buscar_palavra)
botao_buscar.grid(row=0, column=1, padx=5, pady=5)

# Cria um botão para remover palavras da árvore e o adiciona à janela
botao_remover = ttk.Button(frame_botao, text="Remover", command=remover_palavra)
botao_remover.grid(row=1, column=0, padx=5, pady=5)


# Cria um botão para ler um arquivo JSON e adicionar palavras à árvore e o adiciona à janela
botao_ler_json = ttk.Button(frame_botao, text="Ler JSON", command=ler_arquivo_json)
botao_ler_json.grid(row=1, column=1, padx=5, pady=5)


# Titulo do widgt de botões de apresentação
label_titulo_apresentacao = ttk.Label(janela, text="Apresentar Árvore", font=("Helvetica", 12))
label_titulo_apresentacao.pack(pady=10)


# Cria um widget para os botões de apresentação da arvore
frame_opcoes = ttk.Frame(janela)
frame_opcoes.pack(pady=20)

# Botão que aciona a função de apresentação em ordem
botao_em_ordem = ttk.Button(frame_opcoes, text="Em ordem", command=in_ordem)
botao_em_ordem.grid(row=0, column=0, padx=5, pady=5)

# Botão que aciona a função de apresentação em pos ordem
botao_post_ordem = ttk.Button(frame_opcoes, text="Pos ordem", command=post_ordem)
botao_post_ordem.grid(row=0, column=1, padx=5, pady=5)

# Botão que aciona a função de apresentação em pre ordem
botao_pre_ordem = ttk.Button(frame_opcoes, text="Pre ordem", command=pre_ordem)
botao_pre_ordem.grid(row=1, column=0, padx=5, pady=5)

# Widget para listar a arvore quando algum dos botões de apresentação forem pressionados
frame_arvore = ttk.Frame(janela)
frame_arvore.pack(pady=0)

tree = ttk.Treeview(frame_arvore, columns=('Palavra', 'Descrição'), show='headings')
tree.heading('Palavra', text='Palavra')
tree.heading('Descrição', text='Descrição')
tree.pack(fill=tk.BOTH, expand=True)

# apresentacao_arvore = scrolledtext.ScrolledText(janela, width=100, height=50, wrap=tk.WORD)
# apresentacao_arvore.pack()

# # Cria um widget Label para exibir a imagem da árvore e o adiciona à janela
# label_imagem = ttk.Label(janela)
# label_imagem.pack()

# Inicia o loop principal da GUI, mantendo a janela aberta até que o usuário a feche manualmente
janela.mainloop() 
