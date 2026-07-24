# Coding Guidelines

These guidelines are meant to keep the project readable, consistent, and easy to extend as the algorithms grow.

## Python Style Conventions

- Use Black for formatting.
- Keep lines at 88 characters when practical.
- Prefer explicit imports and straightforward control flow.
- Write small functions that are easy to test.
- Avoid premature abstraction.

## Naming Conventions

- Use `snake_case` for functions, modules, and variables.
- Use `PascalCase` for classes.
- Use `UPPER_CASE` for constants.
- Give files names that reflect their responsibility.
- Prefer names that describe biological meaning clearly, such as `gc_content` or `reverse_complement`.

## Documentation Style

- Add docstrings to public modules, classes, and functions.
- Explain the purpose of a function before explaining implementation details.
- Prefer plain language over jargon when possible.
- Use examples when a behavior might be unclear to a beginner.
- Keep documentation aligned with the code so it does not drift.

## Testing Philosophy

- Write tests alongside new features.
- Test one behavior at a time.
- Prefer small, deterministic inputs.
- Keep tests readable so they also serve as examples.
- Add regression tests whenever a bug is fixed.

The project should favor confidence and clarity over large, complicated test setups.

## Git Commit Conventions

Use a lightweight Conventional Commits style.

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for test updates
- `refactor:` for code changes that do not alter behavior
- `chore:` for maintenance tasks and tooling updates

Example commit messages:

- `feat: add FASTA parser skeleton`
- `docs: expand roadmap`
- `test: add package import check`

Keeping commits focused will make it easier to learn from the history of the project.