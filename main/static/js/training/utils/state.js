import { end_times, end_time_ind } from "../interactive.js";

// инициализация констант и переменных

export let is_sub = false; // куплена ли подписка

let task = window.location.href.slice(-2, -1) - 0;
if (task != 9) {
    task += 10;
}
console.log(task);

const char_amount_const = 500;

let element_completed = document.getElementById("completed"); // элемент с пройденными словами
let element_next = document.getElementById("next"); // элемент с предстоящими словами
let element_start = document.getElementById("start"); // элемент с надписью Press space to start
let element_timer = document.getElementById("timer");
element_completed.style.display = "none";
element_next.style.display = "none";

export let is_started = false;

let words_queue = []; // очередь слов
let completed = ""; // все напечатанное
let current_word = ""; // текущее напечатанное слово
let mistake_words = [];

let next_input_view = ""; // отображение следующих слов

init_words_queue().then(() => {
    console.log(words_queue);
    for (let i = 0; i < words_queue.length; i++) {
        plus_next_inp(words_queue[i]);
    }
    if (words_queue[0]["Context_Before"] != "") {
        move_context_before();
    }
    element_next.innerHTML = next_input_view.slice(0, char_amount_const);
    element_completed.innerHTML = completed;

    get_user_sub().then(() => {
        console.log(is_sub);
    });
});

let mistake_counter = 0;
let success_counter = 0;
let timer = 0; // seconds
let timerID = 0;

// вспомогательные функции

window.onload = function () {
    const select = document.getElementById("numbers-select");
    select.value = "task" + task;
};
window.onbeforeunload = function () {
    if (timer == 0 || success_counter + mistake_counter == 0) {
        return;
    }
    post_statistics();
};

function getCSRFToken() {
    return document
        .querySelector('meta[name="csrf-token"]')
        .getAttribute("content");
}

function plus_next_inp(w) {
    if (w["Context_Before"] != "") {
        next_input_view += "(";
        next_input_view += w["Context_Before"];
        next_input_view += ")";
        next_input_view += " ";
    }
    next_input_view += w["Pass"];
    next_input_view += " ";
    if (w["Context_After"] != "") {
        next_input_view += "(";
        next_input_view += w["Context_After"];
        next_input_view += ")";
        next_input_view += " ";
    }
}

function move_context_before() {
    completed += next_input_view.slice(
        0,
        words_queue[0]["Context_Before"].length + 3
    );
    completed += " ";
    next_input_view = next_input_view.slice(
        words_queue[0]["Context_Before"].length + 3
    );
}
function move_context_after() {
    completed += next_input_view.slice(
        0,
        words_queue[0]["Context_After"].length + 3
    );
    completed += " ";
    next_input_view = next_input_view.slice(
        words_queue[0]["Context_After"].length + 3
    );
}

String.prototype.toHHMMSS = function () {
    let sec_num = parseInt(this, 10);
    let hours = Math.floor(sec_num / 3600);
    let minutes = Math.floor((sec_num - hours * 3600) / 60);
    let seconds = sec_num - hours * 3600 - minutes * 60;

    if (hours < 10) {
        hours = "0" + hours;
    }
    if (minutes < 10) {
        minutes = "0" + minutes;
    }
    if (seconds < 10) {
        seconds = "0" + seconds;
    }
    return hours + ":" + minutes + ":" + seconds;
};

async function post_statistics() {
    try {
        const apiUrl =
            window.location.protocol +
            "//" +
            window.location.host +
            "/api/save_statistics";

        const response = await fetch(apiUrl, {
            method: "POST",
            credentials: "include",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken(),
            },
            body: JSON.stringify({
                time: timer,
                successes: success_counter,
                mistakes: mistake_counter,
                mistake_words: mistake_words,
            }),
        });

        if (!response.ok) {
            throw new Error("Сеть ответила с ошибкой: " + response.status);
        }

        const responseData = await response.json();
        return responseData;
    } catch (error) {
        console.error("Error:", error);
        throw error;
    }
}

function get_next_word_api() {
    return new Promise((resolve, reject) => {
        const apiUrl =
            window.location.protocol +
            "//" +
            window.location.host +
            "/api/get_random_word/" +
            task;

        const xhr = new XMLHttpRequest();
        xhr.open("GET", apiUrl, true);
        xhr.withCredentials = true;

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                // Запрос завершен
                if (xhr.status === 200) {
                    // Успешный ответ
                    try {
                        const data = JSON.parse(xhr.responseText);
                        resolve(data);
                    } catch (error) {
                        console.error("Ошибка при парсинг JSON:", error);
                        reject(error);
                    }
                } else {
                    console.error(
                        "Ошибка при получении данных:",
                        xhr.statusText
                    );
                    reject(
                        new Error(
                            "Ошибка при получении данных: " + xhr.statusText
                        )
                    );
                }
            }
        };

        xhr.send();
    });
}
async function get_next_word() {
    try {
        const result = await get_next_word_api();

        // Проверяем наличие нужных полей перед доступом
        if (result && typeof result === "object") {
            words_queue.push(result);
            return result; // Возвращаем результат
        } else {
            throw new Error("Полученные данные имеют неверную структуру");
        }
    } catch (error) {
        console.error("Ошибка:", error.message);
        throw error;
    }
}

