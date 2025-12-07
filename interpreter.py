#####################################################################
# BaLang- An experimental programming language targeted to kids 5yo+#
# Interpreter                                                       #
# Under MIT license - Feel free to fork and modify the code         #
# Copyright 2025 CoolGuy158-Git                                     #
#####################################################################
import sys
variables = {}

def say(value):
    print(variables.get(value, value))

def execute(command):
    command = command.strip()
    if not command:
        return
    try:
        if "=" in command:
            var, val = command.split("=")
            try:
                # Try as integer or float
                val = eval(val)
            except:
                # Keep as string if eval fails
                val = val
            variables[var.strip()] = val
        elif command.startswith("say"):
            content = command[4:].strip()
            say(content)
        elif command.lower() in ["stop", "escape"]:
            return "STOP"
        elif command.startswith("loop"):
            parts = command[4:].strip()

            if "{" in parts and "}" in parts:
                inner = parts.split("{", 1)[1].rsplit("}", 1)[0].strip()
                num_part = parts.split("{", 1)[0].strip()

                if num_part:
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
                if variables.get(var.strip(), var.strip()) == val.strip():
                    for line in inner.splitlines():
                        execute(line)

        else:
            pass
    except:
        pass

if len(sys.argv) < 2:
    print("Usage: python interpreter.py filename.blng")
    sys.exit()

script_file = sys.argv[1]

if not script_file.lower().endswith(".blng"):
    print("Error: File must have .blng extension!")
    sys.exit()

with open(script_file, "r") as f:
    script_lines = f.readlines()

for line in script_lines:
    result = execute(line)
    if result == "STOP":
        break