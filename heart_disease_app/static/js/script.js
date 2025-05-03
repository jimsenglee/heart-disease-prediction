// Wait for the DOM to be ready
document.addEventListener('DOMContentLoaded', function() {
   // Check if we're on the results page
   const resultCard = document.querySelector('.result-card');
   if (resultCard) {
       // Add animation for result card
       setTimeout(() => {
           resultCard.classList.add('animated');
       }, 300);
       
       // Set width and animate the probability meter
       const meterFills = document.querySelectorAll('.meter-fill');
       meterFills.forEach(fill => {
           const width = fill.getAttribute('data-width');
           if (width) {
               // Determine risk level based on percentage
               const percentage = parseFloat(width);
               let riskClass = 'low-risk';
               
               if (percentage >= 70) {
                   riskClass = 'high-risk';
               } else if (percentage >= 40) {
                   riskClass = 'medium-risk';
               }
               
               // Start animation after a short delay
               setTimeout(() => {
                   // Set the final width as a CSS variable
                   fill.style.setProperty('--target-width', width + '%');
                   
                   // Add the risk-appropriate class
                   fill.classList.add(riskClass);
                   
                   // Set the actual width for browsers that don't support CSS variables
                   fill.style.width = width + '%';
               }, 500);
           }
       });
   }
   
   // Add real-time update for range sliders
   const rangeInputs = document.querySelectorAll('input[type="range"]');
   rangeInputs.forEach(input => {
       // Get the correct output element ID based on the slider ID
       let outputId;
       switch(input.id) {
           case 'trestbps':
               outputId = 'bpOutput';
               break;
           case 'thalach':
               outputId = 'hrOutput';
               break;
           case 'oldpeak':
               outputId = 'stOutput';
               break;
           case 'chol':
               outputId = 'cholOutput';
               break;
           case 'age':
               outputId = 'ageOutput';
               break;
           default:
               outputId = input.id + 'Output';
       }
       
       const output = document.getElementById(outputId);
       
       if (output) {
           // Set initial value
           output.textContent = input.value;
           
           // Update the output when the slider is moved
           input.addEventListener('input', function() {
               output.textContent = this.value;
               
               // Change color based on value (for visual feedback)
               const value = parseFloat(this.value);
               const max = parseFloat(this.max);
               const min = parseFloat(this.min);
               const percentage = ((value - min) / (max - min)) * 100;
               
               // Determine if higher values are good or bad for this input
               let hue;
               if (this.id === 'thalach') {
                   // For heart rate, higher is generally better (up to a point)
                   hue = percentage * 1.2; 
               } else {
                   // For blood pressure, cholesterol, oldpeak - lower is better
                   hue = ((100 - percentage) * 1.2);
               }
               
               output.style.backgroundColor = `hsl(${hue}, 80%, 50%)`;
           });
           
           // Trigger the input event to set initial colors
           input.dispatchEvent(new Event('input'));
       }
   });
   const form = document.querySelector('form');
   if (form) {
    // Define validation constraints for each input
    const constraints = {
      age: { min: 20, max: 100 },
      trestbps: { min: 80, max: 200 },
      chol: { min: 100, max: 400 },
      thalach: { min: 70, max: 220 },
      oldpeak: { min: 0, max: 6 },
      sex: { options: ['0', '1'] },
      fbs: { options: ['0', '1'] },
      exang: { options: ['0', '1'] },
      cp: { options: ['0', '1', '2', '3', '4'] },
      restecg: { options: ['0', '1', '2'] },
      slope: { options: ['0', '1', '2'] },
      ca: { options: ['0', '1', '2', '3', '4'] },
      thal: { options: ['0', '1', '2'] }
    };

    // Create error message element
    const errorContainer = document.createElement('div');
    errorContainer.className = 'error-container';
    errorContainer.style.color = 'red';
    errorContainer.style.padding = '10px';
    errorContainer.style.marginBottom = '15px';
    errorContainer.style.display = 'none';
    form.insertBefore(errorContainer, form.firstChild);

    // Form submission validation
    form.addEventListener('submit', function(e) {
      let errors = [];
      
      // Validate each numeric input
      ['age', 'trestbps', 'chol', 'thalach', 'oldpeak'].forEach(field => {
        const input = document.getElementById(field);
        const value = parseFloat(input.value);
        const constraint = constraints[field];
        
        if (isNaN(value) || value < constraint.min || value > constraint.max) {
          errors.push(`${field} must be between ${constraint.min} and ${constraint.max}`);
          input.classList.add('invalid');
        } else {
          input.classList.remove('invalid');
        }
      });
      
      // Validate radio buttons and select elements
      ['sex', 'fbs', 'exang', 'cp', 'restecg', 'slope', 'ca', 'thal'].forEach(field => {
        let value;
        
        // Different handling for radio buttons vs select elements
        if (['sex', 'fbs', 'exang'].includes(field)) {
          const selectedRadio = document.querySelector(`input[name="${field}"]:checked`);
          value = selectedRadio ? selectedRadio.value : null;
        } else {
          const select = document.getElementById(field);
          value = select ? select.value : null;
        }
        
        if (!value || !constraints[field].options.includes(value)) {
          errors.push(`Please select a valid option for ${field}`);
        }
      });
      
      // If there are errors, prevent form submission and show error messages
      if (errors.length > 0) {
        e.preventDefault();
        errorContainer.innerHTML = errors.map(err => `<div>${err}</div>`).join('');
        errorContainer.style.display = 'block';
        
        // Scroll to error messages
        errorContainer.scrollIntoView({ behavior: 'smooth' });
      } else {
        // Clear any previous errors
        errorContainer.style.display = 'none';
        errorContainer.innerHTML = '';
      }
    });
    
    // Add input event listeners to validate in real-time
    ['age', 'trestbps', 'chol', 'thalach', 'oldpeak'].forEach(field => {
      const input = document.getElementById(field);
      if (input) {
        input.addEventListener('input', function() {
          const value = parseFloat(this.value);
          const constraint = constraints[field];
          
          if (isNaN(value) || value < constraint.min || value > constraint.max) {
            this.classList.add('invalid');
          } else {
            this.classList.remove('invalid');
          }
        });
      }
    });
  }
  
  // Add required CSS for validation
  const style = document.createElement('style');
  style.textContent = `
    input.invalid, select.invalid {
      border: 2px solid red !important;
      background-color: rgba(255, 0, 0, 0.1) !important;
    }
    .error-container {
      background-color: #fff0f0;
      border-left: 4px solid #ff5555;
    }
  `;
  document.head.appendChild(style);
});

function changeLanguage() {
    // Get the form and selected language
    var form = document.getElementById('languageForm');
    var lang = document.getElementById('languageSelect').value;
    
    // Use fetch API to submit the form
    fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Reload the current page to show translated content
            window.location.reload();
        }
    })
    .catch(error => console.error('Error:', error));
}