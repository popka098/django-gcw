console.log("data_entry");
document.addEventListener("DOMContentLoaded", function () {
    const cardNumber = document.getElementsByName("cardNumber")[0];
    if (cardNumber) {
        cardNumber.addEventListener("input", function () {
            let value = this.value.replace(/\D/g, "");
            let newValue = "";
            for (let i = 0; i < value.length; i++) {
                if (i > 0 && i % 4 === 0) newValue += " ";
                newValue += value[i];
            }
            this.value = newValue;
        });
    }

    const expiryDate = document.getElementsByName("expiryDate")[0];
    if (expiryDate) {
        expiryDate.addEventListener("input", function () {
            let value = this.value.replace(/\D/g, "");
            if (value.length > 2) {
                value = value.substring(0, 2) + "/" + value.substring(2, 4);
            }
            this.value = value;
        });
    }

    const cvv = document.getElementsByName("cvv")[0];
    if (cvv) {
        cvv.addEventListener("input", function () {
            this.value = this.value.replace(/\D/g, "").substring(0, 4);
        });
    }
});
