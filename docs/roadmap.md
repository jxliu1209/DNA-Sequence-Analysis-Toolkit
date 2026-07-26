# Roadmap

This roadmap is organized so the project starts with the simplest DNA fundamentals and gradually moves toward more advanced algorithms and sequencing workflows.

## Development Phases

### Phase 1: Foundations

Build the basic package structure, core documentation, packaging metadata, and test layout.

Milestones:

- [x] Package skeleton is in place
- [x] Documentation pages describe the project clearly
- [x] Test folders mirror the package layout
- [x] Tooling configuration is ready for development

### Phase 2: DNA Fundamentals

Implement the simplest sequence operations first so the project can validate inputs and report useful sequence statistics.

Milestones:

- [ ] FASTA parsing
- [ ] DNA validation
- [x] GC content
- [x] Nucleotide frequencies
- [ ] Reverse complement
- [ ] Transcription
- [ ] Translation
- [ ] Codon usage
- [ ] Restriction enzyme search

### Phase 3: Sequence Analysis

Add features that work on a single sequence or a small set of sequences.

Milestones:

- [ ] ORF finding
- [ ] Motif search
- [ ] k-mer counting
- [ ] Consensus sequence
- [ ] SNP comparison
- [ ] Mutation simulation

### Phase 4: Classical Algorithms

Introduce textbook algorithms that are useful for learning dynamic programming and sequence comparison.

Milestones:

- [ ] Hamming distance
- [ ] Levenshtein distance
- [ ] Needleman-Wunsch
- [ ] Smith-Waterman
- [ ] Scoring matrices

### Phase 5: Sequencing Data and Extensions

Expand the project toward realistic workflow support and optional presentation features.

Milestones:

- [ ] FASTQ parsing
- [ ] Quality score analysis
- [ ] Simple variant calling
- [ ] Multiple sequence alignment
- [ ] Phylogenetic tree generation
- [ ] Biopython interoperability
- [ ] Visualization
- [ ] Genome annotation
- [ ] Primer design
- [ ] Command-line interface
- [ ] Web interface

## Suggested Implementation Order

1. Set up the package and tests.
2. Implement sequence validation and simple statistics.
3. Add parsing for common input formats.
4. Add derived sequence operations such as reverse complement and transcription.
5. Implement search and counting features.
6. Move to alignment and distance algorithms.
7. Add FASTQ and quality-related functionality.
8. Build CLI and optional presentation layers last.

This order keeps each new step grounded in the previous one and reduces the chance of building on unstable foundations.