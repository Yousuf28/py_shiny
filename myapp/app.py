# from shiny import App, render, ui

# app_ui = ui.page_fluid(
#     ui.h2("Hello Shiny!"),
#     ui.input_slider("n", "N", 0, 100, 20),
#     ui.output_text_verbatim("txt"),
# )


# def server(input, output, session):
#     @output
#     @render.text
#     def txt():
#         return f"n*2 is {input.n() * 2}"


# app = App(app_ui, server)

from shiny import *
from shiny.types import FileInfo
import pandas as pd

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_file("file1", "Choose CSV File", accept=[".csv"], multiple=False),
            ui.input_checkbox("header", "Header", True),
        ),
        ui.panel_main(ui.output_ui("contents")),
    )
)

def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.ui
    def contents():
        if input.file1() is None:
            return "Please upload a csv file"
        f: list[FileInfo] = input.file1()
        df = pd.read_csv(f[0]["datapath"], header=0 if input.header() else None)
        return ui.HTML(df.to_html(classes="table table-striped"))


app = App(app_ui, server)
