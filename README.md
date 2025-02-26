<h1>Task List with Graphical Interface</h1>

### 📌 Description

This is a task list application developed in Python, using Tkinter and ttkbootstrap for the graphical interface. The program allows the user to add, list, undo, and redo tasks, as well as save and load tasks from a JSON file.

### 🚀 Features

+ <b>✅ Add Task:</b> Inserts a new task into the list.

+ <b>📋 List Tasks:</b> Displays all registered tasks.

+ <b>🔙 Undo:</b> Removes the last added task.

+ <b>🔄 Redo:</b> Restores the last removed task.

+ <b>💾 Save and Load Tasks:</b> Tasks are saved in a JSON file for persistence.

+ <b>🎨 Graphical Interface:</b> Built with Tkinter and ttkbootstrap.

### 🛠️ Technologies Used

+ Python

+ Tkinter

+ ttkbootstrap

+ JSON (for data storage)    

### 📥 Installation

<ol>
<li>Clone this repository:</li>

git clone https://github.com/YagoMDS/Lista_de_Tarefas.git

<li>Create a virtual environment:</li>
python -m venv venv
venv\Scripts\Activate

<li>Install the required dependencies:</li>

pip install -r requirements.txt

<li>Run the program:</li>

python Lista_App.py
</ol>

### ▶️ How to Use

<ol>
<li>Open the program.</li>

<li>Enter a task in the input field and click <strong>"Add"</strong>.</li>

<li>To view tasks, click <strong>"List Tasks"</strong>.</li>

<li>Use <strong>"Undo"</strong> to remove the last added task.</li>

<li>Use <strong>"Redo"</strong> to restore a removed task.</li>

<li>Click <strong>"Exit"</strong> to close the program.</li>
</ol>

![Image](https://github.com/user-attachments/assets/f344d3b2-0217-47f6-ab42-29691289c8c1)

### 📁 Code Structure

The program is divided into:

#### Functions for Task Management:

+ <strong>incluir</strong>(task, list): Adds a new task.

+ listar(list): Lists all tasks.

+ desfazer(list): Removes the last task.

+ refazer(list, list_copy): Restores the last removed task.

+ ler(file_path): Loads tasks from the JSON file.

+ salvar(tasks, file_path): Saves tasks to the JSON file.

#### Graphical Interface:

+ Built with Tkinter and ttkbootstrap.

+ Buttons to interact with tasks.

+ Listbox to display tasks.

### 🤝 Contribution

<ol>

<li>Fork this repository.</li>

<li>Create a branch for your feature <strong>(git checkout -b my-feature</strong>).</li>

<li>Commit your changes (<strong>git commit -m 'Adding a new feature'</strong>).</li>

<li>Push to the main branch <strong>(git push origin my-feature</strong>).</li>

<li>Open a Pull Request.</li>
</ol>

### 👨‍💻 Author

Developed by Yago Magalhães da Silva.

LinkedIn: https://www.linkedin.com/in/yago-magalhaes-silva/

GitHub: https://github.com/YagoMDS
