from PLC_GrammarVisitor import PLC_GrammarVisitor
from PLC_GrammarParser import PLC_GrammarParser


class CodeGeneratorVisitor(PLC_GrammarVisitor):
    def __init__(self):
        self.code = []
        self.variables = {}
        self.label_counter = 0

    def getExpressionType(self, ctx):
        text = ctx.getText()
        if '"' in text:
            return "string"
        elif "." in text:
            return "float"
        elif text in ["true", "false"]:
            return "bool"
        elif text.isdigit():
            return "int"
        elif text in self.variables:
            return self.variables[text]
        return "int" 

    def new_label(self):
        label = str(self.label_counter)
        self.label_counter += 1
        return label

    def visitProg(self, ctx):
        for stat in ctx.statement():
            self.visit(stat)
        return self.code

    def visitDeclaration(self, ctx):
        var_type = ctx.type_().getText()
        for var in ctx.ID():
            name = var.getText()
            self.variables[name] = var_type

            if ctx.expression():  
                self.visit(ctx.expression()) 
                expr_type = self.getExpressionType(ctx.expression())
                if var_type == "float" and expr_type == "int":
                    self.code.append("itof")
                self.code.append(f"save {name}")
            else: 
                if var_type == "int":
                    self.code.append("push I 0")
                    self.code.append(f"save {name}")
                elif var_type == "float":
                    self.code.append("push F 0.0")
                    self.code.append(f"save {name}")
                elif var_type == "bool":
                    self.code.append("push B false")
                    self.code.append(f"save {name}")
                elif var_type == "string" or var_type == "FILE":
                    self.code.append('push S ""')
                    self.code.append(f"save {name}")


    def visitAssignement(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        var_name = ctx.getChild(0).getText()
        var_type = self.variables.get(var_name)
        self.visit(ctx.getChild(2))  # Navštív pravú stranu priradenia
        expr_type = self.getExpressionType(ctx.getChild(2))

        if var_type == "float" and expr_type == "int":
            self.code.append("itof")
        self.code.append(f"save {var_name}")

    def visitExpression(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitConcatExpression(self, ctx):
        self.visit(ctx.orExpression(0))
        for i in range(1, len(ctx.orExpression())):
            self.visit(ctx.orExpression(i))
            self.code.append("concat")

    def visitOrExpression(self, ctx):
        self.visit(ctx.andExpression(0))
        for i in range(1, len(ctx.andExpression())):
            self.visit(ctx.andExpression(i))
            self.code.append("or")

    def visitAndExpression(self, ctx):
        self.visit(ctx.equality(0))
        for i in range(1, len(ctx.equality())):
            self.visit(ctx.equality(i))
            self.code.append("and")

    def visitEquality(self, ctx):
        self.visit(ctx.relational(0))
        left_type = self.getExpressionType(ctx.relational(0))

        for i in range(1, len(ctx.relational())):
            op = ctx.getChild(2 * i - 1).getText()
            right_expr = ctx.relational(i)
            right_type = self.getExpressionType(right_expr)

            # Konverzie ak treba
            if left_type == "int" and right_type == "float":
                self.code.append("itof")
                self.visit(right_expr)
                self.code.append("eq F")
                left_type = "float"
            elif left_type == "float" and right_type == "int":
                self.visit(right_expr)
                self.code.append("itof")
                self.code.append("eq F")
                left_type = "float"
            else:
                self.visit(right_expr)
                if left_type == "string":
                    self.code.append("eq S")
                elif left_type == "bool":
                    self.code.append("eq B")
                elif left_type == "float":
                    self.code.append("eq F")
                else:
                    self.code.append("eq I")

            if op == "!=":
                self.code.append("not")
            left_type = left_type  # typ po porovnaní je bool, ale pre konzistenciu

    def visitRelational(self, ctx):
        self.visit(ctx.additive(0))
        left_type = self.getExpressionType(ctx.additive(0))

        for i in range(1, len(ctx.additive())):
            op = ctx.getChild(2 * i - 1).getText()
            right_expr = ctx.additive(i)
            right_type = self.getExpressionType(right_expr)

            if left_type == "int" and right_type == "float":
                self.code.append("itof")
                self.visit(right_expr)
                self.code.append("gt F" if op == ">" else "lt F")
                left_type = "float"
            elif left_type == "float" and right_type == "int":
                self.visit(right_expr)
                self.code.append("itof")
                self.code.append("gt F" if op == ">" else "lt F")
                left_type = "float"
            else:
                self.visit(right_expr)
                instr_type = "F" if left_type == "float" else "I"
                if op == "<":
                    self.code.append(f"lt {instr_type}")
                elif op == ">":
                    self.code.append(f"gt {instr_type}")
                left_type = left_type  # zostáva

    def visitAdditive(self, ctx):
        self.visit(ctx.multiplicative(0))
        left_type = self.getExpressionType(ctx.multiplicative(0))
        for i in range(1, len(ctx.multiplicative())):
            right_expr = ctx.multiplicative(i)
            op = ctx.getChild(2 * i - 1).getText()

            self.visit(right_expr)
            right_type = self.getExpressionType(right_expr)

            if op == "+":
                if left_type == "float" or right_type == "float":
                    if left_type == "int":
                        self.code.append("itof")
                    if right_type == "int":
                        self.code.append("itof")
                    self.code.append("add F")
                    left_type = "float"
                else:
                    self.code.append("add I")
                    left_type = "int"
            elif op == "-":
                if left_type == "float" or right_type == "float":
                    if left_type == "int":
                        self.code.append("itof")
                    if right_type == "int":
                        self.code.append("itof")
                    self.code.append("sub F")
                    left_type = "float"
                else:
                    self.code.append("sub I")
                    left_type = "int"
            elif op == ".":
                self.code.append("concat")
                left_type = "string"

    def visitMultiplicative(self, ctx):
        self.visit(ctx.unary(0))
        left_type = self.getExpressionType(ctx.unary(0))
        for i in range(1, len(ctx.unary())):
            right_expr = ctx.unary(i)
            op = ctx.getChild(2 * i - 1).getText()

            self.visit(right_expr)
            right_type = self.getExpressionType(right_expr)

            if op == "*":
                if left_type == "float" or right_type == "float":
                    if left_type == "int":
                        self.code.append("itof")
                    if right_type == "int":
                        self.code.append("itof")
                    self.code.append("mul F")
                    left_type = "float"
                else:
                    self.code.append("mul I")
                    left_type = "int"
            elif op == "/":
                if left_type == "float" or right_type == "float":
                    if left_type == "int":
                        self.code.append("itof")
                    if right_type == "int":
                        self.code.append("itof")
                    self.code.append("div F")
                    left_type = "float"
                else:
                    self.code.append("div I")
                    left_type = "int"
            elif op == "%":
                self.code.append("mod")
                left_type = "int"

    def visitUnary(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        op = ctx.getChild(0).getText()
        self.visit(ctx.getChild(1))
        if op == "-":
            self.code.append("uminus I")
        elif op == "!":
            self.code.append("not")

    def visitPrimary(self, ctx):
        if ctx.ID():
            name = ctx.ID().getText()
            self.code.append(f"load {name}")
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.expression():
            return self.visit(ctx.expression())

    def visitLiteral(self, ctx):
        if ctx.INT():
            self.code.append(f"push I {ctx.INT().getText()}")
        elif ctx.FLOAT():
            self.code.append(f"push F {ctx.FLOAT().getText()}")
        elif ctx.STRING():
            self.code.append(f'push S {ctx.STRING().getText()}')
        elif ctx.BOOL():
            self.code.append(f"push B {ctx.BOOL().getText()}")

    def visitWrite(self, ctx):
        n = len(ctx.expression())
        for expr in ctx.expression():
            self.visit(expr)
        self.code.append(f"print {n}")

    def visitRead(self, ctx):
        for id_ in ctx.ID():
            name = id_.getText()
            var_type = self.variables.get(name, "int")
            self.code.append(f"read {var_type[0].upper()} {name}")
            self.code.append(f"save {var_type[0].upper()} {name}")

    def visitIfCondition(self, ctx):
        else_label = self.new_label()
        end_label = self.new_label()

        self.visit(ctx.expression())  
        self.code.append(f"fjmp {else_label}")  

        self.visit(ctx.statement(0)) 
        self.code.append(f"jmp {end_label}")  

        self.code.append(f"label {else_label}")
        if ctx.statement(1):  
            self.visit(ctx.statement(1))

        self.code.append(f"label {end_label}")

    def visitWhileCondition(self, ctx):
        start_label = self.new_label()
        end_label = self.new_label()

        self.code.append(f"label {start_label}")
        self.visit(ctx.expression()) 
        self.code.append(f"fjmp {end_label}")

        self.visit(ctx.statement())  
        self.code.append(f"jmp {start_label}")  

        self.code.append(f"label {end_label}")
         
    def visitFileWrite(self, ctx):
        file_name = ctx.ID().getText()
        for expr in ctx.assignment():
            self.visit(expr)
            self.code.append(f"load {file_name}")
            self.code.append(f"fwrite {file_name}")

    