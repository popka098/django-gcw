import { BackspaceCommand } from "./BackspaceCommand.js";
import { SpaceCommand } from "./SpaceCommand.js";
import { StartCommand } from "./StartCommand.js";

export class CommandManager {
    constructor() {
        this.commands = new Map();
    }

    register(key, command) {
        this.commands.set(key, command);
    }

    execute(key, fallback) {
        if (this.commands.has(key)) {
            this.commands.get(key).execute();
        } else if (fallback) {
            fallback();
        }
    }
}

export const commandManager = new CommandManager();

commandManager.register("start", new StartCommand());
commandManager.register("space", new SpaceCommand());
commandManager.register("backspace", new BackspaceCommand());

