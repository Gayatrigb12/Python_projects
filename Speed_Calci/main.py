import time
from termcolor import colored  # For colored output (install using pip install termcolor)

# Paragraph to type
text_to_type = """Learning to code is not just about mastering a language; it's about developing a mindset. When you write code, you’re not just telling a computer what to do—you’re solving problems, thinking logically, and learning to be patient and precise. The journey may be challenging, but every bug you fix brings you one step closer to becoming a better problem-solver."""

def calculate_errors_and_show(original, typed):
    errors = 0
    result = []

    for i in range(min(len(original), len(typed))):
        if original[i] == typed[i]:
            result.append(original[i])  # Correct char
        else:
            result.append(colored(typed[i], 'red'))  # Error in red
            errors += 1

    # Remaining unmatched characters
    if len(typed) > len(original):
        for c in typed[len(original):]:
            result.append(colored(c, 'red'))
            errors += 1
    elif len(original) > len(typed):
        missing = original[len(typed):]
        result.append(colored(f"(Missing: {missing})", 'yellow'))
        errors += len(missing)

    return errors, ''.join(result)

def typing_test():
    print("\n💬 Type the following paragraph:\n")
    print("👉", text_to_type, "\n")
    input("🎯 Press Enter when you're ready to start...")

    print("\n⌨️ Start typing below:\n")
    start_time = time.time()
    typed_input = input()
    end_time = time.time()

    time_taken = end_time - start_time
    time_taken_minutes = time_taken / 60

    word_count = len(typed_input.split())
    speed_wpm = round(word_count / time_taken_minutes) if time_taken_minutes > 0 else 0

    errors, highlighted_output = calculate_errors_and_show(text_to_type, typed_input)

    print("\n📊 Typing Test Results:")
    print(f"🕒 Time Taken: {round(time_taken, 2)} seconds")
    print(f"⚡ Speed: {speed_wpm} words per minute")
    print(f"❌ Total Errors: {errors} character(s)\n")

    print("🔎 Here's your typing with mistakes highlighted:\n")
    print(highlighted_output)

if __name__ == "__main__":
    typing_test()
