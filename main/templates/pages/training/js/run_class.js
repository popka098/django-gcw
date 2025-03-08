/*

класс основного поведения при вводе и выводе
*/
function isLetter(str) {
    return str.length === 1 && str.match(/[а-я]/i);
}

const char_amount = 50;
export class Run {
    constructor(words, el_compl, el_next) {
        this.el_compl = el_compl;
        this.el_next = el_next;

        this.words = words; // все слова
        this.next_words = []; // очаредь слов
        for (var i = 0; i < 10; i++) {
            next_words.push(words[Math.floor(Math.random() * words.length)]);
        }

        this.compl = ""; // все напечатанное
        this.cur_compl = ""; // текущее напечатанное слово

        this.next_inp = ""; // отображение следующих слов
    }

    run(e) {
        const key = e.key;
        if (!(isLetter(key) || key == " " || e.code == "Backspace")) {
            // проверка на необходимый символ
            return;
        }

        if (key == " ") {
            // проверка введенного слова cur_compl на правильность
            this.key_space;
            return;
        }

        if (e.code == "Backspace") {
            // удаление символов
            this.key_backspace;
            return;
        }

        // ограничение возможного ввода при предопределенных символах (символы кроме .)
        this.compl += key;
        this.cur_compl += key;
        this.el_compl.innerHTML = compl;
    }

    key_backspace() {
        this.compl = compl.slice(0, -1);
        this.cur_compl = cur_compl.slice(0, -1);
        this.el_compl.innerHTML = compl;
        return;
    }

    key_space() {
        if (cur_compl == next_words) {
            this.next_words = next_words.slice(1);
            this.next_words.push(words[Math.floor(Math.random() * words.length)]);
            this.cur_compl = "";
        }

        this.el_compl.innerHTML = compl;
        this.compl += key;
        return;
    }
};
