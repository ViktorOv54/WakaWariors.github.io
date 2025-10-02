// Sample products
let products = JSON.parse(localStorage.getItem("products") || "[]");
if(products.length === 0){
  products = [
    {id:1,name:"Dragon Boat Club Tee",price:35,image:"images/tee.jpg",description:"Soft cotton t-shirt with embroidered logo."},
    {id:2,name:"Club Hoodie",price:65,image:"images/hoodie.jpg",description:"Warm, fleece-lined hoodie."},
    {id:3,name:"Insulated Bottle",price:22,image:"images/bottle.jpg",description:"Keeps drinks cold for 24 hours."}
  ];
  localStorage.setItem("products", JSON.stringify(products));
}

const catalog = document.getElementById("catalog");

function renderCatalog(){
  catalog.innerHTML = "";
  products.forEach((p,index)=>{
    const div=document.createElement("div");
    div.className="card";
    div.innerHTML=`
      <img src="${p.image}" alt="${p.name}">
      <h3>${p.name}</h3>
      <div class="price">$${p.price.toFixed(2)}</div>
      <p>${p.description}</p>
      <div class="actions">
        <button class="btn add" onclick="addToCart(${p.id})">Add to Cart</button>
        <button class="btn buy" onclick="buyNow(${p.id})">Buy Now</button>
      </div>
    `;
    catalog.appendChild(div);
  });
}

function addToCart(id){
  let cart = JSON.parse(localStorage.getItem("cart") || "[]");
  const product = products.find(p=>p.id===id);
  cart.push(product);
  localStorage.setItem("cart", JSON.stringify(cart));
  alert(`${product.name} added to cart`);
}

function buyNow(id){
  addToCart(id);
  window.location.href="cart.html";
}

renderCatalog();