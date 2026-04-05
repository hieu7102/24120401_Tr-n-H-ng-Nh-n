import requests

url = "http://127.0.0.1:8000/generate"

def test_valid():
    data = {"prompt": "Explain AI"}
    response = requests.post(url, json=data)
    
    print("=== VALID INPUT ===")
    print("Status:", response.status_code)
    print("Response:", response.json())
    print()

def test_empty():
    data = {"prompt": ""}
    response = requests.post(url, json=data)
    
    print("=== EMPTY INPUT ===")
    print("Status:", response.status_code)
    print("Response:", response.json())
    print()

def test_long():
    data = {"prompt": "AI " * 300}
    response = requests.post(url, json=data)
    
    print("=== LONG INPUT ===")
    print("Status:", response.status_code)
    print("Response:", response.json())
    print()

if __name__ == "__main__":
    test_valid()
    test_empty()
    test_long()