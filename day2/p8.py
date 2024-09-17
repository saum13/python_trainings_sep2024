import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python p8.py '\"string1\" \"string2\" ...'")
        sys.exit(1)

    # Combine all arguments into a single string
    input_str = ' '.join(sys.argv[1:])
    print(f"Input string: {input_str}")

    # Split by ' " ' (space between quotes) but handle quoted segments
    # This will ensure we capture each quoted segment properly
    import shlex
    parts = shlex.split(input_str)
    print(f"Parts after splitting: {parts}")

    # Initialize lists
    l1 = []
    l2 = []

    # Process each part and populate lists
    for part in parts:
        if part:
            elements = part.split()
            if len(elements) == 2:
                l1.append(elements[0])
                l2.append(elements[1])
    
    print("l1 =", l1)
    print("l2 =", l2)

if __name__ == "__main__":
    main()
