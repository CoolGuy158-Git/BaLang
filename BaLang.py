#####################################################################
# BaLang- An experimental programming language targeted to kids 5yo+#
# Under MIT license - Feel free to fork and modify the code         #
# Copyright 2025 CoolGuy158-Git                                     #
#####################################################################

variables = {}

def say(value):
    print(variables.get(value, value))
    
def ask(prompt, variable_name):
    variables[variable_name] = input(prompt + " ")

def evaluate(val):
    try:
        return eval(val)
    except:
        return val

def execute(command):
    command = command.strip()
    if not command:
        return
    try:
        if "=" in command and not command.startswith("if") and not command.startswith("loop"):
            var, val = command.split("=", 1)
            variables[var.strip()] = evaluate(val.strip())

        elif command.startswith("say"):
            content = command[4:].strip()
            say(content)

        elif command.startswith("ask"):
            parts = command[3:].strip().rsplit(" ", 1)
            if len(parts) != 2:
                say("Error: ask syntax incorrect. Example: ask Hello? choice")
                return
            prompt, var_name = parts
            ask(prompt.strip(), var_name.strip())

        elif command.lower() in ["stop", "escape"]:
            return "STOP"

        elif command.startswith("loop"):
            parts = command[4:].strip()
            if "{" in parts and "}" in parts:
                inner = parts.split("{",1)[1].rsplit("}",1)[0].strip()
                num_part = parts.split("{",1)[0].strip()
                if num_part:  # numeric loop
                    for _ in range(int(num_part)):
                        for line in inner.splitlines():
                            result = execute(line)
                            if result == "STOP":
                                return "STOP"
                else:  
                    while True:
                        for line in inner.splitlines():
                            result = execute(line)
                            if result == "STOP":
                                return "STOP"

        elif command.startswith("if"):
            condition = command[2:].split("{")[0].strip()
            inner = command.split("{")[1].split("}")[0].strip()
            if " is " in condition:
                var, val = condition.split(" is ")
                var_val = str(variables.get(var.strip(), ""))
                if var_val == val.strip():
                    for line in inner.splitlines():
                        result = execute(line)
                        if result == "STOP":
                            return "STOP"

    except Exception as e:
        print(f"Error executing command '{command}': {e}")

print("Welcome to BaLang! Type 'Run' to execute your script.")
print("Commands: say, variables (=), stop/escape, loop, if/else, ask")

script_lines = []
while True:
    line = input(">>>")
    if line.strip().upper() == "RUN":
        break
    script_lines.append(line)

for line in script_lines:
    result = execute(line)
    if result == "STOP":
        break
