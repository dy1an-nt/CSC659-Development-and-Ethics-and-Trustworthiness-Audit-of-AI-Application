# Trustworthiness Audit of AI Code Generation Tools
### CSC 659/859 – Ethical and Trustworthy AI · Team 06 · San Francisco State University · Spring 2026

---

## Overview

This repository contains all testing artifacts, execution logs, and analysis from a structured empirical audit of three major AI code generation tools — **ChatGPT (GPT-5.5)**, **Claude (Claude 4 Sonnet)**, and **DeepSeek (V4)** — evaluated across 150 live coding test cases.

The goal was to measure how trustworthy these tools are for real software development workflows, using a five-dimensional rubric covering correctness, completeness, code quality, efficiency, and explainability.

---

## Team

| Name | Role |
|------|------|
| Dylan Gabe Teopaco | Claude Model Tester · Execution & Verification Lead |
| Daniel Smirnoff | ChatGPT Model Tester |
| Sergei Strizhov | DeepSeek Model Tester |
| Cassie Wang | Project Coordination & Report |

---

## What Was Tested

**50 standardized coding prompts** submitted to each of the 3 models — 150 total test cases.

| Difficulty | Python | C++ | Java | Total |
|------------|--------|-----|------|-------|
| Easy | 6 | 5 | 5 | 16 |
| Medium | 6 | 6 | 5 | 17 |
| Hard | 6 | 5 | 6 | 17 |
| **Total** | **18** | **16** | **16** | **50** |

**Task categories covered:**
- Core algorithms: binary search, two-sum, longest palindromic substring, Dijkstra's shortest path
- Data structures: linked list, stack (array-backed), binary search tree with deletion
- Object-oriented design: inheritance, interfaces, method overriding, SOLID/SRP refactoring
- Concurrency: multithreading, thread-safe singleton (double-checked locking), producer-consumer with mutex/condition_variable, deadlock detection and prevention
- Memory management: RAII, `unique_ptr`, `shared_ptr`, Rule of Three, dangling pointer diagnosis
- Security: SQL injection prevention (parameterized queries), memory leak identification, segmentation fault root-cause analysis
- Language features: Python decorators, Java Stream API + Records, C++ lambda sorting, `std::map`

---

## Evaluation Rubric

Each of the 150 responses was scored on a 1–5 scale across five weighted dimensions:

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| Correctness | 30% | Compiles, runs, and produces exact expected output |
| Completeness | 20% | Handles edge cases, null/empty inputs, boundary conditions |
| Code Quality | 20% | Follows PEP 8 / Google C++ Style; readable and modular |
| Efficiency | 15% | Optimal time and space complexity for the problem |
| Explainability | 15% | Explanation is accurate, clear, and useful for human review |

---

## Results Summary

| Model | Pass Rate | Avg Score | Follow-up Prompts Needed |
|-------|-----------|-----------|--------------------------|
| Claude 4 Sonnet | **100%** (50/50) | **4.94 / 5.0** | 0 |
| ChatGPT GPT-5.5 | **100%** (50/50) | **4.94 / 5.0** | 0 |
| DeepSeek V4 | 98% (49/50) | 4.48 / 5.0 | 7 |

**Key findings:**
- Claude and ChatGPT tied for first — every response compiled and ran correctly on the first attempt, with zero follow-up corrections needed across all 50 prompts.
- DeepSeek critically failed on P50 (Dijkstra's algorithm — Java Hard) due to hallucinated graph variable state that could not be resolved after multiple follow-ups.
- All three models performed well on security audit prompts (SQL injection, memory leaks, deadlocks) — none reproduced unsafe code.
- DeepSeek's lowest scores were concentrated in Hard Java tasks, driven by missing imports, missing `main()` methods, and verbose/unverifiable explanations.

---

## How to Run the Test Harness

**Requirements:**
- Python 3.10+
- `g++` with C++14 or later (`brew install gcc` on macOS / `apt install g++` on Linux)
- Java 14+ (`javac` and `java` on PATH)

**Run all 50 Claude prompt executions:**

```bash
cd run_tests
python3 run_all.py
```

This will:
1. Write all source files to `python/`, `cpp/`, and `java/` subdirectories
2. Compile all C++ programs with the appropriate flags
3. Compile and run all Java programs in isolated directories
4. Run all Python scripts
5. Capture stdout, stderr, and exit codes for each
6. Save a full results report to `execution_results.md`

Expected output: **50/50 PASS**

---

## Testing Methodology

- All prompts were submitted through the official **web browser interfaces** of each AI tool — no API tokens, IDE plugins, or code interpreter extensions were used.
- Each tester was assigned exclusively to one model (Dylan → Claude, Daniel → ChatGPT, Sergei → DeepSeek) to prevent cross-contamination.
- A calibration meeting was held before testing began to align scoring standards across all three testers.
- All code was executed locally in the tester's own development environment. Results were verified by hand.
- Full chat histories were preserved as timestamped PDF logs and collected as provenance artifacts.
- Follow-up prompts were permitted up to a maximum of 3 iterations per failed response; the exact count was recorded as a core ease-of-use metric.

---

## Ethical Considerations

This audit examined the following trustworthiness dimensions in the context of AI code generation:

- **Accuracy & Reliability** — Pass rates and score distributions across difficulty levels and languages
- **Safety & Security** — Behavior on prompts involving SQL injection, memory leaks, dangling pointers, and deadlocks
- **Transparency & Explainability** — Quality and accuracy of AI-provided explanations alongside generated code
- **Human Oversight** — Documentation of where AI output required correction and why human verification is mandatory
- **Privacy** — No private data, API keys, credentials, or proprietary code was submitted to any AI tool during testing
- **Fairness** — Analysis of how verbose or confusing AI responses may disadvantage less experienced developers

**Main finding on oversight:** Human compilation, execution, and review are mandatory before trusting any AI-generated code. A confident explanation is not proof of correctness.

---

## Environment

| Component | Version |
|-----------|---------|
| Python | 3.13.9 |
| C++ Compiler | Apple Clang 16.0.0 |
| Java | OpenJDK 25.0.2 |
| Testing Period | May 2026 |
| Claude Model | claude-sonnet-4-20250514 |
| ChatGPT Model | GPT-5.5 |
| DeepSeek Model | V4 / R1 Architecture |

---

## References

- Chen, M. et al. (2021). *Evaluating Large Language Models Trained on Code.* OpenAI. [HumanEval benchmark]
- Yetiştiren, B. et al. (2023). *Evaluating the Code Quality of AI-Assisted Code Generation Tools: An Empirical Study on GitHub Copilot, Amazon CodeWhisperer, and ChatGPT.*

---

*CSC 659/859 – Ethical and Trustworthy AI · San Francisco State University · Spring 2026*
