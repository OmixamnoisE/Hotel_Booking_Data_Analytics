const ctx = document.getElementById('visitorChart').getContext('2d');

const visitorChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [], // Labels will be updated based on button clicks
        datasets: [{
            label: 'Visitors',
            data: [], // Data will be updated based on button clicks
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Sample data for different views
const data = {
    daily: {
        labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'],
        values: [50, 70, 80, 90, 100]
    },
    monthly: {
        labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        values: [200, 250, 300, 400]
    },
    yearly: {
        labels: ['January', 'February', 'March', 'April'],
        values: [1200, 1300, 1400, 1500]
    }
};

function updateChart(view) {
    visitorChart.data.labels = data[view].labels;
    visitorChart.data.datasets[0].data = data[view].values;
    visitorChart.update();
}

document.getElementById('dailyBtn').addEventListener('click', () => updateChart('daily'));
document.getElementById('monthlyBtn').addEventListener('click', () => updateChart('monthly'));
document.getElementById('yearlyBtn').addEventListener('click', () => updateChart('yearly'));

// Initialize with daily data
updateChart('daily');
