import requests
import time
import json

# Constants
API_BASE_URL = "https://api.trigger.dev/api/v1/tasks"
TASK_NAME = "send-prompt-to-bedrock"
AUTH_TOKEN = "Bearer tr_dev_INSERT_HERE"

# Headers
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": AUTH_TOKEN
}

# Query Payload
PAYLOAD = {
    "payload": {
        # Modify the query as needed
        "query": "Can tell me about the junior dev home assignment from INKI?"
    }
}

def trigger_task():
    """Triggers the task and returns the run ID."""
    url = f"{API_BASE_URL}/{TASK_NAME}/trigger"
    response = requests.post(url, headers=HEADERS, json=PAYLOAD)
    response_data = response.json()

    if "id" in response_data:
        print("Task triggered successfully:", response_data)
        return response_data["id"]
    else:
        raise ValueError("The 'id' key was not found in the response:", response_data)

def get_task_results(run_id):
    """Fetches the results of the triggered task."""
    retrieve_url = f"https://api.trigger.dev/api/v3/runs/{run_id}"
    # Introduce a short delay to ensure the task is completed
    time.sleep(5)
    response = requests.get(retrieve_url, headers=HEADERS)
    response_data = response.json()
    return response_data

def parse_retrieval_results(results):
    """Parses and prints the retrievalResults."""
    retrieval_output = results.get("output")
    if not retrieval_output:
        print("No output found.")
        return
    
    retrieval_results = retrieval_output.get("retrievalResults", [])
    if not retrieval_results:
        print("No retrieval results found.")
        return

    print("\n--- Retrieval Results ---")
    for result in retrieval_results:
        content = result["content"]["text"]
        uri = result["location"]["s3Location"]["uri"]
        score = result["score"]
        print(f"\nContent:\n{content}\n")
        print(f"Document Location: {uri}")
        print(f"Relevance Score: {score}\n")

# Main Execution
try:
    # Step 1: Trigger the task
    run_id = trigger_task()

    # Step 2: Retrieve task results
    results = get_task_results(run_id)
    print("\nFull Response:", json.dumps(results, indent=2))

    # Step 3: Parse and display retrieval results
    parse_retrieval_results(results)
except Exception as e:
    print("An error occurred:", e)
