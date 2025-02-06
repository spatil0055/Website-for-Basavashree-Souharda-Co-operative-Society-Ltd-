// Function to append messages to chat
function appendMessage(message, type) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add(type);
    messageDiv.innerText = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Function to send user input
function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim()) {
        appendMessage(userInput, 'user-message'); // Show user message
        document.getElementById('user-input').value = ''; // Clear input field

        // Get the CSRF token from the page
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        // Send AJAX request to get bot's response
        fetch('/chatbot/chatbot-api/', {
            method: 'POST',
            body: new URLSearchParams({ 'user_input': userInput }),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken  // Add CSRF token here
            }
        })
        .then(response => response.json())
        .then(data => {
            appendMessage(data.response, 'bot-message'); // Show bot response
        })
        .catch(error => console.error('Error:', error));
    }
}
