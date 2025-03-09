/*

класс основного поведения при вводе и выводе
*/
const char_amount = 50;
let el_compl = document.getElementById("compl"); // элемент с пройденными словами
let el_next = document.getElementById("next"); // элемент с предстоящими словами

export class Run {
    constructor(words, el_compl, el_next) {
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
        console.log("RUN");
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
        el_compl.innerHTML = this.compl;
    }

    key_backspace() {
        this.compl = this.compl.slice(0, -1);
        this.cur_compl = this.cur_compl.slice(0, -1);
        el_compl.innerHTML = this.compl;
        return;
    }

    key_space() {
        if (cur_compl == next_words) {
            this.next_words = this.next_words.slice(1);
            this.next_words.push(
                this.words[Math.floor(Math.random() * this.words.length)]
            );
            this.cur_compl = "";
        }

        el_compl.innerHTML = this.compl;
        this.compl += key;
        return;
    }
}
