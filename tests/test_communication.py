import pytest
import os
import logging
import json
from shufflepy.communication import Communication
from shufflepy.module import Singul
from felds import SLACK_MSG_FIELDS,SLACK_CHANNEL_FIELDS,SLACK_CONTACT_FIELDS,SLACK_ATTACHMENT_FIELDS


# --------------------------------------------------------------------------------------------------
# Global variables for storing credentials
# --------------------------------------------------------------------------------------------------

BASE_URL = os.environ.get("SHUFFLE_BASE_URL", default="https://shuffler.io")
SHUFFL_API = os.environ.get("SHUFFLE_AUTHORIZATION", default="*********************************")
SHUFFL_ORG_ID = os.environ.get("SHUFFLE_ORG_ID", default="*****************************************")
SLACK_BOT_TOCKEN = os.environ.get("SLACK_BOT_TOKEN", default="*******************************************")

# --------------------------------------------------------------------------------------------------
# Logging Configuration
# --------------------------------------------------------------------------------------------------

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# --------------------------------------------------------------------------------------------------
# Fixture: Create real Communication instance
# --------------------------------------------------------------------------------------------------

@pytest.fixture
def communication_real_instance():
    """Fixture for creating a Communication instance with real Singul."""

    if not SHUFFL_API or not BASE_URL:
        pytest.fail("Missing environment variables: SHUFFLE_AUTHORIZATION or SHUFFLE_BASE_URL")

    singul = Singul(SHUFFL_API, BASE_URL)
    return Communication(singul)


# --------------------------------------------------------------------------------------------------
# Parametrized Test: Flexible key variants for list_messages
# --------------------------------------------------------------------------------------------------

# is not get any message form the channel (IT might be connfigraion issue of authenticaion)

@pytest.mark.parametrize("channel_field", SLACK_CHANNEL_FIELDS)
def test_list_messages_key_variants(communication_real_instance, channel_field):
    """Test list_messages with different flexible channel key variants."""
    app = "slack"


    fields = [
        channel_field,
    ]

    logging.info("Testing list_messages with channel key='%s'", channel_field["key"])

    try:
        response = communication_real_instance.list_messages(
            app=app,
            org_id=SHUFFL_ORG_ID,
            fields=fields
        )

        logging.info("Status: %s", response.get("status"))
        logging.debug("Raw response:\n%s", json.dumps(response.get("raw_response", {}), indent=4))

    except Exception as e:
        pytest.fail(f"list_messages failed with channel='{channel_field['key']}': {e}")

    assert isinstance(response, dict), "Response should be a dictionary"
    assert response.get("status") == 200, f"Listing messages failed for channel key: {channel_field['key']}"

    raw_response = response.get("raw_response", {})
    body = raw_response.get("body", {})
    output = response.get("output", {})

    assert isinstance(body, (dict, list)), "Response body should be a dictionary or list"
    assert output, f"Expected non-empty output, got empty output with channel='{channel_field['key']}'"


# --------------------------------------------------------------------------------------------------
# Parametrized Test: Flexible key variants for msg & channel for send_message
# --------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("msg_field", SLACK_MSG_FIELDS)
@pytest.mark.parametrize("channel_field", SLACK_CHANNEL_FIELDS)
def test_send_message_key_variants(communication_real_instance, msg_field, channel_field):
    """Test send_message with different flexible key names for message and channel."""
    app = "slack"
    auth_id = ""

    if not SHUFFL_ORG_ID:
        pytest.fail("Missing SHUFFLE_ORG_ID environment variable.")

    # Combine dynamic message + channel field
    fields = [msg_field, channel_field]

    logging.info("Testing with keys: msg='%s', channel='%s'", msg_field["key"], channel_field["key"])

    try:
        response = communication_real_instance.send_message(
            app=app,
            org_id=SHUFFL_ORG_ID,
            fields=fields,
            auth_id=auth_id
        )

        logging.info("Status: %s", response.get("status"))
        logging.debug("Raw response:\n%s", json.dumps(response.get("raw_response", {}), indent=4))

    except Exception as e:
        pytest.fail(
            f"send_message failed with msg='{msg_field['key']}' and channel='{channel_field['key']}': {e}"
        )

    # Assertions
    assert isinstance(response, dict), "Response should be a dictionary"
    assert response.get("status") == 200, (
        f"Message sending failed with keys: msg='{msg_field['key']}', channel='{channel_field['key']}'"
    )

    raw_response = response.get("raw_response", {})
    body = raw_response.get("body", {})

    assert isinstance(body, dict), "Response body should be a dictionary"
    assert body.get("ok") is True, "Expected 'ok': true in response body"
    assert "raw_response" in response, "Expected 'raw_response' key in response"


