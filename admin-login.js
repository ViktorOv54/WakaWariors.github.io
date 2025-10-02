// login.js

document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("loginForm");
    const errorMsg = document.getElementById("error-msg");
    const backButton = document.getElementById("back-btn");

    // Example admin credentials (change as needed)
    const adminCredentials = {
        username: "admin",
        password: "dragon123"
    };

    // Back button
    if (backButton) {
        backButton.addEventListener("click", () => {
            window.history.back();
        });
    }

    // Handle form submit
    loginForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const username = document.getElementById("username").value.trim();
        const password = document.getElementById("password").value.trim();

        if (username === adminCredentials.username && password === adminCredentials.password) {
            // Successful login
            localStorage.setItem("isAdmin", "true"); // optional, can be used in admin.html
            window.location.href = "admin.html";
        } else {
            // Wrong credentials
            errorMsg.textContent = "❌ Invalid username or password!";
        }
    });
});     