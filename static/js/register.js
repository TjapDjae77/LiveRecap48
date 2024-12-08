document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("register-form");
    const fields = Array.from(form.querySelectorAll("input[type='text'], input[type='password'], input[type='email']"));
    const registerButton = document.getElementById("register-button");

    const checkFields = () => {
        const allFilled = fields.every(field => field.value.trim() !== "");
        registerButton.disabled = !allFilled;
    };

    fields.forEach(field => field.addEventListener("input", checkFields));
});
