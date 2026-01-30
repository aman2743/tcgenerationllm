# Project Constitution (gemini.md)

## Data Schemas

### 1. API: Generate Tests (POST /api/generate)
**Request Payload:**
```json
{
  "userInput": "string", // The code snippet or scenario description
  "model": "string"      // Default: "llama3.2"
}
```

**Response Payload (Streamed):**
- The server will stream raw text chunks.
- Final event might indicate completion.

### 2. Frontend State
**Message Object:**
```typescript
interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  isStreaming?: boolean;
}
```

## Behavioral Rules
- **Reliability:** The system must handle Ollama connection failures gracefully (e.g., prompt user to ensure Ollama is running).
- **Templating:** The "Test Case Template" must be stored in the backend and applied invisibly to the user's input. The user only sees their input and the result.
- **Aesthetics:** The UI must be "Premium" (Dark mode, smooth animations, glassmorphism) as per system instructions.

## Architectural Invariants
- **A.N.T. Architecture:**
    - **A (Architect/Backend):** Python/FastAPI (Proxy & Template Engine).
    - **N (Nexus/API):** REST API `/api/generate` (StreamingResponse).
    - **T (Terminal/Frontend):** Vanilla HTML/CSS/JS (No Frameworks).
- **Protocol:** B.L.A.S.T. applies to all updates.
