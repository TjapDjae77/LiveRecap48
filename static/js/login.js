document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("login-form");
    const usernameField = document.getElementById("id_username");
    const passwordField = document.getElementById("id_password");
    const loginButton = document.getElementById("login-button");

    // Function to check if all fields are filled
    const checkFields = () => {
        const isUsernameFilled = usernameField.value.trim() !== "";
        const isPasswordFilled = passwordField.value.trim() !== "";
        loginButton.disabled = !(isUsernameFilled && isPasswordFilled); // Enable button if all fields are filled
    };

    // Add event listeners for real-time input validation
    usernameField.addEventListener("input", checkFields);
    passwordField.addEventListener("input", checkFields);
});
