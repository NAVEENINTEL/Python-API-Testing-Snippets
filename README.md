# Python API Testing Snippets

A collection of Python code snippets demonstrating various API authentication methods and testing scenarios using pytest.

## Overview

This repository contains code snippets and examples showcasing how to perform API testing using Python. The snippets cover different authentication methods commonly used in API testing and demonstrate how to write test cases using `pytest`.

## Table of Contents

- [Authentication Methods](#authentication-methods)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Authentication Methods

### Basic Authentication
Demonstrates how to perform API requests using basic authentication.

### Token-based Authentication (Bearer Token)
Example code for making API requests using a Bearer token.

### OAuth 2.0 Authentication
Illustrates OAuth 2.0 authentication flow and making authenticated requests.

## Project Structure

- **`tests/`:** Contains test scripts for different authentication methods.
- **`utils/`:** Utility functions for making API requests.
- **`config/`:** Configuration files for storing endpoint URLs and credentials.
- **`requirements.txt`:** Lists project dependencies.

## Usage

To run the tests:
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Navigate to each test script in the `tests/` directory and run them using `pytest`.

Modify the configurations in the `config/config.py` file to include your specific endpoint URLs and authentication credentials.

## Dependencies

- [pytest](https://pytest.org): Testing framework for Python.
- [requests](https://docs.python-requests.org): HTTP library for making requests.
- [requests-oauthlib](https://requests-oauthlib.readthedocs.io): Library for OAuth 2.0 authentication.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
