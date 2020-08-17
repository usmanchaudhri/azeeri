"""
Design book my show system- note here the panel is confused between autherizatin vs communication protocols

# list all available shows for a particular date
# what all theaters the show is played
# what is the capacity of the particular theater
# book the show for a consumer

# each city can have multiple Cinemas
# each Cinema will have multiple halls
# each movie will have many Shows and each Show will have multiple Bookings
# a user can have multiple Bookings
# system should be concurrent

Movie
Show
Theater
Cinema
Cinema_Hall
Seat
City
Booking
User

"""

from datetime import date
class Movie:
    def __init__(self, title, description, duration, language, release_date, country, genre):
        self.title = title
        self.description = description
        self.duration = duration
        self.language = language
        self.release_date = release_date
        self.country = country
        self.genre = genre

class Show:
    def __init__(self, date, start_time, end_time, cinema_hall_id, movie_id):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.cinema_hall_id = cinema_hall_id
        self.movie_id = movie_id

class City:
    def __init__(self, name, state, zipcode):
        self.city_id = None     # auto-generated
        self.name = name
        self.state = state
        self.zipcode = zipcode

class Cinema:
    def __init__(self, name, num_of_halls, location, city_id):
        self.name = name
        self.num_of_halls = num_of_halls
        self.location = location
        self.city = city_id

class CinemaHall:
    def __init__(self, name, total_seats, cinema_id):
        self.cinema_hall_id = None  # auto-generated
        self.total_seats = total_seats
        self.cinema_id = cinema_id

class Bookings:
    # booking seats in a cinema hall
    def __init__(self, num_of_seats, user_id, show_id, timestamp, status):
        self.booking_id = None      # auto-generated
        self.num_of_seats = num_of_seats
        self.user_id = user_id
        self.show_id = show_id
        self.timestamp = timestamp
        self.status = status

class Payments:
    def __init__(self, booking_id, amount, payment_method, discount_id, date):
        self.payment_id = None      # auto-generated
        self.booking_id = booking_id
        self.amount = amount
        self.payment_method = payment_method
        self.discount_id = discount_id
        self.date = date






