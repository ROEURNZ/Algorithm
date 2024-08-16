# Getting Started with Python

Python is a versatile programming language that's great for beginners. This guide will help you get started with Python, covering everything from setting up your environment to running your first Python script.

## 1. Setting Up Code or Text Editors

### Visual Studio Code (VS Code)
- **Download & Install**: [Download VS Code](https://code.visualstudio.com/)
- **Install Extensions**:
  - **Python Extension**: Provides rich support for Python, including features like IntelliSense (code completion), linting, debugging, and more.
  - **Pylance Extension**: Enhances Python support with better type checking, code navigation, and more powerful IntelliSense.
  - **Code Runner Extension**: Allows you to run code snippets or files quickly with a simple click or keybinding.
  - **AI Tabnine Extension**: Offers AI-powered code completions to boost productivity by predicting what you might want to type next.

### Visual Studio (Full IDE)
- **Download & Install**: [Download Visual Studio](https://visualstudio.microsoft.com/)
- **Install Workloads**: During installation, select the "Python development" workload. This will install all the necessary tools to start coding in Python, including the Python interpreter, templates, and debugging tools.

## 2. Download & Install Python
- **Download**: Go to the [Python official download page](https://www.python.org/downloads/) and download the latest version for your operating system (Windows, macOS, or Linux).
- **Install**: Follow the installation instructions provided on the download page. Be sure to check the option "Add Python to PATH" during installation.

## 3. Install Required Extensions

### VS Code
- **Python Extension**: Ensure that the Python extension is installed. You can find it in the Extensions view (`Ctrl + Shift + X`).
- **Optional Extensions**: For enhanced productivity, you might consider installing extensions like:
  - **Prettier**: A code formatter that ensures consistent styling across your Python code.
  - **GitLens**: Helps you manage your Git repositories with enhanced features.

### Visual Studio
- The necessary extensions and tools should be included in the installation if you selected the "Python development" workload. This includes the Python interpreter, debugging tools, and project templates.

## 4. Running Python Code

To run Python code, you need to ensure you're in the right directory where your Python script is located.

### Running in VS Code Terminal
- Open the terminal in VS Code (`Ctrl + `).
- Navigate to the directory containing your Python file:
  ```bash
  cd path/to/your/script
    ```
# Python Script Guide

## Run the Python Script

```bash
python main.py  # Replace 'main.py' with your filename
```


## Running in Command Prompt or Terminal

1. Open your command prompt or terminal.
2. Navigate to the directory where your Python script is saved.
3. Run the script using:
```bash
python main.py  # Replace 'main.py' with your filename
```
## Understanding Strings and Substrings in Python
### **Strings**
In Python, strings are sequences of characters. You can create a string by enclosing characters within quotes.

```code
my_string = "Hello, World!"
```

## Understanding Strings and Substrings in Python
### **Substrings**
A substring is a portion of a string. You can extract a substring using slicing.

```code
my_string = "Hello, World!"
substring = my_string[0:5]  # Extracts 'Hello'
```

- Concatenation: You can concatenate strings using the + operator.

```code
greeting = "Hello, " + "World!"
```
- Finding Substrings: Use the find() method to locate a substring.

```code
position = my_string.find("World")  # Returns 7

```
- Replacing Substrings: Replace a part of the string with another string using the replace() method.

```code
new_string = my_string.replace("World", "Python")  # Returns 'Hello, Python!'


```
## Advanced Substring Techniques
- Slicing with Steps: You can specify a step value when slicing.

```code
sliced_string = my_string[0:5:2]  # Extracts 'Hlo'
```
- Reversing a String: Reverse a string by slicing with a negative step.

```code
reversed_string = my_string[::-1]  # Returns '!dlroW ,olleH'
```
