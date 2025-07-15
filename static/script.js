
setInterval(() => {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            renderRequests(data.requests);
        });
}, 5000);

function renderRequests(requests) {
    const container = document.getElementById("requests-container");
    container.innerHTML = "";

    requests.forEach(req => {
        const card = document.createElement("div");
        card.classList.add("request-card");

        card.innerHTML = `
            <h3>${req.name} (${req.city})</h3>
            <p><a href="${req.profile}" target="_blank">Открыть профиль</a></p>

            <div class="field">
                <label>Ссылка на спектакль</label>
                <input type="text" id="link-${req.id}" value="${req.link || ''}">
                <button onclick="sendField('${req.id}','link')">Отправить</button>
                <span class="status">${req.link_sent ? '✅' : ''}</span>
            </div>

            <div class="field">
                <label>Выбор мест</label>
                <input type="text" id="seats-${req.id}" value="${req.seats || ''}">
                <button onclick="sendField('${req.id}','seats')">Отправить</button>
                <span class="status">${req.seats_sent ? '✅' : ''}</span>
            </div>

            <div class="field">
                <label>Прикрепить билет</label>
                <input type="file" id="ticket-${req.id}">
                <button onclick="sendTicket('${req.id}')">Отправить</button>
                <span class="status">${req.ticket_sent ? '✅' : ''}</span>
            </div>

            <div class="field">
                <label>Номер карты</label>
                <input type="text" id="card-${req.id}" value="${req.card || ''}">
                <button onclick="sendField('${req.id}','card')">Отправить</button>
                <span class="status">${req.card_sent ? '✅' : ''}</span>
            </div>

            <div class="actions">
                <button class="action-btn buy" onclick="sendAction('${req.id}','Купил')">Купил</button>
                <button class="action-btn support" onclick="sendAction('${req.id}','Написал в поддержку')">Поддержка</button>
                <button class="action-btn return" onclick="sendAction('${req.id}','Возврат 1')">Возврат 1</button>
                <button class="action-btn return" onclick="sendAction('${req.id}','Возврат 2')">Возврат 2</button>
                <button class="action-btn return" onclick="sendAction('${req.id}','Возврат 3')">Возврат 3</button>
                <button class="action-btn return" onclick="sendAction('${req.id}','Возврат 4')">Возврат 4</button>
                <button class="action-btn return" onclick="sendAction('${req.id}','Возврат 5')">Возврат 5</button>
                <button class="action-btn return" onclick="sendAction('${req.id}','Возврат 6')">Возврат 6</button>
                <button class="action-btn delete" onclick="sendAction('${req.id}','Удалить анкету')">Удалить анкету</button>
            </div>
        `;

        container.appendChild(card);
    });
}

function sendField(id, field) {
    const value = document.getElementById(`${field}-${id}`).value;
    fetch('/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `username=${id}&message=${field}:${value}`
    });
    alert(`Отправлено: ${field}`);
}

function sendTicket(id) {
    const fileInput = document.getElementById(`ticket-${id}`);
    const file = fileInput.files[0];
    if (!file) return alert("Выберите файл!");

    const formData = new FormData();
    formData.append("file", file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    }).then(() => alert("Билет отправлен! ✅"));
}

function sendAction(id, actionType) {
    fetch('/action', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `profile_id=${id}&action_type=${actionType}`
    }).then(() => alert(`Действие: ${actionType}`));
}

function sendCommand() {
    const cmd = document.getElementById("bot-command").value;
    fetch('/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `username=manual&message=${cmd}`
    }).then(() => document.getElementById("cmd-status").textContent = '✅');
}

function sendQuestion() {
    const qst = document.getElementById("bot-question").value;
    fetch('/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `username=manual&message=${qst}`
    }).then(() => document.getElementById("qst-status").textContent = '✅');
}
