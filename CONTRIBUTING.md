# Contributing to SQL for Business Analytics

Contributions are welcome! Here's how you can help.

## How to Contribute

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/your-feature`)
3. **Commit** your changes (`git commit -m "Add your feature"`)
4. **Push** to the branch (`git push origin feature/your-feature`)
5. **Open** a Pull Request

## Development Setup

```bash
git clone https://github.com/methila-2056/methila-2056-SQL-for-Business-Analytics.git
cd methila-2056-SQL-for-Business-Analytics
pip install -r requirements.txt
```

## Running Tests

```bash
python tests/test_sql_analysis.py
```

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to new functions
- Keep SQL queries readable with proper formatting

## Reporting Issues

- Use GitHub Issues to report bugs
- Include steps to reproduce the issue
- Mention your Python version and OS

## Adding New Queries

1. Add the SQL file to the `sql/` directory
2. Follow the naming convention: `XX_description.sql`
3. Add the corresponding Python method in `sql_analysis.py`
4. Update the README if it's a new category
