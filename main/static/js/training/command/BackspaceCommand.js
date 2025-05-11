import { key_backspace } from "../utils/state.js";
import { Command } from "./Command.js";

export class BackspaceCommand extends Command {
    execute() {
        key_backspace();
    }
}
