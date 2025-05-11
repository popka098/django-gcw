import { start } from "../utils/state.js";
import { Command } from "./Command.js";

export class StartCommand extends Command {
    execute() {
        start();
    }
}
