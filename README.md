# VITLink: WiFi Communication

## Overview
**VITLink** is a powerful and intuitive Flask-based web application designed to facilitate real-time communication through notifications. Leveraging the capabilities of WebSocket technology, VITLink enables instant messaging between clients, making it an ideal solution for applications requiring immediate data exchange.

## Features
- **Real-time Messaging**: Utilize Flask-SocketIO for seamless, real-time communication.
- **SQLite Database**: Efficiently log messages and maintain a history of interactions.
- **User-Friendly Interface**: A simple and intuitive web interface that enhances user experience.
- **Cross-Platform Compatibility**: Works on various operating systems, ensuring accessibility for all users.

## Table of Contents
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up a Virtual Environment](#set-up-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

### Prerequisites
Before you begin, ensure you have the following installed:
- **Python 3.x**: The programming language used for this application.
- **pip**: The Python package installer, which is typically included with Python installations.

### Clone the Repository
To get a local copy of the project, run the following commands in your terminal:
```bash
git clone https://github.com/majilacodes/VITLink-wificomm.git
cd VITLink-wificomm
```

### Set Up a Virtual Environment
It is recommended to create a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
Once your virtual environment is activated, install the required packages:
```bash
pip install -r requirements.txt
```

## Usage
To get started with VITLink, follow these steps:

1. **Initialize the Database**:
   This step sets up the SQLite database for logging messages.
   ```bash
   python server.py
   ```

2. **Run the Application**:
   Start the Flask application to begin using VITLink.
   ```bash
   python server.py
   ```

3. **Access the Application**:
   Open your web browser and navigate to `http://192.168.102.81:5002` to access the VITLink interface.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.
---

Thank you for checking out VITLink! We hope you find it useful and enjoyable to work with. If you have any questions or feedback, feel free to reach out!
