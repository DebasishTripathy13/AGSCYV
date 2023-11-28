# AGSCYV Chrome Extension - Summarizer
Generating summaries and comments for YouTube videos


## Overview
1.Load the extension in Chrome:

-Open Chrome and navigate to chrome://extensions/.
-Enable "Developer mode" in the top right.
-Click "Load unpacked" and select the extension directory.

2. Load the extension in Chrome:

   - Open Chrome and navigate to `chrome://extensions/`.
   - Enable "Developer mode" in the top right.
   - Click "Load unpacked" and select the extension directory.

## Usage

1. Open a webpage in Chrome.
2. Click on the extension icon in the toolbar.
3. Click the "Summarize" button on the popup to initiate summarization and commenting.

## Project Structure

- **background.js:** Handles background tasks and communicates with the content script.
- **content.js:** Injected into web pages and handles user interactions.
- **popup.html:** Provides the UI for the extension popup.
- **popup.js:** Manages interactions in the extension popup.

## Dependencies

- [Flask Server](https://github.com/your-username/your-flask-server): The extension communicates with this server for summarization.

## Known Issues

- CORS issues: Ensure the server allows requests from the extension's origin.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/my-feature`.
3. Make your changes and commit them: `git commit -m 'Add my feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
