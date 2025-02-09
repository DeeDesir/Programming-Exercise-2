
# List of common spam words/phrases
spam_keywords = [
    "free", "win", "winner", "prize", "discount", "cash", "gift", "lottery", "urgent", 
    "offer", "exclusive", "limited time", "special promotion", "claim now", 
    "guaranteed", "risk-free", "credit", "loan", "debt", "congratulations", "buy now", 
    "best deal", "billion dollars", "invest", "make money", "income", "click here", 
    "new customer", "free trial", "money back", "hurry"
]

# Function to scan email for spam words/phrases
def scan_for_spam(email):
    spam_score = 0
    found_keywords = []

    # Convert the email to lowercase to make the search case-insensitive
    email_lower = email.lower()

    # Check each keyword/phrase and see if it's in the email
    for keyword in spam_keywords:
        if keyword in email_lower:
            spam_score += 1
            found_keywords.append(keyword)

    return spam_score, found_keywords

# Function to classify the likelihood of spam
def classify_spam(spam_score):
    if spam_score >= 10:
        return "High likelihood of spam"
    elif spam_score >= 5:
        return "Moderate likelihood of spam"
    else:
        return "Low likelihood of spam"

# Main function to run the program
def main():
    email_message = input("Enter the email message to scan: ")
    
    # Scan for spam keywords
    spam_score, found_keywords = scan_for_spam(email_message)
    
    # Classify spam likelihood
    spam_likelihood = classify_spam(spam_score)
    
    # Output the results
    print(f"\nSpam score: {spam_score}")
    print(f"Spam likelihood: {spam_likelihood}")
    if found_keywords:
        print("Words/phrases causing the spam score:")
        for keyword in found_keywords:
            print(f"  - {keyword}")
    else:
        print("No spam-related words found.")

# Run the application
if __name__ == "__main__":
    main()