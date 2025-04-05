// этот код не будет робить для н и нн ((((

// инициализация констант и переменных

// init
const char_amount_const = 500;

let element_compl = document.getElementById("compl"); // элемент с пройденными словами
let element_next = document.getElementById("next"); // элемент с предстоящими словами
let element_start = document.getElementById("start"); // элемент с надписью Press space to start

element_compl.style.display = "none";
element_next.style.display = "none";

let is_started = false;

const words = [
    {
        Word: "фланелевый",
        Context_Before: "",
        Pass: "фланел.вый",
        Context_After: "",
    },
    {
        Word: "ситечко",
        Context_Before: "чайное",
        Pass: "сит.чко",
        Context_After: "",
    },
    {
        Word: "ветряная",
        Context_Before: "",
        Pass: "ветр.ная",
        Context_After: "мельница",
    },
]; // тестовые слова
let words_queue = []; // очаредь слов
for (var i = 0; i < 10; i++) {
    words_queue.push(words[Math.floor(Math.random() * words.length)]);
}
console.log(words_queue);

let compl = ""; // все напечатанное
let current_word = ""; // текущее напечатанное слово

let next_input_view = ""; // отображение следующих слов

for (let i = 0; i < words_queue.length; i++) {
    plus_next_inp(words_queue[i]);
}
if (words_queue[0]["Context_Before"] != "") {
    move_context_before();
}
element_next.innerHTML = next_input_view.slice(0, char_amount_const);
element_compl.innerHTML = compl;

// вспомогательные функции

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
    compl += next_input_view.slice(
        0,
        words_queue[0]["Context_Before"].length + 3
    );
    compl += " ";
    next_input_view = next_input_view.slice(
        words_queue[0]["Context_Before"].length + 3
    );
}
function move_context_after() {
    compl += next_input_view.slice(
        0,
        words_queue[0]["Context_After"].length + 3
    );
    compl += " ";
    next_input_view = next_input_view.slice(
        words_queue[0]["Context_After"].length + 3
    );
}

function update_word_queue() {
    words_queue = words_queue.slice(1); // добавление новыйх слов в очаредь
    words_queue.push(words[Math.floor(Math.random() * words.length)]);
    plus_next_inp(words_queue[words_queue.length - 1]);
}

function update_next_inp_front() {
    next_input_view = next_input_view.slice(1);
}
function update_next_inp_back() {
    next_input_view =
        words_queue[0]["Pass"][current_word.length - 1] + next_input_view;
}

function slice_completed() {
    if (compl.length > char_amount_const) {
        compl = compl.slice(-char_amount_const);
    }
}
function isLetter(str) {
    return str.length === 1 && str.match(/[а-я]/i);
}

function highlight_correct() {
    let ind, len;
    ind = words_queue[0]["Pass"].indexOf(".");
    len = words_queue[0]["Pass"].length;

    compl =
        compl.slice(0, -(len - ind)) +
        "<span style='color: green'>" + // 27
        compl.slice(-(len - ind), -(len - ind) + 1) +
        "</span>" + // 7
        compl.slice(-(len - ind) + 1);
}
function highlight_incorrect() {
    let ind, len;
    ind = words_queue[0]["Pass"].indexOf(".");
    len = words_queue[0]["Pass"].length;

    compl =
        compl.slice(0, -(len - ind)) +
        "<span style='color: red'>" + // 25
        compl.slice(-(len - ind), -(len - ind) + 1) +
        "</span>" + // 7
        compl.slice(-(len - ind) + 1);
}

// основные функции при вводе
function key_backspace() {
    if (current_word.length < 1) {
        console.log("BF");
        return;
    }

    update_next_inp_back();

    compl = compl.slice(0, -1);
    current_word = current_word.slice(0, -1);

    element_next.innerHTML = next_input_view.slice(0, char_amount_const);
    element_compl.innerHTML = compl;
    return;
}

function key_space(key) {
    if (current_word.length < words_queue[0]["Word"].length) {
        console.log("space_barrier"); // не дает перейти на следующее слово пока не написано текущее
        return;
    }

    if (current_word == words_queue[0]["Word"]) {
        console.log("Correct!");
        highlight_correct();
    } else {
        console.log("Fail!");
        highlight_incorrect();
    }
    compl += key;

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
    element_compl.innerHTML = compl;

    update_next_inp_front();
    element_next.innerHTML = next_input_view.slice(0, char_amount_const);

    return;
}

function input(key) {
    if (
        (key != words_queue[0]["Pass"][current_word.length] &&
        words_queue[0]["Pass"][current_word.length] != ".") ||
        !isLetter(key)
    ) {
        return;
    }
    compl += key;
    current_word += key;

    slice_completed();
    element_compl.innerHTML = compl;
    update_next_inp_front();
    element_next.innerHTML = next_input_view.slice(0, char_amount_const);
    return;
}

// контроллер ¯\_(ツ)_/¯
window.addEventListener("keydown", controller);

function controller(e) {
    console.clear();

    const key = e.key.toLowerCase();

    if (!is_started) {
        if (key == " ") {
            element_start.style.display = "none";

            element_compl.style.display = "block";
            element_next.style.display = "block";

            is_started = true;
        }
        return;
    }

    if (key == " ") {
        // проверка введенного слова cur_compl на правильность
        console.log(words_queue[0]["Word"].length);
        key_space(key);
        return;
    }

    if (e.code == "Backspace") {
        // удаление символов
        key_backspace();
        // return;
    }

    input(key);

    console.log(current_word);
    console.log(current_word.length);
    return;
}
