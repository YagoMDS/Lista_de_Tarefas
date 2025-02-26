<h1>Lista de Tarefas com Desfazer e Refazer</h1>

### Descrição

Este é um programa desenvolvido em Python que permite gerenciar uma lista de tarefas com funcionalidades de adicionar, listar, desfazer e refazer tarefas. A interface gráfica foi criada utilizando Tkinter e a biblioteca ttkbootstrap para um design moderno.

### Funcionalidades

+ Adicionar tarefa: Insere uma nova tarefa na lista.

+ Listar tarefas: Exibe todas as tarefas cadastradas.

+ Desfazer: Remove a última tarefa adicionada.

+ Refazer: Restaura a última tarefa removida.

+ Salvar e carregar tarefas: As tarefas são salvas em um arquivo JSON para persistência.

+ Interface gráfica: Criada com Tkinter e ttkbootstrap.

### Tecnologias Utilizadas

Python

Tkinter

ttkbootstrap

JSON para armazenamento

### Instalação

Clone este repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git

Instale as dependências necessárias:

pip install ttkbootstrap

Execute o programa:

python seu_arquivo.py

### Como Usar

Abra o programa.

Digite uma tarefa no campo de entrada e clique em "Incluir".

Para visualizar as tarefas, clique em "Listar Tarefas".

Utilize "Desfazer" para remover a última tarefa adicionada.

Utilize "Refazer" para restaurar uma tarefa removida.

Clique em "Sair" para fechar o programa.

### Estrutura do Código

O programa é dividido em:

Funções para manipulação das tarefas:

incluir(tarefa, lista): Adiciona uma nova tarefa.

listar(lista): Lista todas as tarefas.

desfazer(lista): Remove a última tarefa.

refazer(lista, listacopia): Restaura a última tarefa removida.

ler(caminho_arquivo): Carrega tarefas do arquivo JSON.

salvar(tarefas, caminho_arquivo): Salva tarefas no arquivo JSON.

Interface Gráfica:

Criada com Tkinter e ttkbootstrap.

Botões para interagir com as tarefas.

Listbox para exibir tarefas.

### Autor

Desenvolvido por [Seu Nome].