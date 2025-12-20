import requests
from bs4 import BeautifulSoup

# global variables = [white list of all the injectable fields]
# response parameters = {res_time, content_length, }
# base_line_parameters = {base_line_time, base_line_length, etc}
# dummy_data = {username, password, email, age, a static dictionary with generic form fields data}


def get_forms():
    # get the forms from the html page by first fetching it.
    # Only fields in the white list.
    # add them to input_fields dictionary which includes injectable fields from whitelist. 
    # return the input_fields dictionary.
    # For required fields -> required ? True : False.
    pass


# baseline response -> inject fields one at a time and compare the response with baseline response -> difference ? yes : no 
# function for the baseline dictionary generation
def base_response():
    # ṃake a initial request by getting all the injectable fields with actual dummy data from the dictionary 
    # Exract the injectable fields from this response along with there values and add themm to the baseline_dictionary.
    pass


def sql_injection():
    # input fields = []
    # one by one inject different payloads in the input fields.
    # return the responses per payload..
    pass


