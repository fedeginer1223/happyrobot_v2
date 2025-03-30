from flask import Blueprint, request, abort, Response, jsonify
from loguru import logger
import requests
import json
import redis

from services import validate_params

## Name of the route
ROUTE_NAME = 'clients'

# Create recommendations blueprint
clients_bp = Blueprint(ROUTE_NAME, __name__)

### Endpoints
# getting load information
@clients_bp.route('/get_info', methods=['GET'])
def get_client_info():
    """
    Retrieves client details given the inbound calling number.
    """
    # Read parameters
    params = request.args.to_dict()

    # Validate input parameters
    logger.info('Request to get load details. Validating params...')
    
    try:
        validate_params(params)
    except ValueError as e:
        logger.error(f'Error validating inputs: {e}')
        abort(400, description=f'Error validating inputs: {e}')
    
    logger.info('Params and Token validated successfully.')


    try:
        # Establishing connection with the database
        r = redis.Redis(
        host='redis-11037.c280.us-central1-2.gce.redns.redis-cloud.com',
        port=11037,
        decode_responses=True,
        username="default",
        password="krewkgFxukPnveGxrFQNscISVC1uNFXg",
        )

        print(f"number {params.get('phone_number')}")

        # Set variables
        phone_number  = params.get("phone_number").replace(" ","")

        # Get client
        print(f'client:{phone_number}')
        cliente = r.hgetall(f'client:{phone_number}')
        return jsonify(cliente)

    except Exception as e:
        abort(404, description=f'The referenced value has not been found')

# getting carrier information
@clients_bp.route('/update_info', methods=['GET'])
def update_client_info():
    """
    Returns carrier information
    """
    # Read parameters
    params = request.args.to_dict()

    # Validate input parameters
    logger.info('Request to get load details. Validating params...')
    
    try:
        validate_params(params)
    except ValueError as e:
        logger.error(f'Error validating inputs: {e}')
        abort(400, description=f'Error validating inputs: {e}')
    
    logger.info('Params and Token validated successfully.')


    try:
        # Establishing connection with the database
        r = redis.Redis(
        host='redis-11037.c280.us-central1-2.gce.redns.redis-cloud.com',
        port=11037,
        decode_responses=True,
        username="default",
        password="krewkgFxukPnveGxrFQNscISVC1uNFXg",
        )

        # Set variables
        phone_number  = params.get("phone_number").replace(" ","")
        communication = params.get("recall_communicated")
        notes = params.get("notes")

        # Set value of a hash
        r.hset(f'client:{phone_number}', 'recall_communicated', f'{communication}')
        r.hset(f'client:{phone_number}', 'notes', f'{notes}')
        return jsonify({"Client info updated"})

    except Exception as e:
        abort(404, description=f'The referenced value has not been found')