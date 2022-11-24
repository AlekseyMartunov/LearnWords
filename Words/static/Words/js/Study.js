async function getResponce() {
	
	let csrf = document.querySelector('[name="csrfmiddlewaretoken"]').value;
	let language = document.querySelector('input[name="language"]:checked').value;
	
	let headers = {
		'X-Requested-With': 'XMLHttpRequest',
		'Content-Type':  'application/json',
		'X-CSRFToken': csrf,
		}

	let responce = await fetch('/study/', {
		method: 'POST',
		headers: headers,
		body: JSON.stringify({'language': language}),
		});

	let data = await responce.json();
	return data	
}

function renderQuestion(global_queryset){
	queryset = global_queryset[current_index];

	document.querySelectorAll('.element_answer').forEach(e => e.remove());

	let question_text = document.getElementById('question_text');
	question_text.innerHTML = 'Выберите правильный перевод слова '+ queryset["question"] + ':';

	let answers = queryset['answers']

	for (let i = 0; i<4; i++){
			let new_div = document.createElement('div');
			new_div.innerHTML = answers[i];
			new_div.onclick = get_result;
			new_div.className = 'element_answer';
			question_text.append(new_div);
			
		}
	let progres_bar = document.createElement('div');
	progres_bar.innerHTML = `Вопрос ${current_index+1} из ${global_queryset.length}`;
	progres_bar.className = 'progresBar';
	question_text.append(progres_bar);

}

function get_result(){
	let queryset = global_queryset[current_index];
	let pk = queryset['pk'];
	
	if (event.target.innerHTML == queryset['correct']){
		results[pk] = true
		event.target.style.backgroundColor = '#56e123'; 

	}
	else{
		event.target.style.backgroundColor = 'red';
		results[pk] = false
	}
	current_index += 1;
	if (global_queryset[current_index] == undefined){
			renderEnd();
		}
	else{
			setTimeout(()=>{
			renderQuestion(global_queryset);
			}, 150);
		}
	}




 function renderEnd(){
 	document.querySelectorAll('.element_answer').forEach(e => e.remove());
 	
 	let correctAnswers = 0;

	for (let key in results){
		if (results[key]) { correctAnswers+=1 }	;	
	}

	let question_text = document.getElementById('question_text');
	question_text.innerHTML = `Вы ответели на все вопросы. Правильных ответов: ${correctAnswers}.`;
	sendResults(); 
 }

 async function sendResults(){
 	let csrf = document.querySelector('[name="csrfmiddlewaretoken"]').value;
	let headers = {
		'X-Requested-With': 'XMLHttpRequest',
		'Content-Type':  'application/json',
		'X-CSRFToken': csrf,
		}

	fetch('/study/', {
		method: 'POST',
		headers: headers,
		body: JSON.stringify({'results': results}),
		});

	results = {};
	current_index = 0;

 }



async function start(){
	global_queryset = await getResponce();
	renderQuestion(global_queryset);
}

let current_index = 0;
let results = {};
let button = document.getElementById('button');
button.addEventListener('click', start);