



let block = document.querySelector("div");

/// перебирает слова
function changeColorText(phrase) {
    let arrWord = phrase.split(" ");

    arrWord.forEach(function (item_word) {
        getWord(item_word);
    });
}

///// вставьте любую фразу
changeColorText("Какая то строка со словами");

/// проверяет количество букв в слове и изменяет текст
function getWord(word) {
    let arr_letter = word.split("");

    /// если число букв в слове больше пяти, то окрашивается в красный, если меньше или равно пяти, в зеленый.
    if (arr_letter.length > 5) {
        let span = document.createElement("span");
        span.textContent = word + " ";

        span.style.color = "red";

        block.appendChild(span);
    } else {
        let span = document.createElement("span");
        span.textContent = word + " ";

        span.style.color = "green";

        block.appendChild(span);
    }
}
