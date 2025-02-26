# Lista de Tarefas com Strings
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import copy
import json
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

import tkinter as tk
from tkinter import messagebox


# Inclui uma nova tarefa na lista 
def incluir(tarefa, lista = None):

    if lista is None:
        lista = []

    tarefa = tarefa.strip()

    if not tarefa:
        messagebox.showwarning("Aviso", "Você não digitou uma tarefa.")
        return lista
    
    lista.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

    return lista


# Lista as tarefas existentes 
def listar(lista = None):

    if lista is None:
        lista = []

    # Verifica se a lista está vazia 
    if not lista:
        messagebox.showinfo("Informação", "Não exitem tarefas a serem listadas")
        return lista

    print(f"\n\tTAREFAS\n")
    for i, tarefa in enumerate(lista, 1):
        print(f"{i}. {tarefa}")

    return lista


# Desfaz uma a última tarefa 
def desfazer(lista = None):
    if lista is None:
        lista = []

    # Verificação se a lista está vazia pelo tamanho 
    if len(lista) > 0:
        lista.pop()
        listar(lista)
    else:
        messagebox.showinfo("Informação", "Não há itens para desfazer.")
    
    return lista


# Refazer a última tarefa desfeita 
def refazer(lista = None, listacopia = None):
   # Inicializa as listas corretamente, se não forem passadas como argumento
    if lista is None:
        lista = []
    if listacopia is None:
        listacopia = []

    # Verifica se há algo para refazer
    if not listacopia or len(lista) >= len(listacopia):
        messagebox.showinfo("Informação", "Não existe uma tarefa a ser refeita.")
        return lista, listacopia

    # Adiciona o próximo item de listacopia a lista
    lista.append(listacopia[len(lista)])
    listar(lista)
    return lista


def ler(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding='utf8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado, criando um novo arquivo de tarefas.")
    return []


def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, "w", encoding="utf8") as arquivo:
        json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)


def main():

    CAMINHO_ARQUIVO = 'lista_de_tarefas.json'

    tarefas = ler(CAMINHO_ARQUIVO)
    lista_copia = []

    # Inicializa a janela principal do Tkinter
    root = tk.Tk()
    root.title("Agenda de Tarefas")
    root.geometry("510x500")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(2, weight=1)
    style = Style(theme="superhero")

    frame_topo = ttk.Frame(root)
    frame_topo.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
    frame_topo.columnconfigure(0, weight=1)

    entry_tarefa = ttk.Entry(frame_topo)
    entry_tarefa.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    botao_adicionar = ttk.Button(frame_topo, text="Incluir", command=lambda: adicionar_tarefa())
    botao_adicionar.grid(row=0, column=1, padx=5, pady=5)

    frame_botoes = ttk.Frame(root)
    frame_botoes.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
    frame_botoes.columnconfigure((0, 1, 2, 3, 4), weight=1)

    botao_desfazer = ttk.Button(frame_botoes, text="Desfazer", command=lambda: desfazer_tarefa())
    botao_desfazer.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    botao_refazer = ttk.Button(frame_botoes, text="Refazer", command=lambda: refazer_tarefa())
    botao_refazer.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    botao_listar = ttk.Button(frame_botoes, text="Listar Tarefas", command=lambda: listar_tarefas())
    botao_listar.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

    botao_sair = ttk.Button(frame_botoes, text="Sair", command=lambda: sair())
    botao_sair.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

    listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 10))
    listbox.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

    # Função para atualizar a lista de tarefas na interface
    def atualizar_lista():
        texto = listar(tarefas)
        listbox.delete(0, tk.END)  # Limpa a Listbox
        if texto:
            for i, tarefa in enumerate(texto, start=1):
                listbox.insert(tk.END, f"{i} - {tarefa}")  # Adiciona as tarefas à Listbox

    # Função chamada quando o botão "Adicionar" é clicado
    def adicionar_tarefa():
        tarefa = entry_tarefa.get()
        if tarefa:
            nonlocal tarefas, lista_copia
            tarefas = incluir(tarefa, tarefas)
            lista_copia = copy.deepcopy(tarefas)
            salvar(tarefas, CAMINHO_ARQUIVO)
            entry_tarefa.delete(0, tk.END)  # Limpa o campo de entrada
            atualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Digite uma tarefa para adicionar.")

    # Função chamada quando o botão "Desfazer" é clicado
    def desfazer_tarefa():
        nonlocal tarefas
        desfazer(tarefas)
        salvar(tarefas, CAMINHO_ARQUIVO)
        atualizar_lista()

    # Função chamada quando o botão "Refazer" é clicado
    def refazer_tarefa():
        nonlocal tarefas, lista_copia
        refazer(tarefas, lista_copia)
        salvar(tarefas, CAMINHO_ARQUIVO)
        atualizar_lista()

    # Função chamada quando o botão "Listar" é clicado
    def listar_tarefas():
        tarefas_texto = listar(tarefas)
        tarefas_formatadas = "\n".join(f"{i+1}. {tarefa}" for i, tarefa in enumerate(tarefas_texto))

        # Exibir a lista formatada em uma messagebox
        messagebox.showinfo("Tarefas", tarefas_formatadas)


    # Função para sair da aplicação
    def sair():
        resposta = messagebox.askyesno("Confirmar saída", "Você tem certeza que deseja sair?")
        if resposta:
            root.quit()  # Fecha a janela e encerra o programa

    # Botões para ações
    # botao_adicionar = tk.Button(root, text="Incluir", command=adicionar_tarefa)
    # botao_adicionar.grid(row=0, column=1, padx=1, pady=1, sticky="w")
    
    # botao_desfazer = tk.Button(root, text="Desfazer", command=desfazer_tarefa)
    # botao_desfazer.grid(row=1, column=1, padx=1, pady=1, sticky="w")

    # botao_refazer = tk.Button(root, text="Refazer", command=refazer_tarefa)
    # botao_refazer.grid(row=1, column=2, padx=1, pady=1, sticky="w")

    # botao_listar = tk.Button(root, text="Listar Tarefas", command=listar_tarefas)
    # botao_listar.grid(row=1, column=3, padx=1, pady=1, sticky="w")

    # botao_sair = tk.Button(root, text="Sair", command=sair)  # Botão "Sair"
    # botao_sair.grid(row=1, column=4, padx=1, pady=1, sticky="w")

    
    # Inicia a interface gráfica
    root.mainloop()

if __name__ == "__main__":
    main()