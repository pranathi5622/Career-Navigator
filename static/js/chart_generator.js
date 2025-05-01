/**
 * Career Chart Generator
 * Creates various chart visualizations for career data using Chart.js
 */

// Function to generate a radar chart for career skill comparison
function generateSkillsRadarChart(elementId, careerOne, careerTwo) {
    const ctx = document.getElementById(elementId).getContext('2d');
    
    // Define skills to compare
    const skills = [
        'Technical Skills',
        'Communication',
        'Problem Solving',
        'Creativity',
        'Leadership',
        'Analytical Thinking'
    ];
    
    // Get random scores for each career (in a real app, this would be real data)
    const careerOneScores = careerOne.skills.map(() => Math.floor(Math.random() * 5) + 3);
    const careerTwoScores = careerTwo.skills.map(() => Math.floor(Math.random() * 5) + 3);
    
    // Create the chart
    const radarChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: skills,
            datasets: [
                {
                    label: careerOne.title,
                    data: careerOneScores,
                    fill: true,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgb(54, 162, 235)',
                    pointBackgroundColor: 'rgb(54, 162, 235)',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: 'rgb(54, 162, 235)'
                },
                {
                    label: careerTwo.title,
                    data: careerTwoScores,
                    fill: true,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgb(255, 99, 132)',
                    pointBackgroundColor: 'rgb(255, 99, 132)',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: 'rgb(255, 99, 132)'
                }
            ]
        },
        options: {
            elements: {
                line: {
                    borderWidth: 3
                }
            },
            scales: {
                r: {
                    angleLines: {
                        display: true
                    },
                    suggestedMin: 0,
                    suggestedMax: 10
                }
            }
        }
    });
    
    return radarChart;
}

// Function to generate a bar chart for salary comparison
function generateSalaryComparisonChart(elementId, careerOne, careerTwo) {
    const ctx = document.getElementById(elementId).getContext('2d');
    
    // Parse salary ranges (in a real app, this would handle real data more robustly)
    const careerOneSalaryRange = careerOne.salaryRange || "$70,000 - $120,000";
    const careerTwoSalaryRange = careerTwo.salaryRange || "$60,000 - $100,000";
    
    // Extract min and max values
    const careerOneMin = parseInt(careerOneSalaryRange.match(/\$([0-9,]+)/)[1].replace(',', ''));
    const careerOneMax = parseInt(careerOneSalaryRange.match(/\$([0-9,]+)\+?$/)[1].replace(',', ''));
    
    const careerTwoMin = parseInt(careerTwoSalaryRange.match(/\$([0-9,]+)/)[1].replace(',', ''));
    const careerTwoMax = parseInt(careerTwoSalaryRange.match(/\$([0-9,]+)\+?$/)[1].replace(',', ''));
    
    // Create the chart
    const barChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Minimum Salary', 'Maximum Salary'],
            datasets: [
                {
                    label: careerOne.title,
                    data: [careerOneMin, careerOneMax],
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    borderColor: 'rgb(54, 162, 235)',
                    borderWidth: 1
                },
                {
                    label: careerTwo.title,
                    data: [careerTwoMin, careerTwoMax],
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',
                    borderColor: 'rgb(255, 99, 132)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Salary (USD)'
                    }
                }
            }
        }
    });
    
    return barChart;
}

// Function to generate a roadmap chart
function generateRoadmapChart(elementId, careerData) {
    const ctx = document.getElementById(elementId).getContext('2d');
    
    // Get milestones
    const milestones = careerData.milestones || [];
    
    // Create labels and data
    const labels = milestones.map(m => m.title);
    const data = milestones.map((_, index) => index + 1); // Simple progression
    
    // Determine colors based on level
    const backgroundColors = milestones.map(m => {
        switch(m.level) {
            case 'Beginner': return 'rgba(75, 192, 192, 0.5)';
            case 'Intermediate': return 'rgba(54, 162, 235, 0.5)';
            case 'Advanced': return 'rgba(153, 102, 255, 0.5)';
            default: return 'rgba(201, 203, 207, 0.5)';
        }
    });
    
    const borderColors = milestones.map(m => {
        switch(m.level) {
            case 'Beginner': return 'rgb(75, 192, 192)';
            case 'Intermediate': return 'rgb(54, 162, 235)';
            case 'Advanced': return 'rgb(153, 102, 255)';
            default: return 'rgb(201, 203, 207)';
        }
    });
    
    // Create the chart
    const roadmapChart = new Chart(ctx, {
        type: 'horizontalBar', // This type is deprecated in Chart.js v3, so we would use 'bar' with indexAxis: 'y' in a real app
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Career Progression',
                    data: data,
                    backgroundColor: backgroundColors,
                    borderColor: borderColors,
                    borderWidth: 1
                }
            ]
        },
        options: {
            indexAxis: 'y', // For Chart.js v3
            responsive: true,
            scales: {
                x: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Progression'
                    }
                }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        afterLabel: function(context) {
                            const index = context.dataIndex;
                            return milestones[index].description;
                        }
                    }
                }
            }
        }
    });
    
    return roadmapChart;
}

// Function to generate a doughnut chart for job metrics
function generateJobMetricsChart(elementId, careerData) {
    const ctx = document.getElementById(elementId).getContext('2d');
    
    // Get metrics
    const workLifeBalance = careerData.workLifeBalance || 3;
    const jobSatisfaction = careerData.jobSatisfaction || 3;
    const jobStability = careerData.jobStability || 3;
    
    // Create the chart
    const doughnutChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: [
                'Work-Life Balance',
                'Job Satisfaction',
                'Job Stability'
            ],
            datasets: [{
                label: 'Job Metrics',
                data: [workLifeBalance, jobSatisfaction, jobStability],
                backgroundColor: [
                    'rgb(255, 99, 132)',
                    'rgb(54, 162, 235)',
                    'rgb(255, 205, 86)'
                ],
                hoverOffset: 4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const value = context.parsed;
                            return `Rating: ${value} out of 5`;
                        }
                    }
                }
            }
        }
    });
    
    return doughnutChart;
}
