from PLC_GrammarVisitor import PLC_GrammarVisitor
from PLC_GrammarParser import PLC_GrammarParser

class TypeCheckerVisitor(PLC_GrammarVisitor):
    def __init__(self):
        self.symbol_table = {} # Meno premenej -> typ
        self.errors = []

    # Nastivenie kazdeho prikazu (int x, x=5 atd.)
    def visitProg(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        return self.errors

    def visitDeclaration(self, ctx):
        var_type = ctx.type_().getText()
        for id_token in ctx.ID():
            var_name = id_token.getText()
            if var_name in self.symbol_table:
                self.errors.append(f"Chyba: Premenná '{var_name}' už bola deklarovana.")
            else:
                self.symbol_table[var_name]= var_type
        return None
    
    def visitRead(self, ctx):
        for id_token in ctx.ID():
            var_name = id_token.getText()
            if var_name not in self.symbol_table:
                self.errors.append(f"Chyba: Premenná '{var_name}' nie je deklarovana.")

    def visitWrite(self, ctx):
        for expr in ctx.expression():
            self.visit(expr)
    
    def visitBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
    
    def visitIfCondition(self, ctx):
        cond_type = self.visit(ctx.expression())
        if cond_type != "bool":
            self.errors.append("Chyba: Podmienka v 'if' musi mat typ bool.")
        self.visit(ctx.statement(0))
        if ctx.statement(1):
            self.visit(ctx.statement(1))

    def visitWhileCondition(self, ctx):
        cond_type = self.visit(ctx.expression())
        if cond_type != "bool":
            self.errors.append("Chyba: Podmienka vo 'while' musi mat typ bool.")
        self.visit(ctx.statement())
        
    def visitDoWhileCondition(self, ctx):
        self.visit(ctx.statement())
        cond_type = self.visit(ctx.expression())
        if cond_type != "bool":
            self.errors.append("Chyba: Podmienka v 'do while' musi mat typ bool.")

            
            
    def visitAssignment(self, ctx):
        if ctx.getChildCount() == 3:
            left_expr = ctx.getChild(0)
            right_expr = ctx.getChild(2)

            left_var = left_expr.getText()
            if left_var not in self.symbol_table:
                self.errors.append(f"Chyba: Premenná '{left_var}' nie je deklarovana.")
                return None
            left_type = self.symbol_table[left_var]
            right_type = self.visit(right_expr)

            if right_type == left_type:
                return left_type
            elif left_type == "float" and right_type == "int":
                return left_type
            elif right_type is None:
                return None
            else:
                self.errors.append(f"Chyba: Nemožno priradiť typ '{right_type}' do '{left_type}'.")
                return None
        else:
            return self.visit(ctx.or_()) 

    
    def visitOr(self, ctx):
        left_type = self.visit(ctx.and_(0))
        for i in range(1, len(ctx.and_())):
            right_type = self.visit(ctx.and_(i))
            if left_type != "bool" or right_type != "bool":
                self.errors.append(f"Chyba: Operátor '||' je definovany len pre bool.")
                return None
            left_type = "bool"
        return left_type
    
    def visitAnd(self, ctx):
        left_type = self.visit(ctx.equality(0))
        for i in range(1, len(ctx.equality())):
            right_type = self.visit(ctx.equality(i))
            if left_type != "bool" or right_type != "bool":
                self.errors.append(f"Chyba: Operátor '&&' je definovany len pre bool.")
                return None
            left_type = "bool"
        return left_type

    def visitEquality(self, ctx):
        left_type = self.visit(ctx.relational(0))
        for i in range(1, len(ctx.relational())):
            right_type = self.visit(ctx.relational(i))
            if left_type != right_type:
                self.errors.append(f"Chyba: Porovnavanie typov '{left_type}' a '{right_type}' nie je povolene.")
                return None
            left_type = "bool"
        return left_type

    def visitRelational(self, ctx):
        left_type = self.visit(ctx.additive(0))
        for i in range(1, len(ctx.additive())):
            right_type = self.visit(ctx.additive(i))
            if left_type not in ["int", "float"] or right_type not in ["int", "float"]:
                self.errors.append(f"Chyba: Relacny operator je definovany len pre int alebo float, nie '{left_type}' a '{right_type}'.")
                return None
            left_type = "bool"
        return left_type

    def visitAdditive(self, ctx):
        left_type = self.visit(ctx.multiplicative(0))
        for i in range(1, len(ctx.multiplicative())):
            right_type = self.visit(ctx.multiplicative(i))
            op = ctx.getChild(2 * i - 1).getText()

            if op == ".":
                if left_type == right_type == "string":
                    left_type = "string"
                else:
                    self.errors.append(f"Chyba: Operátor '.' je definovany len pre string + string.")
                    return None
            elif left_type == "int" and right_type == "int":
                left_type = "int"
            elif (left_type == "int" and right_type == "float") or (left_type == "float" and right_type == "int") or (left_type == "float" and right_type == "float"):
                left_type = "float"
            else:
                self.errors.append(f"Chyba: Nespravne typy '{left_type}' {op} '{right_type}'.")
                return None
        return left_type

    
    def visitMultiplicative(self, ctx):
        left_type = self.visit(ctx.unary(0))
        for i in range(1, len(ctx.unary())):
            right_type = self.visit(ctx.unary(i))
            op = ctx.getChild(2 * i - 1).getText()

            if op == "%":
                if left_type == right_type == "int":
                    left_type = "int"
                else:
                    self.errors.append(f"Chyba: Operátor '%' je definovany len pre int.")
                    return None
            elif left_type == "int" and right_type == "int":
                left_type = "int"
            elif (left_type == "int" and right_type == "float") or (left_type == "float" and right_type == "int") or (left_type == "float" and right_type == "float"):
                left_type = "float"
            else:
                self.errors.append(f"Chyba: Nespravne typy '{left_type}' {op} '{right_type}'.")
                return None
        return left_type
     
    def visitUnary(self, ctx):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            expr_type = self.visit(ctx.primary())
            if op == "-":
                if expr_type not in ["int", "float"]:
                    self.errors.append(f"Chyba: Unarny minus je povoleny len pre int alebo float, nie '{expr_type}'.")
                    return None
                return expr_type
            elif op == "!":
                if expr_type != "bool":
                    self.errors.append(f"Chyba: Unarny operator '!' je povoleny len pre bool, nie '{expr_type}'.")
                    return None
                return "bool"
        else:
            return self.visit(ctx.primary())
    
    def visitPrimary(self, ctx):
        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in ["true", "false"]:
                return "bool"
            if var_name not in self.symbol_table:
                self.errors.append(f"Chyba: Premenná '{var_name}' nie je deklarovana.")
                return None
            return self.symbol_table[var_name]
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.expression():
            return self.visit(ctx.expression())

    def visitLiteral(self, ctx):
        if ctx.INT():
            return "int"
        if ctx.BOOL():
            return "bool"
        if ctx.STRING():
            return "string"
        if ctx.FLOAT():
            return "float"

    

    

