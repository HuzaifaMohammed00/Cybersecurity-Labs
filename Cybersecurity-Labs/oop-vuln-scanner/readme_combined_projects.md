# 🛡️ Python Programming Paradigms in Cybersecurity (`Meta Python - Module 3`)

**Author:** Huzaifa Mohammed (`HuzaifaMohammed00`)  
**Course:** [Programming in Python by Meta (Coursera)](https://www.coursera.org/learn/programming-in-python) — Module 3: Programming Paradigms  
**Focus:** Procedural, Functional & Object-Oriented Programming (`OOP`) Applied to Web Security  

## 📌 Scenario

After completing Module 3 (`Programming Paradigms`) of [Meta's Programming in Python course](https://www.coursera.org/learn/programming-in-python), I built two practical cybersecurity tools from scratch to apply **Procedural**, **Functional**, and **Object-Oriented Programming (`OOP`)** to real-world web security workflows: preserving forensic HTTP logs and building a modular vulnerability scanner.

## 🔍 Step-by-Step Walkthrough

### 1. Project 1: HTTP Forensic Log Sanitizer (`project1_log_sanitizer.py`) — *Procedural & Functional*
- **Immutability & Pure Functions**: Built `add_log_entry_pure()` and `sanitize_log()` using `.copy()` so raw forensic logs (`RAW_HTTP_LOGS`) are never mutated in memory ([TechGeekBuzz](https://www.techgeekbuzz.com/blog/functional-programming-languages)).
- **`map()`, `filter()` & Comprehensions**: Normalized raw pipe-delimited logs into dictionaries with `map()`, isolated `SQLi`/`XSS`/`LFI` requests with `filter()`, and generated attacker IP sets and status `>= 400` alerts using Set and List Comprehensions.
- **Recursion**: Implemented `count_segments_recursive()` to measure URL endpoint depth without loops or `len()` ([freeCodeCamp](https://www.freecodecamp.org/news/what-exactly-is-a-programming-paradigm/)).

### 2. Project 2: Modular Web Vulnerability Scanner (`project2_oop_scanner.py`) — *Object-Oriented Programming (`OOP`)*
- **Abstraction & Encapsulation**: Created an abstract base class `Scanner(ABC)` with `@abstractmethod run_check()`, a private token `self.__api_token`, and a protected findings list `self._finding = []` ([Adaface Python OOP Guide](https://www.adaface.com/blog/python-oops-interview-questions/)).
- **Inheritance & `super()`**: Built `SQLInjectionScanner` (extending `__init__` via `super()` to add `db_engine`), plus `XSSScanner` and `HeaderScanner` (inheriting parent initialization directly).
- **Mixins, `MRO` & Polymorphism**: Combined `ReportMixin` and `SQLInjectionScanner` into `AdvancedSQLiScanner`, inspected `.mro()`, and executed all scanners together in a unified polymorphic loop.

### 💻 How to Run

```bash
python3 project1_log_sanitizer.py
python3 project2_oop_scanner.py
```

## 💡 Key Takeaways

- **Functional Programming (`Immutability`)** is ideal for security data pipelines and forensic log analysis where raw evidence must remain unaltered.
- **Object-Oriented Programming (`ABC`, `Inheritance`, `Mixins`, `Polymorphism`)** is ideal for extensible security engines and directly prepares for **Django's Class-Based Views (`CBVs`)** and `Models`.
