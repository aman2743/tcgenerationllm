const sendBtn = document.getElementById('send-btn');
const userInput = document.getElementById('user-input');
const chatContainer = document.getElementById('chat-container');

async function generateTest() {
    const text = userInput.value.trim();
    if (!text) return;

    // 1. Add User Message
    addMessage(text, 'user');
    userInput.value = '';
    userInput.focus();

    // 2. Add "Thinking" Indicator
    const thinkingId = 'thinking-' + Date.now();
    const assistantDiv = document.createElement('div');
    assistantDiv.classList.add('message', 'assistant');
    assistantDiv.id = thinkingId;
    assistantDiv.innerHTML = `
        <div class="typing-indicator">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;
    chatContainer.appendChild(assistantDiv);
    scrollToBottom();

    try {
        const response = await fetch('http://localhost:8000/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ userInput: text })
        });

        if (!response.ok) throw new Error("Network response was not ok");

        // Remove typing indicator content
        assistantDiv.innerHTML = '';

        // Create code block for response
        const pre = document.createElement('pre');
        assistantDiv.appendChild(pre);

        const reader = response.body.getReader();
        const decoder = new TextDecoder();

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            const chunk = decoder.decode(value, { stream: true });
            pre.textContent += chunk;
            scrollToBottom();
        }

    } catch (error) {
        assistantDiv.textContent = "Error: " + error.message;
        assistantDiv.style.borderColor = '#ef4444'; // Red border on error
    }

    scrollToBottom();
}

function addMessage(text, role) {
    const div = document.createElement('div');
    div.classList.add('message', role);
    div.textContent = text;
    chatContainer.appendChild(div);
    scrollToBottom();
    return div;
}

function scrollToBottom() {
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Auto-resize textarea
userInput.addEventListener('input', function () {
    this.style.height = '60px';
    this.style.height = (this.scrollHeight) + 'px';
});

// Send on Enter (Shift+Enter for newline)
userInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        generateTest();
    }
});

sendBtn.addEventListener('click', generateTest);
