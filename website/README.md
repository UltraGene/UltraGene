# Website

This website is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.

### Prerequisites

Before installing Docusaurus, you need to install Node.js and Yarn. You can do this easily using Homebrew, a package manager for macOS:

1. **Install Homebrew** (if not already installed):
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
2. **Install Node.js**:
   brew install node
3. **Install Yarn**:
   brew install yarn

### Installation

After installing the prerequisites, you can set up your Docusaurus project:

$ yarn

This command installs all the necessary dependencies for your Docusaurus project.

### Local Development

$ yarn start

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

$ yarn build

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

To deploy your Docusaurus site, you can use the following commands:

Using SSH:

$ USE_SSH=true yarn deploy

Not using SSH:

$ GIT_USER=<Your GitHub username> yarn deploy

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.
