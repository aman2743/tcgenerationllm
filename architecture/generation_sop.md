# Generation technical SOP

## Goal
Generate high-quality, comprehensive test cases from a user-provided code snippet or usage scenario description, using a local Ollama LLM (Llama 3.2).

## Inputs
1.  **User Input (`userInput`)**: Raw string containing code or text description.
2.  **Model (`model`)**: Target model string (default: `llama3.2`).
3.  **Template**:
    *   **System Prompt**:
        """
        You are an expert QA Automation Engineer.
        Your task is to analyze the provided code or requirement and generate a comprehensive set of test cases.
        
        **Output Format:**
        You must strictly follow this format for every test case. Do not wrap in markdown tables, just use plain text headers or a clear list.
        
        Format:
        --------------------------------------------------
        Test Case ID: [ID]
        Description: [What is being tested]
        
        Steps:
        1. [Step 1]
        2. [Step 2]
        
        Expected Result: [What should happen]
        --------------------------------------------------
        
        Ensure you cover:
        1. Positive Path
        2. Negative Path (Edge Cases)
        3. Boundary Values
        """

## Logic Flow (Layer 2 Navigation)
1.  **Receive Request**: API Endpoint `/api/generate` receives JSON.
2.  **Validate**: Ensure `userInput` is not empty.
3.  **Construct Prompt**:
    *   Load "System Prompt" (The Template).
    *   Inject `userInput` into the Template.
4.  **Call LLM**: Send constructed prompt to Ollama (`localhost:11434/api/generate`).
5.  **Stream Response**: Yield chunks of data back to the frontend immediately.

## Edge Cases
-   **Ollama Down**: If connection fails, return 503 error with troubleshooting message ("Is Ollama running?").
-   **Model Missing**: If `llama3.2` is not pulled, return 400 error.
-   **Empty Input**: Return 400 error.

## Tools (Layer 3)
-   `tools/check_ollama.py`: Used for health checks.
-   (Future): `tools/format_code.py` if we need strict formatting of output.
