from tkinter import *
import sqlite3

from datetime import datetime


root = Tk()
root.title('Finance app')

root.geometry("400x600")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('finance_app.db')

# Create cursor
c = conn.cursor()

# # Create Update function to update a record
# def update():
# 	# Create a database or connect to one
# 	conn = sqlite3.connect('address_book.db')
# 	# Create cursor
# 	c = conn.cursor()

# 	record_id = delete_box.get()

# 	c.execute("""UPDATE addresses SET
# 		first_name = :first,
# 		last_name = :last,
# 		address = :address,
# 		city = :city,
# 		state = :state,
# 		zipcode = :zipcode 
# 		WHERE oid = :oid""",
# 		{
# 		'first': f_name_editor.get(),
# 		'last': l_name_editor.get(),
# 		'address': address_editor.get(),
# 		'city': city_editor.get(),
# 		'state': state_editor.get(),
# 		'zipcode': zipcode_editor.get(),
# 		'oid': record_id
# 		})


# 	#Commit Changes
# 	conn.commit()

# 	# Close Connection 
# 	conn.close()

# 	editor.destroy()
# 	root.deiconify()

# Create Edit function to update a record
def edit():
	root.withdraw()
	global editor
	editor = Tk()
	editor.title('Редактировать')
	editor.geometry("400x300")
	# Create a database or connect to one
	conn = sqlite3.connect('finance_app.db')
	# Create cursor
	c = conn.cursor()

	record_id = delete_box.get()

	# Query the database
	c.execute("SELECT * FROM transactions WHERE id=?", (record_id))
	records = c.fetchall()
	
	#Create Global Variables for text box names
	global title
	global value
	global transaction_type
	global income

	# Create Text Boxes
	title_editor = Entry(editor, width=30)
	title_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

	value_editor = Entry(editor, width=30)
	value_editor.grid(row=1, column=1)

	type_editor = Entry(editor, width=30)
	type_editor.grid(row=2, column=1)

	income_editor = Entry(editor, width=30)
	income_editor.grid(row=3, column=1)


	
	# Create Text Box Labels
	title_label = Label(editor, text="Title")
	title_label.grid(row=0, column=0, pady=(10, 0))

	value_label = Label(editor, text="Value")
	value_label.grid(row=1, column=0)

	type_label = Label(editor, text="Type")
	type_label.grid(row=2, column=0)

	income_label = Label(editor, text="Income")
	income_label.grid(row=3, column=0)


	# Loop thru results
	for record in records:
		title_editor.insert(0, record[0])
		value_editor.insert(0, record[1])
		type_editor.insert(0, record[2])
		income_editor.insert(0, record[3])
	

	# Create a Save Button To Save edited record
	edit_btn = Button(editor, text="Save", command=update)
	edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)
	

# DELETE
def delete():
	# Create a database or connect to one
	conn = sqlite3.connect('finance_app.db')

	# Create cursor
	c = conn.cursor()

	# Delete a record
	c.execute("DELETE from transactions WHERE id=?", (delete_box.get()))

	delete_box.delete(0, END)

	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()


# INSERT INTO Query
def submit():
	# Create a database or connect to one
	conn = sqlite3.connect('finance_app.db')
	# Create cursor
	c = conn.cursor()

	# Insert Into Table
	c.execute("INSERT INTO transactions (title, value, type, income, date) VALUES (?, ?, ?, ?, ?)",
			(
				title.get(),
				value.get(),
				transaction_type.get(),
				income.get(),
				datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # like SQLite default
			))


	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()

	# Clear The Text Boxes
	title.delete(0, END)
	value.delete(0, END)
	transaction_type.delete(0, END)
	income.delete(0, END)


# SELECT Query
def query():
	# Create a database or connect to one
	conn = sqlite3.connect('finance_app.db')
	# Create cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT * FROM transactions")
	records = c.fetchall()
	# print(records)

	# Loop Thru Results
	print_records = ''
	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" +str(record[2]) + "\n"

	query_label = Label(root, text=print_records)
	query_label.grid(row=12, column=0, columnspan=2)

	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()


# Create Text Boxes
title = Entry(root, width=30)
title.grid(row=0, column=1, padx=20, pady=(10, 0))

value = Entry(root, width=30)
value.grid(row=1, column=1)

transaction_type = Entry(root, width=30)
transaction_type.grid(row=2, column=1)

income = Entry(root, width=30)
income.grid(row=3, column=1)


delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)


# Create Text Box Labels
title_label = Label(root, text="Название транзакции")
title_label.grid(row=0, column=0, pady=(10, 0))

value_label = Label(root, text="Сумма")
value_label.grid(row=1, column=0)

type_label = Label(root, text="Тип транзакции")
type_label.grid(row=2, column=0)

income_label = Label(root, text="Это доход? (0-1)")
income_label.grid(row=3, column=0)


delete_box_label = Label(root, text="ID для действия")
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = Button(root, text="Добавить доход", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Все транзакции", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create A Delete Button
delete_btn = Button(root, text="Удалить транзакцию", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create an Update Button
edit_btn = Button(root, text="Редактировать", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)


#Commit Changes
conn.commit()

# Close Connection 
conn.close()

root.mainloop()