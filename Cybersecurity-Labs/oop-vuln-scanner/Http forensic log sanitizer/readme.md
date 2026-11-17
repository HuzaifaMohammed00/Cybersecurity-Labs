# 🛡️ HTTP Forensic Log Sanitizer (`Meta Python - Module 3`)

**Author:** Huzaifa Mohammed (`HuzaifaMohammed00`)  
**Course:** [Programming in Python by Meta (Coursera)](https://www.coursera.org/learn/programming-in-python) — Module 3: Programming Paradigms  
**Category:** Functional & Procedural Programming | Web Security Log Analysis  

## 📌 Scenario

During web application incident response and penetration testing, security analysts inspect raw HTTP access logs to identify attack attempts such as **SQL Injection (`SQLi`)**, **Cross-Site Scripting (`XSS`)**, and **Path Traversal (`LFI`)**. A critical forensic rule is **Immutability**: original raw logs must never be mutated in memory while parsing, filtering, or redacting malicious payloads.

To apply the **Procedural** and **Functional Programming** concepts from Module 3 of [Meta's Programming in Python course](https://www.coursera.org/learn/programming-in-python), I built a CLI-driven HTTP log analyzer (`project1_log_sanitizer.py`) from scratch that parses, filters, summarizes, and sanitizes web logs without mutating the original forensic dataset.

## 🔍 Step-by-Step Walkthrough

1. **Preserving Forensic Evidence via Pure Functions (`add_log_entry_pure`)**:
   - Copies the input log list using `.copy()` before appending new entries so the original `RAW_HTTP_LOGS` list remains untouched in memory ([TechGeekBuzz Functional Programming Guide](https://www.techgeekbuzz.com/blog/functional-programming-languages)).

2. **Normalizing Raw Logs with `map()` (`parse_log_single`)**:
   - Splits raw pipe-delimited log strings (`IP | METHOD | ENDPOINT | STATUS`), strips whitespace, normalizes HTTP methods to uppercase, converts status codes to integers, and maps the transformation across all logs via `list(map(parse_log_single, RAW_HTTP_LOGS))`.

3. **Hunting Attack Payloads with `filter()` (`is_suspicious_request`)**:
   - Uses Python's `any()` generator expression to test lowercased endpoints against common attack signatures (`or 1=1--`, `<script>`, `../`, `../../etc`, `union`, `admin`) and isolates malicious traffic using `list(filter(is_suspicious_request, parsed_logs))`.

4. **Building One-Line Security Reports (`Set & List Comprehensions`)**:
   - Extracts deduplicated attacker IPs using a **Set Comprehension** (`{susreq["ip"] for susreq in suspicious_logs}`).
   - Formats high-priority security alerts for HTTP status codes `>= 400` using a conditional **List Comprehension**.
   - Aggregates request frequency per IP address using `.get(ip, 0) + 1`.

5. **Measuring URL Depth with `Recursion` (`count_segments_recursive`)**:
   - Strips query parameters (`?...`), splits the URL path into segments, and calculates path depth recursively using a clean base case (`if segment_list == []: return 0`) and recursive step (`count_segments_recursive(segment_list[1:]) + 1`) ([freeCodeCamp Programming Paradigms](https://www.freecodecamp.org/news/what-exactly-is-a-programming-paradigm/)).

6. **Redacting Dangerous Characters (`sanitize_log`) & Interactive CLI (`main`)**:
   - Replaces dangerous payload characters (`'`, `<`, `>`, `..`) with `[REDACTED]` on a copied dictionary so raw evidence stays intact, wrapped inside an interactive terminal menu (`Options 0–6`).

### 💻 How to Run

```bash
python3 project1_log_sanitizer.py
```

## 💡 Key Takeaways

- **Why Pure Functions Matter in Security**: Defining a dictionary in the global scope causes every iteration of `map()` to overwrite the same memory reference. Creating local copies inside functions guarantees data integrity and prevents accidental evidence tampering.
- **`map()` & `filter()` vs. Manual Loops**: Separating predicate logic (`is_suspicious_request`) from display logic makes security rules modular and reusable across different log sources.
- **Thinking Recursively**: Instead of maintaining manual loop counters, recursion reduces a list slice by slice (`segment_list[1:]`) until hitting the empty-list base case.
