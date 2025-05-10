console.log("choose");
document.addEventListener('DOMContentLoaded', function() {
    const prices = {
        month: "1000 рублей",
        three_month: "2700 рублей",
        year: "9000 рублей"
    };

    const radioButtons = document.querySelectorAll('input[name="period"]');
    const amountElement = document.getElementById('amount');

    function updatePrice() {
        const selectedPeriod = document.querySelector('input[name="period"]:checked').value;
        amountElement.textContent = `Цена: ${prices[selectedPeriod]}`;
    }

    radioButtons.forEach(radio => {
        radio.addEventListener('change', updatePrice);
    });

    updatePrice();
});