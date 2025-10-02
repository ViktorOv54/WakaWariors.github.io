// Replace with your own OpenAI API key
const API_KEY = "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";

document.getElementById("send").addEventListener("click", async () => {
    const inputField = document.getElementById("user-input");
    const userMessage = inputField.value.trim();
    if (!userMessage) return;

    // Display user message
    addMessage(userMessage, "user");
    inputField.value = "";

    // Send to OpenAI
    addMessage("Thinking...", "bot");
    const botMessageElement = document.querySelector(".message.bot:last-child");

    try {
        const response = await fetch("https://api.openai.com/v1/chat/completions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${API_KEY}`
            },
            body: JSON.stringify({
                model: "gpt-3.5-turbo", // you can use "gpt-4" if your key has access
                messages: [
                    { role: "system", content: "You are a helpful assistant." },
                    { role: "user", content: userMessage }
                ]
            })
        });

        const data = await response.json();
        const botReply = data.choices?.[0]?.message?.content || "Sorry, I couldn’t understand.";
        
        botMessageElement.textContent = botReply;
    } catch (error) {
        botMessageElement.textContent = "Error: Unable to reach server.";
        console.error(error);
    }
});

// Helper function to add messages
function addMessage(text, sender) {
    const chatbox = document.getElementById("chatbox");
    const message = document.createElement("div");
    message.classList.add("message", sender);
    message.textContent = text;
    chatbox.appendChild(message);
    chatbox.scrollTop = chatbox.scrollHeight;
}