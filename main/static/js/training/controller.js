import { is_started } from "./utils/state.js";
import { InputCommand } from "./command/InputCommand.js";
import { commandManager } from "./command/CommandManager.js";


export function controller(e) {
    const key = e.key.toLowerCase();

    if (!is_started) {
        if (key === " ") {
            commandManager.execute("start");
        }
        return;
    }

    if (key === " ") {
        commandManager.execute("space");
        return;
    }

    if (e.code === "Backspace") {
        commandManager.execute("backspace");
        return;
    }

    // По умолчанию — передаём в InputCommand
    const inputCmd = new InputCommand(key);
    inputCmd.execute();
}
