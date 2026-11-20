# HTTP Request Tester

A Python-based command-line tool for sending and analyzing HTTP requests using the `Requests` library.

## Overview

HTTP Request Tester allows users to interact with web servers by sending different types of HTTP requests and inspecting server responses.

The project was created to practice Python programming, HTTP fundamentals, request handling, and working with external libraries.

## Features

- Supports multiple HTTP methods:
  - GET
  - POST
  - PUT
  - PATCH
  - DELETE
- Accepts user-provided URLs.
- Supports sending data using `data` and `json` payload formats.
- Allows users to create custom key-value payloads.
- Displays response information:
  - HTTP status code
  - Response headers
  - Response body
  - Response URL
  - Request execution time
- Handles request-related exceptions.
- Includes timeout configuration.
- Validates user input.

## Technologies Used

- Python 3
- Requests
- HTTP Protocol
- Command-line interface (CLI)

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd HTTP-Request-Tester
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python main.py
```

Follow the instructions displayed in the terminal to select an HTTP method, enter a URL, and provide request data when required.

## Project Structure



## Learning Objectives

This project helped me practice:

- Working with HTTP methods and request payloads.
- Using Python's `Requests` library.
- Handling exceptions and invalid user input.
- Creating reusable functions.
- Splitting Python code into multiple modules.
- Processing and analyzing HTTP responses.

## Disclaimer

This tool is intended for educational purposes and authorized testing only.

## Author

Created as part of my Python and cybersecurity learning journey.
