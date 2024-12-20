document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("register-form");
    const fields = Array.from(form.querySelectorAll("input[type='text'], input[type='password'], input[type='email']"));
    const registerButton = document.getElementById("register-button");

    const checkFields = () => {
        const allFilled = fields.every(field => field.value.trim() !== "");
        registerButton.disabled = !allFilled;
    };

    fields.forEach(field => field.addEventListener("input", checkFields));
    // Password visibility toggle
    
    // Expose function to global scope for onclick usage
    function togglePasswordVisibility(inputId) {
        const passwordInput = document.getElementById(inputId);
        const toggleIcon = passwordInput.nextElementSibling.querySelector('img');
        
        if (passwordInput.type === "password") {
            passwordInput.type = "text";
            toggleIcon.src = "/static/img/see.svg";
            toggleIcon.alt = "Show Icon";
        } else {
            passwordInput.type = "password";
            toggleIcon.src = "/static/img/hide.svg";
            toggleIcon.alt = "Hide Icon";
        }
    }
    window.togglePasswordVisibility = togglePasswordVisibility;
});