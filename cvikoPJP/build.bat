@echo off
echo Building ANTLR4 Parser...
java -Xmx500M -cp "C:\antlr\antlr-4.13.0-complete.jar" org.antlr.v4.Tool -Dlanguage=Python3 -visitor PLC_Lab7_expr.g4
pause