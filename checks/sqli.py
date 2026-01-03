import requests
from bs4 import BeautifulSoup

# global variables = [white list of all the injectable fields]
# response parameters = {res_time, content_length, }
# base_line_parameters = {base_line_time, base_line_length, etc}
# dummy_data = {username, password, email, age, a static dictionary with generic form fields data}


def get_forms():
    url = input("Enter the url: ")
    response = requests.get(url)
    form_text = response.text 
    print(form_text)
    return form_text


def parse_forms(text):
    """ Text refers to the text returned from the get_forms() function. """
    soup = BeautifulSoup(text, "html.parser")
    forms = soup.find_all("form")
    all_forms_data = [] 
    for form in forms:
        input_fields = form.find_all(['input', 'textarea', 'select'])
        form_data = []
        for field in input_fields:
            input_data = {
                "name": field.get('name'),
                "type":field.get("type"),
                "required":field.has_attr('required')
            }
            form_data.append(input_data)
        action = form.get('action')
        method = form.get('method')
        print(f'form {input} has action:{action} and method: {method}')
        form_data.append(action)
        form_data.append(method)
        all_forms_data.append(form_data)
    return all_forms_data



# baseline response -> inject fields one at a time and compare the response with baseline response -> difference ? yes : no 
# function for the baseline dictionary generation
def base_response():
    pass


def sql_injection():
    # input fields = []
    # one by one inject different payloads in the input fields.
    # return the responses per payload..
    pass


get_forms()