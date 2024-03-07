document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("signin-form");
    const passwordInput = document.getElementById("password");
    const passwordError = document.getElementById("password-error");

    form.addEventListener("submit", function (e) {
        e.preventDefault();
        
        const password = passwordInput.value;

        if (password.length < 8) {
            passwordError.textContent = "Password must be at least 8 characters long.";
        } else {
            passwordError.textContent = "";
            // Add your sign-in logic here
            // You can submit the form or perform further actions
            // For demonstration, we're just clearing the password field
            passwordInput.value = "";
        }
    });
});
