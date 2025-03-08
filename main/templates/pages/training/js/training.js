



import { Run } from "./run_class";

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

var runner = new Run(words, el_compl, el_next);

window.addEventListener("keydown", runner.run);

