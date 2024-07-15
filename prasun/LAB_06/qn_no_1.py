def justify_text(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) <= width:
            current_line.append(word)
            current_length += len(word) + 1  # +1 for the space
        else:
            lines.append(current_line)
            current_line = [word]
            current_length = len(word) + 1  # reset current_length

    if current_line:
        lines.append(current_line)

    justified_lines = []
    for line in lines:
        if len(line) > 1:
            total_spaces_needed = width - sum(len(word) for word in line)
            num_gaps = len(line) - 1
            if num_gaps > 0:
                spaces_per_gap = total_spaces_needed // num_gaps
                extra_spaces = total_spaces_needed % num_gaps
                justified_line = ""
                for i, word in enumerate(line):
                    if i < len(line) - 1:
                        justified_line += word + ' ' * spaces_per_gap
                        if i < extra_spaces:
                            justified_line += ' '
                    else:
                        justified_line += word
                justified_lines.append(justified_line)
            else:
                justified_lines.append(line[0].ljust(width))
        else:
            justified_lines.append(line[0].ljust(width))

    return justified_lines

# Example usage:
text = "An architect may have a graphics program to draw an entire building but be interested in only ground floor."
width = 30

justified_text = justify_text(text, width)
for line in justified_text:
    print(line)
