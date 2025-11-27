#####################################################################
# BaLang- An experimental programming language targeted to kids 5yo+#
# Under MIT license - Feel free to fork and modify the code         #
# Copyright 2025 CoolGuy158-Git                                     #
#####################################################################

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
            variables[var.strip()] = val.strip()
        elif command.startswith("say"):
            content = command[4:].strip()
            say(content)
        elif command.lower() in ["stop", "escape"]:
            return "STOP"
        elif command.startswith("loop"):
            parts = command[4:].strip()
            if "{" in parts and "}" in parts:
                num, inner = parts.split("{", 1)
                inner = inner.rsplit("}", 1)[0]
                for _ in range(int(num.strip())):
                    for line in inner.strip().splitlines():
                        execute(line)

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

print("Welcome to BaLang! Type 'Run' to execute your script.")
print("Commands: say, variables (=), stop/escape, loop, if/else")

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
