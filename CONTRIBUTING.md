# Contributing to Cus_tkinter_Type_Master

<br>

Thank you for your interest in contributing to the Custom Tkinter Type Master project! This document provides guidelines and information for contributors.

<br>

## 🚀 Getting Started

<br>

### Prerequisites
- Python 3.7 or higher
- Basic knowledge of Python and tkinter
- Git installed on your system

<br>

### Setting Up Development Environment

<br>

1. **Fork the repository**
   ```bash
   # Click the "Fork" button on GitHub, then clone your fork
   git clone https://github.com/qasim032/Cus_tkinter_Type_Master.git
   cd Cus_tkinter_Type_Master
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

<br>

## 🎯 How to Contribute

<br>

### Types of Contributions Welcome

- **🐛 Bug fixes** - Help us squash those pesky bugs
- **✨ New features** - Add typing games, themes, or functionality
- **📚 Documentation** - Improve README, comments, or guides
- **🎨 UI/UX improvements** - Make the interface more user-friendly
- **🧪 Testing** - Add or improve test coverage
- **🌐 Translations** - Help make the app accessible in different languages

### Before You Start

1. **Check existing issues** - Look through [GitHub Issues](https://github.com/qasim032/Cus_tkinter_Type_Master/issues) to see if your idea/bug is already reported
2. **Create an issue** - If not, create a new issue describing your proposed changes
3. **Get feedback** - Wait for maintainer feedback before starting major work

## 📝 Development Guidelines

### Code Style

- **Follow PEP 8** - Use consistent Python coding standards
- **Use meaningful variable names** - `typing_speed` not `ts`
- **Add comments** - Explain complex logic and algorithms
- **Keep functions small** - Aim for single responsibility

### Example Code Structure
```python
def calculate_typing_speed(characters_typed: int, time_elapsed: float) -> float:
    """
    Calculate typing speed in words per minute (WPM).
    
    Args:
        characters_typed (int): Total characters typed
        time_elapsed (float): Time taken in seconds
        
    Returns:
        float: Typing speed in WPM
    """
    if time_elapsed <= 0:
        return 0.0
    
    # Standard: 5 characters = 1 word
    words = characters_typed / 5
    minutes = time_elapsed / 60
    
    return round(words / minutes, 2)
```

## 🔄 Pull Request Process

### 1. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

### 2. Make Your Changes
- Write clean, documented code
- Test your changes thoroughly
- Update documentation if needed

### 3. Commit Your Changes
```bash
git add .
git commit -m "Add: Brief description of your changes"
```

**Commit Message Format:**
- `Add:` for new features
- `Fix:` for bug fixes
- `Update:` for improvements
- `Docs:` for documentation changes

### 4. Push and Create Pull Request
```bash
git push origin your-branch-name
```

Then create a Pull Request on GitHub with:
- **Clear title** describing the change
- **Detailed description** of what was changed and why
- **Screenshots** if UI changes are involved
- **Link to related issues** using `Fixes #123` or `Closes #123`

## 🧪 Testing

### Running Tests
```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_typing_logic.py

# Run with coverage
python -m pytest --cov=src
```

### Writing Tests
- Add tests for new features
- Test edge cases and error conditions
- Use descriptive test names

Example:
```python
def test_typing_speed_calculation_with_zero_time():
    """Test that typing speed returns 0 when time elapsed is 0."""
    result = calculate_typing_speed(100, 0)
    assert result == 0.0
```

## 🎨 UI/UX Guidelines

### Design Principles
- **Simplicity** - Keep the interface clean and intuitive
- **Accessibility** - Ensure good contrast and readable fonts
- **Responsiveness** - Test on different screen sizes
- **Consistency** - Use consistent colors, fonts, and spacing

### Adding New Themes
1. Create theme file in `src/data/themes/`
2. Follow existing theme structure
3. Test with different text types
4. Update theme selection menu

## 📋 Issue Reporting

When reporting bugs, please include:

- **Python version** - `python --version`
- **Operating system** - Windows/macOS/Linux
- **Steps to reproduce** - Clear, numbered steps
- **Expected behavior** - What should happen
- **Actual behavior** - What actually happens
- **Screenshots** - If applicable
- **Error messages** - Full error traceback

## 🤝 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). Please read it before participating.

## 💬 Getting Help

- **GitHub Issues** - For bug reports and feature requests: https://github.com/qasim032/Cus_tkinter_Type_Master/issues
- **Discussions** - For questions and general discussion: https://github.com/qasim032/Cus_tkinter_Type_Master/discussions
- **Email** - [qasim032@example.com] for sensitive issues

## 🏆 Recognition

Contributors will be:
- Listed in the [CONTRIBUTORS.md](CONTRIBUTORS.md) file
- Mentioned in release notes for significant contributions
- Given credit in the application's About section

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project (see [LICENSE](LICENSE) file).

---

**Thank you for helping make Cus_tkinter_Type_Master better! 🎉**

Every contribution, no matter how small, makes a difference. Happy coding! 👨‍💻👩‍💻
