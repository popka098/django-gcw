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
console.log(next_words);

let compl = ""; // все напечатанное
let cur_compl = ""; // текущее напечатанное слово

let next_inp = ""; // отображение следующих слов

function isLetter(str) {
    return str.length === 1 && str.match(/[а-я]/i);
}

function key_backspace() {
    if (cur_compl.length < 1) {
        console.log("BF");
        return;
    }

    compl = compl.slice(0, -1);
    cur_compl = cur_compl.slice(0, -1);
    el_compl.innerHTML = compl;
    return;
}

function key_space(key) {
    if (cur_compl == next_words) {
    } else {
    }
    next_words = next_words.slice(1);
    next_words.push(words[Math.floor(Math.random() * words.length)]);
    cur_compl = "";
    console.log(next_words);

    compl += key;
    if (compl.length > char_amount) {
        compl = compl.slice(-char_amount);
    }
    el_compl.innerHTML = compl;
    cur_compl = "";
    return;
}

function input(key) {
    if (key != next_words[0]["Pass"][cur_compl.length] && next_words[0]["Pass"][cur_compl.length] != ".") {
        return;
    }
    compl += key;
    cur_compl += key;

    if (compl.length > char_amount) {
        compl = compl.slice(-char_amount);
    }
    el_compl.innerHTML = compl;
    return;
}

window.addEventListener("keydown", run);
function run(e) {
    const key = e.key;
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

