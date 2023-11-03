document.addEventListener("DOMContentLoaded", function () {
    const clickMeButton = document.getElementById("clickMeButton");
    
    clickMeButton.addEventListener("click", function () {
        alert("You're not robot! Get out of here!!!");
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const fallingNumbersContainer = document.querySelector(".falling-numbers-container");
    const numberOfNumbers = 500; // Increase the number of falling characters
    const characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // Characters for the matrix effect

    // Create and append falling characters
    for (let i = 1; i <= numberOfNumbers; i++) {
        const fallingCharacter = document.createElement("div");
        fallingCharacter.classList.add("falling-number");
        fallingCharacter.textContent = characters[Math.floor(Math.random() * characters.length)]; // Random character
        fallingCharacter.style.left = Math.random() * 100 + "vw";
        fallingCharacter.style.animationDuration = Math.random() * 2 + 2 + "s"; // Adjust animation duration
        fallingNumbersContainer.appendChild(fallingCharacter);
    }
});