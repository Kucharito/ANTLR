class Interpreter:
    def __init__(self):
        self.stack = []
        self.memory = {}
        self.labels = {}
        self.ip = 0  # inštrukčný ukazateľ

    def execute(self, filename):
        with open(filename, 'r') as f:
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
            instr = parts[0]

            if instr == "push":
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
            elif instr == "pop":
                self.stack.pop()
            elif instr == "print":
                count = int(parts[1])
                values = [self.stack.pop() for _ in range(count)][::-1]
                print(" ".join(map(str, values)))
            elif instr == "add":
                self._binary_op(parts[1], lambda a, b: a + b)
            elif instr == "sub":
                self._binary_op(parts[1], lambda a, b: a - b)
            elif instr == "mul":
                self._binary_op(parts[1], lambda a, b: a * b)
            elif instr == "div":
                self._binary_op(parts[1], lambda a, b: a / b)
            elif instr == "mod":
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a % b)
            elif instr == "uminus":
                t = parts[1]
                a = self.stack.pop()
                self.stack.append(-a)
            elif instr == "concat":
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(str(a) + str(b))
            elif instr == "and":
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a and b)
            elif instr == "or":
                b, a = self.stack.pop(), self.stack.pop()
                self.stack.append(a or b)
            elif instr == "gt":
                self._binary_op(parts[1], lambda a, b: a > b)
            elif instr == "lt":
                self._binary_op(parts[1], lambda a, b: a < b)
            elif instr == "eq":
                self._binary_op(parts[1], lambda a, b: a == b)
            elif instr == "not":
                a = self.stack.pop()
                self.stack.append(not a)
            elif instr == "itof":
                a = self.stack.pop()
                self.stack.append(float(a))
            elif instr == "save":
                varname = parts[1]
                self.memory[varname] = self.stack.pop()
            elif instr == "load":
                varname = parts[1]
                self.stack.append(self.memory.get(varname, 0))
            elif instr == "read":
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
            elif instr == "label":
                pass  # ignorujeme, už spracované
            elif instr == "jmp":
                label = int(parts[1])
                self.ip = self.labels[label]
            elif instr == "fjmp":
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
