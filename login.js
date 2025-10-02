// Load users from localStorage or set default
let users = JSON.parse(localStorage.getItem("devUsers")) || {
  "viktor orlov": "dragon2025!",
  "vinicius scofield": "paddleMaster@88"
};

// Login form handler
document.getElementById("loginForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const username = document.getElementById("username").value.trim().toLowerCase();
  const password = document.getElementById("password").value;

  if (users[username] && users[username] === password) {
    window.location.href = "developer-tools.html";
  } else {
    const msg = document.getElementById("loginMessage");
    msg.textContent = "Invalid username or password.";
    msg.style.color = "red";
  }
});

// Forgot password handler
document.getElementById("forgotPassword").addEventListener("click", function (e) {
  e.preventDefault();

  const username = prompt("Enter your username:");
  if (!username) return;

  const lowerUsername = username.trim().toLowerCase();
  if (!users[lowerUsername]) {
    alert("User not found.");
    return;
  }

  const newPassword = prompt(`Enter a new password for ${username}:`);
  if (!newPassword) {
    alert("Password not changed.");
    return;
  }

  // Update password in object and localStorage
  users[lowerUsername] = newPassword;
  localStorage.setItem("devUsers", JSON.stringify(users));

  alert(`Password for ${username} has been updated successfully.`);
});