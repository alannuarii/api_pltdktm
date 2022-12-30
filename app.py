import hug
from controller.unit import Unit

# Instansiate Object 


@hug.response_middleware()
def process_data(request, response, resource):
    response.set_header("Access-Control-Allow-Origin", "*")

@hug.get('/') 
def hello_world():
    unit = Unit()
    result = unit.get_units()
    return result
