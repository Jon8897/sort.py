# Imports libaries that will be needed to run the program
import PySimpleGUI as sg

def create_main_layout():
    # Layout for the SKU Finder tab
    # This includes a text label, an input field for the URL, a button to initiate the SKU finding, and a text field to display results
    layout_sku_finder = [
        [sg.Text("Enter URL for SKU Finding:"), sg.InputText(key="-SKU-URL-")],  # Row for URL input
        [sg.Button("Find SKU"), sg.Text("", key="-SKU-RESULT-")]  # Row for the submit button and SKU result display
    ]

    # Layout for the SEO Scraper tab
    # This includes a text label, an input field for the URL, a button to initiate the SEO scraping, and a text field to display results
    layout_seo_scraper = [
        [sg.Text("Enter URL for SEO Scraping:"), sg.InputText(key="-SEO-URL-")],  # Row for URL input
        [sg.Button("Scrape SEO"), sg.Text("", key="-SEO-RESULT-")]  # Row for the submit button and SEO result display
    ]

    # Add a progress bar to the layout with a maximum value and an initial value
    progress_bar = sg.ProgressBar(max_value=100, orientation='h', size=(20, 20), key='-PROGRESS BAR-')

    # Group the layouts into tabs
    # Each layout is associated with a tab in the GUI
    tab_group_layout = sg.TabGroup ([
        [sg.Tab("SKU Finder", layout_sku_finder)],  # Tab for SKU Finder
        [sg.Tab("SEO Scraper", layout_seo_scraper)]  # Tab for SEO Scraper
    ])

    # Return the layout wrapped in a TabGroup
    # The TabGroup is a container for the tabs that allows switching between them
    return [
        [tab_group_layout],
        [sg.Text('Progress:'), progress_bar]
    ]