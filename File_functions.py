import pandas as pd


def save_new_company(data):
    excel_file = 'c:/Users/Alex/PycharmProjects/HuntJob/company_list.xlsx'

    # try to find file
    try:
        df = pd.read_excel(excel_file)
    except FileNotFoundError:
        df = pd.DataFrame()

    first_empty_row = df[df.isna().all(axis=1)].index.min()

    if pd.isna(first_empty_row):
        new_row = pd.DataFrame([data], columns=['Name', 'Status', 'Where', 'Times', 'Comments'])
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        df.loc[first_empty_row] = data

    df.to_excel(excel_file, index=False)


def coll_rows():
    excel_file = 'c:/Users/Alex/PycharmProjects/HuntJob/company_list.xlsx'

    # try to find file
    try:
        df = pd.read_excel(excel_file)
        num_rows = len(df)
    except FileNotFoundError:
        num_rows = 0

    return num_rows


def find_company(company_name):
    excel_file = 'c:/Users/Alex/PycharmProjects/HuntJob/company_list.xlsx'
    df = pd.read_excel(excel_file)
    result = df.loc[df['Name'] == company_name]
    result_str = result.to_string(index=False)
    if result.empty:
        result_str = 'Такой компании нет'

    return result_str


def find_allfiles_onetype(info_data):
    excel_file = 'c:/Users/Alex/PycharmProjects/HuntJob/company_list.xlsx'
    df = pd.read_excel(excel_file)

    def is_greater_than_1(cell):
        try:
            return float(cell) > 1
        except ValueError:
            return False

    def search_value(cell):
        return info_data in str(cell)

    if info_data == 'number':
        result = df.map(is_greater_than_1)
        filter_result = df[result.any(axis=1)]
    elif info_data == 'all':
        filter_result = df.to_string(index=False)
    else:
        result = df.map(search_value)
        filter_result = df[result.any(axis=1)]

    return filter_result


def update_data(update_data):
    excel_file = 'c:/Users/Alex/PycharmProjects/HuntJob/company_list.xlsx'
    df = pd.read_excel(excel_file, index_col=0)

    for i in update_data:
        company_name = i['Name']
        row_to_update = df[df.index == company_name]

        if not row_to_update.empty:
            df.loc[company_name] = i
        else:
            new_row = pd.DataFrame([i], columns=df.columns, index=company_name)
            df = pd.concat([df, new_row])

    df.to_excel(excel_file, index=False)

