def run_length_encode(data):
    encoded = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded.append((data[i - 1], count))
            count = 1
    encoded.append((data[-1], count))  # last run
    return encoded

# Example usage:
data = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5]
encoded_data = run_length_encode(data)
print("Original data:", data)
print("Encoded data:", encoded_data)
