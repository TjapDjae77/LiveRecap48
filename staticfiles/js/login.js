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

function togglePasswordVisibility() {
    // Ambil elemen password input dan icon
    const passwordInput = document.getElementById('id_password');
    const toggleIcon = passwordInput.nextElementSibling.querySelector('img');
    
    // Toggle tipe input antara password dan text
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleIcon.src = toggleIcon.src.replace('hide.svg', 'see.svg');
    } else {
        passwordInput.type = 'password';
        toggleIcon.src = toggleIcon.src.replace('see.svg', 'hide.svg');
    }
}
