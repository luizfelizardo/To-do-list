const taskInput = document.getElementById("taskInput");
const addTaskButton = document.getElementById("addTaskButton");
const taskList = document.getElementById("taskList");
const tasks = new Set(); // Conjunto para armazenar as tarefas

addTaskButton.addEventListener("click", addTask);

function addTask() {
  const taskText = taskInput.value.trim();

  if (taskText === "") {
    alert("Por favor, digite uma tarefa!");
    return;
  }

  // Verifica se a tarefa já está no conjunto
  if (tasks.has(taskText)) {
    alert("Essa tarefa já está na lista!");
    return;
  }

  const li = document.createElement("li");
  li.innerHTML = `<span>${taskText}</span><button>Remover</button>`;
  taskList.appendChild(li);
  taskInput.value = "";

  const removeButton = li.querySelector("button");
  removeButton.addEventListener("click", removeTask);

  tasks.add(taskText); // Adiciona a tarefa ao conjunto
}

function removeTask(event) {
  const li = event.target.parentNode;
  const taskText = li.querySelector("span").textContent;
  taskList.removeChild(li);
  tasks.delete(taskText); // Remove a tarefa do conjunto
}