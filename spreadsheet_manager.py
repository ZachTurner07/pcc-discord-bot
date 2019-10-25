import os
import re

from dotenv import load_dotenv

import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Spreadsheet_manager:

    def __init__(self):
        self.scope = ['https://spreadsheets.google.com/feeds' + ' ' +'https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', self.scope)
        self.gclient = gspread.authorize(self.creds)
        
        self.green_spreadsheet = self.gclient.open("Green League Match Statistics - Season 5")
        self.red_spreadsheet   = self.gclient.open("Red League Match Statistics - Season 5")
        self.blue_spreadsheet  = self.gclient.open("Blue League Match Statistics - Season 5")
