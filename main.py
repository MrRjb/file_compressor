import PySimpleGUI
from zip_creator import make_archive

PySimpleGUI.theme("DarkPurple4")

label1 = PySimpleGUI.Text("Select files to compress:")
input1 = PySimpleGUI.Input(tooltip="Enter files to compress")
choose1 = PySimpleGUI.FilesBrowse("Choose", key="files")

label2 = PySimpleGUI.Text("Select Destination folder: ")
input2 = PySimpleGUI.Input(tooltip="Select destionation folder")
choose2 = PySimpleGUI.FolderBrowse("Choose", key="folder")

compress_button = PySimpleGUI.Button("Compress")
output_label = PySimpleGUI.Text(key="output", text_color="green")

window = PySimpleGUI.Window("File Compressor - Created by RJB",
                            font=("Helvetica", 15), 
                            layout=[[label1, input1, choose1],
                                    [label2, input2, choose2],
                                    [compress_button, output_label]])

while True:
    event, values = window.read()
    try:
        filepaths = values["files"].split(";")
        folder = values["folder"]
        make_archive(filepaths, folder)
        window["output"].update(value="Compression Completed Succesfully.")
    except AttributeError:
        break

    if PySimpleGUI.WIN_CLOSED:
        break

window.close()
    