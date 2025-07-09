
document.addEventListener("DOMContentLoaded", () => {
    const cards = [
        {
            name: "Иван",
            username: "@vanok",
            city: "Москва",
            play: "Идеальный мужчина",
            time: "20:00",
            meet_time: "17:30"
        },
        {
            name: "Артём",
            username: "@artemka",
            city: "Санкт-Петербург",
            play: "Комедия ошибок",
            time: "19:00",
            meet_time: "16:30"
        }
    ];

    const container = document.getElementById("cardsContainer");

    cards.forEach((card, index) => {
        const div = document.createElement("div");
        div.className = "card";
        div.innerHTML = `
            <strong>👤 ${card.name} (${card.username})</strong><br>
            🏙️ Город: ${card.city}<br>
            🎭 Спектакль: ${card.play}<br>
            🕒 Встреча: ${card.meet_time}, спектакль: ${card.time}<br><br>
            <button onclick="handleAction('${card.name}', 'Ссылка')">Ссылка на спектакль</button>
            <button onclick="handleAction('${card.name}', 'Купил')">Купил</button>
            <button onclick="handleAction('${card.name}', 'Возврат 1')">Сделал 1 возврат</button>
            <button onclick="handleAction('${card.name}', 'Возврат 2')">Сделал 2 возврат</button>
            <button onclick="handleAction('${card.name}', 'Возврат 3')">Сделал 3 возврат</button>
            <button onclick="handleAction('${card.name}', 'Написал в поддержку')">Написал в поддержку</button>
            <hr>
        `;
        container.appendChild(div);
    });
});

function handleAction(name, action) {
    console.log(`➡️ Действие: ${action} — для ${name}`);
}

function sendManualCommand() {
    const command = document.getElementById('manualCommand').value;
    console.log("📌 Команда вручную:", command);
}

function sendBotAnswer() {
    const answer = document.getElementById('botQuestion').value;
    console.log("🧠 Ответ от бота:", answer);
}
