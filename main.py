from Find_one_type_info import *
from Database_integration import *

# create window PO
window = Tk()
window.geometry('400x100')
window.title('Hunt job')

# create frame for programm
frame = Frame(
    window,
    padx=1,
    pady=1
)
frame.pack(expand=True)

number_of_rows = db.total_number_rows()

# create label for total number of companies
var_total_number = StringVar()
label_total_number = create_label(windows=window, text=var_total_number, text_relief=FLAT)
var_total_number.set(f'Total number of companies: {number_of_rows}')
label_total_number.pack()
label_total_number.place(x=10, y=10)

db = DB()

# create button for add new company
create_new = Button(
    window,
    text='Add new company',
    command=add_new_company
)
create_new.place(x=10, y=50)

# create find button
find_button = Button(
    window,
    text='Find company info',
    command=find_company_info
)
find_button.place(x=140, y=50)

# create show info button
show_info_button = Button(
    window,
    text='Show info',
    command=find_info
)
show_info_button.place(x=270, y=50)

# create close button
close_button = Button(
    window,
    text='Close',
    command=lambda: [db.create_backup(), window.destroy()]
)
close_button.place(x=350, y=50)

# wait while user close the window
window.mainloop()