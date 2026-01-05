import tkinter as tk
from tkinter import messagebox
import logic

book = logic.PhoneBook()

def refresh_list(data=None):
    list_contacts.delete(0, tk.END)
    show = data if data is not None else book.contacts
    for contact in show:
        display_text = f"{contact.name} - {contact.phone_number}"
        list_contacts.insert(tk.END, display_text)


def add_click():
    name = ent_name.get()
    phone = ent_phone.get()

    if not name or not phone:
        messagebox.showwarning("Error", "pls enter name & phone number!")
        return

    try:
        book.add_contact(name, phone)
        refresh_list()
        ent_name.delete(0, tk.END)
        ent_phone.delete(0, tk.END)
        messagebox.showinfo("Done", "contact successfully added.")
    except ValueError as e:
        messagebox.showerror("Error!", str(e))


def search_click():
    text = ent_search.get()
    results = [c for c in book.contacts if text in c.name]
    refresh_list(results)


def delete_click():
    delete = list_contacts.curselection()
    if not delete:
        messagebox.showwarning("Error", "pls select a contact")
        return

    index = delete[0]
    text = list_contacts.get(index)
    name, phone = text.split(" - ")

    for c in book.contacts:
        if c.name == name and c.phone_number == phone:
            book.contacts.remove(c)
            break

    refresh_list()


def smart_exit():
    book.save_to_csv("contacts.csv")
    root.destroy()



root = tk.Tk()
root.title("PhoneBook")
root.geometry("600x550")


frame1 = tk.Frame(root)
frame1.pack(pady=15)

tk.Label(frame1, text="Name :").grid(row=0, column=0)
ent_name = tk.Entry(frame1)
ent_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame1, text="Phone Number :").grid(row=1, column=0)
ent_phone = tk.Entry(frame1)
ent_phone.grid(row=1, column=1, padx=5, pady=5)


frame2 = tk.Frame(root)
frame2.pack(pady=5)

tk.Button(frame2, text="Add Contact", bg="cyan", command=add_click).pack(side=tk.LEFT, padx=5)
tk.Button(frame2, text="Delete", bg="yellow",command=delete_click).pack(side=tk.LEFT, padx=5)
tk.Button(frame2, text="Exit", bg="red", command=smart_exit).pack(side=tk.LEFT, padx=5)


frame3 = tk.Frame(root)
frame3.pack(pady=10)

tk.Label(frame3, text="Search :").pack(side=tk.LEFT)
ent_search = tk.Entry(frame3)
ent_search.pack(side=tk.LEFT, padx=5)
tk.Button(frame3, text="Search",bg="purple",fg="white" ,command=search_click).pack(side=tk.LEFT)


tk.Label(root, text="Contacts List :").pack(pady=10)

list_contacts = tk.Listbox(root, width=50, height=15)
list_contacts.pack()


book.load_from_csv("contacts.csv")
refresh_list()

root.mainloop()
print ("Exit...")