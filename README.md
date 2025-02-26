<h1>Lista de Tarefas com Interface Gráfica</h1>

### 📌Descrição

Este é um aplicativo de lista de tarefas desenvolvido em Python, utilizando tkinter e ttkbootstrap para a interface gráfica. O programa permite que o usuário adicione, liste, desfaça e refaça tarefas, além de salvar e carregar tarefas de um arquivo JSON.

### 🚀Funcionalidades

+ <b>✅ Adicionar tarefa:</b> Insere uma nova tarefa na lista.

+ <b>📋 Listar tarefas:</b> Exibe todas as tarefas cadastradas.

+ <b>🔙 Desfazer:</b> Remove a última tarefa adicionada.

+ <b>🔄 Refazer:</b> Restaura a última tarefa removida.

+ <b>💾 Salvar e carregar tarefas:</b> As tarefas são salvas em um arquivo JSON para persistência.

+ <b>🎨 Interface gráfica:</b> Criada com Tkinter e ttkbootstrap.

### 🛠️Tecnologias Utilizadas

+ Python

+ Tkinter

+ ttkbootstrap

+ JSON (para armazenamento de dados)    

### 📥Instalação

<ol>
<li>Clone este repositório:</li>

git clone https://github.com/YagoMDS/Lista_de_Tarefas.git

<li>Crie um ambiente virtual:</li>
python -m venv venv
venv\Scripts\Activate

<li>Instale as dependências necessárias:</li>

pip install -r requirements.txt

<li>Execute o programa:</li>

python Lista_App.py
</ol>

### ▶️ Como Usar

<ol>
<li>Abra o programa.</li>

<li>Digite uma tarefa no campo de entrada e clique em "Incluir".</li>

<li>Para visualizar as tarefas, clique em "Listar Tarefas".</li>

<li>Utilize "Desfazer" para remover a última tarefa adicionada.</li>

<li>Utilize "Refazer" para restaurar uma tarefa removida.</li>

<li>Clique em "Sair" para fechar o programa.</li>
</ol>

![Image](https://github.com/user-attachments/assets/f344d3b2-0217-47f6-ab42-29691289c8c1)

### 📁 Estrutura do Código

O programa é dividido em:

#### Funções para manipulação das tarefas:

+ incluir(tarefa, lista): Adiciona uma nova tarefa.

+ listar(lista): Lista todas as tarefas.

+ desfazer(lista): Remove a última tarefa.

+ refazer(lista, listacopia): Restaura a última tarefa removida.

+ ler(caminho_arquivo): Carrega tarefas do arquivo JSON.

+ salvar(tarefas, caminho_arquivo): Salva tarefas no arquivo JSON.

#### Interface Gráfica:

+ Criada com Tkinter e ttkbootstrap.

+ Botões para interagir com as tarefas.

+ Listbox para exibir tarefas.

### 🤝 Contribuição

<ol>
Se desejar contribuir com melhorias, siga os passos:

<br><li>Fork este repositório.</li>

<li>Crie um branch para sua funcionalidade <strong>git checkout -b minha-melhoria</strong>.</li>

<li>Comite suas mudanças (**git commit -m 'Adicionando uma nova funcionalidade'**).</li>

<li>Envie para o branch principal (**git push origin minha-melhoria**).</li>

<li>Abra um Pull Request.</li>
</ol>

### 👨‍💻 Autor

Desenvolvido por Yago Magalhães da Silva.

LinkedIn: https://www.linkedin.com/in/yago-magalhaes-silva/

GitHub: https://github.com/YagoMDS


