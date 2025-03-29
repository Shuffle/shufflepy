import pytest
import os
import logging
import json
from shufflepy.intel import Intel
from shufflepy.module import Singul
from felds import MALICIOUS_URLS, MALICIOUS_HASHES, MALICIOUS_IP

# --------------------------------------------------------------------------------------------------
# Environment Variables
# --------------------------------------------------------------------------------------------------

BASE_URL = os.environ.get("SHUFFLE_BASE_URL", default="https://shuffler.io")
SHUFFL_API = os.environ.get("SHUFFLE_AUTHORIZATION", default="**********************************")
SHUFFL_ORG_ID = os.environ.get("SHUFFLE_ORG_ID", default="**************************************")

# --------------------------------------------------------------------------------------------------
# Logging Configuration
# --------------------------------------------------------------------------------------------------

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')

# --------------------------------------------------------------------------------------------------
# IOC Inputs (merged with type labels)
# --------------------------------------------------------------------------------------------------

IOC_INPUTS = [
    *[{"type": "ip", "data": item} for item in MALICIOUS_IP],
    *[{"type": "domain", "data": item} for item in MALICIOUS_URLS],
    *[{"type": "hash", "data": item} for item in MALICIOUS_HASHES],
]

# --------------------------------------------------------------------------------------------------
# Fixture: Intel Real Instance
# --------------------------------------------------------------------------------------------------

@pytest.fixture
def intel_real_instance():
    """Create a real Intel instance using the Singul connection."""
    if not SHUFFL_API or not BASE_URL:
        pytest.fail("Missing SHUFFLE_AUTHORIZATION or SHUFFLE_BASE_URL environment variable")

    singul = Singul(SHUFFL_API, BASE_URL)
    return Intel(singul)

# --------------------------------------------------------------------------------------------------
# Parametrized Test: Test get_ioc with each malicious URL, MALICIOUS_HASHES and MALICIOUS_HASHES
# --------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("ioc", IOC_INPUTS)
def test_get_ioc_all_types(intel_real_instance, ioc):
    """Test Intel.get_ioc for all types of IOCs (IP, URL, Hash) with Virustotal V3 app."""

    app = "Virustotal V3"
    org_id = SHUFFL_ORG_ID  # already fetched above
    fields = [
        ioc["data"],
    ]

    ioc_type = ioc["type"]
    ioc_value = ioc["data"]["value"]

    logging.info("Testing get_ioc with %s: %s", ioc_type.upper(), ioc_value)

    try:
        response = intel_real_instance.get_ioc(
            app=app,
            org_id=org_id,
            fields=fields
        )
    except Exception as e:
        pytest.fail(f"get_ioc failed for {ioc_type}={ioc_value}: {e}")

    # Basic structure validation
    assert isinstance(response, dict), "Response should be a dictionary"
    logging.info("response status : %s",response.get("status"))
    assert response.get("status") == 200, f"Expected status 200, got {response.get('status')}"
    assert "raw_response" in response, "Expected 'raw_response' in response"

    raw_response = response["raw_response"]

    # Pretty-print raw response for debugging
    logging.debug("Raw response:\n%s", json.dumps(raw_response, indent=4))

    body = raw_response.get("body", {})
    assert isinstance(body, dict), "'body' in raw_response should be a dictionary"
    assert "data" in body, "'data' missing in response body"
    assert "attributes" in body["data"], "'attributes' missing in data"

    attributes = body["data"]["attributes"]
    analysis_results = attributes.get("last_analysis_results", {})
    stats = attributes.get("last_analysis_stats", {})

    assert isinstance(analysis_results, dict), "'last_analysis_results' should be a dictionary"
    assert isinstance(stats, dict), "'last_analysis_stats' should be a dictionary"
    assert "harmless" in stats or "malicious" in stats, "'harmless' or 'malicious' not found in stats"

    # Output log summary
    logging.info(
        "Scan complete for %s=%s | Harmless: %s | Malicious: %s | Undetected: %s",
        ioc_type,
        ioc_value,
        stats.get("harmless"),
        stats.get("malicious"),
        stats.get("undetected")
    )

# --------------------------------------------------------------------------------------------------
# Parametrized Test: Test search_ioc with each malicious URL
# --------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("ioc", IOC_INPUTS)
def test_search_ioc_all_types(intel_real_instance, ioc):
    """Test Intel.search_ioc for all types of IOCs (IP, Domain, Hash) using the Virustotal V3 app."""

    app = "Virustotal V3"
    org_id = SHUFFL_ORG_ID
    fields = [
        ioc["data"],
    ]

    ioc_type = ioc["type"]
    ioc_value = ioc["data"]["value"]

    logging.info("Testing search_ioc with %s: %s", ioc_type.upper(), ioc_value)

    try:
        response = intel_real_instance.search_ioc(
            app=app,
            org_id=org_id,
            fields=fields
        )
    except Exception as e:
        pytest.fail(f"search_ioc failed for {ioc_type}={ioc_value}: {e}")

    # Basic structure validation

    assert isinstance(response, dict), "Response should be a dictionary"
    logging.info("Response status : %s", response.get("status"))
    raw_response = response["raw_response"]
    assert raw_response.get("status") == 200, f"Expected status 200, got {raw_response.get('status')}"
    assert "raw_response" in response, "Expected 'raw_response' in response"

    # Pretty-print raw response for debugging
    logging.debug("Raw response:\n%s", json.dumps(raw_response, indent=4))

    body = raw_response.get("body", {})
    assert isinstance(body, dict), "'body' in raw_response should be a dictionary"
    assert "data" in body, "'data' missing in response body"
    assert "attributes" in body["data"], "'attributes' missing in data"

    attributes = body["data"]["attributes"]
    analysis_results = attributes.get("last_analysis_results", {})
    stats = attributes.get("last_analysis_stats", {})

    assert isinstance(analysis_results, dict), "'last_analysis_results' should be a dictionary"
    assert isinstance(stats, dict), "'last_analysis_stats' should be a dictionary"
    assert "harmless" in stats or "malicious" in stats, "'harmless' or 'malicious' not found in stats"

    # Output log summary
    logging.info(
        "Search result for %s=%s | Harmless: %s | Malicious: %s | Undetected: %s",
        ioc_type,
        ioc_value,
        stats.get("harmless"),
        stats.get("malicious"),
        stats.get("undetected")
    )
