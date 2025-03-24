// этот код не будет робить для н и нн ((((

// инициализация констант и переменных

// init
const char_amount = 50;
let element_compl = document.getElementById("compl"); // элемент с пройденными словами
let element_next = document.getElementById("next"); // элемент с предстоящими словами

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
element_next.innerHTML = next_input_view.slice(0, char_amount);
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

function isLetter(str) {
    return str.length === 1 && str.match(/[а-я]/i);
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

    element_next.innerHTML = next_input_view.slice(0, char_amount);
    element_compl.innerHTML = compl;
    return;
}

function key_space(key) {
    if (current_word.length < words_queue[0]["Word"].length - 1) {
        console.log("space_barrier"); // не дает перейти на следующее слово пока не написано текущее
        return;
    }

    if (current_word == words_queue[0]["Word"]) {
        console.log("Correct!");
    } else {
        console.log("Fail!");
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
    console.log(next_input_view);

    current_word = ""; // обновление и обнуление переменных
    if (compl.length > char_amount) {
        compl = compl.slice(-char_amount);
    }
    element_compl.innerHTML = compl;

    update_next_inp_front();
    element_next.innerHTML = next_input_view.slice(0, char_amount);

    return;
}

function input(key) {
    if (
        key != words_queue[0]["Pass"][current_word.length] &&
        words_queue[0]["Pass"][current_word.length] != "."
    ) {
        return;
    }
    compl += key;
    current_word += key;

    if (compl.length > char_amount) {
        compl = compl.slice(-char_amount);
    }
    element_compl.innerHTML = compl;
    update_next_inp_front();
    element_next.innerHTML = next_input_view.slice(0, char_amount);
    return;
}

// контроллер ¯\_(ツ)_/¯
window.addEventListener("keydown", controller);
function controller(e) {
    const key = e.key.toLowerCase();
    if (!isLetter(key) && key != " " && e.code != "Backspace") {
        // проверка на необходимый символ
        console.log("F");
        return;
    }

    if (key == " ") {
        // проверка введенного слова cur_compl на правильность
        key_space(key);
        return;
    }

    if (e.code == "Backspace") {
        // удаление символов
        key_backspace();
        return;
    }

    input(key);
    return;
}
