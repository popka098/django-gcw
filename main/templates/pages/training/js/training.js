



function isLetter(str) 
{
    return str.length === 1 && str.match(/[а-я]/i);
}

var el_compl = document.getElementById("compl"); // элемент с пройденными словами
var el_next = document.getElementById("next"); // элемент с предстоящими словами
var el_context_bef = document.getElementById("context_after"); // элемент с контекстом перед словом
var el_context_aft = document.getElementById("context_before"); // элемент с контекстом после слова

const words = [
    {
        "Word": "фланелевый",
        "Context_Before": "",
        "Pass": "фланел.вый",
        "Context_After": "",
    },
    {
        "Word": "ситечко",
        "Context_Before": "чайное",
        "Pass": "сит.чко",
        "Context_After": "",
    },
    {
        "Word": "ветраяная",
        "Context_Before": "",
        "Pass": "ветр.ная",
        "Context_After": "мельница",
    },
]; // тестовые слова

var rand_item = words[Math.floor(Math.random()*words.length)]; // рандом
console.log(rand_item);

window.addEventListener("keydown", run);
function run(e)
{
    const key = e.key;
    if (!(isLetter(key) || (key == " ") || (e.code == "Backspace"))) // проверка на необходимый символ
    {
        return;
    }
    

}