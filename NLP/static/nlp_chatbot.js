function sendMessage() {
    var userInput = document.getElementById('userInput').value;
    if (userInput.trim() === '') {
        alert('Please type a message.');
        return;
    }

    var chatbox = document.getElementById('chatbox');
    chatbox.innerHTML += `<div>User: ${userInput}</div>`;

    fetch('/analyze_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({text: userInput})
    })
    .then(response => response.json())
    .then(data => {
        chatbox.innerHTML += `<div>Bot: ${data.response}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;
    })
    .catch(error => console.error('Error:', error));

    document.getElementById('userInput').value = '';
}

document.getElementById('userInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        e.preventDefault();  // Prevent default behavior of Enter key
        sendMessage();
    }
});
