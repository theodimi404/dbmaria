import mariadb
from tkinter import *
from tkinter.ttk import *


def create_insert_window():
    window = Tk()
    window.title("Register Data")
    # Create Entry and Label Widgets for name, phone, password, address, email

    lbl = Label(window, text="Register the customer's information")
    lbl.grid(row=0, column=0, sticky='', pady=10)

    frm_entry = Frame(window)
    frm_entry.grid(row=1, column=0, sticky="ns")

    lbl1 = Label(frm_entry, text="Name")
    lbl1.grid(row=0, column=0, sticky="ew", padx=5, pady=10)

    txt1 = Entry(frm_entry, width=30)
    txt1.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

    lbl2 = Label(frm_entry, text="Phone")
    lbl2.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

    txt2 = Entry(frm_entry, width=30)
    txt2.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

    lbl3 = Label(frm_entry, text="Password")
    lbl3.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

    txt3 = Entry(frm_entry, width=30)
    txt3.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

    lbl4 = Label(frm_entry, text="Address")
    lbl4.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

    txt4 = Entry(frm_entry, width=30)
    txt4.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

    lbl5 = Label(frm_entry, text="Email")
    lbl5.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

    txt5 = Entry(frm_entry, width=30)
    txt5.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

    lbl6 = Label(frm_entry, text="Date")
    lbl6.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

    txt6 = Entry(frm_entry, width=30)
    txt6.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

    # Function that adds an entry into table contact
    def add_contact():
        """Adds the given contact to the contacts table"""
        # Connecting with database, fill in the right credentials
        try:
            conn = mariadb.connect(
                user="suport",
                password="support",
                host="localhost",
                port=3306)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        # Getting the values from the widgets
        cur = conn.cursor()
        name = txt1.get()
        phone = txt2.get()
        password = txt3.get()
        address = txt4.get()
        email = txt5.get()
        date = txt6.get()
        cur.execute("INSERT INTO demo.contact(name, phone, password, address, email, date)\
            VALUES (?, ?, ?, ?, ?, ?)",
            (name, phone, password, address, email, date))
        # Closing the connection
        conn.close()

    # Button to register all the data
    frm_buttons = Frame(window)
    frm_buttons.grid(row=2, column=0, sticky="ns")

    btn = Button(frm_buttons, text="REGISTER", command=add_contact)
    btn.grid(row=0, column=0, sticky="ew", pady=10)


def create_select_window():
    window = Tk()
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    frm_entry = Frame(window)
    frm_entry.grid(row=0, column=0, sticky="ns")

    lbl1 = Label(frm_entry, text="choose a name")
    lbl1.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

    txt1 = Entry(frm_entry, width=20)
    txt1.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

    lbl2 = Label(frm_entry, text="choose a phone")
    lbl2.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

    txt2 = Entry(frm_entry, width=20)
    txt2.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

    lbl3 = Label(frm_entry, text="choose a date")
    lbl3.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

    txt3 = Entry(frm_entry, width=20)
    txt3.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

    bigtxt = Text(window, width=30, height=10)
    bigtxt.grid(row=0, column=1, sticky="nsew")

    def show_contact():
        """Adds the given contact to the contacts table"""
        try:
            conn = mariadb.connect(
                user="suport",
                password="support",
                host="localhost",
                port=3306)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        contacts = []
        cur = conn.cursor()
        name = txt1.get()
        phone = txt2.get()
        date = txt3.get()
        if name:
            cur.execute("SELECT name, phone, password, address, email, date FROM demo.contact WHERE name=?", (name,))
        elif date:
            cur.execute("SELECT name, phone, password, address, email, date FROM demo.contact WHERE date=?", (date,))
        elif name and date:
            cur.execute("SELECT name, phone, password, address, email, date FROM demo.contact WHERE name = ? and date=?", (name, date))
        elif phone:
            cur.execute("SELECT name, phone, password, address, email, date FROM demo.contact WHERE phone=?", (phone,))
        # Prepare Contacts
        for (name, phone, password, address, email, date) in cur:
            contacts.append(f'Name: {name}\n Phone: {phone}\n Password: {password}\n Address: {address}\n Email: {email}\n Date: {date}\n\n')
        bigtxt.insert("1.0", contacts)
        conn.close()

    btn = Button(frm_entry, text="Search", command=show_contact)
    btn.grid(row=3, column=0, sticky="", padx=5)


app = Tk()
app.title("Database GUI")
app.geometry("300x130")
app.columnconfigure(0, weight=1)

lbl = Label(app, text="designed by theodimi404")
lbl.grid(row=2, column=0, sticky="", padx=5, pady=5)

buttonInsert = Button(app,
                      text="INSERT",
                      command=create_insert_window)
buttonInsert.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

buttonSelect = Button(app,
                      text="SEARCH",
                      command=create_select_window)
buttonSelect.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

app.mainloop()
