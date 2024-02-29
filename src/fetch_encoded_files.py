# Add this function to your code to fetch data from the database
def fetch_encoded_files():
    try:
        with sqlite3.connect('C:\\Users\\Dell\\Desktop\\python project\\encryptstego-main\\encryptstego-main\\encoded_files.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM encoded_files")
            records = cursor.fetchall()
            return records
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return None

# Modify your existing code to call this function and display the fetched data
# For example, you can modify your 'help_menu' function:

def help_menu():
    global help_opened
    if not help_opened:
        help_window = Toplevel(window)
        help_window.title("Help")
        help_window.geometry('500x420')
        help_window.resizable(False, False)
        help_window.transient(window)
        if windows:
            windll.shcore.SetProcessDpiAwareness(1)

        text_to_decode_label = Label(help_window, text="\nEncryptstego v1.0\nDeveloped by @iamBhawanaAryal")
        text_to_decode_label.config(font=("Open Sans", 12))
        text_to_decode_label.pack()

        # Fetch records from the database
        records = fetch_encoded_files()

        if records:
            # Display fetched records
            records_label = Label(help_window, text="Encoded Files:")
            records_label.config(font=("Open Sans", 12))
            records_label.pack()

            for record in records:
                record_text = f"File: {record[1]}, Filename: {record[2]}, Timestamp: {record[3]}"
                record_label = Label(help_window, text=record_text)
                record_label.config(font=("Open Sans", 10), justify="left", wraplength=450)
                record_label.pack(pady=5)
        else:
            error_label = Label(help_window, text="Error fetching records from the database.")
            error_label.config(font=("Open Sans", 12), fg="red")
            error_label.pack(pady=10)

        help_opened = True
        help_window.protocol("WM_DELETE_WINDOW", lambda: close_help_window(help_window))
