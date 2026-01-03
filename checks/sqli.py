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
    return form_text


def parse_forms(text):
    """ Text refers to the text returned from the get_forms() function. """
    soup = BeautifulSoup(text, "html.parser")
    forms = soup.find_all("form")
    all_form_data = []
    for form in forms:
        action = form.get('action')
        method = form.get('method')
        form_field = []
        input_fields = form.find_all(['input', 'textarea', 'submit'])
        for field in input_fields:
            input_data = {
                "name":field.get('name'),
                "required": field.has_attr('required'),
                "type": field.get('type'),
            }
            form_field.append(input_data)
        form_object = {
            "action": action,
            "method": method,
            "form_data": form_field
        }
        all_form_data.append(form_object)
    return all_form_data



# baseline response -> inject fields one at a time and compare the response with baseline response -> difference ? yes : no 
# function for the baseline dictionary generation
def base_response():

    pass


def sql_injection():
    # input fields = []
    # one by one inject different payloads in the input fields.
    # return the responses per payload..
    pass

form_text = get_forms()
form_data = parse_forms(form_text)
print(form_data)