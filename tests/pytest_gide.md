---

# Pytest Parallel Execution with HTML Report - Usage Guide
This guide explains how to run tests in parallel using `pytest-xdist`, while generating a full, self-contained HTML report with logging, and includes optional benchmarking support.

---

## Requirements

Install the following packages:

```bash
pip install pytest-xdist pytest-html
```

To include optional benchmark reporting:

```bash
pip install pytest-benchmark
```

---

## Run Tests in Parallel with HTML Report

Basic command to run tests in parallel and generate an HTML report:

```bash
python -m pytest -n auto -s --log-cli-level=INFO \
    --capture=tee-sys \
    --html=report.html \
    --self-contained-html \
    tests/test_communication.py
```

---

## Run Tests in Debug Mode with Logging to File

Run tests with debug-level logging and save both the HTML report and full logs to `output.log`:

```bash
python -m pytest -n auto -s --log-cli-level=DEBUG \
    --capture=tee-sys \
    --html=report.html \
    --self-contained-html \
    tests/test_communication.py > output.log 2>&1
```

---

## Explanation of Flags

| Flag                      | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `-n auto`                 | Automatically uses all available CPU cores for parallel test execution      |
| `-s`                      | Displays real-time `print()` and logging output in the console              |
| `--log-cli-level=LEVEL `   | Sets the logging level (`INFO`, `DEBUG`, etc.)                              |
| `--capture=tee-sys`       | Captures stdout/stderr and shows it in both terminal and HTML report        |
| `--html=report.html`      | Path to generate the HTML test report                                       |
| `--self-contained-html`   | Embeds all CSS/JS in the HTML report for full portability                   |

---

## Benchmark Test Documentation

You can write benchmark tests using the `benchmark` fixture from `pytest-benchmark`. Example:

```python
def test_my_function_benchmark(benchmark):
    result = benchmark(my_function_to_test)
    assert result is not None
```

Run the benchmark tests:

```bash
pytest tests/test_benchmark.py
```

### Generate Benchmark JSON Output:

```bash
pytest --benchmark-only --benchmark-json=benchmark.json
```

### Optional: Compare Two Benchmark Runs

First run:

```bash
pytest --benchmark-save baseline
```

Second run (to compare):

```bash
pytest --benchmark-compare
```

---

## Open the HTML Report

After test execution, open `report.html` in any browser. It includes:

- Pass/Fail summary
- Execution time per test
- Captured logs and print outputs
- Parameterized test values (if used)

---

## Summary

With this setup, you get:

- Fast parallel test execution
- Full HTML reports with embedded logs
- Optional debug log files for troubleshooting
- Benchmark performance tracking and comparison



---

