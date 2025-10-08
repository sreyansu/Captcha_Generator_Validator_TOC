// This file handles client-side interactions for the CAPTCHA generator and validator.

document.addEventListener('DOMContentLoaded', function() {
    const captchaImage = document.getElementById('captcha-image');
    const refreshButton = document.getElementById('refresh-captcha');
    const captchaForm = document.getElementById('captcha-form');
    const captchaInput = document.getElementById('captcha-input');
    const messageBox = document.getElementById('message-box');

    // Function to refresh the CAPTCHA image
    function refreshCaptcha() {
        captchaImage.src = '/captcha?' + new Date().getTime(); // Append timestamp to avoid caching
    }

    // Event listener for the refresh button
    refreshButton.addEventListener('click', function(event) {
        event.preventDefault();
        refreshCaptcha();
    });

    // Event listener for form submission
    captchaForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const userInput = captchaInput.value;

        fetch('/validate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ captcha: userInput })
        })
        .then(response => response.json())
        .then(data => {
            messageBox.textContent = data.message;
            if (data.valid) {
                messageBox.style.color = 'green';
                // Optionally redirect or perform other actions on success
            } else {
                messageBox.style.color = 'red';
                refreshCaptcha(); // Refresh CAPTCHA on failure
            }
        })
        .catch(error => {
            console.error('Error:', error);
            messageBox.textContent = 'An error occurred. Please try again.';
            messageBox.style.color = 'red';
        });
    });

    // Initial CAPTCHA load
    refreshCaptcha();
});