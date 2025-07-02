from stats import get_book_text, word_count, count_chars, print_report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>\n")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    print(f"--- Begin report of {sys.argv[1]} ---")
    lowercased = text.lower()
    count = word_count(lowercased)
    print(f"Found {count} total words\n")
    chars = count_chars(lowercased)
    print_report(chars)

main()