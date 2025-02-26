<h1>Lista de Tarefas com Desfazer e Refazer</h1>

### Descrição

Este é um programa desenvolvido em Python que permite gerenciar uma lista de tarefas com funcionalidades de adicionar, listar, desfazer e refazer tarefas. A interface gráfica foi criada utilizando Tkinter e a biblioteca ttkbootstrap para um design moderno.

### Funcionalidades

+ <b>Adicionar tarefa:</b> Insere uma nova tarefa na lista.

+ <b>Listar tarefas:</b> Exibe todas as tarefas cadastradas.

+ <b>Desfazer:</b> Remove a última tarefa adicionada.

+ <b>Refazer:</b> Restaura a última tarefa removida.

+ <b>Salvar e carregar tarefas:</b> As tarefas são salvas em um arquivo JSON para persistência.

+ <b>Interface gráfica:</b> Criada com Tkinter e ttkbootstrap.

### Tecnologias Utilizadas

+ Python

+ Tkinter

+ ttkbootstrap

+ JSON para armazenamento

### Instalação

<ol>
<li>Clone este repositório:</li>

git clone https://github.com/seu-usuario/seu-repositorio.git

<li>Instale as dependências necessárias:</li>

pip install ttkbootstrap

<li>Execute o programa:</li>

python seu_arquivo.py
</ol>

### Como Usar
![Image](https://github.com/user-attachments/assets/f344d3b2-0217-47f6-ab42-29691289c8c1)
<ol>
<li>Abra o programa.</li>

<li>Digite uma tarefa no campo de entrada e clique em "Incluir".</li>

<li>Para visualizar as tarefas, clique em "Listar Tarefas".</li>

<li>Utilize "Desfazer" para remover a última tarefa adicionada.</li>

<li>Utilize "Refazer" para restaurar uma tarefa removida.</li>

<li>Clique em "Sair" para fechar o programa.</li>
</ol>

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
