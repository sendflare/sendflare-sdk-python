# sendflare-sdk-python

The SDK for sendflare service written in Python.

## Requirements

- Python >= 3.7

## Installation

Install via pip:

```bash
pip install sendflare-sdk-python
```

Or install from source:

```bash
git clone https://github.com/sendflare/sendflare-sdk-python.git
cd sendflare-sdk-python
pip install -e .
```

## Quick Start

```python
from sendflare_sdk import SendflareClient, SendEmailReq

client = SendflareClient('your-api-token')

req = SendEmailReq(
    from_='test@example.com',
    to='to@example.com',
    subject='Hello',
    body='Test email'
)

try:
    response = client.send_email(req)
    print(f"Email sent successfully: {response.success}")
except Exception as e:
    print(f"Error: {e}")
```

## Usage Examples

### Send Email

```python
from sendflare_sdk import SendflareClient, SendEmailReq

client = SendflareClient('your-api-token')

req = SendEmailReq(
    from_='sender@example.com',
    to='recipient@example.com',
    subject='Subject Here',
    body='Email body content'
)

response = client.send_email(req)
if response.success:
    print("Email sent successfully!")
```

### Get Contact List

```python
from sendflare_sdk import SendflareClient, ListContactReq

client = SendflareClient('your-api-token')

req = ListContactReq(
    app_id='your-app-id',
    page=1,
    page_size=10
)

response = client.get_contact_list(req)
print(f"Total contacts: {response.total_count}")

for contact in response.data:
    print(f"Email: {contact.email_address}")
```

### Save Contact

```python
from sendflare_sdk import SendflareClient, SaveContactReq

client = SendflareClient('your-api-token')

req = SaveContactReq(
    app_id='your-app-id',
    email_address='john@example.com',
    data={
        'firstName': 'John',
        'lastName': 'Doe',
        'company': 'Acme Corp'
    }
)

response = client.save_contact(req)
if response.success:
    print("Contact saved successfully!")
```

### Delete Contact

```python
from sendflare_sdk import SendflareClient, DeleteContactReq

client = SendflareClient('your-api-token')

req = DeleteContactReq(
    email_address='john@example.com',
    app_id='your-app-id'
)

response = client.delete_contact(req)
if response.success:
    print("Contact deleted successfully!")
```

## API Reference

### SendflareClient

#### Constructor

```python
SendflareClient(token: str)
```

Create a new Sendflare client instance.

**Parameters:**
- `token` - Your Sendflare API token

#### Methods

##### send_email

```python
send_email(req: SendEmailReq) -> SendEmailResp
```

Send an email.

**Parameters:**
- `req` - Send email request object
  - `from_` - Sender email address
  - `to` - Recipient email address
  - `subject` - Email subject
  - `body` - Email body content

**Returns:** `SendEmailResp`

**Raises:** `Exception`

##### get_contact_list

```python
get_contact_list(req: ListContactReq) -> ListContactResp
```

Get contact list with pagination.

**Parameters:**
- `req` - List contact request object
  - `app_id` - Application ID
  - `page` - Page number (default: 1)
  - `page_size` - Items per page (default: 10)

**Returns:** `ListContactResp`

**Raises:** `Exception`

##### save_contact

```python
save_contact(req: SaveContactReq) -> SaveContactResp
```

Create or update a contact.

**Parameters:**
- `req` - Save contact request object
  - `app_id` - Application ID
  - `email_address` - Contact email address
  - `data` - Contact data (optional dict)

**Returns:** `SaveContactResp`

**Raises:** `Exception`

##### delete_contact

```python
delete_contact(req: DeleteContactReq) -> DeleteContactResp
```

Delete a contact.

**Parameters:**
- `req` - Delete contact request object
  - `email_address` - Contact email address
  - `app_id` - Application ID

**Returns:** `DeleteContactResp`

**Raises:** `Exception`

## Model Classes

### Request Models

- `SendEmailReq` - Send email request
- `ListContactReq` - Get contact list request
- `SaveContactReq` - Save contact request
- `DeleteContactReq` - Delete contact request
- `PaginateReq` - Pagination request (base class)

### Response Models

- `SendEmailResp` - Send email response
- `ListContactResp` - Get contact list response
- `SaveContactResp` - Save contact response
- `DeleteContactResp` - Delete contact response
- `CommonResponse` - Common response (base class)
- `PaginateResp` - Pagination response (base class)
- `ContactItem` - Contact information

## Testing

Run tests with unittest:

```bash
python -m unittest discover tests
```

Or with pytest (if installed):

```bash
pip install pytest
pytest
```

## Error Handling

All API methods may raise exceptions. It's recommended to wrap calls in try-except blocks:

```python
try:
    response = client.send_email(req)
    # Handle success
except Exception as e:
    # Handle error
    print(f"Sendflare API error: {e}")
```

## Type Hints

This SDK uses Python type hints for better IDE support and code clarity. All methods and classes are fully typed.

## Dependencies

This SDK has no external dependencies and uses only Python standard library modules:
- `json` - JSON encoding/decoding
- `urllib` - HTTP client
- `dataclasses` - Data class support
- `typing` - Type hints

## Documentation

For more information, visit: [https://docs.sendflare.io](https://docs.sendflare.io)

## License

[MIT](./LICENSE)

