async function SendData() {

	let rus = document.getElementById('rus').value;
	let eng = document.getElementById('eng').value;
	let url = document.getElementById('form').action;
	let csrf = document.querySelector('[name="csrfmiddlewaretoken"]').value;

	let headers = {
		'X-Requested-With': 'XMLHttpRequest',
		'Content-Type':  'application/json',
		'X-CSRFToken': csrf,
		}

	let data = {
				method: 'POST',
				headers: headers,
				body: JSON.stringify({'name_rus': rus, 'name_eng': eng}),
				};

	response = await fetch(url, data);
	renderAnswer(response.status);
}

function renderAnswer(status){
	if (status == 200){
		let form_element = document.getElementById('form');
		let div = document.createElement('div');
		div.className = 'success';
		div.innerHTML = 'Cлова успешно добавлены в ваш словарь';
		form_element.append(div);

		setTimeout(removeElement, 2000);
		function removeElement() {
			div.remove();
		}
	}

	else{
		let form_element = document.getElementById('form');
		let div = document.createElement('div');
		div.className = 'error';
		div.innerHTML = 'Возникла ошибка при добавлении слов в словарь';
		form_element.append(div);

		setTimeout(removeElement, 2000);
		function removeElement() {
			div.remove();
		}
	}
}



const button = document.getElementById('button');
button.addEventListener("click", SendData);


