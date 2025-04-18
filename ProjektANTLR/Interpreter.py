class Interpreter:
    def __init__(self):
        self.stack = []
        self.memory = {}
        self.labels = {}
        self.ip = 0  # inštrukčný ukazateľ

    def execute(self, filename):
        with open(filename, 'r', encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        # predspracovanie labelov
        for idx, line in enumerate(lines):
            if line.startswith("label"):
                label_num = int(line.split()[1])
                self.labels[label_num] = idx

        self.ip = 0
        while self.ip < len(lines):
            line = lines[self.ip]
            self.ip += 1
            parts = line.split()
            instr = parts[0].upper()

            if instr == "PUSH":
                t = parts[1]
                val = " ".join(parts[2:])
                if t == "I":
                    self.stack.append(int(val))
                elif t == "F":
                    self.stack.append(float(val))
                elif t == "S":
                    self.stack.append(val.strip('"'))
                elif t == "B":
                    self.stack.append(val.lower() == "true")

            elif instr == "POP":
                self.stack.pop()

            elif instr == "PRINT":
                if len(parts) == 2:
                    # PRINT I / PRINT F
                    val = self.stack.pop()
                    print(val)
                else:
                    # print <count> - náš nový jazyk
                    count = int(parts[1])
                    values = [self.stack.pop() for _ in range(count)][::-1]
                    print(" ".join(map(str, values)))

            elif instr in {"ADD", "SUB", "MUL", "DIV"}:
                b = self.stack.pop()
                a = self.stack.pop()
                if isinstance(a, int) and isinstance(b, float):
                    a = float(a)
                if isinstance(a, float) and isinstance(b, int):
                    b = float(b)

                if instr == "ADD":
                    self.stack.append(a + b)
                elif instr == "SUB":
                    self.stack.append(a - b)
                elif instr == "MUL":
                    self.stack.append(a * b)
                elif instr == "DIV":
                    self.stack.append(a / b)

            elif instr == "MOD":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a % b)

            elif instr == "UMINUS":
                t = parts[1] if len(parts) > 1 else ""
                a = self.stack.pop()
                self.stack.append(-a)

            elif instr == "CONCAT":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(str(a) + str(b))

            elif instr == "AND":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a and b)

            elif instr == "OR":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a or b)

            elif instr in {"GT", "LT"}:
                op_type = parts[1] if len(parts) > 1 else ""
                b = self.stack.pop()
                a = self.stack.pop()
                if instr == "GT":
                    self.stack.append(a > b)
                elif instr == "LT":
                    self.stack.append(a < b)

            elif instr == "EQ":
                op_type = parts[1] if len(parts) > 1 else ""
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a == b)

            elif instr == "NOT":
                a = self.stack.pop()
                self.stack.append(not a)

            elif instr == "ITOF":
                a = self.stack.pop()
                self.stack.append(float(a))

            elif instr == "SAVE":
                # SAVE <typ> <var> alebo len SAVE <var>
                if len(parts) == 3:
                    varname = parts[2]
                else:
                    varname = parts[1]
                self.memory[varname] = self.stack.pop()

            elif instr == "LOAD":
                varname = parts[1]
                self.stack.append(self.memory.get(varname, 0))

            elif instr == "READ":
                t = parts[1]
                val = input(f"Zadaj {t}: ")
                if t == "I":
                    self.stack.append(int(val))
                elif t == "F":
                    self.stack.append(float(val))
                elif t == "S":
                    self.stack.append(val)
                elif t == "B":
                    self.stack.append(val.lower() == "true")

            elif instr == "LABEL":
                pass  # už bolo spracované predtým

            elif instr == "JMP":
                label = int(parts[1])
                self.ip = self.labels[label]

            elif instr == "FJMP":
                label = int(parts[1])
                condition = self.stack.pop()
                if not condition:
                    self.ip = self.labels[label]

            else:
                raise ValueError(f"Neznáma inštrukcia: {instr}")

    def _binary_op(self, typ, operation):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(operation(a, b))
