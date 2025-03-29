---
icon: globe
---

# Network Module

The `Network` module in Singul allows you to interact with firewall and network infrastructure tools to control IP-based access and retrieve security rules. Supported tools include **Palo Alto**, **FortiGate**, **F5**, **Check Point**, **Trend Micro**, and more.

With just a few API calls, you can block or allow IP addresses and fetch existing rules directly from connected network appliances.

***

### Available Actions

| Action      | Description                                      |
| ----------- | ------------------------------------------------ |
| `get_rules` | Retrieve firewall or network security rules      |
| `allow_ip`  | Allow a specific IP address through the firewall |
| `block_ip`  | Block a specific IP address                      |

***

### Core Parameters

Each method accepts the following parameters:

| Parameter | Description                                                                  |
| --------- | ---------------------------------------------------------------------------- |
| `app`     | Name of the network tool (e.g. `"palo_alto_firewall"`, `"opnsense"`, `"f5"`) |
| `auth_id` | Authentication ID from your [Shuffle](https://shuffler.io/) dashboard        |
| `fields`  | List of key-value pairs specific to the action                               |
| `org_id`  | _(Optional)_ Organization ID if required by the app                          |

***

### Usage Examples

#### Get Firewall Rules

```python
response = singul.network.get_rules(
    app="fortigate_firewall",
    auth_id="YOUR_AUTH_ID"
)
print(response)
```

***

#### Allow IP

```python
response = singul.network.allow_ip(
    app="palo_alto_firewall",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "ip", "value": "203.0.113.45"}
    ]
)
print(response)
```

***

#### Block IP

```python
response = singul.network.block_ip(
    app="f5",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "ip", "value": "192.0.2.99"}
    ]
)
print(response)
```

***

### Supported Network Apps (Examples)

Below are examples of supported network and firewall platforms:

* **Palo Alto Firewall** (`palo_alto_firewall`)
* **FortiGate Firewall** (`fortigate_firewall`)
* **F5** (`f5`)
* **SonicOS API** (`sonicos_api`)
* **OPNsense** (`opnsense`)
* **Check Point GAIA** (`check_point_gaia`)
* **FortiManager** (`fortimanager`)
* **Trend Micro Network Security** (`trend_micro_network_security`)
* **Genian NAC** (`genian_nac`)
* **WiGLE API** (`wigle_api`)

> This is just a sample list. More apps are supported through Shuffle integrations.

***

### Best Practices

* Always verify IPs before adding to allow/block lists.
* Ensure you have appropriate role permissions on the connected firewall.
* Use `get_rules()` to validate rule configuration after making changes.
