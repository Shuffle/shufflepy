---
icon: user-unlock
---

# Identity & Access Management

The `IAM` module in Singul helps manage user access, authentication, and identity actions across integrated platforms like **Active Directory**, **Azure AD**, **CyberArk**, **HashiCorp Vault**, **Microsoft Identity**, and more.

It provides a standardized way to perform critical IAM actions like password resets, enabling/disabling users, and identity lookups using a unified API interface.

***

### Available Actions

Singul currently supports the following IAM actions:

| Action            | Description                                       |
| ----------------- | ------------------------------------------------- |
| `reset_password`  | Reset a user's password                           |
| `enable_user`     | Enable/reactivate a user account                  |
| `disable_user`    | Disable or deactivate a user account              |
| `get_identity`    | Retrieve identity information for a specific user |
| `get_asset`       | Fetch asset linked to a user                      |
| `search_identity` | Search identities based on username or filters    |

***

### Core Parameters

Each method requires the following parameters:

| Parameter | Description                                                                     |
| --------- | ------------------------------------------------------------------------------- |
| `app`     | Name of the IAM provider (e.g. `"activedirectory"`, `"vault"`, `"cyberark"`)    |
| `auth_id` | The app's authentication ID from your [Shuffle](https://shuffler.io/) dashboard |
| `fields`  | List of key-value pairs specific to the action                                  |
| `org_id`  | _(Optional)_ Your organization ID if required by the app                        |

***

### Usage Examples

#### Reset Password

```python
response = singul.iam.reset_password(
    app="activedirectory",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "username", "value": "jdoe"},
        {"key": "new_password", "value": "NewSecurePassword123!"}
    ]
)
print(response)
```

***

#### Enable User

```python
response = singul.iam.enable_user(
    app="azure_ad",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "user_id", "value": "12345"}
    ]
)
print(response)
```

***

#### Disable User

```python
response = singul.iam.disable_user(
    app="cyberark",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "username", "value": "jdoe"}
    ]
)
print(response)
```

***

#### Get Identity Info

```python
response = singul.iam.get_identity(
    app="vault",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "username", "value": "jdoe"}
    ]
)
print(response)
```

***

#### Get Associated Asset

```python
response = singul.iam.get_asset(
    app="hashicorp_cloud_platform",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "user_id", "value": "admin001"}
    ]
)
print(response)
```

***

#### Search Identity

```python
response = singul.iam.search_identity(
    app="microsoft_identity",
    auth_id="YOUR_AUTH_ID",
    fields=[
        {"key": "email", "value": "user@example.com"}
    ]
)
print(response)
```

***

### Supported IAM Platforms

* **Active Directory** (`activedirectory`, `ldap`, `ldaps`, `azure_ad`)
* **HashiCorp Vault / Cloud Platform** (`vault`, `hashicorp_cloud_platform`)
* **CyberArk** (`cyberark`)
* **Microsoft Identity** (`microsoft_identity`)
* **Azure AD Delegated** (`new_azure_ad_delegated`)

> Use the exact `app` string listed in Shuffle when calling each method.

***

### Best Practices

* Always test password resets and user status updates in a dev environment first.
* Use `search_identity` for flexible lookups using email, username, or ID.
* Ensure your authentication tokens and roles have the correct permissions in the connected IAM provider.
