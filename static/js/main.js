document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // File upload preview
    const resumeInput = document.getElementById('resume');
    if (resumeInput) {
        resumeInput.addEventListener('change', function() {
            const fileNameDisplay = document.getElementById('file-name');
            if (fileNameDisplay) {
                const fileName = this.files[0].name;
                fileNameDisplay.textContent = fileName;
                
                // Show the file name container
                document.getElementById('file-name-container').classList.remove('d-none');
            }
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

    // Career path navigation tabs
    const pathTabs = document.querySelectorAll('.path-tab');
    if (pathTabs.length > 0) {
        pathTabs.forEach(tab => {
            tab.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Remove active class from all tabs
                pathTabs.forEach(t => t.classList.remove('active'));
                
                // Add active class to clicked tab
                this.classList.add('active');
                
                // Show the corresponding content
                const targetId = this.getAttribute('data-target');
                const targetContent = document.getElementById(targetId);
                
                // Hide all content sections
                document.querySelectorAll('.path-content').forEach(content => {
                    content.classList.add('d-none');
                });
                
                // Show the target content
                if (targetContent) {
                    targetContent.classList.remove('d-none');
                }
            });
        });
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            
            if (href !== "#" && document.querySelector(href)) {
                e.preventDefault();
                
                document.querySelector(href).scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Progress tracking for multi-step forms
    const progressSteps = document.querySelectorAll('.progress-step');
    if (progressSteps.length > 0) {
        updateProgress();
        
        const stepButtons = document.querySelectorAll('.step-button');
        stepButtons.forEach(button => {
            button.addEventListener('click', function() {
                const step = this.getAttribute('data-step');
                setActiveStep(step);
                updateProgress();
            });
        });
    }

    // Function to update progress bar
    function updateProgress() {
        const activeStep = document.querySelector('.progress-step.active');
        if (activeStep) {
            const stepNumber = parseInt(activeStep.getAttribute('data-step'));
            const totalSteps = progressSteps.length;
            const progressPercent = (stepNumber / totalSteps) * 100;
            
            const progressBar = document.querySelector('.progress-bar');
            if (progressBar) {
                progressBar.style.width = progressPercent + '%';
                progressBar.setAttribute('aria-valuenow', progressPercent);
            }
        }
    }

    // Function to set active step
    function setActiveStep(stepNumber) {
        progressSteps.forEach(step => {
            step.classList.remove('active');
            if (step.getAttribute('data-step') === stepNumber) {
                step.classList.add('active');
            }
        });
        
        const stepContents = document.querySelectorAll('.step-content');
        stepContents.forEach(content => {
            content.classList.add('d-none');
            if (content.getAttribute('data-step') === stepNumber) {
                content.classList.remove('d-none');
            }
        });
    }
});
