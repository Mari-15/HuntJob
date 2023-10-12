from tkinter import *
import Find_company_info
from Database_integration import *
from Find_company_info import *

db = DB()

# list of status
status_list = ['Резюме не просмотрено', 'Просмотрели и не ответили',
               'Отказ', 'Провалила тех собес', 'Провалила hr-интервью',
               'Написали, жду', 'Иное (подробности в комменте)']

# list of times
collect_times = [1, 2, 3, 4, 5]


def create_label(windows, text, text_relief):
    name = Label(
        windows,
        textvariable=text,
        relief=text_relief
    )
    return name


def add_new_company():
    # create a window for function add new company
    window_new_comp = Tk()
    window_new_comp.geometry('950x150')
    window_new_comp.title('Add new company')

    # create frame for function add new company
    frame = Frame(
        window_new_comp,
        padx=1,
        pady=1
    )
    frame.pack(expand=True)

    # create label for company name
    var_new_company = StringVar(window_new_comp)
    var_new_company.set('Name of new company')
    label_new_company = create_label(window_new_comp, var_new_company, FLAT)
    label_new_company.pack()
    label_new_company.place(x=10, y=10)

    # create stoke for enter company name
    stroke_company_name = Entry(
        window_new_comp,
        bd=2,
        width=30
    )
    stroke_company_name.place(x=10, y=40)

    # create list for status
    list_status = StringVar(window_new_comp)
    list_status.set(status_list[0])
    list_status_dropdown = OptionMenu(
        window_new_comp,
        list_status,
        *status_list
    )
    list_status_dropdown.pack()
    list_status_dropdown.place(x=200, y=32)

    # create label for where
    var_where = StringVar(window_new_comp)
    var_where.set('Where')
    label_where = create_label(window_new_comp, var_where, FLAT)
    label_where.pack()
    label_where.place(x=440, y=10)

    # create stoke for enter where
    stroke_where = Entry(
        window_new_comp,
        bd=2,
        width=30
    )
    stroke_where.insert(0, 'hh')
    stroke_where.place(x=440, y=40)

    # create list for how much times
    list_times = StringVar(window_new_comp)
    list_times.set(collect_times[0])
    list_times_dropdown = OptionMenu(
        window_new_comp,
        list_times,
        *collect_times
    )
    list_times_dropdown.pack()
    list_times_dropdown.place(x=630, y=32)

    # create label for comments
    var_comment = StringVar(window_new_comp)
    var_comment.set('Comments')
    label_comment = create_label(window_new_comp, var_comment, FLAT)
    label_comment.pack()
    label_comment.place(x=720, y=10)

    # create stroke for comments
    stroke_comments = Entry(
        window_new_comp,
        bd=2,
        width=30
    )
    stroke_comments.insert(0, '–')
    stroke_comments.place(x=720, y=40)

    # clean all forms
    def clean_all():
        stroke_company_name.delete(0, 'end')
        stroke_where.delete(0, 'end')
        stroke_where.insert(0, 'hh')
        stroke_comments.delete(0, 'end')
        stroke_comments.insert(0, '–')
        list_status.set(status_list[0])
        list_times.set(str(collect_times[0]))

    # get results
    def get_result():
        result_company_name = stroke_company_name.get()
        result_status = list_status.get()
        result_where = stroke_where.get()
        result_times = list_times.get()
        result_comment = stroke_comments.get()
        list_result = [result_company_name, result_status, result_where, result_times, result_comment]
        return list_result

    # create button for save company
    save_company_button = Button(
        window_new_comp,
        text='Save company',
        command=lambda: [db.insert(company_name=stroke_company_name.get(), status=list_status.get(),
                                   where_find=stroke_where.get(), times=list_times.get(),
                                   comment=stroke_comments.get()), clean_all()]
    )
    save_company_button.place(x=250, y=100)

    # create button for update info
    update_info_button = Button(
        window_new_comp,
        text='Update company info',
        command=lambda: [db.update(company_name=stroke_company_name.get(), status=list_status.get(),
                          where_find=stroke_where.get(), times=list_times.get(),
                          comment=stroke_comments.get()), clean_all()]
    )
    update_info_button.place(x=350, y=100)

    # create button for delete company
    delete_company_button = Button(
        window_new_comp,
        text='Delete company',
        command=lambda: [db.delete_data(company_name=stroke_company_name.get()), clean_all()]
    )
    delete_company_button.place(x=490, y=100)

    # create button close
    close_window = Button(
        window_new_comp,
        text='Close',
        command=window_new_comp.destroy
    )
    close_window.place(x=600, y=100)

    # wait while user close the window
    window_new_comp.mainloop()



