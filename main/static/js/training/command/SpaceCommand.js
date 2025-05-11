import { key_space } from "../utils/state.js";
import { Command } from "./Command.js";

export class SpaceCommand extends Command {
    execute() {
        key_space(" ");
    }
}
