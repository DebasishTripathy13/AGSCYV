// content.js

chrome.runtime.sendMessage({
    action: "summarizeAndComment",
    url: window.location.href
});
