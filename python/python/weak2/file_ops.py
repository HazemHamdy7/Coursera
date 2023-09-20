# def read_file(sampletext.txt):
#     """ Reads in a file and prints its contents."""
#     try:
#         with open(sampletext.txt, 'r') as file:
#             file_contents = file.read()
#             print(file_contents)
#             return file_contents
#     except FileNotFoundError:
#         print(f"File '{sampletext.txt}' not found.")
#         return None

# def read_file_into_list(sampletext.txt):
#     """ Reads in a file and stores each line as an element in a list."""
#     try:
#         with open(sampletext.txt, 'r') as file:
#             lines = file.readlines()
#             return lines
#     except FileNotFoundError:
#         print(f"File '{sampletext.txt}' not found.")
#         return []

# def write_first_line_to_file(file_contents, output_filename):
#     """ Writes the first line of a string to a file."""
#     lines = file_contents.split('\n')
#     if len(lines) > 0:
#         first_line = lines[0]
#         try:
#             with open(output_filename, 'w') as file:
#                 file.write(first_line)
#         except IOError:
#             print(f"Error writing to '{output_filename}'.")

# def read_even_numbered_lines(sampletext.txt):
#     """ Reads in the even-numbered lines of a file."""
#     try:
#         with open(sampletext.txt, 'r') as file:
#             lines = file.readlines()
#             even_lines = [line.strip() for i, line in enumerate(lines) if i % 2 == 1]
#             return even_lines
#     except FileNotFoundError:
#         print(f"File '{sampletext.txt}' not found.")
#         return []

# def read_file_in_reverse(sampletext.txt):
#     """ Reads a file and returns a list of the lines in reverse order."""
#     try:
#         with open(sampletext.txt, 'r') as file:
#             lines = file.readlines()
#             reversed_lines = lines[::-1]
#             for line in reversed_lines:
#                 print(line.strip())
#             return reversed_lines
#     except FileNotFoundError:
#         print(f"File '{sampletext.txt}' not found.")
#         return []

# def main():
#     file_contents = read_file("sampletext.txt")
#     # lines = read_file_into_list("sampletext.txt")
#     # write_first_line_to_file(file_contents, "online.txt")
#     # even_lines = read_even_numbered_lines("sampletext.txt")
#     # reversed_lines = read_file_in_reverse("sampletext.txt")

# if __name__ == "__main__":
#     main()
