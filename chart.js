const salesData = {
  labels: ["Tee", "Hoodie", "Bottle", "Paddle", "Cap"],
  datasets: [{
    label: 'Units Sold',
    data: [120, 80, 150, 50, 60],
    backgroundColor: 'rgba(0, 255, 247, 0.7)',
    borderColor: '#00fff7',
    borderWidth: 2,
    borderRadius: 5
  }]
};

const revenueData = {
  labels: ["Jan", "Feb", "Mar", "Apr", "May"],
  datasets: [{
    label: 'Revenue ($)',
    data: [1200, 1500, 900, 2000, 1750],
    backgroundColor: 'rgba(112,34,87,0.7)',
    borderColor: '#702257',
    borderWidth: 2,
    borderRadius: 5
  }]
};

const customersData = {
  labels: ["Alice", "Bob", "Charlie", "David", "Eva"],
  datasets: [{
    label: 'Purchases',
    data: [5, 8, 2, 6, 3],
    backgroundColor: [
      '#00fff7','#702257','#244682','#fff100','#ff0055'
    ],
    borderWidth: 1
  }]
};

// Create charts
new Chart(document.getElementById('salesChart'), {
    type: 'bar',
    data: salesData,
    options: { responsive: true, plugins: { legend: { display: false } } }
});

new Chart(document.getElementById('revenueChart'), {
    type: 'line',
    data: revenueData,
    options: { responsive: true, plugins: { legend: { display: false } } }
});

new Chart(document.getElementById('customersChart'), {
    type: 'pie',
    data: customersData,
    options: { responsive: true }
});