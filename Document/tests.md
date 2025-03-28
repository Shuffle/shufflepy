# Test Case Execution & Benchmarking Guide

This guide helps you run Singul SDK test cases efficiently using `pytest`, along with parallel execution, HTML reporting, logging, and optional benchmarking.

***

### Requirements

Install the necessary testing tools:

```bash
pip install pytest-xdist pytest-html
```

To include performance benchmarking support:

```bash
pip install pytest-benchmark
```

***

### Running Tests in Parallel with HTML Report

Execute test cases in parallel and generate a styled HTML report:

```bash
python -m pytest -n auto -s --log-cli-level=INFO \
    --capture=tee-sys \
    --html=report.html \
    --self-contained-html \
    tests/test_communication.py
```

***

### Debug Mode with Log File Output

Run tests with **debug-level logging**, and save both the HTML report and a full log output:

```bash
python -m pytest -n auto -s --log-cli-level=DEBUG \
    --capture=tee-sys \
    --html=report.html \
    --self-contained-html \
    tests/test_communication.py > output.log 2>&1
```

***

### Explanation of Key Flags

| Flag                    | Description                                              |
| ----------------------- | -------------------------------------------------------- |
| `-n auto`               | Run tests in parallel using all available CPU cores      |
| `--log-cli-level=LEVEL` | Set the log level (`INFO`, `DEBUG`, etc.) for CLI output |
| `--capture=tee-sys`     | Capture stdout/stderr and also display in terminal       |
| `--html=report.html`    | Output test results as an HTML report                    |
| `--self-contained-html` | Include all styles/scripts in a single HTML file         |
| `> output.log 2>&1`     | Save all output (stdout and stderr) to `output.log`      |

***

### Benchmark Testing with `pytest-benchmark`

#### Write a Benchmark Test

```python
def test_my_function_benchmark(benchmark):
    result = benchmark(my_function_to_test)
    assert result is not None
```

#### Run the Benchmark Test

```bash
pytest tests/test_benchmark.py
```

***

#### Generate Benchmark Report in JSON

```bash
pytest --benchmark-only --benchmark-json=benchmark.json
```

***

#### Compare Two Benchmark Runs

1. Save the first run:

```bash
pytest --benchmark-save baseline
```

2. Compare with a new run:

```bash
pytest --benchmark-compare
```

***

### Open the HTML Report

After running your tests, open `report.html` in your browser. The report includes:

* Pass/Fail summary
* Execution time per test
* Captured logs and print output
* Parameterized test values (if used)
* Benchmark results (if enabled)

***

### Summary

With this setup, you get:

* Fast, parallel test execution with `pytest-xdist`
* Beautiful, shareable HTML test reports
* Debug-level logs for troubleshooting
* Optional performance benchmarking with historical comparison
