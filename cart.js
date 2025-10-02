const cartItems = document.getElementById("cart-items");
const cartTotal = document.getElementById("cart-total");

function renderCart(){
  let cart = JSON.parse(localStorage.getItem("cart") || "[]");
  cartItems.innerHTML = "";
  let total=0;
  cart.forEach((item,index)=>{
    total+=item.price;
    const div=document.createElement("div");
    div.innerHTML=`${item.name} - $${item.price.toFixed(2)} <button onclick="removeItem(${index})">Remove</button>`;
    cartItems.appendChild(div);
  });
  cartTotal.textContent=`Total: $${total.toFixed(2)}`;
}

function removeItem(index){
  let cart = JSON.parse(localStorage.getItem("cart") || "[]");
  cart.splice(index,1);
  localStorage.setItem("cart", JSON.stringify(cart));
  renderCart();
}

renderCart();