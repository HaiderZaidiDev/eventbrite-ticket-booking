# eventbrite-ticket-booking
Automatically reserves (free) tickets on Eventbrite, used to automatically book time slots for my apartment's gym.

Disclaimer: This is for ethical and/or educational use cases only. I do not condone, nor recommend use of the script in ways otherwise. 

## Background
During the pandemic, my apartment building books out slots for use of the Gym via Eventbrite, however, these slots open at 9:00am every Monday; 
I wanted to automate the process of booking these slots (Eventbrite tickets. 

## Features
- Scrapes my apartment building's website to get the Eventbrite link for booking gym tickets. 
- Books the last time slot from the available tickets. 

## Usage
Note: If you already have the Eventbrite link, and don't need to scrape, you can delete `link_scrape()`. 

Call the Ticket Booking class with your information, then call the book attribute: 

```
gym_tickets = TicketBooking(url,
                            webdriver.Chrome('./chromedriver'),
                            first_name,
                            last_name,
                            email)
gym_tickets.book()
```
