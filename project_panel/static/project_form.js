document.addEventListener('DOMContentLoaded', function () {

    let taskList = [];

    document.querySelector('#submit_task').disabled = true;

    document.querySelector('#input_task').onkeyup = function() {
        if (document.querySelector('#input_task').value.length > 0) {
            document.querySelector('#submit_task').disabled = false;
        }
        else {
            document.querySelector('#submit_task').disabled = true;
        }
    }

    document.querySelector('#submit_task').onclick = function () {
        let task = document.querySelector('#input_task').value;

        taskList.push(task);

        let li = document.createElement('li');
        li.classList.add("to_do");
        li.innerHTML = task;

        let new_input_task = document.createElement('input');
        new_input_task.setAttribute('type', 'hidden');
        new_input_task.setAttribute('value', task);
        new_input_task.setAttribute('name', ('task'+task));

        document.querySelector('#main_form').append(new_input_task);

        document.querySelector('#task_list').append(li);

        document.querySelector('#input_task').value = "";
        document.querySelector('#submit_task').disabled = true;

        return false;
    }
});