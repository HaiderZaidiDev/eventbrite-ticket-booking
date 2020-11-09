from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests as r

def link_scrape(url):
    """ Scrapes Eventbrite booking link from apartment site."""
    page = r.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    page_links = soup.find_all("a")
    try:
        # Last link on page containing "eventbrite"
        eventbrite_link = [link['href'] for link in page_links if 'eventbrite' in link['href']][-1]
    except:
        eventbrite_link = False
    return eventbrite_link

class TicketBooking:
    """Books free tickets on Eventbrite given a URL."""
    def __init__(self, url, driver, first_name, last_name, email):
        self.url = url
        self.driver = driver
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def start_driver(self):
        self.driver.get(self.url)

    def get_event_id(self):
        """Parses event id from url."""
        event_id = self.url.split('-')[-1]
        return event_id

    def click_register_button(self, delay):
        """ Finds & clicks the register button"""
        time.sleep(delay)
        poss_register_buttons = self.driver.find_elements_by_tag_name("button")
        register_button = [button for button in poss_register_buttons if button.text == "Register"][-1].click()
        time.sleep(delay)

    def select_avail_tickets(self):
        """ Books the ticket in the last time-slot."""
        select_date_menu_id = f"eventbrite-widget-modal-trigger-{self.get_event_id()}"
        select_date_button = self.driver.find_element_by_id(select_date_menu_id).click()
        self.driver.switch_to.frame(f"eventbrite-widget-modal-{self.get_event_id()}") # Switches to iFrame pop-up.
        time.sleep(5)
        ticket_buttons = self.driver.find_elements_by_tag_name("button")
        avail_tickets = [button for button in ticket_buttons if button.text == "Tickets"]
        ticket_to_book = avail_tickets[-1].click()

    def fill_form(self):
        """ Fills in the contact form."""
        first_name = self.driver.find_element_by_id("buyer.N-first_name")
        last_name = self.driver.find_element_by_id("buyer.N-last_name")
        email = self.driver.find_element_by_id("buyer.N-email")
        confirmed_email = self.driver.find_element_by_id("buyer.confirmEmailAddress")

        first_name.send_keys(self.first_name)
        last_name.send_keys(self.last_name)
        email.send_keys(self.email)
        confirmed_email.send_keys(self.email)

    def book(self):
        """ Intitiates booking process"""
        self.start_driver()
        self.select_avail_tickets()
        self.click_register_button(5)
        self.fill_form()
        self.click_register_button(0)
