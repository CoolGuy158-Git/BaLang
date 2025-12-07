# BaLang

BaLang is an experimental programming language designed for beginners and young learners (5yo+). It features a minimal set of commands for variables, output, loops, and simple conditionals.

## Overview

- **Variables:** Store values using `=`  
- **Output:** Display values with `say`  
- **Loops:** Repeat commands using `loop n { ... }`  
- **Conditionals:** Simple `if var is value { ... }`  
- **Stop Execution:** Use `stop` or `escape`  

## Example

```Blng
mama = mama1
say mama
loop 3 {say hi}
if mama is mama1 {say yes}
stop
```

## Interpreter
To run BaLang scripts:

1. Make sure your BaLang file is named with the .blng extension, e.g., hello.blng.

2. Place your script in the same folder as interpreter.py or navigate to the BaLang folder in the terminal.

3. Run the script with:

```bash
python interpreter.py <filename>.blng
```

Example:
```bash
python interpreter.py hello.blng
```

**Optional**
### Turn interpreter into a executable
In your terminal run 
```bash
pip install pyinstaller
```
Build the executable
```bash
pyinstaller interpreter.py --onefile
```
Place the executable into any folder that is connected to paths via enviromental variables
This lets you run commands like
```bash
interpreter <path to file>.blng
```

## Notes

- Syntax errors are ignored safely.  
- Future versions will include a dedicated IDE for easier script writing and testing.

