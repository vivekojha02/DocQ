// static/js/main.js

let otpCooldown = 120; // 2 minutes
let resendTimer;
let idleTimeout;
let idleTimeLimit = 10 * 60 * 1000; // 10 minutes

function startResendCooldown() {
    const button = document.querySelector('form[action="/verify_email"] button');
    button.disabled = true;
    let timeLeft = otpCooldown;

    resendTimer = setInterval(() => {
        if (timeLeft <= 0) {
            button.disabled = false;
            button.textContent = "Send OTP";
            clearInterval(resendTimer);
        } else {
            button.textContent = `Wait ${timeLeft}s`;
            timeLeft--;
        }
    }, 1000);
}

function resetIdleTimer() {
    clearTimeout(idleTimeout);
    idleTimeout = setTimeout(() => {
        alert("Session expired due to inactivity.");
        window.location.href = "/";
    }, idleTimeLimit);
}

// Attach idle timer to all activity
['mousemove', 'keydown', 'click'].forEach(event => {
    document.addEventListener(event, resetIdleTimer);
});

// Basic OTP resend restriction (on load)
window.onload = () => {
    if (document.querySelector('form[action="/verify_email"]')) {
        startResendCooldown();
    }
    resetIdleTimer();
};
