// popup.js

document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('summarise');
    const output = document.getElementById('output');

    // Add a click event listener to the "Summarise" button
    button.addEventListener('click', function () {
        // Disable the button to prevent multiple clicks
        button.disabled = true;

        // Get the current active tab URL
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            const url = tabs[0].url;

            // Send a message to the background script to initiate the summarization and commenting
            chrome.runtime.sendMessage({ action: "summarizeAndComment", url: url }, function (response) {
                // Handle the response from the background script
                if (response.success) {
                    output.textContent = response.summary;
                } else {
                    output.textContent = 'Error: ' + response.error;
                }

                // Re-enable the button
                button.disabled = false;
            });
        });
    });
});
