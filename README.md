  <h1 align="center">CTF Challenges</h1>

<p align="center">CTF beginner challenges for <b>Chesterton Comunity College</b> 2023.</p>

## Table of Contents

- [Getting Started](#getting-started)
    - [Installation](#installation)
- [Template](#template)
  - [Flag format](#flag-format)
  - [Directory structure](#directory-structure)
  - [Template for Readme.md](#template-for-readmemd)
- [Contributing](#contributing)

## Getting Started

The following categories are available:

- Cryptography
- Web
- PPC
- pwn
- Reverse Engineering



### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Perchinka/CCC_ctf.git
   ```

2. Install docker
    
    Debian:
    ```sh
    sudo apt install docker.io docker-compose
    ```
    Arch:
    ```sh
    sudo pacman -S docker docker-compose
    ```

3. Build and up containers
    ```sh
    docker-compose up --build
    ```

## Template
### Flag format

- All flags are enclosed in `CCC{}`.
- All flags passes the regex `CCC{[a-zA-Z0-9_!@#$%^&*()-=+?]+}`.
- Flags are hard to guess (I believe so) :D

### Directory structure

- Each challenge is in its own directory
- Each challenge directory contains a `README.md` file with the challenge description and solution
- Every challenge that requires a server to be run is in its own docker container, so they have their own Dockerfile in challenge directory
- **src** directory contains all the source code for the challenges
- **files** directory contains all the files that are needed for the challenges

### Template for Readme.md

Every README.md file follows the following template:

```markdown
# Challenge Name
Category: Category Name

## Description
Description of the challenge

## Solution
Solution of the challenge

The flag is: `CCC{flag}`
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Requests.