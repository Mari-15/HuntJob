from Find_company_info import *
from Database_integration import *


db = DB()


def create_checkbox(windows, check_text, variable, height=1, width=5,
                    check_onvalue=1, check_offvalue=0):
    name = Checkbutton(
        windows,
        text=check_text,
        variable=variable,
        height=height,
        width=width,
        onvalue=check_onvalue,
        offvalue=check_offvalue
    )
    return name


def find_info():
    # create a window for function find company
    window_info = Tk()
    window_info.geometry('220x150')
    window_info.title('Find info')

    # create frame for function find company
    frame = Frame(
        window_info,
        padx=1,
        pady=1
    )
    frame.pack(expand=True)

    # create checkboxes for options
    check_checkbox_reject = IntVar(window_info)
    check_checkbox_more_than_one = IntVar(window_info)
    check_checkbox_write_and_wait = IntVar(window_info)
    check_checkbox_all = IntVar(window_info)
    checkbox_reject = create_checkbox(windows=window_info, check_text='Отказы',
                                      variable=check_checkbox_reject)
    checkbox_more_than_one = create_checkbox(windows=window_info, check_text='Больше 1 раза', width=10,
                                             variable=check_checkbox_more_than_one)
    checkbox_write_and_wait = create_checkbox(windows=window_info, check_text='Написали, жду', width=12,
                                              variable=check_checkbox_write_and_wait)
    checkbox_all = create_checkbox(windows=window_info, check_text='Показать всю таблицу', width=18,
                                   variable=check_checkbox_all)
    checkbox_reject.place(x=13, y=10)
    checkbox_more_than_one.place(x=16, y=30)
    checkbox_write_and_wait.place(x=10, y=50)
    checkbox_all.place(x=10, y=70)

    def get_result_checkbox():
        reject, number, wait, all_data = check_checkbox_reject.get(), check_checkbox_more_than_one.get(), \
            check_checkbox_write_and_wait.get(), check_checkbox_all.get()
        result = [reject, number, wait, all_data]
        options = ['Отказ', 'number', 'Написали, жду', 'all']
        result_info = '0'
        for i in range(len(result)):
            if result[i] == 1:
                result_info = options[i]

        return result_info

    def clean_all_checkboxes():
        checkbox_reject.deselect()
        checkbox_more_than_one.deselect()
        checkbox_write_and_wait.deselect()
        checkbox_all.deselect()

    # create button find
    find_window = Button(
        window_info,
        text='Find',
        command=lambda: [info_result(db.view_and_search(get_result_checkbox()))]
    )
    find_window.place(x=10, y=100)

    # create button refresh
    close_window = Button(
        window_info,
        text='Refresh',
        command=clean_all_checkboxes
    )
    close_window.place(x=50, y=100)

    # create button close
    close_window = Button(
        window_info,
        text='Close',
        command=window_info.destroy
    )
    close_window.place(x=110, y=100)