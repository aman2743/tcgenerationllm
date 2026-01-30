import requests
import sys

def check_ollama():
    print("Checking Ollama connection...")
    try:
        # Standard Ollama port is 11434
        response = requests.get('http://localhost:11434/')
        if response.status_code == 200:
            print("✅ Ollama is RUNNING and reachable.")
            print("Server response:", response.text)
            return True
        else:
            print(f"❌ Ollama responded with status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to Ollama at localhost:11434. Is it running?")
        print("Tip: Run 'ollama serve' in a separate terminal.")
        return False
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return False

def check_model(model_name="llama3.2"):
    print(f"\nChecking for model '{model_name}'...")
    try:
        response = requests.get('http://localhost:11434/api/tags')
        if response.status_code == 200:
            models = response.json().get('models', [])
            found = any(m['name'] == model_name or m['name'] == f"{model_name}:latest" for m in models)
            if found:
                print(f"✅ Model '{model_name}' found.")
            else:
                print(f"⚠️ Model '{model_name}' NOT found in list. Available models:")
                for m in models:
                    print(f" - {m['name']}")
                print(f"Tip: Run 'ollama pull {model_name}'")
            return found
    except Exception as e:
        print(f"❌ Could not check models: {e}")
        return False

if __name__ == "__main__":
    success_conn = check_ollama()
    if success_conn:
        check_model("llama3.2")
