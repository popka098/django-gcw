function isLetter(str) {
    return str.length === 1 && str.match(/[а-я]/i);
}

var el_compl = document.getElementById("compl"); // элемент с пройденными словами
var el_next = document.getElementById("next"); // элемент с предстоящими словами

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
const char_amount = 50;

var next_words = [];
for (var i = 0; i < 10; i++) {
    next_words.push(words[Math.floor(Math.random() * words.length)]);
}

window.addEventListener("keydown", run);
var compl = ""; // все напечатанное
var cur_compl = ""; // текущее напечатанное слово
function run(e) {
    const key = e.key;
    if (!(isLetter(key) || key == " " || e.code == "Backspace")) {
        // проверка на необходимый символ
        return;
    }

    if (key == " ") {
        // проверка введенного слова cur_compl на правильность
        return;
    }

    if (e.code == "Backspace") {
        // удаление символов
        compl = compl.slice(0, -1);
        cur_compl = cur_compl.slice(0, -1);
        el_compl.innerHTML = compl;
        return;
    }

    // ограничение возможного ввода при предопределенных символах (символы кроме .)
    compl += key;
    cur_compl += key;
    el_compl.innerHTML = compl;
}
