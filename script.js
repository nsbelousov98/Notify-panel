
let users = JSON.parse(localStorage.getItem("users") || "[]");

if (!localStorage.getItem("linkRequestInjected")) {
    users.push({
        name: "@aleksey_msk",
        city: "Москва",
        link: "",
        date: "7 июля, 20:00 — Запросил ссылку на спектакль",
        marks: {}
    });
    localStorage.setItem("linkRequestInjected", "true");
    localStorage.setItem("users", JSON.stringify(users));
}

function saveUsers() {
    localStorage.setItem("users", JSON.stringify(users));
}

function toggleMark(userIndex, action) {
    const user = users[userIndex];
    if (!user.marks) user.marks = {};
    user.marks[action] = !user.marks[action];
    saveUsers();
    renderUsers();
}

function renderUsers() {
    const container = document.getElementById("user-cards");
    container.innerHTML = "";
    users.forEach((user, index) => {
        const div = document.createElement("div");
        div.className = "user-card";
        const isLink = user.link && user.link.trim().length > 0;
        div.innerHTML = `
            <b>👤 ${user.name}</b><br>
            📍 ${user.city}<br>
            🎫 ${
                isLink
                    ? `<a href="${user.link}" target="_blank">Спектакль</a>`
                    : `<span style="color:red;">❗ Запросил ссылку на спектакль</span>`
            }<br>
            🕓 ${user.date}<br><br>
            <div class="actions">
                ${["Купил", "Написал в поддержку", "Сделал 1 возврат", "Сделал 2 возврата", "Сделал 3 возврат", "Сделал 4 возврата", "Сделал 5 возвратов", "Сделал 6 возвратов", "Не звать никого 30 мин"].map(action => {
                    const checked = user.marks && user.marks[action];
                    return `
                        <div class="mark-item">
                            <button onclick="mark(${index}, '${action}')">${action}</button>
                            <div class="checkbox ${checked ? 'checked' : ''}" onclick="toggleMark(${index}, '${action}')">${checked ? '✓' : ''}</div>
                        </div>
                    `;
                }).join("")}
            </div>
        `;
        container.appendChild(div);
    });
}

function mark(index, action) {
    alert("Отметка для " + users[index].name + ": " + action);
}

renderUsers();
