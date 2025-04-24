email = input("Enter Email: ").strip()

k = 0  # Flag to track if any rule is violated

# Step 1: Minimum length
if len(email) >= 6:
    
    # Step 2: Starts with an alphabet
    if email[0].isalpha():
        
        # Step 3: Contains exactly one '@'
        if email.count('@') == 1:
            at_index = email.index('@')
            dot_index = email.rfind('.')

            # Step 4: At least one '.' after '@' and it's at 3rd/4th from the end
            if dot_index > at_index and (email[-4] == '.' or email[-3] == '.'):
                
                for char in email:
                    if char.isspace():
                        print("Email should not contain spaces.")
                        k = 1
                        break
                    elif char.isupper():
                        print("Email should not contain uppercase letters.")
                        k = 1
                        break
                    elif not (char.isalnum() or char in ['@', '.', '_']):
                        print(f"Invalid character found: {char}")
                        k = 1
                        break

                if k == 0:
                    print(" Valid email.")
            else:
                print("'.' should be at 3rd or 4th position from the end.")
        else:
            print("Email must contain only one '@' symbol.")
    else:
        print("Email should start with a letter.")
else:
    print("Email should be at least 6 characters long.")
