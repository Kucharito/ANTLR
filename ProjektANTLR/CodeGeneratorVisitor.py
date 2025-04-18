from PLC_GrammarVisitor import PLC_GrammarVisitor
from PLC_GrammarParser import PLC_GrammarParser

class CodeGeneratorVisitor(PLC_GrammarVisitor):
    def __init__(self):
        self.type_stack = [] 
        self.code = []  # Generovaný kód
        self.label_counter = 0
        self.var_types = {}  # Mapa typov premenných

    def get_next_label(self):
        label = self.label_counter
        self.label_counter += 1
        return label

    def visitProg(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        return self.code

    def visitDeclaration(self, ctx):
        var_type = ctx.type_().getText()
        for id_token in ctx.ID():
            var_name = id_token.getText()
            self.var_types[var_name] = var_type
            if var_type == "int":
                self.code.append("push I 0")
            elif var_type == "float":
                self.code.append("push F 0.0")
            elif var_type == "string":
                self.code.append('push S ""')
            elif var_type == "bool":
                self.code.append("push B false")
            elif var_type == "FILE":
                self.code.append('push S ""')
            self.code.append(f"save {var_name}")

    def visitExpression(self, ctx):
        return self.visit(ctx.assignment())

    def visitAssignment(self, ctx):
        # Ak je to priradenie typu A = B = C = ... = výraz
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0).getText()
            right_ctx = ctx.getChild(2)

            value_type = self.visit(right_ctx)

            # Každý assignment musí zduplikovať hodnotu pred uložením
            # takže pridáme nový push pre každé ukladanie späť do zásobníka
            # Priraď iba raz pre najhlbšieho potomka
            self.code.append(f"save {left}")
            # Zduplikujeme hodnotu predchádzajúcimi priradeniami
            if isinstance(right_ctx, PLC_GrammarParser.AssignmentContext):
                self.code.append(f"load {left}")  # push back to stack for previous
            return value_type
        else:
            return self.visit(ctx.or_())


    def visitLiteral(self, ctx):
        if ctx.INT():
            value = ctx.INT().getText()
            self.code.append(f"push I {value}")
            return "int"
        elif ctx.FLOAT():
            value = ctx.FLOAT().getText()
            self.code.append(f"push F {value}")
            return "float"
        elif ctx.STRING():
            value = ctx.STRING().getText()
            self.code.append(f"push S {value}")
            return "string"
        elif ctx.BOOL():
            value = ctx.BOOL().getText()
            self.code.append(f"push B {value}")
            return "bool"

    def visitPrimary(self, ctx):
        if ctx.ID():
            var_name = ctx.ID().getText()
            # ak je to boolean literál, nevolaj load!
            if var_name == "true":
                self.code.append("push B true")
                return "bool"
            elif var_name == "false":
                self.code.append("push B false")
                return "bool"
            self.code.append(f"load {var_name}")
            return self.var_types.get(var_name, "int")
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.expression():
            return self.visit(ctx.expression())


    def visitAdditive(self, ctx):
        left_type = self.visit(ctx.multiplicative(0))
        for i in range(1, len(ctx.multiplicative())):
            right_type = self.visit(ctx.multiplicative(i))
            op = ctx.getChild(2*i-1).getText()
            if op == "+":
                if left_type == right_type == "int":
                    self.code.append("add I")
                    left_type = "int"
                elif left_type == right_type == "float":
                    self.code.append("add F")
                    left_type = "float"
                elif left_type == "int" and right_type == "float":
                    self.code.append("itof")
                    self.code.append("add F")
                    left_type = "float"
                elif left_type == "float" and right_type == "int":
                    self.code.append("itof")
                    self.code.append("add F")
                    left_type = "float"
            elif op == "-":
                if left_type == right_type == "int":
                    self.code.append("sub I")
                    left_type = "int"
                else:
                    self.code.append("sub F")
                    left_type = "float"
            elif op == ".":
                self.code.append("concat")
                left_type = "string"
        return left_type

    def visitMultiplicative(self, ctx):
        left_type = self.visit(ctx.unary(0))
        for i in range(1, len(ctx.unary())):
            right_type = self.visit(ctx.unary(i))
            op = ctx.getChild(2*i - 1).getText()

            if op == "%":
                self.code.append("mod")
                left_type = "int"
            elif op == "*":
                if left_type == right_type == "int":
                    self.code.append("mul I")
                    left_type = "int"
                elif "float" in [left_type, right_type]:
                    if left_type == "int":
                        self.code.insert(-1, "itof")
                    if right_type == "int":
                        self.code.append("itof")
                    self.code.append("mul F")
                    left_type = "float"
            elif op == "/":
                if left_type == right_type == "int":
                    self.code.append("div I")
                    left_type = "int"
                elif "float" in [left_type, right_type]:
                    if left_type == "int":
                        self.code.insert(-1, "itof")
                    if right_type == "int":
                        self.code.append("itof")
                    self.code.append("div F")
                    left_type = "float"
        return left_type


    def visitWrite(self, ctx):
        for expr in ctx.expression():
            self.visit(expr)
        self.code.append(f"print {len(ctx.expression())}")

    def visitRead(self, ctx):
        for id_token in ctx.ID():
            var_name = id_token.getText()
            typ = self.var_types.get(var_name, "int")
            self.code.append(f"read {typ[0].upper()}")
            self.code.append(f"save {var_name}")

    def visitUnary(self, ctx):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            typ = self.visit(ctx.primary())
            if op == "-":
                self.code.append("uminus I")
                return "int"
            elif op == "!":
                self.code.append("not")
                return "bool"
        else:
            return self.visit(ctx.primary())

    def visitEquality(self, ctx):
        left_type = self.visit(ctx.relational(0))
        for i in range(1, len(ctx.relational())):
            right_type = self.visit(ctx.relational(i))
            op = ctx.getChild(2 * i - 1).getText()

            # Automatická konverzia int -> float
            if left_type == "int" and right_type == "float":
                self.code.insert(-1, "itof")
                result_type = "float"
            elif left_type == "float" and right_type == "int":
                self.code.insert(-2, "itof")
                result_type = "float"
            elif left_type == right_type:
                result_type = left_type
            else:
                result_type = "string"  # fallback na eq S ak by typy neboli rovnaké a nie float/int

            # Pridaj inštrukciu eq s typom
            if result_type == "int":
                self.code.append("eq I")
            elif result_type == "float":
                self.code.append("eq F")
            elif result_type == "bool":
                self.code.append("eq B")
            elif result_type == "string":
                self.code.append("eq S")

            if op == "!=":
                self.code.append("not")

            left_type = "bool"  # výstupom porovnania je vždy bool

        return "bool"





    def visitIfCondition(self, ctx):
        label_else = self.get_next_label()
        label_end = self.get_next_label()
        self.visit(ctx.expression())
        self.code.append(f"fjmp {label_else}")
        self.visit(ctx.statement(0))
        self.code.append(f"jmp {label_end}")
        self.code.append(f"label {label_else}")
        if ctx.statement(1):
            self.visit(ctx.statement(1))
        self.code.append(f"label {label_end}")

    def visitWhileCondition(self, ctx):
        label_start = self.get_next_label()
        label_end = self.get_next_label()
        self.code.append(f"label {label_start}")
        self.visit(ctx.expression())
        self.code.append(f"fjmp {label_end}")
        self.visit(ctx.statement())
        self.code.append(f"jmp {label_start}")
        self.code.append(f"label {label_end}")

    def visitBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitOr(self, ctx):
        self.visit(ctx.and_(0))
        for i in range(1, len(ctx.and_())):
            self.visit(ctx.and_(i))
            self.code.append("or")
        return "bool"

    def visitAnd(self, ctx):
        self.visit(ctx.equality(0))
        for i in range(1, len(ctx.equality())):
            self.visit(ctx.equality(i))
            self.code.append("and")
        return "bool"

    def visitRelational(self, ctx):
        left_type = self.visit(ctx.additive(0))
        for i in range(1, len(ctx.additive())):
            right_type = self.visit(ctx.additive(i))
            op = ctx.getChild(2 * i - 1).getText()

            if left_type == "int" and right_type == "float":
                self.code.insert(-1, "itof")
                instr = "lt F" if op == "<" else "gt F"
                left_type = "float"
            elif left_type == "float" and right_type == "int":
                self.code.insert(-2, "itof")
                instr = "lt F" if op == "<" else "gt F"
                left_type = "float"
            elif left_type == right_type == "float":
                instr = "lt F" if op == "<" else "gt F"
            else:
                instr = "lt I" if op == "<" else "gt I"
            self.code.append(instr)
            left_type = "bool"
        return "bool"

