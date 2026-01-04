def reverse_text(text):
    # Return the reversed string
    return text[::-1]

# Main program to get input and print output
if __name__ == "__main__":
    # Prompt the user to enter a string
    user_input = input("Enter text to reverse: ")
    
    # Call the reverse_text function
    reversed_output = reverse_text(user_input)
    
    # Display the reversed text
    print("Reversed text:", reversed_output)
