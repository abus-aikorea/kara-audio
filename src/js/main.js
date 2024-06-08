let main_parent = document.getElementById("chat-tab").parentNode;
let extensions = document.getElementById("extensions");

main_parent.childNodes[0].classList.add("header_bar");
main_parent.style = "padding: 0; margin: 0";
main_parent.parentNode.style = "gap: 0";
main_parent.parentNode.parentNode.style = "padding: 0";

document.querySelector(".header_bar").addEventListener("click", function(event) {
  if (event.target.tagName === "BUTTON") {
    const buttonText = event.target.textContent.trim();

    let chat_visible = (buttonText == "Chat");
    let default_visible = (buttonText == "Default");
    let notebook_visible = (buttonText == "Notebook");

    // Check if one of the generation tabs is visible
    if (chat_visible || notebook_visible || default_visible) {
      extensions && (extensions.style.display = "flex");

      if (chat_visible) {
        this.style.marginBottom = "0px";
        extensions && (extensions.style.maxWidth = "880px");
        extensions && (extensions.style.padding = "0px");
      } else {
        this.style.marginBottom = "19px";
        extensions && (extensions.style.maxWidth = "none");
        extensions && (extensions.style.padding = "15px");
      }
    } else {
      this.style.marginBottom = "19px";
      extensions && (extensions.style.display = "none");
    }
  }
});

//------------------------------------------------
// Keyboard shortcuts
//------------------------------------------------
let previousTabId = "chat-tab-button";
document.addEventListener("keydown", function(event) {

  // Stop generation on Esc pressed
  if (event.key === "Escape") {
    // Find the element with id 'stop' and click it
    var stopButton = document.getElementById("stop");
    if (stopButton) {
      stopButton.click();
    }
  }

  // Show chat controls on Ctrl + S
  else if (event.ctrlKey && event.key == "s") {
    event.preventDefault();

    var showControlsElement = document.getElementById("show-controls");
    if (showControlsElement && showControlsElement.childNodes.length >= 4) {
      showControlsElement.childNodes[3].click();

      var arr = document.getElementById("chat-input").childNodes[2].childNodes;
      arr[arr.length - 1].focus();
    }
  }

  // Regenerate on Ctrl + Enter
  else if (event.ctrlKey && event.key === "Enter") {
    event.preventDefault();
    document.getElementById("Regenerate").click();
  }

  // Continue on Alt + Enter
  else if (event.altKey && event.key === "Enter") {
    event.preventDefault();
    document.getElementById("Continue").click();
  }

  // Remove last on Ctrl + Shift + Backspace
  else if (event.ctrlKey && event.shiftKey && event.key === "Backspace") {
    event.preventDefault();
    document.getElementById("Remove-last").click();
  }

  // Copy last on Ctrl + Shift + K
  else if (event.ctrlKey && event.shiftKey && event.key === "K") {
    event.preventDefault();
    document.getElementById("Copy-last").click();
  }

  // Replace last on Ctrl + Shift + L
  else if (event.ctrlKey && event.shiftKey && event.key === "L") {
    event.preventDefault();
    document.getElementById("Replace-last").click();
  }

  // Impersonate on Ctrl + Shift + M
  else if (event.ctrlKey && event.shiftKey && event.key === "M") {
    event.preventDefault();
    document.getElementById("Impersonate").click();
  }

  // Switch between tabs on Tab
  else if (!event.ctrlKey && !event.shiftKey && !event.altKey && !event.metaKey && event.key === "Tab") {
    event.preventDefault();
    var parametersButton = document.getElementById("parameters-button");
    var parentContainer = parametersButton.parentNode;
    var selectedChild = parentContainer.querySelector(".selected");

    if (selectedChild.id == "parameters-button") {
      document.getElementById(previousTabId).click();
    } else {
      previousTabId = selectedChild.id;
      parametersButton.click();
    }
  }
});

//------------------------------------------------
// Position the chat typing dots
//------------------------------------------------
typing = document.getElementById("typing-container");
typingParent = typing.parentNode;
typingSibling = typing.previousElementSibling;
typingSibling.insertBefore(typing, typingSibling.childNodes[2]);

//------------------------------------------------
// Chat scrolling
//------------------------------------------------
const targetElement = document.getElementById("chat").parentNode.parentNode.parentNode;
targetElement.classList.add("pretty_scrollbar");
targetElement.classList.add("chat-parent");
let isScrolled = false;

targetElement.addEventListener("scroll", function() {
  let diff = targetElement.scrollHeight - targetElement.clientHeight;
  if(Math.abs(targetElement.scrollTop - diff) <= 10 || diff == 0) {
    isScrolled = false;
  } else {
    isScrolled = true;
  }
});

