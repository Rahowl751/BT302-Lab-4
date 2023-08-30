def pairwise_alignment(seq1, seq2, gap_penalty=-2, match_score=1, mismatch_penalty=-1):
    # Initialize the scoring matrix and traceback matrix
    len_seq1, len_seq2 = len(seq1), len(seq2)
    score_matrix = [[0] * (len_seq2 + 1) for _ in range(len_seq1 + 1)]

    for i in range(len_seq1 + 1):
        score_matrix[i][0] = gap_penalty * i
    for j in range(len_seq2 + 1):
        score_matrix[0][j] = gap_penalty * j

    # ... (rest of the pairwise alignment logic)

    # Construct and return the aligned sequences
    aligned_seq1, aligned_seq2 = "", ""
    i, j = len_seq1, len_seq2

    # ... (traceback logic)

    return aligned_seq1, aligned_seq2

def progressive_alignment(sequences, gap_penalty=-2, match_score=1, mismatch_penalty=-1):
    num_sequences = len(sequences)
    
    # Perform pair-wise alignment of all sequences
    alignments = [sequences[0]]
    for i in range(1, num_sequences):
        aligned_seq, _ = pairwise_alignment(alignments[i - 1], sequences[i], gap_penalty, match_score, mismatch_penalty)
        alignments.append(aligned_seq)
    
    # Create a profile alignment using the pair-wise alignments
    profile_alignment = alignments[0]
    for i in range(1, num_sequences):
        profile_alignment, _ = pairwise_alignment(profile_alignment, alignments[i], gap_penalty, match_score, mismatch_penalty)
    
    return profile_alignment

# Collect user input for protein sequences
def collect_sequences():
    num_sequences = int(input("Enter the number of protein sequences: "))
    sequences = []

    for i in range(num_sequences):
        sequence = input(f"Enter protein sequence {i + 1}: ")
        sequences.append(sequence)
    
    return sequences

def main():
    sequences = collect_sequences()

    # Perform progressive multiple sequence alignment
    aligned_sequence = progressive_alignment(sequences)

    # Print the aligned sequence
    print("Progressive Multiple Sequence Alignment:")
    print(aligned_sequence)

if __name__ == "__main__":
    main()
