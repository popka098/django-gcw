



// инициализация констант и переменных
const char_amount = 50;
let el_compl = document.getElementById("compl"); // элемент с пройденными словами
let el_next = document.getElementById("next"); // элемент с предстоящими словами

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
        Word: "ветраяная",
        Context_Before: "",
        Pass: "ветр.ная",
        Context_After: "мельница",
    },
]; // тестовые слова
let next_words = []; // очаредь слов
for (var i = 0; i < 10; i++) {
    next_words.push(words[Math.floor(Math.random() * words.length)]);
}

let compl = ""; // все напечатанное
let cur_compl = ""; // текущее напечатанное слово

let next_inp = ""; // отображение следующих слов

function isLetter(str) {
    return str.length === 1 && str.match(/[а-я]/i);
}

function key_backspace(key) {
    console.log("B");
    compl = compl.slice(0, -1);

    console.log(compl);

    cur_compl = cur_compl.slice(0, -1);
    el_compl.innerHTML = compl;
    return;
}

function key_space(key) {
    if (cur_compl == next_words) {
        next_words = next_words.slice(1);
        next_words.push(
            words[Math.floor(Math.random() * words.length)]
        );
        cur_compl = "";
    }

    el_compl.innerHTML = compl;
    compl += key;
    return;
}

function input(key) {
    compl += key;
    cur_compl += key;
    el_compl.innerHTML = compl;
    return;
}

function run(e) {
    const key = e.key;
    if (!isLetter(key) && key != " " && e.code != "Backspace") {
        // проверка на необходимый символ
        console.log("F")
        return;
    }

    if (key == " ") {
        // проверка введенного слова cur_compl на правильность
        key_space(key);
        return;
    }

    if (e.code == "Backspace") {
        // удаление символов
        key_backspace(key);
        return;
    }

    input(key);
    return;
}

window.addEventListener("keydown", run);


