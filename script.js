document.addEventListener('DOMContentLoaded', () => {
    const submitButton = document.getElementById('submitButton');
    const mainInput = document.getElementById('mainInput');
    const resultContainer = document.getElementById('resultContainer');
    const resultText = document.querySelector('.ResultofSpam');  // Changed this line
    const toggleCheckbox = document.getElementById('toggle');

    submitButton.addEventListener('click', async () => {
        const message = mainInput.value.trim();

        if (!message) {
            alert('Please enter a message');
            return;
        }

        try {
            const response = await fetch('http://localhost:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();

            toggleCheckbox.checked = true;
            resultContainer.classList.remove('spam', 'not-spam');

            if (data.is_spam) {
                resultContainer.classList.add('spam');
                resultText.textContent = `Spam`;
            } else {
                resultContainer.classList.add('not-spam');
                resultText.textContent = `Not Spam`;
            }

        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again later.');
            toggleCheckbox.checked = false;
        }
    });
});