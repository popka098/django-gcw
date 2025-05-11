import { is_started, is_sub } from "./utils/state.js";

function redirect() {
    const select = document.getElementById("numbers-select");
    const val = select.value;

    console.log(val);

    window.location.href = "../" + val;
}
window.redirect = redirect;

let element_choose_time_button = document.getElementById("choose_time_button");
export let end_times = [120, 180, 300, 600];
export let end_time_ind = 0;
function change_time_end() {
    if (is_started) {
        return;
    }

    if (!is_sub) {
        window.location.href = "../../subscribe/choose";
        return;
    }

    end_time_ind++;
    if (end_time_ind >= end_times.length) {
        end_time_ind = 0;
    }

    element_choose_time_button.innerHTML = end_times[end_time_ind];
}
window.change_time_end = change_time_end;

