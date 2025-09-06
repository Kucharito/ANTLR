# 📘 ANTLR Projects

This repository contains multiple practice and semester projects created with **ANTLR**.  
Each folder represents an independent project with its own grammar and example usage.

---

## 🔧 How to Run
In all project folders you can run:

```bash
.\build.bat
.\run.bat
```

# 📂 Projects

## 1. HelloWorld
- The simplest example of using ANTLR.  
- Contains a minimal grammar and generated parser.

## 2. MathExpr
- Parser for mathematical expressions.  
- Supports basic operations `+ - * /` and expression evaluation.

## 3. MyLangCalc
- A simple calculator-like language.  
- Allows variable assignments, calculations, and printing results.

## 4. ProjektANTLR
- Main semester project.  
- Implements a parser for a custom PLC-like language according to assignment.  
- Includes:
  - **TypeChecker**
  - **CodeGeneratorVisitor**
  - **Interpreter** for stack-based code

## 5. ProjektANTLR2 – ProjektANTLRf
- Extended versions of the main project.  
- Step-by-step improvements:
  - Support for `if`, `while`, `for`
  - Automatic type conversion (`int → float`)
  - File handling with **FILE** type and writing (`f << ...`)
  - Reverse translation from stack-based code back to PLC-like source code

## 6. ProjektDoWhile
- Demonstration of `do ... while` loop implementation in ANTLR.

---

# 🛠 Technologies
- **ANTLR4**
- **Java / Python** (depending on the project folder)
- Custom `.g4` grammars
- Visitor classes for:
  - Type checking
  - Code generation
  - Interpretation of stack-based code

# 🧑‍💻 Author
Created by **Adam Kuchár**  
Developed as exercises and a semester project for the **PJP course**.