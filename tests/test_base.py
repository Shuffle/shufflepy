import pytest
import json
import logging
import time
from unittest.mock import MagicMock
from shufflepy.base import BaseCategory

# ------------------------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------------------------

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# ------------------------------------------------------------------------------
# Dummy Child Class for BaseCategory Testing
# ------------------------------------------------------------------------------

class DummyCategory(BaseCategory):
    def __init__(self, singul):
        super().__init__(singul)

# ------------------------------------------------------------------------------
# Fixtures
# ------------------------------------------------------------------------------

@pytest.fixture
def mock_singul_success():
    """Mocked Singul with a successful response."""
    mock = MagicMock()
    mock.connect.return_value = {
        "status": 200,
        "result": "ok",
        "data": {
            "id": "asset-123",
            "type": "host",
            "ip": "10.0.0.1"
        }
    }
    return mock

@pytest.fixture
def mock_singul_failure():
    """Mocked Singul with a failed response."""
    mock = MagicMock()
    mock.connect.return_value = {
        "status": 500,
        "result": "error",
        "message": "Internal server error"
    }
    return mock

# ------------------------------------------------------------------------------
# Pass Test Case
# ------------------------------------------------------------------------------

def test_base_category_connect_success(mock_singul_success):
    category = DummyCategory(mock_singul_success)

    # Arrange
    action = "list_assets"
    app = "test_app"
    org_id = "org-pass"
    fields = [{"key": "field1", "value": "value1"}]
    auth_id = "auth-pass"
    skip_workflow = True

    logging.info("Testing success case for %s", category.__class__.__name__)

    # Act
    result = category._connect(
        action=action,
        app=app,
        org_id=org_id,
        fields=fields,
        auth_id=auth_id,
        skip_workflow=skip_workflow
    )

    # Log response
    logging.info("Response:\n%s", json.dumps(result, indent=4))

    # Assert
    mock_singul_success.connect.assert_called_once_with(
        app=app,
        action=action,
        org_id=org_id,
        fields=fields,
        auth_id=auth_id,
        category="dummycategory",
        skip_workflow=skip_workflow
    )

    assert result["status"] == 200
    assert result["result"] == "ok"
    assert "data" in result

# ------------------------------------------------------------------------------
# Fail Test Case
# ------------------------------------------------------------------------------

def test_base_category_connect_failure(mock_singul_failure):
    category = DummyCategory(mock_singul_failure)

    # Arrange
    action = "list_assets"
    app = "test_app"
    org_id = "org-fail"
    fields = [{"key": "field1", "value": "bad_value"}]
    auth_id = "auth-fail"
    skip_workflow = False

    logging.info("Testing failure case for %s", category.__class__.__name__)

    # Act
    result = category._connect(
        action=action,
        app=app,
        org_id=org_id,
        fields=fields,
        auth_id=auth_id,
        skip_workflow=skip_workflow
    )

    # Log response
    logging.warning("Response:\n%s", json.dumps(result, indent=4))

    # Assert
    mock_singul_failure.connect.assert_called_once_with(
        app=app,
        action=action,
        org_id=org_id,
        fields=fields,
        auth_id=auth_id,
        category="dummycategory",
        skip_workflow=skip_workflow
    )

    assert result["status"] != 200
    assert result["result"] == "error"
    assert "message" in result

# ------------------------------------------------------------------------------ 
# Performance Test
# ------------------------------------------------------------------------------

def test_base_category_connect_performance(mock_singul_success):
    category = DummyCategory(mock_singul_success)

    action = "list_assets"
    app = "perf_app"
    org_id = "org-perf"
    fields = [{"key": "field", "value": "value"}]
    auth_id = "auth-perf"

    total_runs = 100
    total_time = 0

    for i in range(total_runs):
        start = time.perf_counter()
        result = category._connect(
            action=action,
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )
        end = time.perf_counter()
        assert result["status"] == 200
        total_time += (end - start)

    avg_ms = (total_time / total_runs) * 1000
    logging.info("Average _connect() time over %d runs: %.2f ms", total_runs, avg_ms)

    # Optional performance assertion
    assert avg_ms < 50  # You can tune this threshold

# ------------------------------------------------------------------------------
# Benchmark Test
# ------------------------------------------------------------------------------

def test_base_category_connect_benchmark(benchmark, mock_singul_success):
    category = DummyCategory(mock_singul_success)

    # Benchmark target function
    def connect_call():
        return category._connect(
            action="benchmark_test",
            app="benchmark_app",
            org_id="org-benchmark",
            fields=[{"key": "field", "value": "value"}],
            auth_id="auth-benchmark"
        )

    result = benchmark(connect_call)

    # Optional: assert correctness
    assert result["status"] == 200
    assert "result" in result
