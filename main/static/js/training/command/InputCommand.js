import { input } from "../utils/state.js";
import { Command } from "./Command.js";

export class InputCommand extends Command {
    constructor(key) {
        super();
        this.key = key;
    }

    execute() {
        input(this.key);
    }
}
