# Imports libaries that will be needed to run the program
import PySimpleGUI as sg
from gui_layouts import create_main_layout
from skufinder import find_sku
from seoscraper import run_seo_scraper as scrape_seo
import threading

# The main function where the program starts execution
def main():
    # Create the main application window with the layout defined in gui_layouts.py
    window = sg.Window("My Application", create_main_layout(), size=(500,150))

    # Event loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # If the user closes the window, end the loop
        if event == sg.WIN_CLOSED:
            break

        # If the 'Find SKU' button is clicked
        if event == "Find SKU":
            # Start the find_sku function in a new thread
            threading.Thread(target=find_sku, args=(values['-SKU-URL-'], window, 'PROGRESS BAR-'), daemon=True).start()

        # If the 'Scrape SEO' button is clicked
        if event == "Scrape SEO":
            # Start the scrape_seo function in a new thread
            threading.Thread(target=scrape_seo, args=(values["-SEO-URL-"], window, '-PROGRESS BAR-'), daemon=True).start()

        # Handle the event that is called after the thread finishes execution
        if event == '-THREAD DONE-':
            # The result is passed back from the thread using window.write_event_value
            # Update the SEO result text element with the result from the thread
            window["-SEO-RESULT-"].update(str(values[event]))

    # Close the window when the event loop is exited
    window.close()

# Check if the script is being run directly (as opposed to being imported)
if __name__ == "__main__":
    main()  # Call the main function