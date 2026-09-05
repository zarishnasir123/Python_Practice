# Python Practice

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-actively%20learning-brightgreen?style=flat-square)
![Chapters](https://img.shields.io/badge/chapters%20completed-6-blue?style=flat-square)

A structured, chapter-by-chapter log of my journey learning Python from the ground up — every
concept file, exercise, and problem-set solution I write while working through the fundamentals.

Each chapter pairs **concept files** (annotated code I write while learning a topic) with a
**problem set** (`Chapter N PS/`) where I solve exercises on that topic without notes. The goal is
consistent, visible practice — not polished production code.

---

## Table of Contents

- [About This Repository](#about-this-repository)
- [Topics Covered](#topics-covered)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Roadmap](#roadmap)
- [Author](#author)

---

## About This Repository

I'm learning Python by writing code every day rather than only reading about it. This repository is
the record of that work:

- **Concept files** — heavily commented scripts where I break down a single idea (slicing, list
  methods, type conversion) and prove to myself that I understand it.
- **Problem sets** — self-contained exercise solutions, one file per problem, kept exactly as I
  solved them so my progress over time stays honest and traceable.
- **Daily commits** — small, frequent commits that reflect real, incremental learning.

---

## Topics Covered

| # | Chapter | Concepts | Practice |
|:-:|---------|----------|:--------:|
| 1 | **Getting Started** | `print()`, comments, running scripts, importing external modules (`pyjokes`, `pyttsx3`), the `os` module | ✅ |
| 2 | **Variables & Data Types** | `int`, `float`, `str`, `bool`, `None`, naming rules, `input()`, implicit vs. explicit type conversion, arithmetic / comparison / logical operators | ✅ |
| 3 | **Strings** | Quoting styles, indexing, negative indexing, slicing with steps, string methods, `.replace()`, f-strings | ✅ |
| 4 | **Lists & Tuples** | Mutability, indexing and slicing, `append` / `insert` / `pop` / `sort` / `reverse`, tuple immutability, packing & unpacking, `count()` and `index()` | ✅ |
| 5 | **Dictionaries & Sets** | Key–value pairs, nested dictionaries, dictionary methods, set uniqueness rules, `add` / `update` / `remove` / `discard`, `{}` vs. `set()` | ✅ |
| 6 | **Conditional Expressions** | `if` / `elif` / `else`, independent vs. chained conditions, comparison logic, branching on user input | ✅ |

---

## Repository Structure

```
Python Practice/
├── Chapter 1/                  # Getting started with Python
│   ├── first.py                # First program
│   ├── module.py               # Working with external modules
│   └── Chapter 1 - PS/         # Problem set
├── Chapter 2/                  # Variables, data types & operators
│   ├── variables.py
│   ├── datatypes.py
│   ├── rules_var.py
│   ├── input.py
│   └── type.py                 # Type conversion
├── Chapter 3/                  # Strings
│   ├── string.py
│   └── Chapter 3 PS/
├── Chapter 4/                  # Lists & tuples
│   ├── 1_list.py
│   ├── 2_listmethods.py
│   ├── 3_listtuple.py
│   └── Chapter 4 PS/
├── Chapter 5/                  # Dictionaries & sets
│   ├── dict.py
│   ├── set.py
│   └── Chapter 5 PS/
└── Chapter 6/                  # Conditional expressions
    ├── conditionals.py
    └── quiz.py
```

---

## Getting Started

### Prerequisites

- [Python 3.10+](https://www.python.org/downloads/) (developed on 3.13)

### Clone the repository

```bash
git clone https://github.com/zarishnasir123/Python_Practice.git
cd Python_Practice
```

### Run any script

```bash
python "Chapter 4/2_listmethods.py"
```

### Optional dependencies

Two scripts in Chapter 1 use third-party libraries. Install them only if you want to run those files:

```bash
pip install pyjokes pyttsx3
```

| Library | Used in | Purpose |
|---------|---------|---------|
| `pyjokes` | `Chapter 1/module.py` | Demonstrates importing and using an external module |
| `pyttsx3` | `Chapter 1 - PS/prob3.py` | Offline text-to-speech |

> **Note:** Several scripts read from `input()`, so run them from a terminal rather than a
> non-interactive runner.

---

## Roadmap

Concepts I'm working toward next:

- [ ] Loops (`for`, `while`, `break`, `continue`)
- [ ] Functions & recursion
- [ ] File I/O
- [ ] Object-oriented programming
- [ ] Exception handling
- [ ] Modules, packages & virtual environments
- [ ] Small end-to-end projects applying the above

---

## Author

**Zarish Nasir**

[![GitHub](https://img.shields.io/badge/GitHub-zarishnasir123-181717?style=flat-square&logo=github)](https://github.com/zarishnasir123)

---

<p align="center"><i>Learning in public — one chapter at a time. ⭐ Star the repo to follow along.</i></p>
