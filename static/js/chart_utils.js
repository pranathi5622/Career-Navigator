// Chart utilities for career guidance application

/**
 * Creates a career roadmap chart
 * @param {string} elementId - Canvas element ID
 * @param {number} currentStage - User's current career stage (0-3)
 * @param {string[]} stageLabels - Array of stage labels
 */
function createRoadmapChart(elementId, currentStage, stageLabels = ['Entry Level', 'Mid-Level', 'Senior Level', 'Expert / Leadership']) {
    const canvas = document.getElementById(elementId);
    if (!canvas || !canvas.getContext) return;
    
    const ctx = canvas.getContext('2d');
    
    return new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: stageLabels,
            datasets: [{
                label: 'Career Progression',
                data: [100, 100, 100, 100],
                backgroundColor: [
                    currentStage >= 0 ? 'rgba(40, 167, 69, 0.7)' : 'rgba(108, 117, 125, 0.3)',
                    currentStage >= 1 ? 'rgba(40, 167, 69, 0.7)' : 'rgba(108, 117, 125, 0.3)',
                    currentStage >= 2 ? 'rgba(40, 167, 69, 0.7)' : 'rgba(108, 117, 125, 0.3)',
                    currentStage >= 3 ? 'rgba(40, 167, 69, 0.7)' : 'rgba(108, 117, 125, 0.3)'
                ],
                borderColor: [
                    currentStage === 0 ? 'rgba(40, 167, 69, 1)' : 'rgba(108, 117, 125, 0.5)',
                    currentStage === 1 ? 'rgba(40, 167, 69, 1)' : 'rgba(108, 117, 125, 0.5)',
                    currentStage === 2 ? 'rgba(40, 167, 69, 1)' : 'rgba(108, 117, 125, 0.5)',
                    currentStage === 3 ? 'rgba(40, 167, 69, 1)' : 'rgba(108, 117, 125, 0.5)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    display: false,
                    max: 100
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

/**
 * Creates a career comparison radar chart
 * @param {string} elementId - Canvas element ID
 * @param {Object} data - Comparison data
 */
function createComparisonChart(elementId, data) {
    const canvas = document.getElementById(elementId);
    if (!canvas || !canvas.getContext) return;
    
    const ctx = canvas.getContext('2d');
    
    return new Chart(ctx, {
        type: 'radar',
        data: {
            labels: ['Skill Match', 'Education Fit', 'Salary Potential', 'Growth Outlook', 'Work/Life Balance'],
            datasets: [
                {
                    label: data.career1.name,
                    data: [
                        data.career1.skillMatch,
                        data.career1.educationFit,
                        data.career1.salaryPotential,
                        data.career1.growthOutlook,
                        data.career1.workLifeBalance
                    ],
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgb(54, 162, 235)',
                    pointBackgroundColor: 'rgb(54, 162, 235)',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: 'rgb(54, 162, 235)'
                },
                {
                    label: data.career2.name,
                    data: [
                        data.career2.skillMatch,
                        data.career2.educationFit,
                        data.career2.salaryPotential,
                        data.career2.growthOutlook,
                        data.career2.workLifeBalance
                    ],
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
                    suggestedMax: 100
                }
            }
        }
    });
}

/**
 * Creates a career recommendation bar chart
 * @param {string} elementId - Canvas element ID
 * @param {Array} recommendations - Array of recommendation objects
 */
function createRecommendationChart(elementId, recommendations) {
    const canvas = document.getElementById(elementId);
    if (!canvas || !canvas.getContext || !recommendations || !recommendations.length) return;
    
    const ctx = canvas.getContext('2d');
    
    const labels = recommendations.map(item => item.career);
    const scores = recommendations.map(item => item.score);
    
    return new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Match Score',
                data: scores,
                backgroundColor: 'rgba(75, 192, 192, 0.7)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Match Score'
                    }
                }
            }
        }
    });
}

/**
 * Creates a skill gap doughnut chart
 * @param {string} elementId - Canvas element ID
 * @param {Object} data - Skill data with matching and missing skills
 */
function createSkillGapChart(elementId, data) {
    const canvas = document.getElementById(elementId);
    if (!canvas || !canvas.getContext) return;
    
    const ctx = canvas.getContext('2d');
    
    return new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Matching Skills', 'Skill Gaps'],
            datasets: [{
                data: [data.matchingSkills.length, data.missingSkills.length],
                backgroundColor: [
                    'rgba(40, 167, 69, 0.7)',
                    'rgba(220, 53, 69, 0.7)'
                ],
                borderColor: [
                    'rgba(40, 167, 69, 1)',
                    'rgba(220, 53, 69, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.formattedValue || '';
                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                            const percentage = Math.round((context.raw / total) * 100);
                            return `${label}: ${value} (${percentage}%)`;
                        }
                    }
                }
            }
        }
    });
}

/**
 * Helper function to format salary ranges for display in charts
 * @param {string} salaryRange - Salary range string (e.g., "$70,000 - $150,000+")
 * @returns {number} - Normalized salary score from 0-100
 */
function normalizeSalaryForChart(salaryRange) {
    if (!salaryRange || typeof salaryRange !== 'string') return 50;
    
    // Extract the upper end of the salary range
    const match = salaryRange.match(/\$(\d+,\d+)\+?/g);
    if (!match || match.length === 0) return 50;
    
    // Get the highest number mentioned
    let highestSalary = 0;
    match.forEach(salary => {
        const cleanSalary = parseInt(salary.replace(/[\$,\+]/g, ''));
        if (cleanSalary > highestSalary) {
            highestSalary = cleanSalary;
        }
    });
    
    // Normalize to 0-100 scale (assuming $200,000 is the top end)
    return Math.min(Math.round((highestSalary / 200000) * 100), 100);
}

/**
 * Helper function to format job outlook for display in charts
 * @param {string} outlookText - Job outlook text
 * @returns {number} - Normalized outlook score from 0-100
 */
function normalizeOutlookForChart(outlookText) {
    if (!outlookText || typeof outlookText !== 'string') return 50;
    
    const lowerText = outlookText.toLowerCase();
    
    if (lowerText.includes('much faster')) {
        return 90;
    } else if (lowerText.includes('faster')) {
        return 75;
    } else if (lowerText.includes('average')) {
        return 50;
    } else if (lowerText.includes('slower')) {
        return 25;
    } else if (lowerText.includes('decline')) {
        return 10;
    }
    
    // Extract growth percentage if available
    const percentMatch = lowerText.match(/(\d+)%/);
    if (percentMatch && percentMatch[1]) {
        const percent = parseInt(percentMatch[1]);
        return Math.min(percent * 5, 100); // Normalize: 20% growth = 100 score
    }
    
    return 50; // Default value if no pattern matches
}
