# -*- coding: utf-8 -*-
from oauth2client.client import flow_from_clientsecrets
import httplib2
from googleapiclient.discovery import build
from oauth2client.file import Storage
import webbrowser

def get_credentials():
    scope = 'https://www.googleapis.com/auth/blogger'
    flow = flow_from_clientsecrets(
        'client_id.json', scope,
        redirect_uri='urn:ietf:wg:oauth:2.0:oob')
    storage = Storage('credentials.dat')
    credentials = storage.get()

    if  not credentials or credentials.invalid:
        auth_uri = flow.step1_get_authorize_url()
        webbrowser.open(auth_uri)
        auth_code = 'ブラウザに表示された文字列をここに貼り付ける'
        credentials = flow.step2_exchange(auth_code)
        storage.put(credentials)
    return credentials

def get_service():
    """Returns an authorised blogger api service."""
    credentials = get_credentials()
    http = httplib2.Http()
    http = credentials.authorize(http)
    service = build('blogger', 'v3', http=http)
    return service

if __name__ == '__main__':
    served = get_service()
    blogs = served.blogs()
    blog_get_obj = blogs.get(blogId='ブログID')
    details = blog_get_obj.execute()
    print details