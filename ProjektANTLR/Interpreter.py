class Interpreter:
    def __init__(self):
        self.stack = []
        self.memory = {}
        self.labels = {}
        self.file_writes = {}
        self.file_names = {}
        self.ip = 0

    def format_value(self, value):
        if isinstance(value, bool):
            return "true" if value else "false"
        return str(value)

    def print_reverse_filewrites(self):
        print("\n")
        for file_value, values in self.file_writes.items():
            varname = self.file_names.get(file_value, file_value)
            print(f'FILE {varname} = "{file_value}";')
            print(f'{varname} << ' + ' << '.join(repr(v) for v in values) + ';')

    def execute(self, filename):
        with open(filename, 'r', encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

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
                if len(parts) == 2 and parts[1].isdigit():
                    count = int(parts[1])
                    if len(self.stack) < count:
                        raise ValueError(f"Chyba: Nedostatok hodnôt na zásobníku pre PRINT {count}.")
                    values = [self.stack.pop() for _ in range(count)][::-1]
                    print("".join(self.format_value(v) for v in values))
                else:
                    if not self.stack:
                        raise ValueError("Chyba: Zásobník je prázdny pre PRINT.")
                    val = self.stack.pop()
                    print(self.format_value(val))

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
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a > b if instr == "GT" else a < b)

            elif instr == "EQ":
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
                varname = parts[-1]
                value = self.stack.pop()
                self.memory[varname] = value


            elif instr == "LOAD":
                varname = parts[1]
                self.stack.append(self.memory.get(varname, 0))

            elif instr == "READ":
                t = parts[1]
                var_name = parts[2] if len(parts) > 2 else None
                if t == "I":
                    val = int(input(f"Enter value for {var_name or 'int'}: "))
                elif t == "F":
                    val = float(input(f"Enter value for {var_name or 'float'}: "))
                elif t == "S":
                    val = input(f"Enter value for {var_name or 'string'}: ")
                elif t == "B":
                    val = input(f"Enter value for {var_name or 'bool'} (true/false): ").lower() == "true"
                self.stack.append(val)

            elif instr == "LABEL":
                pass

            elif instr == "JMP":
                label = int(parts[1])
                self.ip = self.labels[label]

            elif instr == "FJMP":
                label = int(parts[1])
                condition = self.stack.pop()
                if not condition:
                    self.ip = self.labels[label]
                    
            elif instr == "FWRITE":
                filename = self.stack.pop()
                value = self.stack.pop()

                try:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(str(value) + "\n") 
                except Exception as e:
                    print(f"Chyba pri zapisovaní do súboru '{filename}': {e}")



            else:
                raise ValueError(f"Neznáma inštrukcia: {instr}")

        if self.file_writes:
            self.print_reverse_filewrites()
