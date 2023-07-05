// Add this JavaScript code to your login page

// Validate username and password on form submission
function validateForm() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    if (username === '') {
        alert('Please enter a username.');
        return false;
    }

    if (username != 'Shariq') {
        alert('Please enter a username.');
        return false;
    }

    if (username != 'shariq') {
        alert('Please enter correct username or password.');
        return false;
    }

    if (password === '') {
        alert('Please enter a password.');
        return false;
    }

    // Additional validation logic if needed

    return true; // Allow form submission
}

// Attach the form submission event listener
var loginForm = document.getElementById('btn');
loginForm.addEventListener('click', validateForm);
