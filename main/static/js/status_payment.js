console.log("status")
const now = new Date();
document.getElementById("transactionDate").textContent =
    now.toLocaleDateString("ru-RU") + " " + now.toLocaleTimeString("ru-RU");
