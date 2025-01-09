import re
def email_slicer():
    # Input multiple email addresses
    emails = input("Enter email addresses separated by commas: ").strip()
    email_list = list(set(email.strip() for email in emails.split(",") if email.strip()))  # Remove duplicates and extra spaces
    output_data = []
    # Email validation regex
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    for email in email_list:
        if re.match(email_regex, email):
            username, domain = email.split("@")
            domain_type = domain.split(".")[0].capitalize()
            output_data.append({
                "email": email,
                "username": username,
                "domain": domain,
                "domain_type": domain_type
            })
        else:
            print(f"Invalid email format: {email}")
    if output_data:
        # Display all results
        print("\nProcessed Email Details:")
        for data in output_data:
            print(f"Email: {data['email']}")
            print(f"  Username: {data['username']}")
            print(f"  Domain: {data['domain']}")
            print(f"  Domain Type: {data['domain_type']}")
        # Ask if the user wants to save the output
        save_to_file = input("\nDo you want to save the results to a file? (yes/no): ").strip().lower()
        if save_to_file == "yes":
            with open("email_slicer_output.txt", "w") as file:
                file.write("\n".join([
                    f"Email: {data['email']}\n  Username: {data['username']}\n  Domain: {data['domain']}\n  Domain Type: {data['domain_type']}"
                    for data in output_data
                ]))
            print("Results saved to 'email_slicer_output.txt'.")
    else:
        print("\nNo valid email addresses were provided.")
# Call the function
email_slicer()

