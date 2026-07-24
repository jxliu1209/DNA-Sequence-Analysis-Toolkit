# Architecture

This project uses a small, explicit package structure designed for learning. The goal is to keep the code easy to navigate while leaving room for future algorithms and data formats.

## Overall Package Architecture

The installable package lives under `src/dna_toolkit/`. That package is split into focused subpackages:

- `sequence/` for sequence-centric logic
- `io/` for reading and writing supported file formats
- `analysis/` for higher-level analysis routines
- `utils/` for shared helpers that do not belong to a single domain
- `cli/` for command-line entry points when the project grows

This layout keeps the domain code separate from documentation, tests, and example material.

## Folder Responsibilities

- `docs/` stores project planning, design notes, and coding guidance.
- `src/` contains the installable package and all production code.
- `tests/` mirrors the package structure and holds automated checks.
- `examples/` is reserved for short usage examples that show how the package should feel to use.
- `data/sample/` contains tiny sample inputs that are safe to commit.
- `scripts/` is for maintenance helpers and one-off project scripts.
- `notebooks/` is for exploratory analysis and teaching notes.
- `.github/workflows/` holds automation such as continuous integration.

## Module Interactions

The intended flow is simple:

1. `io` reads raw sequence or annotation data.
2. `sequence` validates and normalizes sequence representations.
3. `analysis` performs calculations using the cleaned sequence data.
4. `utils` provides shared helpers used by multiple modules.
5. `cli` exposes selected features to the command line.

Keeping these layers separate will help prevent the code from turning into a single large script.

## Design Philosophy

The project favors readability over cleverness.

- Prefer small functions with single responsibilities.
- Make data flow obvious.
- Use descriptive names instead of compact but cryptic abstractions.
- Keep public APIs stable and simple.
- Delay abstraction until there is a real need for it.

This approach is especially useful for a learning project because it makes the codebase easier to study and extend.

## Extensibility Principles

The architecture is meant to grow in layers.

- Add new algorithms without changing unrelated modules.
- Keep file parsing logic separate from analysis logic.
- Introduce reusable helpers only after the same pattern appears more than once.
- Add tests alongside each feature so behavior stays documented.
- Prefer data structures that are easy to inspect and test.

These principles make it easier to add later features such as alignment algorithms, FASTQ handling, or visualization without redesigning the whole repository.