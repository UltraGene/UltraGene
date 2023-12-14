
# Website Documentation

## Overview
This website is powered by [Docusaurus](https://docusaurus.io/), a modern static website generator, offering a streamlined process for creating and deploying websites.

## Getting Started

### Prerequisites

To set up Docusaurus, ensure you have Node.js and Yarn installed. If you're using macOS, these can be installed via Homebrew, a package manager for macOS.

#### Steps to Install Prerequisites

1. **Install Homebrew**  
   If Homebrew is not already installed, run the following command in your terminal:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. **Install Node.js**  
   To install Node.js, use the command:
   ```bash
   brew install node
   ```
3. **Install Yarn**  
   Finally, install Yarn using:
   ```bash
   brew install yarn
   ```

### Installation

After the prerequisites are installed, set up your Docusaurus project:

```bash
yarn
```

This command installs all necessary dependencies for your Docusaurus project.

### Local Development

```bash
yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```bash
yarn build
```

This command generates static content into the `build` directory and can be served using any static content hosting service.

### Deployment

Deploy your Docusaurus site using the following commands:

#### Using SSH:

```bash
USE_SSH=true yarn deploy
```

#### Not using SSH:

```bash
GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.
