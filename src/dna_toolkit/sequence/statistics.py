def get_seq_length(sequence):
    """sequence length getter"""
    return len(sequence)


def get_gc_content(sequence):
    """GC content getter"""
    total_gc = sequence.count("G") + sequence.count("C")
    return (total_gc / len(sequence)) if len(sequence) > 0 else 0


def get_at_content(sequence):
    """AT content getter"""
    total_at = sequence.count("A") + sequence.count("T")
    return (total_at / len(sequence)) if len(sequence) > 0 else 0


def get_nucleotide_counts(sequence):
    """Nucleotide counts getter"""
    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "C": sequence.count("C"),
        "G": sequence.count("G"),
    }


def get_nucleotide_frequencies(sequence):
    """Nucleotide frequencies getter"""
    length = len(sequence)
    if length == 0:
        return {"A": 0, "T": 0, "C": 0, "G": 0}
    counts = get_nucleotide_counts(sequence)
    return {nucleotide: count / length for nucleotide, count in counts.items()}


def get_dinucleotide_frequencies(sequence):
    """Dinucleotide frequencies getter"""
    length = len(sequence)
    if length < 2:
        return {}

    dinucleotide_counts = {}
    for i in range(length - 1):
        dinucleotide = sequence[i : i + 2]
        if dinucleotide in dinucleotide_counts:
            dinucleotide_counts[dinucleotide] += 1
        else:
            dinucleotide_counts[dinucleotide] = 1

    total_dinucleotides = length - 1
    return {
        dinucleotide: count / total_dinucleotides
        for dinucleotide, count in dinucleotide_counts.items()
    }
