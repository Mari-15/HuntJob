import tkinter
from Add_new_company import *
from Database_integration import *


db = DB()


def info_result(data):
    # create a window for search result
    window_result = Tk()
    window_result.geometry('900x300')
    window_result.title('Search result')

    # create frame for search result
    frame_result = Frame(
        window_result,
        padx=1,
        pady=1
    )
    frame_result.pack(expand=True)

    result_box = tkinter.Text(window_result)
    result_box.pack()
    result_box.insert('1.0', data)

    window_result.mainloop()


def find_company_info():
    # create a window for function find company
    window_comp_info = Tk()
    window_comp_info.geometry('275x150')
    window_comp_info.title('Find the company')

    # create frame for function find company
    frame = Frame(
        window_comp_info,
        padx=1,
        pady=1
    )
    frame.pack(expand=True)

    # create label for company name
    var_new_company = StringVar(window_comp_info)
    var_new_company.set('Name of the company')
    label_new_company = create_label(window_comp_info, var_new_company, FLAT)
    label_new_company.pack()
    label_new_company.place(x=10, y=10)

    # create stoke for enter company name
    stroke_company_name = Entry(
        window_comp_info,
        bd=2,
        width=37
    )
    stroke_company_name.place(x=10, y=40)

    # create button find
    find_window = Button(
        window_comp_info,
        text='Find',
        command=lambda: [info_result(db.search_by_companyname(stroke_company_name.get()))]
    )
    find_window.place(x=70, y=100)

    # create button close
    close_window = Button(
        window_comp_info,
        text='Close',
        command=window_comp_info.destroy
    )
    close_window.place(x=120, y=100)