// Create a MutationObserver instance
const observer = new MutationObserver(function(mutations) {
  mutations.forEach(function(mutation) {
    updateCssProperties();

    if(!isScrolled) {
      targetElement.scrollTop = targetElement.scrollHeight;
    }

    const firstChild = targetElement.children[0];
    if (firstChild.classList.contains("generating")) {
      typing.parentNode.classList.add("visible-dots");
      document.getElementById("stop").style.display = "flex";
      document.getElementById("Generate").style.display = "none";
    } else {
      typing.parentNode.classList.remove("visible-dots");
      document.getElementById("stop").style.display = "none";
      document.getElementById("Generate").style.display = "flex";
    }

  });
});

// Configure the observer to watch for changes in the subtree and attributes
const config = {
  childList: true,
  subtree: true,
  characterData: true,
  attributeOldValue: true,
  characterDataOldValue: true
};

// Start observing the target element
observer.observe(targetElement, config);

//------------------------------------------------
// Add some scrollbars
//------------------------------------------------
const textareaElements = document.querySelectorAll(".add_scrollbar textarea");
for(i = 0; i < textareaElements.length; i++) {
  textareaElements[i].classList.remove("scroll-hide");
  textareaElements[i].classList.add("pretty_scrollbar");
  textareaElements[i].style.resize = "none";
}

//------------------------------------------------
// Remove some backgrounds
//------------------------------------------------
const noBackgroundelements = document.querySelectorAll(".no-background");
for(i = 0; i < noBackgroundelements.length; i++) {
  noBackgroundelements[i].parentNode.style.border = "none";
  noBackgroundelements[i].parentNode.parentNode.parentNode.style.alignItems = "center";
}

const slimDropdownElements = document.querySelectorAll(".slim-dropdown");
for (i = 0; i < slimDropdownElements.length; i++) {
  const parentNode = slimDropdownElements[i].parentNode;
  parentNode.style.background = "transparent";
  parentNode.style.border = "0";
}

//------------------------------------------------
// Create the hover menu in the chat tab
// The show/hide events were adapted from:
// https://github.com/SillyTavern/SillyTavern/blob/6c8bd06308c69d51e2eb174541792a870a83d2d6/public/script.js
//------------------------------------------------
var buttonsInChat = document.querySelectorAll("#chat-tab:not(.old-ui) #chat-buttons button");
var button = document.getElementById("hover-element-button");
var menu = document.getElementById("hover-menu");
var istouchscreen = (navigator.maxTouchPoints > 0) || "ontouchstart" in document.documentElement;

function showMenu() {
  menu.style.display = "flex"; // Show the menu
}

function hideMenu() {
  menu.style.display = "none"; // Hide the menu
  if (!istouchscreen) {
    document.querySelector("#chat-input textarea").focus(); // Focus on the chat input
  }
}

if (buttonsInChat.length > 0) {
  for (let i = buttonsInChat.length - 1; i >= 0; i--) {
    const thisButton = buttonsInChat[i];
    menu.appendChild(thisButton);

    thisButton.addEventListener("click", () => {
      hideMenu();
    });

    const buttonText = thisButton.textContent;
    const matches = buttonText.match(/(\(.*?\))/);

    if (matches && matches.length > 1) {
      // Apply the transparent-substring class to the matched substring
      const substring = matches[1];
      const newText = buttonText.replace(substring, `&nbsp;<span class="transparent-substring">${substring.slice(1, -1)}</span>`);
      thisButton.innerHTML = newText;
    }
  }
} else {
  buttonsInChat = document.querySelectorAll("#chat-tab.old-ui #chat-buttons button");
  for (let i = 0; i < buttonsInChat.length; i++) {
    buttonsInChat[i].textContent = buttonsInChat[i].textContent.replace(/ \(.*?\)/, "");
  }
  document.getElementById("gr-hover-container").style.display = "none";
}

function isMouseOverButtonOrMenu() {
  return menu.matches(":hover") || button.matches(":hover");
}

button.addEventListener("mouseenter", function () {
  if (!istouchscreen) {
    showMenu();
  }
});

button.addEventListener("click", function () {
  if (menu.style.display === "flex") {
    hideMenu();
  }
  else {
    showMenu();
  }
});

// Add event listener for mouseleave on the button
button.addEventListener("mouseleave", function () {
  // Delay to prevent menu hiding when the mouse leaves the button into the menu
  setTimeout(function () {
    if (!isMouseOverButtonOrMenu()) {
      hideMenu();
    }
  }, 100);
});

// Add event listener for mouseleave on the menu
menu.addEventListener("mouseleave", function () {
  // Delay to prevent menu hide when the mouse leaves the menu into the button
  setTimeout(function () {
    if (!isMouseOverButtonOrMenu()) {
      hideMenu();
    }
  }, 100);
});

// Add event listener for click anywhere in the document
document.addEventListener("click", function (event) {
  // Check if the click is outside the button/menu and the menu is visible
  if (!isMouseOverButtonOrMenu() && menu.style.display === "flex") {
    hideMenu();
  }

  if (event.target.classList.contains("pfp_character")) {
    toggleBigPicture();
  }
});

