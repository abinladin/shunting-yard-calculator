# Shunting Yard Calculator

## Description

The ```Main.py``` file is composed of three functions:
- ```tokenizer```, which takes a mathematical expression in the form of an input string, and returns a list of tokens comprising integers and operators
- ```shunting_yard```, which implements Djikstra's shunting yard algorithm, converting the list from ```tokenizer``` into a Reverse Polish Notation format`
- ```rpn_evaluate```, which evaluates the RPN list from ```shunting_yard``` to a solution.

The script currently lacks support for floating point numbers and negative numbers.

## License
MIT License

Copyright &copy; 2023 Abdullah Binladin 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.