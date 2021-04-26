import logging

import azure.functions as func
from . import calculator


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    val1 = int(req.params.get('val1'))
    val2 = int(req.params.get('val2'))
    print('Proff of concept by Software Archicture')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}.\nSum of {val1} + {val2} = {calculator.sum_number(val1, val2)}\n Less of {val1} - {val2} = {calculator.less_number(val1, val2)}\n Div of {val1} / {val2} = {calculator.div_number(val1, val2)}\n Plus of {val1} x {val2} = {calculator.plus_number(val1, val2)}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