# --------------------------------------------------------------------------------------------------
# Parametrized Test: Flexible key variants for msg & channel for get message
# --------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("msg_field", SLACK_MSG_FIELDS)
@pytest.mark.parametrize("channel_field", SLACK_CHANNEL_FIELDS)
def test_get_message_key_variants(communication_real_instance, msg_field, channel_field):
    """Test get_message with flexible key variants for message and channel fields."""
    
    app = "slack"

    if not SLACK_BOT_TOCKEN:
        pytest.fail("Missing SLACK_BOT_TOKEN environment variable")

    fields = [
        # {"key": "token", "value": SLACK_BOT_TOCKEN},
        channel_field,
        msg_field,
    ]

    logging.info("Testing get_message with msg='%s' and channel='%s'", msg_field["key"], channel_field["key"])

    try:
        response = communication_real_instance.get_message(
            app=app,
            org_id=SHUFFL_ORG_ID,
            fields=fields
        )

        logging.info("Status: %s", response.get("status"))
        logging.debug("Full response:\n%s", json.dumps(response, indent=4))

    except Exception as e:
        pytest.fail(f"get_message failed with msg='{msg_field['key']}' and channel='{channel_field['key']}': {e}")

    # Assertions
    assert isinstance(response, dict), "Response should be a dictionary"
    assert response.get("status") == 200, f"get_message failed for channel='{channel_field['key']}'"

    raw_response = response.get("raw_response", {})
    output = response.get("output", {})

    assert "raw_response" in response, "Expected 'raw_response' in response"
    assert output, f"Expected non-empty output from get_message, got: {output}"

    body = raw_response.get("body", {})

    if isinstance(body, dict) and body.get("ok") is False:
        pytest.fail(f"Slack API responded with ok=false for channel='{channel_field['key']}'")


# ------------------------------------------------------------------------------
# Parametrized Test: search_messages
# ------------------------------------------------------------------------------

@pytest.mark.parametrize("msg_field", SLACK_MSG_FIELDS)
@pytest.mark.parametrize("channel_field", SLACK_CHANNEL_FIELDS)
def test_search_messages_flexible_keys(communication_real_instance, msg_field, channel_field):
    """Test search_messages with flexible key variants for message and channel fields."""
    app = "slack"

    if not SLACK_BOT_TOCKEN:
        pytest.fail("Missing SLACK_BOT_TOKEN environment variable")

    fields = [
        # {"key": "token", "value": SLACK_BOT_TOCKEN},  # If needed by your system
        channel_field,
        msg_field,
        {"key": "return", "value": "messages"},
    ]

    logging.info("Testing search_messages with msg='%s' and channel='%s'", msg_field["key"], channel_field["key"])

    try:
        response = communication_real_instance.search_messages(
            app=app,
            org_id=SHUFFL_ORG_ID,
            fields=fields
        )

        logging.info("Status: %s", response.get("status"))
        logging.debug("Full response:\n%s", json.dumps(response, indent=4))

    except Exception as e:
        pytest.fail(f"search_messages failed with msg='{msg_field['key']}' and channel='{channel_field['key']}': {e}")

    # --- Assertions ---
    assert isinstance(response, dict), "Response should be a dictionary"
    assert response.get("status") == 200, f"search_messages failed for channel='{channel_field['key']}'"

    raw_response = response.get("raw_response", {})
    output = response.get("output", {})

    assert "raw_response" in response, "Expected 'raw_response' in response"
    assert output is not None, f"Expected non-empty output from search_messages, got: {output}"

    body = raw_response.get("body", {})

    if isinstance(body, dict) and body.get("ok") is False:
        pytest.fail(f"Slack API responded with ok=false for channel='{channel_field['key']}'")

# ------------------------------------------------------------------------------
# Parametrized Test: list_attachments
# ------------------------------------------------------------------------------

@pytest.mark.parametrize("channel_field", SLACK_CHANNEL_FIELDS)
def test_list_attachments_flexible_keys(communication_real_instance, channel_field):
    """Test list_attachments with flexible channel field keys."""
    app = "slack"

    if not SLACK_BOT_TOCKEN:
        pytest.fail("Missing SLACK_BOT_TOKEN environment variable")

    fields = [
        # {"key": "token", "value": SLACK_BOT_TOCKEN},  # Add if needed
        channel_field,
        {"key": "return", "value": "attachments"},
    ]

    logging.info("Testing list_attachments with channel key='%s'", channel_field["key"])

    try:
        response = communication_real_instance.list_attachments(
            app=app,
            org_id=SHUFFL_ORG_ID,
            fields=fields
        )

        logging.info("Status: %s", response.get("status"))
        logging.debug("Full response:\n%s", json.dumps(response, indent=4))

    except Exception as e:
        pytest.fail(f"list_attachments failed for channel='{channel_field['key']}': {e}")

    # --- Assertions ---
    assert isinstance(response, dict), "Response should be a dictionary"
    assert response.get("status") == 200, f"list_attachments failed for channel='{channel_field['key']}'"

    raw_response = response.get("raw_response", {})
    output = response.get("output", {})

    assert "raw_response" in response, "Expected 'raw_response' in response"
    assert output is not None, f"No attachments found for channel='{channel_field['key']}'"

    body = raw_response.get("body", {})

    if isinstance(body, dict) and body.get("ok") is False:
        pytest.fail(f"Slack API responded with ok=false for channel='{channel_field['key']}'")

