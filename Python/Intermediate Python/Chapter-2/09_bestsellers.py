import csv

# Step 1: Open the input CSV file for reading
with open('/home/jiten/Documents/CodeDex/Intermediate Python/Chapter-2/bestsellers.csv', 'r', encoding='utf8') as file:
    csv_reader = csv.reader(file)
    
    # Step 2: Skip the header row
    next(csv_reader)
    
    # Step 3: Initialize variables
    max_sales = 0
    best_selling_book = None
    
    # Step 4: Loop through each row to find the max sales
    for row in csv_reader:
        try:
            current_sales = float(row[4])  # Assuming sales are in the 5th column
            if current_sales > max_sales:
                max_sales = current_sales
                best_selling_book = row
        except ValueError:
            # Handle potential conversion errors if data isn't clean
            continue

# Step 5: Write the best-seller info to a new CSV file
with open('/home/jiten/Documents/CodeDex/Intermediate Python/Chapter-2/bestseller_info.csv', 'w', newline='', encoding='utf8') as outfile:
    csv_writer = csv.writer(outfile)
    
    # Step 6: Write header and data
    csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])
    if best_selling_book:
        # Extract relevant columns from the best_selling_book
        # Make sure the indices match your CSV's structure
        book_title = best_selling_book[0]
        author = best_selling_book[1]
        sales = best_selling_book[4]
        csv_writer.writerow([book_title, author, sales])