# Visla

A Simple Syntax Drawing Language

![repo status wip](https://www.repostatus.org/badges/latest/wip.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![Language](https://img.shields.io/badge/python-3.9-blue.svg)

## Purpose:

This language was written as an educational tool for myself to understand the components and composition of a "programming" language. For this reasons Visla uses the following conventional language components:

- Lexer
- Tokenization
- Parser
- Abstract Synax Tree
- Interpreter

## Installation:
- Todo

## Syntax:

Visla in its current early state uses a very json esc syntax as can be seen below:

```
canvas{
    width = 300;
    height = 300;
    line {
        width = 1;
        start = (50,0);
        end = (50, 100);
        color = (255, 255, 255);
    };
    line {
        start = (0,50);
        end = (100, 50);
        color = (0, 255, 0);
    };
    rect {
        center = (50,50);
        width = 100;
        height = 100;
        color = (0, 0, 255);
    };
    ellipse {
        center = (50,50);
        width = 100;
        height = 100;
        color = (255, 0, 0);
    };
};
```

Which will create the following drawing:
![](https://github.com/cmmeyer1800/visla/blob/main/assets/simple_example.png?raw=true)