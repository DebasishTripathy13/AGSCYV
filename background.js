// background.js

chrome.runtime.onInstalled.addListener(function () {
    // Perform any necessary setup or initialization here
});

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === "summarizeAndComment") {
        const url = request.url;

        // Make a request to the Flask server to get the summary
        fetch(`http://127.0.0.1:5000/comment-and-summary?url=${encodeURIComponent(url)}`)
            .then(response => response.json())
            .then(data => {
                // Send the summary back to the content script
                chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
                    chrome.tabs.sendMessage(tabs[0].id, { action: "updateSummary", summary: data.summary }, function (response) {
                        // Handle the response from the content script if needed
                    });
                });
            })
            .catch(error => console.error(error));
    }
});
