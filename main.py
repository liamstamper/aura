# main.py
from client import AuraClient

def main():
    # Initialize the client with a base URL
    client = AuraClient(base_url="https://jsonplaceholder.typicode.com")

    # Optionally, set default headers for all requests
    client.set_default_headers({"Accept": "application/json"})

    # Test GET request with query parameters
    print("Testing GET request:")
    response = client.get("/posts", params={"userId": 1})
    print("GET Response:", response)

    # Test POST request with JSON data
    print("\nTesting POST request:")
    response = client.post("/posts", json={"title": "foo", "body": "bar", "userId": 1})
    print("POST Response:", response)

    # Test PUT request with JSON data
    print("\nTesting PUT request:")
    response = client.put("/posts/1", json={"title": "updated title", "body": "updated body", "userId": 1})
    print("PUT Response:", response)

    # Test DELETE request
    print("\nTesting DELETE request:")
    response = client.delete("/posts/1")
    print("DELETE Response:", response)

if __name__ == "__main__":
    main()
