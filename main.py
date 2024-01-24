# Imports libaries that will be needed to run the program
import PySimpleGUI as sg
from gui_layouts import create_main_layout
from skufinder import find_sku
from seoscraper import scrape_seo

# The main function where the program starts execution
def main():
    # Create the main application window with the layout defined in gui_layouts.py
    window = sg.Window("My Application", create_main_layout())

    # Event loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # If the user closes the window, end the loop
        if event == sg.WIN_CLOSED:
            break

        # If the 'Find SKU' button is clicked
        if event == "Find SKU":
            # Call the find_sku function and pass the URL provided by the user
            result = find_sku(values["-SKU-URL-"])
            # Update the text element with the key '-SKU-RESULT-' with the result
            window["-SKU-RESULT-"].update(result)

        # If the 'Scrape SEO' button is clicked
        if event == "Scrape SEO":
            # Call the scrape_seo function and pass the URL provided by the user
            result = scrape_seo(values["-SEO-URL-"])
            # Update the text element with the key '-SEO-RESULT-' with the result
            window["-SEO-RESULT-"].update(result)

    # Close the window when the event loop is exited
    window.close()

# Check if the script is being run directly (as opposed to being imported)
if __name__ == "__main__":
    main()  # Call the main function