//------------------------------------------------
// Relocate the "Show controls" checkbox
//------------------------------------------------
var elementToMove = document.getElementById("show-controls");
var parent = elementToMove.parentNode;
for (var i = 0; i < 2; i++) {
  parent = parent.parentNode;
}

parent.insertBefore(elementToMove, parent.firstChild);

//------------------------------------------------
// Make the chat input grow upwards instead of downwards
//------------------------------------------------
document.getElementById("show-controls").parentNode.style.position = "absolute";
document.getElementById("show-controls").parentNode.style.bottom = "0px";

//------------------------------------------------
// Focus on the chat input
//------------------------------------------------
const chatTextArea = document.getElementById("chat-input").querySelector("textarea");

function respondToChatInputVisibility(element, callback) {
  var options = {
    root: document.documentElement,
  };

  var observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      callback(entry.intersectionRatio > 0);
    });
  }, options);

  observer.observe(element);
}

function handleChatInputVisibilityChange(isVisible) {
  if (isVisible) {
    chatTextArea.focus();
  }
}

respondToChatInputVisibility(chatTextArea, handleChatInputVisibilityChange);

//------------------------------------------------
// Show enlarged character picture when the profile
// picture is clicked on
//------------------------------------------------
let bigPictureVisible = false;

function addBigPicture() {
  var imgElement = document.createElement("img");
  var timestamp = new Date().getTime();
  imgElement.src = "/file/cache/pfp_character.png?time=" + timestamp;
  imgElement.classList.add("bigProfilePicture");
  imgElement.addEventListener("load", function () {
    this.style.visibility = "visible";
  });
  imgElement.addEventListener("error", function () {
    this.style.visibility = "hidden";
  });

  var imgElementParent = document.getElementById("chat").parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode;
  imgElementParent.appendChild(imgElement);
}

function deleteBigPicture() {
  var bigProfilePictures = document.querySelectorAll(".bigProfilePicture");
  bigProfilePictures.forEach(function (element) {
    element.parentNode.removeChild(element);
  });
}

function toggleBigPicture() {
  if(bigPictureVisible) {
    deleteBigPicture();
    bigPictureVisible = false;
  } else {
    addBigPicture();
    bigPictureVisible = true;
  }
}

//------------------------------------------------
// Handle the chat input box growth
//------------------------------------------------
let currentChatInputHeight = 0;

// Update chat layout based on chat and input dimensions
function updateCssProperties() {
  const chatContainer = document.getElementById("chat").parentNode.parentNode.parentNode;
  const chatInputHeight = document.querySelector("#chat-input textarea").clientHeight;

  // Check if the chat container is visible
  if (chatContainer.clientHeight > 0) {

    // Calculate new chat height and adjust CSS properties
    var numericHeight = chatContainer.parentNode.clientHeight - chatInputHeight + 40 - 100;
    if (document.getElementById("chat-tab").style.paddingBottom != "") {
      numericHeight += 20;
    }
    const newChatHeight = `${numericHeight}px`;

    document.documentElement.style.setProperty("--chat-height", newChatHeight);
    document.documentElement.style.setProperty("--input-delta", `${chatInputHeight - 40}px`);

    // Get and set header height
    const header = document.querySelector(".header_bar");
    const headerHeight = `${header.clientHeight}px`;
    document.documentElement.style.setProperty("--header-height", headerHeight);

    // Adjust scrollTop based on input height change
    if (chatInputHeight !== currentChatInputHeight) {
      chatContainer.scrollTop += chatInputHeight > currentChatInputHeight ? chatInputHeight : -chatInputHeight + 40;
      currentChatInputHeight = chatInputHeight;
    }
  }
}

// Observe textarea size changes and call update function
new ResizeObserver(updateCssProperties)
  .observe(document.querySelector("#chat-input textarea"));

// Handle changes in window size
window.addEventListener("resize", updateCssProperties);

//------------------------------------------------
// Keep track of the display width to position the past
// chats dropdown on desktop
//------------------------------------------------
function updateDocumentWidth() {
  var updatedWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
  document.documentElement.style.setProperty("--document-width", updatedWidth + "px");
}

updateDocumentWidth();
window.addEventListener("resize", updateDocumentWidth);

//------------------------------------------------
// Focus on the rename text area when it becomes visible
//------------------------------------------------
const renameTextArea = document.getElementById("rename-row").querySelector("textarea");

function respondToRenameVisibility(element, callback) {
  var options = {
    root: document.documentElement,
  };

  var observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      callback(entry.intersectionRatio > 0);
    });
  }, options);

  observer.observe(element);
}


function handleVisibilityChange(isVisible) {
  if (isVisible) {
    renameTextArea.focus();
  }
}

respondToRenameVisibility(renameTextArea, handleVisibilityChange);

