



// этот код не будет робить для н и нн ((((

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
let last_inp = "";

function plus_next_inp(w) {
    if (w["Context_Before"] != "") {
        next_inp += "(";
        next_inp += w["Context_Before"];
        next_inp += ")";
        next_inp += " ";
    }
    next_inp += w["Pass"];
    next_inp += " ";
    if (w["Context_After"] != "") {
        next_inp += "(";
        next_inp += w["Context_After"];
        next_inp += ")";
        next_inp += " ";
    }
}

for (let i = 0; i < next_words.length; i++) {
    plus_next_inp(next_words[i]);
}
el_next.innerHTML = next_inp.slice(0, char_amount);

function update_next_inp_front() {
    next_inp = next_inp.slice(1);
}
function update_next_inp_back() {
    next_inp = next_words[0]["Pass"][cur_compl.length - 1] + next_inp;
}

function isLetter(str) {
    return str.length === 1 && str.match(/[а-я]/i);
}

function key_backspace() {
    if (cur_compl.length < 1) {
        console.log("BF");
        return;
    }

    update_next_inp_back();
    el_next.innerHTML = next_inp.slice(0, char_amount);
    compl = compl.slice(0, -1);
    cur_compl = cur_compl.slice(0, -1);
    el_compl.innerHTML = compl;
    return;
}

function key_space(key) {
    if (cur_compl.length < next_words[0]["Word"].length - 1) {
        console.log("space_barrier");
        return;
    }    


    if (cur_compl == next_words) {
    } else {
    }
    compl += key;

    if (next_words[0]["Context_After"] != "") {
        compl += next_inp.slice(0, next_words[0]["Context_After"].length + 3);
        compl += " ";
        next_inp = next_inp.slice(next_words[0]["Context_After"].length + 3);
    }

    next_words = next_words.slice(1); // добавление новыйх слов в очаредь
    next_words.push(words[Math.floor(Math.random() * words.length)]);
    plus_next_inp(next_words[next_words.length - 1]);
    
    if (next_words[0]["Context_Before"] != "") {
        compl += next_inp.slice(0, next_words[0]["Context_Before"].length + 3);
        compl += " ";
        next_inp = next_inp.slice(next_words[0]["Context_Before"].length + 3);
    }
    
    console.log(next_words); // вывод для дебага
    console.log(next_inp);
    
    cur_compl = ""; // обновление и обнуление переменных
    if (compl.length > char_amount) {
        compl = compl.slice(-char_amount);
    }
    el_compl.innerHTML = compl;

    update_next_inp_front();
    el_next.innerHTML = next_inp.slice(0, char_amount);


    return;
}

function input(key) {
    if (
        key != next_words[0]["Pass"][cur_compl.length] &&
        next_words[0]["Pass"][cur_compl.length] != "."
    ) {
        return;
    }
    compl += key;
    cur_compl += key;

    if (compl.length > char_amount) {
        compl = compl.slice(-char_amount);
    }
    el_compl.innerHTML = compl;
    update_next_inp_front();
    el_next.innerHTML = next_inp.slice(0, char_amount);
    return;
}

window.addEventListener("keydown", controller);
function controller(e) {
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