# ------------------------------------------------------------------------------
# Helper: Get a valid attachment_id from list_attachments
# ------------------------------------------------------------------------------

def get_first_attachment_id(communication, app, org_id):
    """Call list_attachments and return the first attachment ID found."""
    response = communication.list_attachments(
        app=app,
        org_id=org_id,
        fields=[{"key": "channel", "value": "general"}]
    )

    attachments = response.get("output", {}).get("attachments", [])
    if not attachments:
        pytest.skip("No attachments found in channel to test get_attachment")

    # Extract the ID field (assuming it's 'id' or 'file_id')
    return attachments[0].get("id") or attachments[0].get("file_id")

# ------------------------------------------------------------------------------
# Test: Get attachment using flexible field key variants
# ------------------------------------------------------------------------------

@pytest.mark.parametrize("field_template", SLACK_ATTACHMENT_FIELDS)
def test_get_attachment_with_flexible_keys(communication_real_instance, field_template):
    """Test get_attachment using flexible field key variants."""
    app = "slack"
    org_id = SHUFFL_ORG_ID

    # Step 1: Fetch one valid attachment ID
    attachment_id = get_first_attachment_id(communication_real_instance, app, org_id)
    logging.info("Using attachment_id: %s", attachment_id)

    # Step 2: Prepare test fields with key variant
    test_field = field_template.copy()
    test_field["value"] = attachment_id

    fields = [
        test_field,
        {"key": "return", "value": "attachment"},
    ]

    try:
        response = communication_real_instance.get_attachment(
            app=app,
            org_id=org_id,
            fields=fields
        )

        logging.info("Status: %s", response.get("status"))
        logging.debug("Full response:\n%s", json.dumps(response, indent=4))

    except Exception as e:
        pytest.fail(f"get_attachment failed with key='{test_field['key']}': {e}")

    # --- Assertions ---
    assert isinstance(response, dict), "Response should be a dictionary"
    assert response.get("status") == 200, f"get_attachment failed for key='{test_field['key']}'"

    raw_response = response.get("raw_response", {})
    output = response.get("output", {})

    assert output is not None, "Expected non-empty output from get_attachment"
    assert isinstance(raw_response, dict), "Raw response should be a dictionary"

    if isinstance(raw_response.get("body", {}), dict) and raw_response["body"].get("ok") is False:
        pytest.fail(f"Slack API returned ok=false for key='{test_field['key']}'")

# ------------------------------------------------------------------------------
# Parametrized Test: get_contact with flexible keys
# ------------------------------------------------------------------------------

@pytest.mark.parametrize("contact_field", SLACK_CONTACT_FIELDS)
def test_get_contact_flexible_keys(communication_real_instance, contact_field):
    """Test get_contact with different flexible user/contact field key variants."""
    app = "slack"

    if not SLACK_BOT_TOCKEN:
        pytest.fail("Missing SLACK_BOT_TOKEN environment variable")

    fields = [
        # {"key": "token", "value": SLACK_BOT_TOCKEN},  # Uncomment if token field is required
        contact_field,
        {"key": "return", "value": "contact"},
    ]

    logging.info("Testing get_contact with key='%s'", contact_field["key"])

    try:
        response = communication_real_instance.get_contact(
            app=app,
            org_id=SHUFFL_ORG_ID,
            fields=fields
        )

        logging.info("Status: %s", response.get("status"))
        logging.debug("Full response:\n%s", json.dumps(response, indent=4))

    except Exception as e:
        pytest.fail(f"get_contact failed for key='{contact_field['key']}': {e}")

    # --- Assertions ---
    assert isinstance(response, dict), "Response should be a dictionary"
    assert response.get("status") == 200, f"get_contact failed for key='{contact_field['key']}'"

    output = response.get("output", {})
    raw_response = response.get("raw_response", {})

    assert output is not None, f"No output returned for key='{contact_field['key']}'"
    assert "raw_response" in response, "Expected 'raw_response' in response"

    if isinstance(raw_response.get("body", {}), dict) and raw_response["body"].get("ok") is False:
        pytest.fail(f"Slack API returned ok=false for key='{contact_field['key']}'")