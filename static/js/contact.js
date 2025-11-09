document.addEventListener('DOMContentLoaded', function () {
    // 📩 Contact form submission
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', async function (event) {
            event.preventDefault(); // Prevent page reload

            // Clear previous errors
            const errorElements = contactForm.querySelectorAll('.field-error');
            errorElements.forEach(el => el.remove());

            let isValid = true;

            // Get form fields
            const firstName = contactForm.querySelector('[name="first_name"]');
            const lastName = contactForm.querySelector('[name="last_name"]');
            const email = contactForm.querySelector('[name="email"]');
            const subject = contactForm.querySelector('[name="subject"]');
            const message = contactForm.querySelector('[name="message"]');

            // Validation
            if (!firstName.value.trim()) {
                showFieldError(firstName, 'First name is required');
                isValid = false;
            }

            if (!lastName.value.trim()) {
                showFieldError(lastName, 'Last name is required');
                isValid = false;
            }

            if (!email.value.trim()) {
                showFieldError(email, 'Email is required');
                isValid = false;
            } else if (!validateEmail(email.value.trim())) {
                showFieldError(email, 'Invalid email format');
                isValid = false;
            }

            if (!subject.value.trim()) {
                showFieldError(subject, 'Subject is required');
                isValid = false;
            }

            if (!message.value.trim()) {
                showFieldError(message, 'Message is required');
                isValid = false;
            }

            if (!isValid) return; // Stop submission if validation fails

            // Prepare FormData
            const formData = new FormData(contactForm);

            try {
                const response = await fetch(contactForm.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                    },
                });

                if (response.ok) {
                    showNotification('Your message has been sent successfully ✅', 'success');
                    contactForm.reset();
                } else {
                    showNotification('Failed to send the message ❌', 'error');
                }
            } catch (error) {
                console.error('Error:', error);
                showNotification('Unable to connect to the server ⚠️', 'warning');
            }
        });
    }

    // Function to show field errors
    function showFieldError(field, message) {
        const error = document.createElement('div');
        error.className = 'field-error';
        error.style.color = 'red';
        error.style.fontSize = '0.9rem';
        error.style.marginTop = '3px';
        error.textContent = message;
        field.parentNode.appendChild(error);
    }

    // Simple email validation regex
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    // ❓ FAQ accordion
    const faqQuestions = document.querySelectorAll('.contact-faq-question');

    faqQuestions.forEach(question => {
        question.addEventListener('click', function () {
            this.classList.toggle('active');
            const answer = this.nextElementSibling;
            answer.classList.toggle('active');
        });
    });

    // 🔔 Notification function
    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <div class="notification-message">${message}</div>
                <button class="notification-close">&times;</button>
            </div>
        `;

        const style = document.createElement('style');
        style.textContent = `
            .notification {
                position: fixed;
                top: 20px;
                right: 20px;
                min-width: 300px;
                padding: 15px 20px;
                border-radius: 8px;
                background: white;
                color: #333;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
                z-index: 1000;
                display: flex;
                align-items: center;
                justify-content: space-between;
                animation: slideIn 0.3s ease-out;
            }

            .notification-success {
                background: linear-gradient(90deg, #4CAF50, #45a049);
                color: white;
            }

            .notification-info {
                background: linear-gradient(90deg, #2196F3, #0b7dda);
                color: white;
            }

            .notification-warning {
                background: linear-gradient(90deg, #ff9800, #e68900);
                color: white;
            }

            .notification-error {
                background: linear-gradient(90deg, #f44336, #d32f2f);
                color: white;
            }

            .notification-close {
                background: none;
                border: none;
                font-size: 20px;
                cursor: pointer;
                color: inherit;
                margin-left: 15px;
            }

            @keyframes slideIn {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
        `;
        document.head.appendChild(style);

        document.body.appendChild(notification);

        const closeBtn = notification.querySelector('.notification-close');
        closeBtn.addEventListener('click', () => notification.remove());

        setTimeout(() => notification.remove(), 5000);
    }
});
