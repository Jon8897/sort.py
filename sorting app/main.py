# Imports libaries that will be needed to run the program
import PySimpleGUI as sg
from gui_layouts import create_main_layout
from skufinder import find_sku
from seoscraper import scrape_seo

def main():
    window = sg.Window("My Application", create_main_layout())

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == "Find SKU":
            result = find_sku(values["-SKU-URL-"])
            window["-SKU-RESULT-"].update(result)

        if event == "Scrape SEO":
            result = scrape_seo(values["-SEO-URL-"])
            window["-SEO-RESULT-"].update(result)

    window.close()

if __name__ == "__main__":
    main()