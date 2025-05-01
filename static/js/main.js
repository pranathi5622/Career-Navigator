// Career Guidance Application - Main JavaScript file

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips and popovers if Bootstrap is available
    if (typeof bootstrap !== 'undefined') {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });

        const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
        popoverTriggerList.map(function (popoverTriggerEl) {
            return new bootstrap.Popover(popoverTriggerEl);
        });
    }

    // Form validation 
    const forms = document.querySelectorAll('.needs-validation');
    
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            
            form.classList.add('was-validated');
        }, false);
    });

    // File input handling for resume upload
    const resumeInput = document.getElementById('resume');
    if (resumeInput) {
        resumeInput.addEventListener('change', function() {
            const fileLabel = document.querySelector('.custom-file-label');
            if (fileLabel) {
                fileLabel.textContent = this.files[0]?.name || 'Choose file';
            }
            
            // Simple validation for file type
            const fileType = this.files[0]?.type;
            const validTypes = ['application/pdf'];
            
            if (this.files.length > 0 && !validTypes.includes(fileType)) {
                alert('Please upload a PDF file');
                this.value = '';
                if (fileLabel) {
                    fileLabel.textContent = 'Choose file';
                }
            }
        });
    }

    // Career selection handling - update the form when a career is selected
    const careerSelect = document.getElementById('career');
    if (careerSelect) {
        careerSelect.addEventListener('change', function() {
            const selectedCareer = this.value;
            if (selectedCareer) {
                // You could make an AJAX call here to get career details if needed
                console.log(`Career selected: ${selectedCareer}`);
            }
        });
    }

    // Handle multi-step forms if present
    setupMultiStepForm();

    // Setup any charts on the page
    setupCharts();
});

function setupMultiStepForm() {
    const multiStepForms = document.querySelectorAll('.multi-step-form');
    
    multiStepForms.forEach(form => {
        const steps = form.querySelectorAll('.form-step');
        const nextButtons = form.querySelectorAll('.btn-next');
        const prevButtons = form.querySelectorAll('.btn-prev');
        const progress = form.querySelector('.progress-bar');
        
        let currentStep = 0;
        
        // Show the initial step
        if (steps.length > 0) {
            showStep(currentStep);
        }
        
        // Setup next buttons
        nextButtons.forEach(button => {
            button.addEventListener('click', function() {
                // Validate the current step before proceeding
                const currentStepElement = steps[currentStep];
                const inputs = currentStepElement.querySelectorAll('input, select, textarea');
                let isValid = true;
                
                inputs.forEach(input => {
                    if (input.hasAttribute('required') && !input.value) {
                        isValid = false;
                        input.classList.add('is-invalid');
                    } else {
                        input.classList.remove('is-invalid');
                    }
                });
                
                if (isValid && currentStep < steps.length - 1) {
                    currentStep++;
                    showStep(currentStep);
                }
            });
        });
        
        // Setup previous buttons
        prevButtons.forEach(button => {
            button.addEventListener('click', function() {
                if (currentStep > 0) {
                    currentStep--;
                    showStep(currentStep);
                }
            });
        });
        
        function showStep(stepIndex) {
            // Hide all steps
            steps.forEach(step => step.classList.add('d-none'));
            
            // Show the current step
            steps[stepIndex].classList.remove('d-none');
            
            // Update progress bar if it exists
            if (progress) {
                const progressPercentage = ((stepIndex + 1) / steps.length) * 100;
                progress.style.width = `${progressPercentage}%`;
                progress.setAttribute('aria-valuenow', progressPercentage);
            }
            
            // Update button states
            prevButtons.forEach(button => {
                button.disabled = stepIndex === 0;
            });
            
            nextButtons.forEach(button => {
                if (stepIndex === steps.length - 1) {
                    button.textContent = 'Submit';
                    button.classList.add('btn-success');
                    button.classList.remove('btn-primary');
                    // Change the button type to submit on the last step
                    button.setAttribute('type', 'submit');
                } else {
                    button.textContent = 'Next';
                    button.classList.add('btn-primary');
                    button.classList.remove('btn-success');
                    button.setAttribute('type', 'button');
                }
            });
        }
    });
}

function setupCharts() {
    // Set up roadmap chart if it exists
    const roadmapChartElement = document.getElementById('roadmapChart');
    if (roadmapChartElement) {
        const ctx = roadmapChartElement.getContext('2d');
        const currentStage = parseInt(roadmapChartElement.dataset.currentStage || 0);
        
        const roadmapChart = new Chart(ctx, {
            type: 'horizontalBar',
            data: {
                labels: ['Entry Level', 'Mid-Level', 'Senior Level', 'Expert / Leadership'],
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
    
    // Set up comparison chart if it exists
    const comparisonChartElement = document.getElementById('comparisonChart');
    if (comparisonChartElement) {
        const ctx = comparisonChartElement.getContext('2d');
        const career1 = comparisonChartElement.dataset.career1;
        const career2 = comparisonChartElement.dataset.career2;
        const career1SkillMatch = parseFloat(comparisonChartElement.dataset.skillMatch1 || 0);
        const career2SkillMatch = parseFloat(comparisonChartElement.dataset.skillMatch2 || 0);
        
        const comparisonChart = new Chart(ctx, {
            type: 'radar',
            data: {
                labels: ['Skill Match', 'Education Fit', 'Salary Potential', 'Growth Outlook', 'Work/Life Balance'],
                datasets: [
                    {
                        label: career1,
                        data: [
                            career1SkillMatch,
                            parseFloat(comparisonChartElement.dataset.eduFit1 || 50),
                            parseFloat(comparisonChartElement.dataset.salary1 || 50),
                            parseFloat(comparisonChartElement.dataset.growth1 || 50),
                            parseFloat(comparisonChartElement.dataset.balance1 || 50)
                        ],
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        borderColor: 'rgb(54, 162, 235)',
                        pointBackgroundColor: 'rgb(54, 162, 235)',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: 'rgb(54, 162, 235)'
                    },
                    {
                        label: career2,
                        data: [
                            career2SkillMatch,
                            parseFloat(comparisonChartElement.dataset.eduFit2 || 50),
                            parseFloat(comparisonChartElement.dataset.salary2 || 50),
                            parseFloat(comparisonChartElement.dataset.growth2 || 50),
                            parseFloat(comparisonChartElement.dataset.balance2 || 50)
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
    
    // Set up recommendation chart if it exists
    const recommendationChartElement = document.getElementById('recommendationChart');
    if (recommendationChartElement) {
        const ctx = recommendationChartElement.getContext('2d');
        const recommendationData = JSON.parse(recommendationChartElement.dataset.recommendations || '[]');
        
        if (recommendationData.length > 0) {
            const labels = recommendationData.map(item => item.career);
            const scores = recommendationData.map(item => item.score);
            
            const recommendationChart = new Chart(ctx, {
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
    }
}
