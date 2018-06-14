import pyexcel
# make sure you had pyexcel-xls installed
a_list_of_dictionaries = [
    {
        "title" : ""},
    {
        "link" : ""}
]

pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="text.xlsx")