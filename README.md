# Random Debug Word Sublime Text Plugin

## Description

This Sublime Text plugin provides an easy way to add printf debugging to your Go code. It auto-generates a print statement with a random, Japanese-like pseudo-word that you can search for in your logs or grep whilst you're debugging the execution of your program. 

The idea is that you can bind this to a key combination and then insert a quick debug print statement with a random word. This is useful when printf debugging and you want to see the flow of your program. Instead of using random characters to build the word, we use a list of Japanese syllables. I didn't want to use words because I don't want to get distracted by the meaning, but I wanted something that was easy to read and remember. I chose Japanese because it has a limited set of syllables that work well as random combinations. I also think it is easier to read than the random characters I've used before.

The print statement will be of the form: `fmt.Printf("pseudo_word %v \n", [cursor])`

Where:

- `pseudo_word` is a randomly generated, 5-letter, Japanese-like pseudo-word.
- `[cursor]` is the location your cursor will be after the command is run.

## Installation

- Open Sublime Text.
- Select Preferences > Browse Packages...
- Create a new Python file (with .py extension) inside the User directory.
- Paste the content of the plugin code in this Python file.
- Save the file. The command is now available to be used.

## Usage

To use the plugin you can set up a custom key binding for the command by going to Preferences > Keybindings, and adding an entry like the following in your user keybindings file:

```json
{
    "keys": ["f1"], 
    "command": "go_debug_print"
}
```

Three other commands exist; `"go_debug_print_word"`, `"remove_go_debug_print"` and `"print_word"` which print a single Printf statement containing the random word with no other parameters, deletes all occurences of inserted debug printf's in the current buffer and just prints the word by itself, respectively. 

## Example

Example keymap entry: 
```json
{ "keys": ["ctrl+alt+shift+g"], "command": "go_debug_print" },
```

Replace `"f1"` with whatever key combination you prefer.

After running the command, the print statement will be inserted at your cursor's location.

Example output: 
```go
fmt.Printf("seiku %v \n", )
```

