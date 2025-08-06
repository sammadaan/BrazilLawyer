# Contributing to mais petiçoes

Thank you for your interest in contributing to mais petiçoes! 🇧🇷

## How to Contribute

### 🐛 Bug Reports
- Use GitHub Issues to report bugs
- Include steps to reproduce
- Provide error messages and logs

### ✨ Feature Requests
- Open an issue with the "enhancement" label
- Describe the feature and its use case
- Explain how it benefits Brazilian legal professionals

### 🔧 Code Contributions

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature`
3. **Make your changes**
4. **Add tests** for new functionality
5. **Run the test suite**: `pytest tests/`
6. **Commit with clear messages**: `git commit -m "Add case similarity analysis"`
7. **Push to your fork**: `git push origin feature/your-feature`
8. **Open a Pull Request**

### 📝 Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/mais-peticoes.git
cd BrazilLawyer

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Run tests
pytest tests/