async function init_words_queue() {
    try {
        const apiUrl =
            window.location.protocol +
            "//" +
            window.location.host +
            "/api/get_random_words/" +
            task +
            "/" +
            20;

        const response = await fetch(apiUrl, {
            method: "GET",
            credentials: "include",
        });
        if (!response.ok) {
            throw new Error("Сеть ответила с ошибкой: " + response.status);
        }
        const data = await response.json();

        // Проверяем, есть ли ключ words и массив ли он
        if (Array.isArray(data.words)) {
            words_queue = data.words; // Сохраняем массив
        } else {
            console.error('Ключ "words" отсутствует или не является массивом');
        }
    } catch (error) {
        console.error("Ошибка при получении данных:", error);
    }
}

async function get_user_sub() {
    try {
        const apiUrl =
            window.location.protocol +
            "//" +
            window.location.host +
            "/api/get_user_sub";

        const response = await fetch(apiUrl, {
            method: "GET",
            credentials: "include",
        });
        if (!response.ok) {
            throw new Error("Сеть ответила с ошибкой: " + response.status);
        }
        const data = await response.json();

        is_sub = data.sub;
    } catch (error) {
        console.error("Ошибка при получении данных:", error);
    }
}

function update_word_queue() {
    words_queue = words_queue.slice(1); // добавление новых слов в очередь
    get_next_word().then(() => {
        plus_next_inp(words_queue[words_queue.length - 1]);
    });
}

function update_next_inp_front() {
    next_input_view = next_input_view.slice(1);
}
function update_next_inp_back() {
    next_input_view =
        words_queue[0]["Pass"][current_word.length - 1] + next_input_view;
}

function slice_completed() {
    if (completed.length > char_amount_const) {
        completed = completed.slice(-char_amount_const);
    }
}
function isLetter(str) {
    return str.length === 1 && str.match(/[а-я]/i);
}

function highlight_correct() {
    let ind, len;
    ind = words_queue[0]["Pass"].indexOf(".");
    len = words_queue[0]["Pass"].length;

    if (ind == len - 1) {
        completed =
            completed.slice(0, -1) +
            "<span style='color: green'>" +
            completed.slice(-1) +
            "</span>";
        return;
    }

    completed =
        completed.slice(0, -(len - ind)) +
        "<span style='color: green'>" +
        completed.slice(-(len - ind), -(len - ind) + 1) +
        "</span>" +
        completed.slice(-(len - ind) + 1);
}
function highlight_incorrect() {
    let ind, len;
    ind = words_queue[0]["Pass"].indexOf(".");
    len = words_queue[0]["Pass"].length;

    if (ind == len - 1) {
        completed =
            completed.slice(0, -1) +
            "<span style='color: red'>" +
            completed.slice(-1) +
            "</span>";
        return;
    }

    completed =
        completed.slice(0, -(len - ind)) +
        "<span style='color: red'>" +
        completed.slice(-(len - ind), -(len - ind) + 1) +
        "</span>" +
        completed.slice(-(len - ind) + 1);
}

export function start() {
    element_start.style.display = "none";

    element_completed.style.display = "block";
    element_next.style.display = "block";

    is_started = true;

    timerID = setInterval(timer_tick, 1000);
}

function timer_tick() {
    timer++;
    element_timer.innerHTML = (timer + "").toHHMMSS();

    if (timer >= end_times[end_time_ind]) {
        clearInterval(timerID);
        window.location.href = "../../stats";
        console.log("END");
    }
}

// основные функции при вводе
export function key_backspace() {
    if (current_word.length < 1) {
        console.log("BF");
        return;
    }

    update_next_inp_back();

    completed = completed.slice(0, -1);
    current_word = current_word.slice(0, -1);

    element_next.innerHTML = next_input_view.slice(0, char_amount_const);
    element_completed.innerHTML = completed;
    return;
}

export function key_space(key) {
    if (current_word.length < words_queue[0]["Word"].length) {
        console.log("space_barrier"); // не дает перейти на следующее слово пока не написано текущее
        return;
    }

    if (current_word == words_queue[0]["Word"]) {
        console.log("Correct!");
        highlight_correct();
        success_counter++;
    } else {
        console.log("Fail!");
        highlight_incorrect();

        mistake_words.push(words_queue[0]);
        mistake_words[mistake_words.length - 1]["Mistake"] = current_word;
        mistake_counter++;
    }
    completed += key;

    if (words_queue[0]["Context_After"] != "") {
        move_context_after();
    }

    update_word_queue();

    if (words_queue[0]["Context_Before"] != "") {
        move_context_before();
    }

    console.log(words_queue); // вывод для дебага

    current_word = ""; // обновление и обнуление переменных
    slice_completed();
    element_completed.innerHTML = completed;

    update_next_inp_front();
    element_next.innerHTML = next_input_view.slice(0, char_amount_const);

    return;
}

export function input(key) {
    if (
        (key != words_queue[0]["Pass"][current_word.length] &&
            words_queue[0]["Pass"][current_word.length] != ".") ||
        (!isLetter(key) && key != ".")
    ) {
        return;
    }
    completed += key;
    current_word += key;

    slice_completed();
    element_completed.innerHTML = completed;
    update_next_inp_front();
    element_next.innerHTML = next_input_view.slice(0, char_amount_const);
    return;
}
