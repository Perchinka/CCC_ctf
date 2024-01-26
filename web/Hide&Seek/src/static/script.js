function createGlitch() {
    const glitch = document.getElementById('glitch');
    for(let i = 0; i < 6; i++) {
        let glitchDiv = document.createElement('div');
        glitchDiv.className = 'glitch-img';
        glitch.appendChild(glitchDiv);
    }
    setTimeout(() => {
        glitch.innerHTML = '';
    }, 500);
}

setInterval(createGlitch, 2000);

// Yeah this code does nothin, but here 3rd part of flag: 6a7d7d}