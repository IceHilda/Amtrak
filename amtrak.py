# import web scraper - BeautifulSoup
import time


"""
amtrak.help
A tool to automatically check train times and report to a user.


"""
# TODO: Host on Flask
# TODO: Allow user to specify their trains
# TODO: Figure out specifics of BeautifulSoup call


def soup_placeholder(train_num, station):
    # Make some call to the website via API or scraping
    # ...
    """
    [Estimated Arrival] / [ARRIVED]
    10:51p
    19 minutes early
    Scheduled 11:10p
    """
    # if response says "Estimated Arrival", arrived=False, if says "arrived", arrived=True
    status_from_site = {
        "arrived": True,
        "arrival_time": "10:51p",
        "time_offset": -19,
        "scheduled_time": "11:10p"
    }
    return status_from_site  # or None if the call failed (aka wrong direction)

# Random variable initialization, etc.

# Test the network connections to the website


# Determine what train we're looking up
# 1: By station, train < - can't check one without the other
# 2: ETA on train from station 1 to station 2

# When do we check?
# 1: In a loop every x minutes, or
# 2: At a specified datetime <- Probably this one based on user needs



# From user, know/get train # and line

station_list = ("CHI", "SMT", "JOL", "DWT", "PON", "BNL", "LCN", "SPI", "CRV", "ALN", "STL")  #Full list of CHI-STL line
my_trains = [303, 307]
max_late_allowed = 5  # Minutes late a train is allowed to run

def find_my_train(train):
    for station in station_list:
        result = soup_placeholder(train, station)
        if result["arrived"] == False:
            return result
    print("No results found")


running = True
while running:
    for train in my_trains:
        current_status = find_my_train()
        if current_status["time_offset"] > max_late_allowed:
            text_messenger()  # Oh shit someone's in trouble

    # Wait 5 minutes
    time.sleep(300)
    # if user types quit:
    #     running = False
