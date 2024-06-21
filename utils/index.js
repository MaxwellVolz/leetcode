// Import the Turndown library
import TurndownService from 'turndown';

// Create a new instance of the Turndown service
const turndown = new TurndownService();

function checkForTabContainer() {
    // Select the target element
    const contentElement = document.querySelector('.elfjS');

    if (contentElement) {
        console.log("Tab container found");

        // Convert the content to Markdown using Turndown
        const markdown = turndown.turndown(contentElement.innerHTML);

        // Create and configure a new button element
        const button = document.createElement('button');
        button.innerText = 'Copy as Markdown';
        button.addEventListener('click', () => {
            navigator.clipboard.writeText(markdown).then(() => {
                console.log('Markdown copied to clipboard successfully!');
            }).catch(err => {
                console.error('Failed to copy markdown:', err);
            });
        });

        // Append the button to the content element
        contentElement.appendChild(button);
        console.log("Button appended");
    } else {
        console.log("Tab container not found");
        setTimeout(checkForTabContainer, 1000);
    }
}

window.addEventListener('load', () => {
    console.log("Page loaded");
    checkForTabContainer();
});

console.log("Script loaded");