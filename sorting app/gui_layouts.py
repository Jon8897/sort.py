# imports libaries that will be needed to run the program
import PySimpleGUI as sg

def create_main_layout():
    layout_sku_finder = [
        [sg.Text("Enter URL for SKU Finding:"), sg.InputText(key="-SKU-URL-")],
        [sg.Button("Find SKU"), sg.Text("", key="-SKU-RESULT-")]
    ]

    layout_seo_scraper = [
        [sg.Text("Enter URL for SEO Scraping:"), sg.InputText(key="-SEO-URL-")],
        [sg.Button("Scrape SEO"), sg.Text("", key="-SEO-RESULT-")]
    ]

    tab_group_layout = [
        [sg.Tab("SKU Finder", layout_sku_finder)],
        [sg.Tab("SEO Scraper", layout_seo_scraper)]
    ]

    return [[sg.TabGroup([tab_group_layout])]]