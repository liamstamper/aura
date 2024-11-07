# 🌌 Aura

**Aura** is a lightweight, simplified HTTP client for Python, inspired by Drizzle. Aura's minimal and clean API makes it easy to handle HTTP requests with fewer lines of code, focusing on simplicity and readability.

## 🚀 Features

- **Fluent API** for concise GET, POST, PUT, and DELETE requests.
- **Custom Headers**: Easily set global headers or request-specific headers.
- **Flexible Query Parameters and JSON Support**: Handle query parameters and JSON payloads directly.
- **Error Handling**: Built-in basic error handling for streamlined usage.
- **Lightweight and Fast**: No unnecessary bloat; just what you need to get the job done.

## 🎉 Getting Started

Import and initialize the client by specifying the base URL for your API.

```python
from Aura import AuraClient

# Initialize the client with a base URL
client = AuraClient(base_url="https://jsonplaceholder.typicode.com")

# Set default headers (optional)
client.set_default_headers({"Accept": "application/json"})
```

### Example Usage

#### 🔹 GET with Query Parameters
Fetches posts for a specific user.

```python
response = client.get("/posts", params={"userId": 1})
print("GET Response:", response)
```

#### 🔹 POST with JSON Data
Creates a new post with a title, body, and user ID.
```python
response = client.post("/posts", json={"title": "New Post", "body": "This is the content", "userId": 2})
print("POST Response:", response)
```

#### 🔹 PUT to Update Data
Updates an existing post with new title and content.
```python
response = client.put("/posts/1", json={"title": "Updated Title", "body": "Updated content"})
print("PUT Response:", response)
```

#### 🔹 DELETE a Resource
Deletes a post with the specified ID.
```python
response = client.delete("/posts/1")
print("DELETE Response:", response)
```

## 📜 API Reference

Aura offers the following methods:

- `set_default_headers(headers: Dict[str, str])`: Sets headers to be included in all requests.
- `get(path: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None)`: Sends a GET request.
- `post(path: str, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None)`: Sends a POST request with JSON data.
- `put(path: str, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None)`: Sends a PUT request with JSON data.
- `delete(path: str, headers: Optional[Dict[str, str]] = None)`: Sends a DELETE request.
