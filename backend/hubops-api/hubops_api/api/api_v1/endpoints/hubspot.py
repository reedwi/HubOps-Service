from hubops_api.logger import get_logger
from fastapi import APIRouter, status
from hubops_api import supabase
import os
import requests

router = APIRouter(prefix='/hubspot')

logger = get_logger(__name__)

@router.get('/install', status_code=status.HTTP_201_CREATED)
def hubspot_install(code: str, state: str):
    data = {
        'grant_type': 'authorization_code',
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
        'redirect_uri': os.getenv('REDIRECT_URI'),
        'code': code
    }

    res = requests.post(
        url='https://api.hubapi.com/oauth/v1/token', 
        data=data,
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )

    try:
        portal_info = requests.get(
            url=f'https://api.hubapi.com/oauth/v1/access-tokens/{res.json()["access_token"]}',
            headers={'Content-Type': 'application/json'}
        )

    except:
        logger.error(f'Error getting access token on install of HubSpot App: {res.text}')
        return None
    
    try:
        portal_info = portal_info.json()
        from hubops_api.models.portals import Portal
        portal = Portal(
            portal_id=portal_info['hub_id'],
            portal_name=portal_info['hub_domain'],
            installer_email=portal_info['user'],
            access_token=res.json()['access_token'],
            refresh_token=res.json()['refresh_token'],
        )
        supabase.table('portals').insert(portal.dict(), returning='minimal').execute()
    except:
        logger.error(f'Error inserting portal into database: {portal_info}')
        return None
    
    try:
        from hubops_api.models.portals import PortalUser
        portal_user = PortalUser(
            portal_id=portal_info['hub_id'],
            user_id=state
        )
        supabase.table('portal_users').insert(portal_user.dict(), returning='minimal').execute()
    except:
        logger.error(f'Error inserting portal user into database: {portal_info}')
        return None
    
    return None