# Calculator Application

## Link to Video:

https://drive.google.com/file/d/1sSdCkbh6o7AMIcdAxVIu2TTY9f_3upbo/view?usp=sharing

## Link to Calculator Paper:

https://drive.google.com/file/d/1ORAfSXhefVy2xyqg87A8EyRbdIqvV3_n/view?usp=sharing

## Overview

This calculator application is designed to perform basic arithmetic operations, including addition, subtraction, multiplication, division, and exponentiation. It supports command-line interface (CLI) commands and dynamically loaded plugins. The application also includes comprehensive logging to track operations, data manipulations, and errors.

## Features

- Basic arithmetic operations: add, subtract, multiply, divide, exponent.
- Command-line interface for user interaction.
- Plugin architecture to add new commands.
- History management: view, clear, delete, save, and load calculation history.
- Comprehensive logging with different severity levels (INFO, WARNING, ERROR).
- Dynamic logging configuration through environment variables.
- Extensive unit testing with pytest.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/calculator-app.git
   cd calculator-app
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the project root with the following content:

   ```env
   LOG_LEVEL=INFO
   ```

## Usage

### Running the Application

To start the application, run:

```bash
python main.py
```

You can also perform calculations directly from the command line:

```bash
python main.py <number1> <number2> <operation>
```

Example:

```bash
python main.py 3 4 add
```

### Available Commands

- `add`: Add two numbers.
- `subtract`: Subtract two numbers.
- `multiply`: Multiply two numbers.
- `divide`: Divide two numbers.
- `exponent`: Exponentiation of two numbers.
- `view_history`: View the calculation history.
- `clear_history`: Clear the calculation history.
- `delete_history`: Delete the history file.
- `save_history`: Save the history to a file.
- `load_history`: Load the history from a file.

### Examples

```bash
>>> add 3 4
The result of 3 add 4 is equal to 7
```

```bash
>>> view_history
Operation  Operand_A  Operand_B  Result
0       add        3.0        4.0     7.0
```

## Logging

The application uses Python's built-in `logging` module to log detailed information about operations, errors, and informational messages. The logging level and output destination can be configured via environment variables.

### Configuration

- **LOG_LEVEL**: Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR). Default is INFO.

## Testing

The application includes a comprehensive suite of unit tests using pytest. Tests cover all aspects of the application, including arithmetic operations, command handling, plugin management, and history management.

### Running Tests

To run the tests, use:

```bash
pytest
```

### Test Coverage

The project uses pytest-cov to measure test coverage. To generate a coverage report, run:

```bash
pytest --cov=calculator --cov-report=html
```

This will create an HTML coverage report in the `htmlcov` directory.

## Project Structure

```
calculator-app/
├── calculator/
│   ├── __init__.py
│   ├── calculations.py
│   ├── calculation.py
│   ├── operations.py
│   ├── operation_functions.py
├── plugins/
│   ├── __init__.py
│   ├── plugin_interface.py
│   └── ...
├── tests/
│   ├── __init__.py
│   ├── test_calculation.py
│   ├── test_calculator.py
│   ├── test_conftest.py
│   ├── test_dynamic_plugins.py
│   ├── test_history.py
│   ├── test_main.py
│   └── test_utils.py
├── .env
├── .gitignore
├── main.py
├── plugin_manager.py
├── command_handler.py
├── requirements.txt
├── README.md
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

You can copy and paste the above content into your `README.md` file. Feel free to customize it as needed!
