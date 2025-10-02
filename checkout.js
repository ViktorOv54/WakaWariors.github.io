const form = document.getElementById("checkoutForm");
const confirmation = document.getElementById("confirmation");

form.addEventListener("submit", function(e){
    e.preventDefault();
    // Simple validation
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    if(name && email){
        localStorage.removeItem("cart"); // clear cart
        form.classList.add("hidden");
        confirmation.classList.remove("hidden");
    }
});