document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll('.admin-section');
    
    // Show only one section
    window.showSection = function(id){
        sections.forEach(sec => sec.style.display = (sec.id === id ? 'block' : 'none'));
    }

    // Initialize default section
    showSection('dashboard');

    // --- Product Management ---
    const productForm = document.getElementById("productForm");
    const productCards = document.getElementById("productCards");
    let products = JSON.parse(localStorage.getItem("products") || "[]");

    function renderProducts(){
        productCards.innerHTML = "";
        products.forEach(p=>{
            const div = document.createElement("div");
            div.className = "product-card";
            div.innerHTML = `<img src="${p.image}" alt="${p.name}"><h3>${p.name}</h3><div class="price">$${p.price}</div><p>${p.description}</p>`;
            productCards.appendChild(div);
        });
    }
    renderProducts();

    productForm.addEventListener("submit", (e)=>{
        e.preventDefault();
        const name = document.getElementById("productName").value;
        const price = parseFloat(document.getElementById("productPrice").value);
        const image = document.getElementById("productImage").value;
        const desc = document.getElementById("productDesc").value;
        const newProduct = {id: Date.now(), name, price, image, description: desc};
        products.push(newProduct);
        localStorage.setItem("products", JSON.stringify(products));
        renderProducts();
        productForm.reset();
    });

    // --- Orders Section (dummy data) ---
    const ordersTable = document.querySelector("#ordersTable tbody");
    const dummyOrders = [
        {name:"John",surname:"Doe",email:"john@example.com",phone:"123456",address:"Street 1",product:"Tee",quantity:2,total:70},
        {name:"Jane",surname:"Smith",email:"jane@example.com",phone:"987654",address:"Street 2",product:"Hoodie",quantity:1,total:65},
    ];
    dummyOrders.forEach(o=>{
        const tr = document.createElement("tr");
        tr.innerHTML = `<td>${o.name}</td><td>${o.surname}</td><td>${o.email}</td><td>${o.phone}</td><td>${o.address}</td><td>${o.product}</td><td>${o.quantity}</td><td>$${o.total}</td>`;
        ordersTable.appendChild(tr);
    });

    // --- Analytics Chart ---
    const ctx = document.getElementById('salesChart').getContext('2d');
    new Chart(ctx, {
        type:'bar',
        data:{
            labels:['Jan','Feb','Mar','Apr','May'],
            datasets:[{
                label:'Sales ($)',
                data:[500,700,400,800,600],
                backgroundColor:'rgba(36,70,130,0.7)',
                borderColor:'rgba(112,34,87,0.8)',
                borderWidth:1
            }]
        },
        options:{
            responsive:true,
            scales:{
                y:{beginAtZero:true}
            }
        }
    });
});