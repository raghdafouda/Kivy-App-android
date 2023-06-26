## Raghda Fouda    
#  Imports
from datetime import date
import mimetypes
from kivymd.app import MDApp
from email.message import EmailMessage
import smtplib
from smtplib import *
import ssl
import email
from tkinter import filedialog
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, ColorProperty, ListProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.imagelist import imagelist
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp
import mysql.connector
import webbrowser
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.uix.filemanager import MDFileManager
from kivymd.theming import ThemableBehavior 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivymd.toast import toast
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
import os.path
import sys
import subprocess
import io
import random
from kivy.resources import resource_add_path, resource_find
import os

#  minus_img = "./images/minus.png" # <-- this doesn't work

root = os.path.dirname(__file__)
minus_img = os.path.join(root, "media", "intro.png",)
 
# final path 
#######################################################
app_path=sys.path[0].split('\\')
# del app_path[-1]
final_path=''
for i in app_path:
    final_path=final_path+i+'\\'
try:
    os.mkdir(final_path+'whatsapp_data')
except:
    pass
   
# window size
Window.size = (500, 600)
#########################################################
# kivy language
KV = """
<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#0a1640"
    icon_color: "#FFFFFF"
    focus_behavior: False
    selected_color: "#0a1640"
    _no_ripple_effect: True

<MyOption@SpinnerOption>:
    font_size: 12


<MyNewApp>:
# Intro Screen (Sign in)
    Screen:
        name: "Intro"
        id: signin
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'images/intro.png'
        MDCard:
            size_hint: None, None
            size: 250, 380
            pos_hint: {"center_x":.5, "center_y":.45}
            elevation: 15
            md_bg_color: "#E8B010"
            padding: 15
            spacing: 10
            orientation: "vertical"
            MDFloatLayout:
                MDLabel:
                    text: "Sign in to your account"
                    font_style: "Caption"
                    bold: True
                    font_size: 20
                    color: "white" 
                    halign: "center"
                    size_hint_y: .5
                    pos_hint:{"center_x": .50, "center_y": .95}
                    height: self.texture_size[1]
                    padding_y: 15
                MDLabel:
                    text: "Enter your email and password"
                    font_style: "Caption"
                    font_size: 12
                    color: "white" 
                    halign: "center"
                    size_hint_y: .5
                    pos_hint:{"center_x": .51, "center_y": .87}    
                MDTextField:
                    id: email1
                    hint_text: "Email"
                    line_color_focus: (1, 1, 1, 1)
                    size_hint_x: None
                    width: 220
                    pos_hint:{"center_x": .50, "center_y": .72}
                    color_active: [1,1,1,1]
                MDTextField:
                    id: password
                    hint_text: "Password"
                    line_color_focus: (1, 1, 1, 1)
                    size_hint_x: None
                    width: 220
                    pos_hint:{"center_x": .5, "center_y": .54}
                    password: True
                    color_active: [1,1,1,1]
                MDCheckbox:
                    size_hint: None, None
                    size: "48dp" , "48dp"
                    pos_hint: {"center_x": .05, "center_y": .4}
                    on_active: root.show_password(*args)
                MDLabel:
                    id: password_text
                    text: "Show Password"
                    pos_hint: {"center_x": .6, "center_y": .4}
                MDFillRoundFlatButton:
                    text: 'Log in'
                    text_color: "white"
                    md_bg_color: (27/255, 39/255, 71/255, 1)
                    font_size: 16
                    pos_hint:{"center_x": .50, "center_y": .28}
                    size_hint_x: 0.8
                    size_hint_y: 0.07
                    on_release: 
                        root.connect()
                        root.add_products()
                MDLabel:
                    text: "Don't have an account?"
                    font_style: "Body1"
                    font_size: 14
                    color: "black" 
                    pos_hint:{"center_x": .5, "center_y": .12}
                MDTextButton:
                    text: "Sign up"
                    bold: True
                    color: (27/255, 39/255, 71/255, 1)
                    font_size: 14    
                    pos_hint:{"center_x": .78, "center_y": .12}
                    on_release:
                        root.current = 'Signup'
                        root.transition.direction = 'left'
    # Sign up Screen
    Screen:
        name: "Signup"
        MDBoxLayout:
            orientation: "vertical"
            size: root.width, root.height
            padding: 5
            MDTopAppBar:
                id: topbar
                title:"Sign Up"
                md_bg_color:(202/255, 125/255, 0/255, 1)
                left_action_items: [["chevron-left", lambda x : root.get_intro('Intro')]]
            MDFloatLayout:
                MDLabel:
                    text: "Create new Account"
                    font_style: 'H4'
                    font_size: 22
                    bold: True
                    pos_hint:{"center_x": .53, "center_y": .94}
                TextInput:
                    id: email
                    hint_text: "Email"
                    icon_right: "email"
                    width: 180
                    size_hint: (.67, .06)
                    pos_hint:{"center_x": .36,  "center_y": .85}
                    multiline: False 
                TextInput:
                    id: passwd
                    hint_text: "Password"
                    icon_right: "eye-off"
                    width: 180
                    size_hint: (.67, .06)
                    bold: True
                    pos_hint:{"center_x": .36, "center_y": .75}
                    multiline: False
                TextInput:
                    id: phone
                    hint_text: "Phone"
                    icon_right: "phone"
                    size_hint: (.67, .06)
                    pos_hint:{"center_x": .36, "center_y": .65}
                    multiline: False
                TextInput:
                    id: whats
                    hint_text: "WhatsApp"
                    icon_right: "whatsapp"
                    size_hint: (.67, .06)
                    pos_hint:{"center_x": .36, "center_y": .54}
                    multiline: False
                TextInput:
                    id: country
                    hint_text: "Country"
                    icon_right: "map-marker"
                    size_hint: (.67, .06)
                    pos_hint:{"center_x": .36, "center_y": .45}
                    multiline: False
                MDLabel:
                    text: "Business Type"
                    font_style: 'H4'
                    font_size: 16
                    bold: True
                    pos_hint:{"center_x": .53, "center_y": .36}    
                Spinner:
                    id: usertype
                    size_hint: (.3, 0.06)
                    pos_hint:{"center_x": .5, "center_y": .36}
                    text: 'select'
                    values: ["Exporter", "Importer", "Service Provider"]
                TextInput:
                    id: category
                    hint_text: "Category"
                    size_hint: (.67, .06)
                    mode: "round"
                    pos_hint:{"center_x": .36, "center_y": .27} 
                    multiline: False 
                TextInput:
                    id: signup_product
                    hint_text: "Enter Product"
                    size_hint: (.5, .06)
                    mode: "round"
                    pos_hint:{"center_x": .28, "center_y": .175} 
                    multiline: False
                MDRaisedButton:
                    text: "Add"
                    pos_hint: {"center_x": .62, "center_y": .175}
                    size_hint: (.05, .05)
                    on_release:
                        root.add_signup_pro()
                Spinner:
                    id: signup_pro_sp
                    text: "Added Products"
                    values: [""]
                    pos_hint: {"center_x": .85, "center_y": .175}
                    size_hint: (.3, 0.06)
                MDFillRoundFlatButton:
                    text: 'Sign up'
                    text_color: (1, 1, 1, 1)
                    font_size: 18
                    bold: True
                    size_hint_x: 0.3
                    size_hint_y: 0.07
                    pos_hint: {"center_x": .49, "center_y": .06}
                    md_bg_color:(202/255, 125/255, 0/255, 1)
                    on_release: 
                        root.save()
    # Main Screen 
    Screen:
        name: "Main"
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'images/main.jpg'
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            md_bg_color:"#0a1640"
                            elevation: 8
                            left_action_items: [['menu', lambda x: nav_drawer.set_state("toggle")]]
                            right_action_items: [['logout', lambda x : root.logout_user('Intro')]]
                        MDFloatLayout:
            MDNavigationDrawer:
                id: nav_drawer
                elevation: 0
                md_bg_color: "#B3B6B7"
                MDNavigationDrawerMenu:
                    orientation: "vertical"
                    padding: "8dp"
                    spacing: "8dp"
                    AnchorLayout:
                        anchor_x: "left"
                        size_hint_y: None
                        height: avatar.height

                        Image:
                            id: avatar
                            width: 100
                            allow_stretch: True
                            source: "images/logo.png"

                    MDNavigationDrawerLabel:
                        text: "info@e-markets.org"
                        font_style: "Button"
                        font_size: 22
                        
                    MDNavigationDrawerLabel:
                        text: "Trade"
                    DrawerLabelItem:
                        id: export_nav
                        icon: "export"
                        text: "Export your product"
                        on_release:
                            root.transition.direction = 'left'
                            root.current = 'exporterdb' # Exporter Database Screen 
                    DrawerLabelItem:
                        id: import_nav
                        icon: "database-import"
                        text: "Import your product"
                        on_release:
                            root.transition.direction = 'left'
                            root.current = 'importerdb'
                            root.add_expproduct()
                    MDNavigationDrawerDivider:
                    MDNavigationDrawerLabel:
                        text: "Logistics"
                    DrawerLabelItem:
                        id: service_provider_nav
                        icon: "truck-cargo-container"
                        text: "Service Provider"
                        on_release: root.load_servtable()
                    MDNavigationDrawerDivider:
                    MDNavigationDrawerLabel:
                        text: "Deals"
                    DrawerLabelItem:
                        id: export_opp_nav
                        icon: "gesture-tap-box"
                        text: "Export Opportunity"
                        on_release:
                            root.transition.direction = 'left'
                            root.current = 'expopportunity' # Export Opportunity Screen 
                            root.get_exp_product()
                    DrawerLabelItem:
                        id: import_opp_nav
                        icon: "gesture-tap-box"
                        text: "import Opportunity"
                        on_release:
                            root.transition.direction = 'left'
                            root.current = 'impopportunity' #Import Opportunity Screen 
                            root.get_imp_product()
                    MDNavigationDrawerDivider:
                    MDNavigationDrawerLabel:
                        text: "Go to website"
                    DrawerLabelItem:
                        icon: "web"
                        text: "Egypte-market Website"
                        on_release: root.openweb()
                    MDNavigationDrawerDivider:
                    MDNavigationDrawerLabel:
                        text: "Who are you"
                    DrawerLabelItem:
                        icon: "information"
                        text: "About us"
                        on_release:
                            root.transition.direction = 'left'
                            root.current = 'about'   # About Us Screen 
                    DrawerLabelItem:
                        icon: "card-account-phone"
                        text: "Contact us"
                        on_release:
                            root.transition.direction = 'left'
                            root.current = 'contact'  # Contact Us Screen 
   
    # Screen About Us            
    Screen: 
        name: "about"
        MDFloatLayout:
            Image:
                source: 'images/company.jpg'
                keep_ratio: False
                allow_stretch: True
                opacity: 0.8
                size_hint: None, None
                size: 500, 100
                pos_hint: { 'y': 0.83}
                MDIconButton:
                    icon: "arrow-left-bold-circle"
                    theme_icon_color: "Custom"
                    icon_color: 1, 1, 1, 1
                    pos_hint: {"y": 0.83} 
                    on_release: 
                        root.get_main('Main')  
            MDLabel:
                text: "Our Company"
                font_style: 'H4'
                font_size: 20
                bold: True
                pos_hint:{"center_x": .53, "center_y": .79}
            MDLabel:
                text: "Global digital market and structural database for management\\ntrade excharge between countries based on AI"
                font_style: 'Subtitle2'
                font_size: 16
                bold: True
                pos_hint:{"center_x": .58, "center_y": .72}    
            MDLabel:
                text: "Our Team"
                font_style: 'H4'
                font_size: 20
                bold: True
                pos_hint:{"center_x": .53, "center_y": .63}
            MDLabel:
                text: "Experts in international marketing & export\\nmanagement and professional team in technology"
                font_style: 'Subtitle2'
                font_size: 16
                bold: True
                pos_hint:{"center_x": .58, "center_y": .56}
            MDLabel:
                text: "Our Vision"
                font_style: 'H4'
                font_size: 20
                bold: True
                pos_hint:{"center_x": .53, "center_y": .47}
            MDLabel:
                text: "Optimum utilization of commercial data of each country\\nto make ideal and smart trade exchange management."
                font_style: 'Subtitle2'
                font_size: 18
                bold: True
                pos_hint:{"center_x": .58, "center_y": .40}
            MDLabel:
                text: "Our Mission"
                font_style: 'H4'
                font_size: 20
                bold: True
                pos_hint:{"center_x": .53, "center_y": .30}
            MDLabel:
                text: "Specialized platform (B2B) E-commerce specialized\\ncommercial database for each country."
                font_style: 'Subtitle2'
                font_size: 16
                bold: True
                pos_hint:{"center_x": .58, "center_y": .24}
    # Screen Contact Us            
    Screen: 
        name: "contact"
        MDFloatLayout:
            Image:
                source: 'images/contact.jpg'
                keep_ratio: False
                allow_stretch: True
                opacity: 0.8
                size_hint: None, None
                size: 500, 100
                pos_hint: { 'y': 0.83}
                MDIconButton:
                    icon: "arrow-left-bold-circle"
                    theme_icon_color: "Custom"
                    icon_color: 1, 1, 1, 1
                    pos_hint: {"y": 0.83} 
                    on_release: 
                        root.get_main('Main')
            MDFloatLayout:
                size_hint: .5, 0.7
                pos_hint: {'x': .02, 'y': 0.1}
                canvas:
                    Color:
                        rgb: 0, 0, 0, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [6]
                canvas.before:
                    Color:
                        rgb: 230/255, 230/255, 230/255, 1
                    Line:
                        width: 2
                        rounded_rectangle: self.x, self.y, self.width, self.height, 6, 6, 6, 6, 100 
                MDLabel:
                    text: "Leave us a message"
                    font_style: 'Subtitle2'
                    font_size: 18
                    bold: True
                    pos_hint:{"x": .12, "y": .44}
                TextInput:
                    id: contact_email
                    hint_text: "Email"
                    size_hint: .9, None
                    pos_hint: {"x": .03, "y": .78}
                    height: self.minimum_height
                    multiline: False
                    font_style: "Poppins"
                    font_size: "18sp"
                    hint_text_color: 170/255, 170/255, 170/255, 1
                    padding: 6
                    cursor_color: 0, 0, 0, 1
                TextInput:
                    id: contact_passwd
                    hint_text: "Password"
                    password: True
                    size_hint: .9, None
                    pos_hint: {"x": .03, "y": .65}
                    height: self.minimum_height
                    multiline: False
                    font_style: "Poppins"
                    font_size: "18sp"
                    hint_text_color: 170/255, 170/255, 170/255, 1
                    padding: 6
                    cursor_color: 0, 0, 0, 1
                TextInput:
                    id: contact_msg
                    hint_text: "Message"
                    size_hint: .9, .4
                    pos_hint: {"x": .03, "y": .2}
                    height: self.minimum_height
                    multiline: True
                    font_style: "Poppins"
                    font_size: "18sp"
                    hint_text_color: 170/255, 170/255, 170/255, 1
                    padding: 6
                    cursor_color: 0, 0, 0, 1
                MDFillRoundFlatButton:
                    text: "Send"
                    halign: 'center'
                    valign: 'bottom'
                    text_color: 0, 0, 0, 1
                    font_size: 16
                    size_hint_x: 0.4
                    size_hint_y: 0.07
                    pos_hint: {"x": .3, "y": .08}
                    md_bg_color: 1, 1, 1, 1
                    on_release:
                        root.contact()
            MDLabel:
                text: "Egypt"
                font_style: 'H3'
                underline: True
                font_size: 24
                bold: True
                pos_hint:{"x": .7, "y": .25}
            MDLabel:
                text: "Address: 45 Kambiz Street, Ad Doqi,\\nGiza District, Giza Governorate 12311"
                font_style: 'Subtitle1'
                font_size: 14
                bold: True
                pos_hint:{"x": .55, "y": .15}
            MDLabel:
                text: "Email: info@e-markets.org"
                font_style: 'Subtitle1'
                font_size: 14
                bold: True
                pos_hint:{"x": .55, "y": .09} 
            MDLabel:
                text: "Mobile: +201211766667"
                font_style: 'Subtitle1'
                font_size: 14
                bold: True
                pos_hint:{"x": .55, "y": .04} 
    # Screen Exporter Database
    Screen:
        name: "exporterdb"                                   
        MDBoxLayout:
            orientation: "vertical"
            size: root.width, root.height
            spacing: 20
            padding: 5
            MDTopAppBar:
                id: topbar
                title: "Database"
                md_bg_color: (202/255, 125/255, 0/255, 1)
                left_action_items: [["chevron-left", lambda x : root.get_main('Main')]]
            MDFloatLayout:
                MDLabel:
                    text: "Country"
                    font_style: 'Subtitle2'
                    font_size: 20
                    bold: True
                    pos_hint:{"center_x": .55, "center_y": .94}
                Spinner:
                    size_hint: (.6, 0.06)
                    pos_hint: {"center_x": 0.65, "center_y": 0.95}
                    background_normal: ''
                    background_color: 1, 1, 1, 1  # white
                    color: 0, 0, 0, 1
                    text: 'Egypt'
                #    values: 'Egypt',
                MDLabel:
                    text: "Product Name"
                    font_style: 'Subtitle2'
                    font_size: 20
                    bold: True
                    pos_hint:{"center_x": .55, "center_y": .84}
                Spinner:
                    id: pro_spinner
                    pos_hint: {"center_x": 0.65, "center_y": 0.85}
                    background_normal: ''
                    background_color: 1, 1, 1, 1  # white
                    color: 0, 0, 0, 1
                    text: 'Select product'
                    option_cls: "MyOption"
                    values: [""]
                    size_hint: (.6, 0.06)
                    height: 50
                    font_size: 12
                    on_text:
                        root.add_hscode(self.text)
                        root.add_market(self.text)
                MDLabel:
                    text: "HS Code"
                    font_style: 'Subtitle2'
                    font_size: 20
                    bold: True
                    pos_hint: {"center_x": .55, "center_y": .74}
                Spinner:
                    id: code_sp
                    size_hint: (.6, 0.06)
                    pos_hint: {"center_x": 0.65, "center_y": 0.75}
                    background_normal: ''
                    background_color: 1, 1, 1, 1  # white
                    color: 0, 0, 0, 1
                    font_size: 12
                    text: "Hscode"
                MDLabel:
                    text: "Target Market"
                    font_style: 'Subtitle2'
                    font_size: 20
                    bold: True
                    pos_hint: {"center_x": .55, "center_y": .64}    
                Spinner:
                    id: market_sp 
                    size_hint: (.6, 0.06)
                    pos_hint:{"center_x": .65, "center_y": .65}
                    background_normal: ''
                    background_color: 1, 1, 1, 1  # white
                    color: 0, 0, 0, 1
                    font_size: 14
                    text: "Select market"
                    values: [""]
                MDFillRoundFlatButton:
                    text: 'Importers List'
                    text_color: "white"
                    md_bg_color:(202/255, 125/255, 0/255, 1)
                    font_size: 16
                    pos_hint: {"center_x": 0.2, "center_y": 0.45}
                    on_release:
                        root.load_imptable()
                        root.add_improw()
                        root.get_emails()
                        root.get_whatsapp()

                MDFillRoundFlatButton:
                    text: 'Market Analysis'
                    text_color: "white"
                    md_bg_color:(202/255, 125/255, 0/255, 1)
                    font_size: 16
                    pos_hint: {"center_x": 0.2, "center_y": 0.30}
                    on_release:
                        root.load_markettable()

                MDFillRoundFlatButton:
                    text: 'Marketing Plan'
                    text_color: "white"
                    md_bg_color:(202/255, 125/255, 0/255, 1)
                    font_size: 16
                    pos_hint: {"center_x": 0.2, "center_y": 0.15}
                    on_release:
                        root.check_marketplan()
    # Screen Importer List      
    Screen:
        name: "importer"
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                id: topbar
                title: "Customers List"
                md_bg_color: app.theme_cls.bg_dark
                left_action_items: [["chevron-left", lambda x : root.get_screenexporterdb("exporterdb")]]
            MDTabs:
                id:tabs
                on_tab_switch: root.on_tab_switch(*args)
                Tab:
                    id: importers_tab
                    title: "Importers"
                
                Tab:
                    title: "Send Email"
                    MDFloatLayout:
                        TextInput:
                            id: email_from
                            hint_text: "From"
                            mode: "rectangle"
                            multiline: False
                            pos_hint:{"x": .05, "y": .88}
                            size_hint: 0.4, 0.07
                        TextInput:
                            id: email_passwd
                            hint_text: "Password"
                            mode: "rectangle"
                            password: True
                            multiline: False
                            pos_hint:{"x": .55, "y": .88}
                            size_hint: 0.4, 0.07
                        Spinner:
                            id: email_to_list
                            background_normal: ''
                            background_color: 1, 1, 1, 1  # white
                            color: 0, 0, 0, 1
                            mode: "rectangle"
                            pos_hint:{"x": .05, "y": .78}
                            size_hint: 0.90, 0.07
                            value: [""]
                        TextInput:
                            id: email_subject
                            hint_text: "Subject"
                            mode: "rectangle"
                            multiline: False
                            pos_hint:{"x": .05, "y": .68}
                            size_hint: 0.90, 0.07
                        TextInput:
                            id: email_msg
                            hint_text: "Message"
                            multiline: True
                            mode: "rectangle"
                            pos_hint:{"x": .05, "y": .26}
                            size_hint: 0.9, 0.4
                        MDRoundFlatIconButton:
                            text: "Attach files"
                            icon: "paperclip"
                            pos_hint: {'x': .05, 'center_y': .2} 
                            on_release: root.attach_files()

                        TextInput:
                            id: attach_box
                            hint_text: "Files"
                            multiline: True
                            mode: "rectangle"
                            pos_hint:{"center_x": .57, "center_y": .185}
                            size_hint: 0.5, 0.13

                        MDFillRoundFlatButton:
                            text: 'Send'
                            text_color: "white"
                            md_bg_color:(202/255, 125/255, 0/255, 1)
                            font_size: 16
                            size_hint_x: 0.5
                            size_hint_y: 0.07
                            pos_hint: {"center_x": 0.5, "center_y": 0.05}
                            on_release: root.send_email()
                Tab:
                    title: "Send WhatsApp"
                    MDFloatLayout:
                        Spinner:
                            id: whatsapp_to_list
                            background_normal: ''
                            background_color: 1, 1, 1, 1  # white
                            color: 0, 0, 0, 1
                            mode: "rectangle"
                            pos_hint:{"x": .05, "y": .85}
                            size_hint: 0.90, 0.07
                            values: [""]

                        TextInput:
                            id: whatsapp_msg
                            hint_text: "Message"
                            multiline: True
                            mode: "rectangle"
                            pos_hint:{"x": .05, "y": .4}
                            size_hint: 0.9, 0.4
                            
                        MDFillRoundFlatButton:
                            text: 'Send'
                            text_color: "white"
                            md_bg_color:(202/255, 125/255, 0/255, 1)
                            font_size: 16
                            size_hint_x: 0.2
                            size_hint_y: 0.07
                            pos_hint: {"center_x": 0.3, "center_y": 0.23}
                            on_release: root.send_whatsapp()

                        MDFillRoundFlatButton:
                            text: 'Send All'
                            text_color: "white"
                            md_bg_color:(202/255, 125/255, 0/255, 1)
                            font_size: 16
                            size_hint_x: 0.2
                            size_hint_y: 0.07
                            pos_hint: {"center_x": 0.6, "center_y": 0.23}
                            on_release: root.send_all_whatsapp()

    # Screen Market analysis for exporter                         
    Screen:
        name: "marketanalysis" 
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                id: topbar
                title: "Market Analysis"
                md_bg_color: app.theme_cls.bg_dark
                left_action_items: [["chevron-left", lambda x : root.get_screenexporterdb('exporterdb')]]
            MDTabs:
                id:tabs
                on_tab_switch: root.on_tab_switch(*args)
                Tab:
                    title: "Competitive"
                    TwoLineListItem:
                        id: market_name_tab
                        text: "Market Name"
                        secondary_text: ""
                        pos_hint: {"center_x": 0.5, "center_y": 0.9}
                    TwoLineListItem:
                        id: market_total_imports_tab
                        text: "Market total imports"
                        secondary_text: ""
                        pos_hint: {"center_x": 0.5, "center_y": 0.75}  
                    TwoLineListItem:
                        id: egypt_total_exports_tab
                        text: "Egypt total exports"
                        secondary_text: ""
                        pos_hint: {"center_x": 0.5, "center_y": 0.6}
                    TwoLineListItem:
                        id: competing_country_tab
                        text: "Competing country"
                        secondary_text: ""
                        pos_hint: {"center_x": 0.5, "center_y": 0.45} 
                    TwoLineListItem:
                        id: competitive_country_exports_tab
                        text: "Competitive country exports"
                        secondary_text: ""
                        pos_hint: {"center_x": 0.5, "center_y": 0.3}            
                Tab:
                    title: "PESTLE"
                    MDLabel:
                        text: "Political"
                        pos_hint: {"center_x": .55, "center_y": .9}
                        font_size: "18"
                        bold: True

                    MDLabel:
                        text: "Economic"
                        pos_hint: {"center_x": .55, "center_y": .75}
                        font_size: "18"
                        bold: True

                    MDLabel:
                        text: "Social"
                        pos_hint: {"center_x": .55, "center_y": .6}
                        font_size: "18"
                        bold: True

                    MDLabel:
                        text: "Technological"
                        pos_hint: {"center_x": .55, "center_y": .45}
                        font_size: "18"
                        bold: True

                    MDLabel:
                        text: "Legal"
                        pos_hint: {"center_x": .55, "center_y": .3}
                        font_size: "18"
                        bold: True

                    MDLabel:
                        text: "Environmental"
                        pos_hint: {"center_x": .55, "center_y": .15}
                        font_size: "18"
                        bold: True

                    MDRaisedButton:
                        text: "Show Report"
                        pos_hint: {"center_x": .65, "center_y":.9}
                        bold: True
                        size_hint: (.3, .05)
                        on_release: root.show_political_dialog()

                    MDRaisedButton:
                        text: "Show Report"
                        pos_hint: {"center_x": .65, "center_y":.75}
                        bold: True
                        size_hint: (.3, .05)
                        on_release: root.show_economic_dialog()

                    MDRaisedButton:
                        text: "Show Report"
                        pos_hint: {"center_x": .65, "center_y":.6}
                        bold: True
                        size_hint: (.3, .05)
                        on_release: root.show_social_dialog()

                    MDRaisedButton:
                        text: "Show Report"
                        pos_hint: {"center_x": .65, "center_y":.45}
                        bold: True
                        size_hint: (.3, .05)
                        on_release: root.show_tech_dialog()

                    MDRaisedButton:
                        text: "Show Report"
                        pos_hint: {"center_x": .65, "center_y":.3}
                        bold: True
                        size_hint: (.3, .05)
                        on_release: root.show_legal_dialog()

                    MDRaisedButton:
                        text: "Show Report"
                        pos_hint: {"center_x": .65, "center_y":.15}
                        bold: True
                        size_hint: (.3, .05)
                        on_release: root.show_env_dialog()

                Tab:
                    title: "SWOT"
                    MDLabel:
                        text: "Strenghts"
                        pos_hint: {"center_x": .55, "center_y": .85}
                        font_size: "18"
                        bold: True

                    MDLabel:
                        text: "Weakness"
                        pos_hint: {"center_x": .55, "center_y": .65}
                        font_size: "18"
                        bold: True

                    MDLabel:
                        text: "Opportunities"
                        pos_hint: {"center_x": .55, "center_y": .45}
                        font_size: "18"
                        bold: True

                    MDLabel:
                        text: "Threats"
                        pos_hint: {"center_x": .55, "center_y": .25}
                        font_size: "18"
                        bold: True

                    MDRaisedButton:
                        text: "Show Report"
                        pos_hint: {"center_x": .65, "center_y":.85}
                        bold: True
                        size_hint: (.3, .05)
                        on_release: root.show_strenghts()

                    MDRaisedButton:
                        text: "Show Report"
                        pos_hint: {"center_x": .65, "center_y":.65}
                        bold: True
                        size_hint: (.3, .05)
                        on_release: root.show_weakness()

                    MDRaisedButton:
                        text: "Show Report"
                        pos_hint: {"center_x": .65, "center_y":.45}
                        bold: True
                        size_hint: (.3, .05)
                        on_release: root.show_opportunities()

                    MDRaisedButton:
                        text: "Show Report"
                        pos_hint: {"center_x": .65, "center_y":.25}
                        bold: True
                        size_hint: (.3, .05)
                        on_release: root.show_threats()

    # Screen Market Plan for Exporter
    Screen:
        name: "marketplan"
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                id: topbar
                title: "Marketing Plan"
                md_bg_color: app.theme_cls.bg_dark
                left_action_items: [["chevron-left", lambda x : root.get_screenexporterdb('exporterdb')]]
            MDTabs:
                id:tabs
                on_tab_switch: root.on_tab_switch(*args)
                Tab:
                    title: "4Ps"
                    MDLabel:
                        text: "Product"
                        pos_hint: {"center_x": .55, "center_y": .85}
                        font_size: "18"
                        bold: True

                    MDLabel:
                        text: "Promotion"
                        pos_hint: {"center_x": .55, "center_y": .65}
                        font_size: "18"
                        bold: True

                    MDLabel:
                        text: "Price"
                        pos_hint: {"center_x": .55, "center_y": .45}
                        font_size: "18"
                        bold: True

                    MDLabel:
                        text: "Place"
                        pos_hint: {"center_x": .55, "center_y": .25}
                        font_size: "18"
                        bold: True

                    MDRaisedButton:
                        text: "Show Report"
                        pos_hint: {"center_x": .65, "center_y":.85}
                        bold: True
                        size_hint: (.3, .05)
                        on_release: root.show_product()

                    MDRaisedButton:
                        text: "Show Report"
                        pos_hint: {"center_x": .65, "center_y":.65}
                        bold: True
                        size_hint: (.3, .05)
                        on_release: root.show_promotion()

                    MDRaisedButton:
                        text: "Show Report"
                        pos_hint: {"center_x": .65, "center_y":.45}
                        bold: True
                        size_hint: (.3, .05)
                        on_release: root.show_Price()

                    MDRaisedButton:
                        text: "Show Report"
                        pos_hint: {"center_x": .65, "center_y":.25}
                        bold: True
                        size_hint: (.3, .05)
                        on_release: root.show_place()
                Tab:
                    title: "Requirements"
                    MDLabel:
                        text: "Product Requirements"
                        pos_hint: {"center_x": .55, "center_y": .7}
                        font_size: "18"
                        bold: True

                    MDRaisedButton:
                        text: "Show Report"
                        pos_hint: {"center_x": .65, "center_y":.7}
                        bold: True
                        size_hint: (.3, .05)
                        on_release: root.show_req_data()

    # Screen Importer Database                     
    Screen: 
        name: "importerdb"
        MDBoxLayout:
            orientation: "vertical"
            size: root.width, root.height
            spacing: 20
            padding: 5
            MDTopAppBar:
                id: topbar
                title: "Database"
                md_bg_color: (202/255, 125/255, 0/255, 1)
                left_action_items: [["chevron-left", lambda x : root.get_main('Main')]]
            MDFloatLayout:
                MDLabel:
                    text: "Country"
                    font_style: 'Subtitle2'
                    font_size: 20
                    bold: True
                    pos_hint:{"center_x": .55, "center_y": .9}
                Spinner:
                    size_hint: (.6, 0.06)
                    pos_hint: {"center_x": 0.65, "center_y": 0.91}
                    background_normal: ''
                    background_color: 1, 1, 1, 1  # white
                    color: 0, 0, 0, 1
                    text: 'Egypt'
                MDLabel:
                    text: "Product Name"
                    font_style: 'Subtitle2'
                    font_size: 20
                    bold: True
                    pos_hint:{"center_x": .55, "center_y": .8}
                Spinner:
                    id: exppro_spinner
                    pos_hint: {"center_x": 0.65, "center_y": 0.81}
                    background_normal: ''
                    background_color: 1, 1, 1, 1  # white
                    color: 0, 0, 0, 1
                    text: 'Select product'
                    option_cls: "MyOption"
                    values: [""]
                    size_hint: (.6, 0.06)
                    height: 50
                    font_size: 12
                    on_text:
                        root.add_exphscode(self.text)
                MDLabel:
                    text: "HS Code"
                    font_style: 'Subtitle2'
                    font_size: 20
                    bold: True
                    pos_hint: {"center_x": .55, "center_y": .7}
                Spinner:
                    id: expcode_sp
                    size_hint: (.6, 0.06)
                    pos_hint: {"center_x": 0.65, "center_y": 0.71}
                    background_normal: ''
                    background_color: 1, 1, 1, 1  # white
                    color: 0, 0, 0, 1
                    font_size: 12
                    text: "Hscode"
                MDFillRoundFlatButton:
                    text: 'Exporters List'
                    text_color: "white"
                    md_bg_color:(202/255, 125/255, 0/255, 1)
                    font_size: 16
                    size_hint: .4, .07
                    pos_hint: {"center_x": 0.65, "center_y": 0.45}
                    on_release:
                        root.load_exptable()
                        root.get_exp_emails()
                        root.get_whatsappexp()
    # Screen Exporter List                    
    Screen:
        name: "exporter"
        MDBoxLayout:
            orientation: "vertical"
            size: root.width, root.height
            MDTopAppBar:
                id: topbar
                title: "Exporters"
                md_bg_color: app.theme_cls.bg_dark
                left_action_items: [["chevron-left", lambda x : root.get_screendataexp('importerdb')]]                        
            MDTabs:
                Tab:
                    id: exporter_tab
                    title: "Exporter List"

                Tab:
                    title: "Send Email"
                    MDFloatLayout:
                        TextInput:
                            id: emailexp_from
                            hint_text: "From"
                            mode: "rectangle"
                            multiline: False
                            pos_hint:{"x": .05, "y": .88}
                            size_hint: 0.4, 0.07
                        TextInput:
                            id: emailexp_passwd
                            hint_text: "Password"
                            mode: "rectangle"
                            password: True
                            multiline: False
                            pos_hint:{"x": .55, "y": .88}
                            size_hint: 0.4, 0.07
                        Spinner:
                            id: emailexp_to_list
                            background_normal: ''
                            background_color: 1, 1, 1, 1  # white
                            color: 0, 0, 0, 1
                            mode: "rectangle"
                            pos_hint:{"x": .05, "y": .78}
                            size_hint: 0.90, 0.07
                            value: [""]
                        TextInput:
                            id: emailexp_subject
                            hint_text: "Subject"
                            mode: "rectangle"
                            multiline: False
                            pos_hint:{"x": .05, "y": .68}
                            size_hint: 0.90, 0.07
                        TextInput:
                            id: emailexp_msg
                            hint_text: "Message"
                            multiline: True
                            mode: "rectangle"
                            pos_hint:{"x": .05, "y": .26}
                            size_hint: 0.9, 0.4
                        MDRoundFlatIconButton:
                            text: "Attach files"
                            icon: "paperclip"
                            pos_hint: {'x': .05, 'center_y': .2} 
                            on_release: root.attach_exp_files()

                        TextInput:
                            id: attachexp_box
                            hint_text: "Files"
                            multiline: True
                            mode: "rectangle"
                            pos_hint:{"center_x": .57, "center_y": .185}
                            size_hint: 0.5, 0.13

                        MDFillRoundFlatButton:
                            text: 'Send'
                            text_color: "white"
                            md_bg_color:(202/255, 125/255, 0/255, 1)
                            font_size: 16
                            size_hint_x: 0.5
                            size_hint_y: 0.07
                            pos_hint: {"center_x": 0.5, "center_y": 0.05}
                            on_release: root.send_emailexp()
                Tab:
                    title: "Send WhatsApp"
                    MDFloatLayout:
                        Spinner:
                            id: whatsappexp_to_list
                            background_normal: ''
                            background_color: 1, 1, 1, 1  # white
                            color: 0, 0, 0, 1
                            mode: "rectangle"
                            pos_hint:{"x": .05, "y": .85}
                            size_hint: 0.90, 0.07
                            values: [""]

                        TextInput:
                            id: whatsappexp_msg
                            hint_text: "Message"
                            multiline: True
                            mode: "rectangle"
                            pos_hint:{"x": .05, "y": .4}
                            size_hint: 0.9, 0.4
                            
                        MDFillRoundFlatButton:
                            text: 'Send'
                            text_color: "white"
                            md_bg_color:(202/255, 125/255, 0/255, 1)
                            font_size: 16
                            size_hint_x: 0.2
                            size_hint_y: 0.07
                            pos_hint: {"center_x": 0.3, "center_y": 0.23}
                            on_release: root.send_whatsappexp()

                        MDFillRoundFlatButton:
                            text: 'Send All'
                            text_color: "white"
                            md_bg_color:(202/255, 125/255, 0/255, 1)
                            font_size: 16
                            size_hint_x: 0.2
                            size_hint_y: 0.07
                            pos_hint: {"center_x": 0.6, "center_y": 0.23}
                            on_release: root.send_all_whatsappexp()

    # Screen Service Provider (Modiator Parties)                                                                                                      
    Screen: 
        name: "serviceprovider"
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                id: topbar
                title: "Service Provider"
                md_bg_color: app.theme_cls.bg_dark
                left_action_items: [["chevron-left", lambda x : root.get_main("Main")]]
            MDTabs:
                id:tabs
                on_tab_switch: root.on_tab_switch(*args)
                
                Tab:
                    id: service_tab
                    title: "Modiator Parties"
                    
                    
    # Screen Export Opportunity
    Screen:
        name: "expopportunity"
        MDBoxLayout:
            orientation: "vertical"
            size: root.width, root.height
            MDTopAppBar:
                id: topbar
                title: "Export Opportunity"
                md_bg_color: app.theme_cls.bg_dark
                left_action_items: [["chevron-left", lambda x : root.get_main('Main')]]
            MDTabs:
                id:tabs
                on_tab_switch: root.on_tab_switch(*args)
                Tab:
                    id: find_expopp_tab
                    title: "Find Opportunity"    
                    MDFloatLayout:
                        MDLabel:
                            text: "Product Name"
                            font_style: 'Subtitle2'
                            font_size: 20
                            bold: True
                            pos_hint:{"center_x": .55, "center_y": .94}
                        Spinner:
                            id: exp_product_sp
                            pos_hint:{"center_x": .65, "center_y": .945}
                            background_normal: ''
                            background_color: 1, 1, 1, 1  # white
                            color: 0, 0, 0, 1
                            text: 'Select product'
                            option_cls: "MyOption"
                            values: [""]
                            size_hint: (.6, 0.06)
                            height: 50
                            font_size: 12
                            on_text:
                                root.get_exp_country(self.text)

                        MDLabel:
                            text: "Country"
                            font_style: 'Subtitle2'
                            font_size: 20
                            bold: True
                            pos_hint:{"center_x": .55, "center_y": .84}

                        Spinner:
                            id: exp_country_sp
                            pos_hint: {"center_x": 0.65, "center_y": 0.845}
                            background_normal: ''
                            background_color: 1, 1, 1, 1  # white
                            color: 0, 0, 0, 1
                            text: 'Select country'
                            option_cls: "MyOption"
                            values: [""]
                            size_hint: (.6, 0.06)
                            height: 50
                            font_size: 12
                            on_text: root.get_expopp_data(self.text)
                        
                        MDCard:
                            size_hint: None, None
                            size: 165, 320
                            pos_hint: {"center_x":.18, "center_y":.39}
                            elevation: 15
                            md_bg_color: "#3498DB"
                            orientation: "vertical"
            
                        MDLabel:
                            text: "Opportunity Name"
                            pos_hint: {"center_x": .53, "center_y": .68}
                            font_size: "16"
                            bold: True

                        MDLabel:
                            text: "Company Name"
                            pos_hint: {"center_x": .53, "center_y": .58}
                            font_size: "16"
                            bold: True

                        MDLabel:
                            text: "Contact Way"
                            pos_hint: {"center_x": .53, "center_y": .48}
                            font_size: "16"
                            bold: True

                        MDLabel:
                            text: "Quantity"
                            pos_hint: {"center_x": .53, "center_y": .38}
                            font_size: "16"
                            bold: True

                        MDLabel:
                            text: "Price"
                            pos_hint: {"center_x": .53, "center_y": .28}
                            font_size: "16"
                            bold: True
                            
                        MDLabel:
                            text: "Terms Of Shipping"
                            pos_hint: {"center_x": .53, "center_y": .18}
                            font_size: "16"
                            bold: True

                        MDLabel:
                            text: "Terms Of Paymemt"
                            pos_hint: {"center_x": .53, "center_y": .095}
                            font_size: "16"
                            bold: True

                        MDCard:
                            size_hint: None, None
                            size: 315, 320
                            pos_hint: {"center_x":.665, "center_y":.39}
                            elevation: 15
                            md_bg_color: "#3498DB"
                            orientation: "vertical"

                Tab:
                    title: "Make Offer"
                    MDFloatLayout:
                        MDLabel:
                            text: "Product"
                            font_style: 'Subtitle2'
                            font_size: 18
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .93}
                        TextInput:
                            id: expopport
                            hint_text: "Product_Name"
                            mode: "rectangle"
                            size_hint: .4, .07
                            color_active: "white"
                            pos_hint: {'center_x': .56, 'center_y': .92} 
                            multiline: False
                        MDLabel:
                            text: "Company"
                            font_style: 'Subtitle2'
                            font_size: 18
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .83}
                        TextInput:
                            id: expcomp
                            hint_text: "Company"
                            mode: "rectangle"
                            color_active: "white"
                            size_hint: .4, .07
                            pos_hint: {'center_x': .56, 'center_y': .82} 
                            multiline: False      
                        MDLabel:
                            text: "Country"
                            font_style: 'Subtitle2'
                            font_size: 18
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .73}
                        TextInput:
                            id: expcountry
                            hint_text: "Country"
                            mode: "rectangle"
                            size_hint: .4, .07
                            pos_hint: {'center_x': .56, 'center_y': .72} 
                            multiline: False
                        MDLabel:
                            text: "Email/Phone"
                            font_style: 'Subtitle2'
                            font_size: 18
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .63}
                        TextInput:
                            id: expcontact
                            hint_text: "Enter Your Email Or Phone"
                            mode: "rectangle"
                            size_hint: .4, .07
                            color_active: "white"
                            pos_hint: {'center_x': .56, 'center_y': .62} 
                            multiline: False    
                        MDLabel:
                            text: "Quantity"
                            font_style: 'Subtitle2'
                            font_size: 18
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .53}
                        TextInput:
                            id: expquantity
                            hint_text: "Quantity"
                            mode: "rectangle"
                            size_hint: .4, .07
                            pos_hint: {'center_x': .56, 'center_y': .52} 
                            color_active: "white"
                            multiline: False
                        MDLabel:
                            text: "Price"
                            font_style: 'Subtitle2'
                            font_size: 18
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .43}
                        TextInput:
                            id: expprice
                            hint_text: "Price"
                            mode: "rectangle"
                            size_hint: .4, .07
                            color_active: "white"
                            pos_hint: {'center_x': .56, 'center_y': .42} 
                            multiline: False
                        MDLabel:
                            text: "Terms of Shipping"
                            font_style: 'Subtitle2'
                            font_size: 14
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .33}
                        TextInput:
                            id: expshipping
                            hint_text: "Terms of Shipping"
                            mode: "rectangle"
                            size_hint: .4, .07
                            color_active: "white"
                            pos_hint: {'center_x': .56, 'center_y': .32} 
                            multiline: False
                        MDLabel:
                            text: "Terms of payment"
                            font_style: 'Subtitle2'
                            font_size: 14
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .23}
                        TextInput:
                            id: exppayment
                            hint_text: "Terms of payment"
                            mode: "rectangle"
                            color_active: "white"
                            size_hint: .4, .07
                            pos_hint: {'center_x': .56, 'center_y': .22} 
                            multiline: False 
                        MDFillRoundFlatButton:
                            text: 'Submit'
                            text_color: "white"
                            md_bg_color:(202/255, 125/255, 0/255, 1)
                            font_size: 16
                            size_hint: 0.4, 0.07
                            pos_hint: {"center_x": 0.56, "center_y": 0.1}
                            on_release:
                                root.exp_submit_offer()

    Screen:
        name: "impopportunity"
        MDBoxLayout:
            orientation: "vertical"
            size: root.width, root.height
            MDTopAppBar:
                id: topbar
                title: "Import Opportunity"
                md_bg_color: app.theme_cls.bg_dark
                left_action_items: [["chevron-left", lambda x : root.get_main('Main')]]
            MDTabs:
                id:tabs
                on_tab_switch: root.on_tab_switch(*args)
                Tab:
                    id: find_impopp_tab
                    title: "Find Opportunity"    
                    MDFloatLayout:
                        MDLabel:
                            text: "Product Name"
                            font_style: 'Subtitle2'
                            font_size: 20
                            bold: True
                            pos_hint:{"center_x": .55, "center_y": .94}
                        Spinner:
                            id: imp_product_sp
                            pos_hint:{"center_x": .65, "center_y": .945}
                            background_normal: ''
                            background_color: 1, 1, 1, 1  # white
                            color: 0, 0, 0, 1
                            text: 'Select product'
                            option_cls: "MyOption"
                            values: [""]
                            size_hint: (.6, 0.06)
                            height: 50
                            font_size: 12
                            on_text:
                                root.get_imp_country(self.text)

                        MDLabel:
                            text: "Country"
                            font_style: 'Subtitle2'
                            font_size: 20
                            bold: True
                            pos_hint:{"center_x": .55, "center_y": .84}
                        Spinner:
                            id: imp_country_sp
                            pos_hint: {"center_x": 0.65, "center_y": 0.845}
                            background_normal: ''
                            background_color: 1, 1, 1, 1  # white
                            color: 0, 0, 0, 1
                            text: 'Select country'
                            option_cls: "MyOption"
                            values: [""]
                            size_hint: (.6, 0.06)
                            height: 50
                            font_size: 12
                            on_text: root.get_impopp_data(self.text)

                        MDCard:
                            size_hint: None, None
                            size: 165, 320
                            pos_hint: {"center_x":.18, "center_y":.39}
                            elevation: 15
                            md_bg_color: "#3498DB"
                            orientation: "vertical"
            
                        MDLabel:
                            text: "Opportunity Name"
                            pos_hint: {"center_x": .53, "center_y": .68}
                            font_size: "16"
                            bold: True

                        MDLabel:
                            text: "Company Name"
                            pos_hint: {"center_x": .53, "center_y": .58}
                            font_size: "16"
                            bold: True

                        MDLabel:
                            text: "Contact Way"
                            pos_hint: {"center_x": .53, "center_y": .48}
                            font_size: "16"
                            bold: True

                        MDLabel:
                            text: "Quantity"
                            pos_hint: {"center_x": .53, "center_y": .38}
                            font_size: "16"
                            bold: True

                        MDLabel:
                            text: "Price"
                            pos_hint: {"center_x": .53, "center_y": .28}
                            font_size: "16"
                            bold: True
                            
                        MDLabel:
                            text: "Terms Of Shipping"
                            pos_hint: {"center_x": .53, "center_y": .18}
                            font_size: "16"
                            bold: True

                        MDLabel:
                            text: "Terms Of Paymemt"
                            pos_hint: {"center_x": .53, "center_y": .095}
                            font_size: "16"
                            bold: True

                        MDCard:
                            size_hint: None, None
                            size: 315, 320
                            pos_hint: {"center_x":.665, "center_y":.39}
                            elevation: 15
                            md_bg_color: "#3498DB"
                            orientation: "vertical"
                        
                Tab:
                    title: "Make Offer"
                    MDFloatLayout:
                        MDLabel:
                            text: "Product"
                            font_style: 'Subtitle2'
                            font_size: 18
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .93}
                        TextInput:
                            id: impopport
                            hint_text: "Product_Name"
                            mode: "rectangle"
                            size_hint: .4, .07
                            color_active: "white"
                            pos_hint: {'center_x': .56, 'center_y': .92} 
                            multiline: False
                        MDLabel:
                            text: "Company"
                            font_style: 'Subtitle2'
                            font_size: 18
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .83}
                        TextInput:
                            id: impcomp
                            hint_text: "Company"
                            mode: "rectangle"
                            color_active: "white"
                            size_hint: .4, .07
                            pos_hint: {'center_x': .56, 'center_y': .82} 
                            multiline: False      
                        MDLabel:
                            text: "Country"
                            font_style: 'Subtitle2'
                            font_size: 18
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .73}
                        TextInput:
                            id: impcountry
                            hint_text: "Country"
                            mode: "rectangle"
                            size_hint: .4, .07
                            pos_hint: {'center_x': .56, 'center_y': .72} 
                            multiline: False
                        MDLabel:
                            text: "Email/Phone"
                            font_style: 'Subtitle2'
                            font_size: 18
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .63}
                        TextInput:
                            id: impcontact
                            hint_text: "Enter Your Email Or Phone"
                            mode: "rectangle"
                            size_hint: .4, .07
                            color_active: "white"
                            pos_hint: {'center_x': .56, 'center_y': .62} 
                            multiline: False    
                        MDLabel:
                            text: "Quantity"
                            font_style: 'Subtitle2'
                            font_size: 18
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .53}
                        TextInput:
                            id: impquantity
                            hint_text: "Quantity"
                            mode: "rectangle"
                            size_hint: .4, .07
                            pos_hint: {'center_x': .56, 'center_y': .52} 
                            color_active: "white"
                            multiline: False
                        MDLabel:
                            text: "Price"
                            font_style: 'Subtitle2'
                            font_size: 18
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .43}
                        TextInput:
                            id: impprice
                            hint_text: "Price"
                            mode: "rectangle"
                            size_hint: .4, .07
                            color_active: "white"
                            pos_hint: {'center_x': .56, 'center_y': .42} 
                            multiline: False
                        MDLabel:
                            text: "Terms of Shipping"
                            font_style: 'Subtitle2'
                            font_size: 14
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .33}
                        TextInput:
                            id: impshipping
                            hint_text: "Terms of Shipping"
                            mode: "rectangle"
                            size_hint: .4, .07
                            color_active: "white"
                            pos_hint: {'center_x': .56, 'center_y': .32} 
                            multiline: False
                        MDLabel:
                            text: "Terms of payment"
                            font_style: 'Subtitle2'
                            font_size: 14
                            bold: True
                            pos_hint:{'center_x': .59, 'center_y': .23}
                        TextInput:
                            id: imppayment
                            hint_text: "Terms of payment"
                            mode: "rectangle"
                            color_active: "white"
                            size_hint: .4, .07
                            pos_hint: {'center_x': .56, 'center_y': .22} 
                            multiline: False 
                        MDFillRoundFlatButton:
                            text: 'Submit'
                            text_color: "white"
                            md_bg_color:(202/255, 125/255, 0/255, 1)
                            font_size: 16
                            size_hint: 0.4, 0.07
                            pos_hint: {"center_x": 0.56, "center_y": 0.1}
                            on_release:
                                root.imp_submit_offer()
"""

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    text_color_normal = ColorProperty((0, 0, 0, 1))
    text_color_active = ColorProperty((0, 0, 0, 0))
    text_color_normal = ColorProperty(None)
    text_color_active = ColorProperty(None)
    tab = ObjectProperty()
    tab_bar = ObjectProperty()
    font_name = StringProperty("Roboto")

class Popups(FloatLayout):
    pass

class MyNewApp(ScreenManager):
    ##########################################################################################
    ## Login Button > Connect Function
    ##########################################################################################
    def connect(self):
        global entered_email
        entered_email = self.ids.email1.text
        entered_password = self.ids.password.text

        #connect to MySQL
        db = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cursor = db.cursor()

        #run query to check email/password
        query = "SELECT email, password FROM user where email= %s and password= %s;"
        cursor.execute(query,[(entered_email),(entered_password)])
        counter = 0
        password = []
        email = []
        for i in cursor:

            for j in i:
                if counter%2 == 0:
                    email.append(j)
            else:
                password.append(j)
            counter += 1    ## Ctrl + \
        temp = ''
        wemp = ''
        if entered_email and entered_password:
            for email in email:
                if entered_email == email:
                    temp += 'yes'

            for p in password:
                if entered_password == p:
                    wemp += 'yes'
        if len(wemp) > 0 and len(temp) > 0:
            ## check usertype
            db = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
            cursor = db.cursor()
            query = "SELECT business_type FROM user where email= %s;"
            cursor.execute(query,[(entered_email),])
            data = cursor.fetchall()
            
            ## Permissions
            if data[0][0] == "Exporter":
                self.ids.import_nav.disabled = "True"
                self.ids.import_opp_nav.disabled = "True"
                

            elif data[0][0] == "Importer":
                self.ids.export_nav.disabled = "True"
                self.ids.export_opp_nav.disabled = "True"
    
            elif data[0][0] == "Service Provider":
                self.ids.import_nav.disabled = "True"
                self.ids.import_opp_nav.disabled = "True"
                self.ids.export_nav.disabled = "True"
                self.ids.export_opp_nav.disabled = "True"
                self.ids.service_provider_nav.disabled = "True"

            else:
                self.ids.import_nav.enable = "True"
                self.ids.import_opp_nav.enable = "True"
                self.ids.export_nav.enable = "True"
                self.ids.export_opp_nav.enable = "True" 

            self.current = "Main"
            db.commit()
            db.close()
        else:
            print(f"DATA > {cursor}")
            print(f"Email > {self.ids.email1.text}")
            print(f"Password > {self.ids.password.text}")
            toast('Error logging in, Please enter correct data')

        pass

    # ##########################################################################################
    # ## SignUp Button > Save Function
    # ##########################################################################################
    data_items = ListProperty([])
    def populate_fields(self, instance): # NEW
        columns = self.data_items[instance.index]['range']
        self.ids.email.text = self.data_items[columns[0]]['text']
        self.ids.passwd.text = self.data_items[columns[1]]['text']
        self.ids.phone.text = self.data_items[columns[2]]['text']
        self.ids.whats.text = self.data_items[columns[3]]['text']
        self.ids.country.text = self.data_items[columns[4]]['text']
        self.ids.usertype.text = self.data_items[columns[5]]['text']
        self.ids.category.text = self.data_items[columns[6]]['text']
        self.ids.product.text = self.data_items[columns[7]]['text']
        
    def get_table_column_headings(self):
        # global total_col_headings
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cursor = connection.cursor()
        cursor.execute("select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'user'")

        col_headings = cursor.fetchall()
        # total_col_headings
        print(len(col_headings))

    def get_users(self):
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user")
        rows = cursor.fetchall()
        # print(f"ROWS >>> {rows}")
        # print("*******************************")
        # create list with connection column, connection primary key, and connection column range
        cursor.execute("select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'user'")
        col_headings = cursor.fetchall()
        col_headings_len = len(col_headings)
        data = []
        low = 0
        high = col_headings_len - 1
        # Using database column range for populating the TextInput widgets with values from the row clicked/pressed.
        self.data_items = []
        for row in rows:
            for col in row:
                data.append([col, row[0], [low, high]])
            low += col_headings_len
            high += col_headings_len
        # create data_items
        self.data_items = [{'text': str(x[0]), 'Index': str(x[1]), 'range': x[2]} for x in data]
        print("DONE...")


    
    # ########################################################################################## 
    # Sign UP Screen Functions
    # ########################################################################################## 
    def save(self):
        email = self.ids.email.text 
        password = self.ids.passwd.text
        phone = self.ids.phone.text
        whatsapp = self.ids.whats.text
        country = self.ids.country.text
        business_type = self.ids.usertype.text
        category = self.ids.category.text
        userType = self.ids.usertype.values
        product = self.ids.signup_pro_sp.values

        if email == "" or password == "" or phone == "" or whatsapp == "" or country == "" or business_type == "" or category == "" or product == "" or userType == "select":
            toast("Please Fill The Empty Fields !")
        
        elif phone.isnumeric() == False or whatsapp.isnumeric() == False:
            toast("Please Enter An Interger Value In Whatsapp Or Phone Field !")
            
        else:
            try:
                connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
                cursordata = connection.cursor()
                sql_email = " SELECT email FROM user"
                cursordata.execute(sql_email)
                fetched_emails = cursordata.fetchall()

                if email in fetched_emails[0]:
                    toast("Email Is Already Exist")

                else:
                    connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
                    cursordata = connection.cursor()
                    save_sql = "INSERT INTO user ( email, password, phone, whatsapp, country, business_type, category, product) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    cursordata.execute(save_sql, (email, password, phone, whatsapp, country, business_type, category, str(product)))
                    connection.commit()
                    connection.close()

                    self.current = "Intro"

            except mysql.connector.IntegrityError as e:
                print("Error: ", e)
            self.get_users() #NEW


    global product_list
    product_list = []
    def add_signup_pro(self):
        signup_pro_lbl = self.ids.signup_product.text
        
        product_list.append(signup_pro_lbl)
        self.ids.signup_pro_sp.values = product_list
        toast(f"{signup_pro_lbl} added successfully")

    # ##########################################################################################
    # ## Login Button > Add Products Function
    # ##########################################################################################
    def add_products(self):
        #connect database products
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cursor = connection.cursor()
        sql_select_query = "SELECT ProductName FROM product INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email =%s ;"
        cursor.execute(sql_select_query, (entered_email,))
        productresult = cursor.fetchall()
        new_list = []
        for i in productresult:
            new_list.append(i[0])

        self.ids.pro_spinner.values = new_list

    

    # ##########################################################################################
    # # Function Open Egypt e-market Website
    # ##########################################################################################
    def openweb(self):
        new = 1
        url = "https://www.egypte-market.com"
        webbrowser.open(url,new=new)

    # ########################################################################################## 
    # # define popup function in this we create the popup
    # ########################################################################################## 
    def show_popup(self):
        show = Popups()
        popupWindow = Popup(title ="Message Us", content = show,
                            size_hint =(None, None), size =(360, 450))
        # open popup window
        popupWindow.open()

    # ########################################################################################## 
    # # Function to get importer database Screen
    # ########################################################################################## 
    def get_screendataexp(self, importerdb):
        self.current = importerdb    

    # ########################################################################################## 
    # # Function to get exporter database Screen
    # ########################################################################################## 
    def get_screenexporterdb(self, exporterdb):
        self.current = exporterdb

    # ########################################################################################## 
    # # Function to get main Screen 
    # ########################################################################################## 
    def get_main(self, Main):
        self.current = Main

    # ########################################################################################## 
    # # Function to get Intro(Sign in) Screen
    # ########################################################################################## 
    def get_intro(self, Intro):
        self.current = Intro


    def logout_user(self, Intro):
        self.current = Intro
        toast("You Logged Out!")
        self.ids.email1.text = ""
        self.ids.password.text = ""

    # ########################################################################################## 
    # # Function to call message us into main screen
    # ########################################################################################## 
    def callemail(self, instance):
        if instance.icon == "email":
            self.show_popup()

    #############################################################################
    # User's Product HsCode
    #############################################################################
    def add_hscode(self, selected_pro):
        #connect database hscode
        # print(f"SELECTED >>> {selected_pro}")
        pro_name = selected_pro
        conn = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        curs = conn.cursor()
        sql_hscode = "SELECT `ProductHScode` FROM `product` INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email= %s and product.ProductName= %s;"
        curs.execute(sql_hscode, (entered_email, pro_name))
        data = curs.fetchall()
        self.ids.code_sp.text = data[0][0]

    ###############################################################################
    # User's product markets     
    ###############################################################################
    def add_market(self, selected_pro):
        pro_name = selected_pro
        conn = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        curs1 = conn.cursor()
        sql_market = "SELECT MarketName FROM targetmarket INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s;"
        curs1.execute(sql_market, (entered_email, pro_name))
        marketresult = curs1.fetchall()
        market = []
        for j in marketresult:
            market.append(j[0])
            print(market)
        self.ids.market_sp.values = market


    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''
        Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''
        count_icon = instance_tab.icon  # get the tab icon



    ###############################################################################
    # Importers Data Table
    ###############################################################################
    def load_imptable(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        entered_email = self.ids.email1.text

        if selected_market == "Select market" or selected_product == "Select product":
            toast("Please Fill The Empty Fields!")
        
        else:
            self.transition.direction = 'left'
            self.current = 'importer'
            connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
            cur = connection.cursor()
            sql_select_importer = "SELECT importer.companyname, importer.website, importer.imp_email, importer.phone, importer.whatsapp, importer.address, importer.contact_person, importer.social_media FROM importer INNER JOIN `market_importer` ON importer.importerID=market_importer.importer_id INNER JOIN `targetmarket` ON market_importer.marktid = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
            cur.execute(sql_select_importer,(entered_email,selected_product,selected_market,))
            data = cur.fetchall()
            self.name_list = []
            self.website_list = []
            self.email_list = []
            self.phone_list = []
            self.whatsapp_list = []
            self.addresse_list = []
            self.contact_list = []
            self.social_list = []
            for index, item in enumerate(data):
                comp_name = data[index][0]
                self.name_list.append(comp_name)

                comp_website = data[index][1]
                self.website_list.append(comp_website)

                comp_email = data[index][2]
                self.email_list.append(comp_email)

                comp_phone = data[index][3]
                self.phone_list.append(comp_phone)

                comp_whatsapp = data[index][4]
                self.whatsapp_list.append(comp_whatsapp)

                comp_address = data[index][5]
                self.addresse_list.append(comp_address)

                comp_contact = data[index][6]
                self.contact_list.append(comp_contact)

                comp_social = data[index][7]
                self.social_list.append(comp_social)

            print(self.name_list)
            print(self.website_list)
            print(self.email_list)
            print(self.phone_list)
            print(self.whatsapp_list)
            print(self.addresse_list)
            print(self.contact_list)
            print(self.social_list)


            self.data_tables = MDDataTable(
                background_color_header="#075e9f",
                background_color_cell="#000000",
                background_color_selected_cell="#FF941D",
                pos_hint={'center_x': .490, 'center_y': .523},
                size_hint=(1.05, 1.05),
                use_pagination=True,
                rows_num = 10,
                check=False,
                column_data=[
                    ("ID", dp(10)),
                    ("Company Name", dp(50)),
                    ("Website", dp(50)),
                    ("E-mail", dp(50)),
                    ("Telephone", dp(30)),
                    ("WhatsApp", dp(30)),
                    ("Address", dp(50)),
                    ("Contact Person", dp(30)),
                    ("Social Media", dp(50))],
                row_data=[
                    (f"1", self.name_list[0], self.website_list[0], self.email_list[0], self.phone_list[0], self.whatsapp_list[0], self.addresse_list[0], self.contact_list[0], self.social_list[0])],)
                    
            self.ids.importers_tab.add_widget(self.data_tables)


    ###############################################################################
    # Add_Row In Importer Data Table
    ###############################################################################
    def add_improw(self, *args):
        entered_email = self.ids.email1.text
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        
        if selected_market == "Select market" or selected_product == "Select product":
            toast("Please Fill The Empty Field !")
        else:
            self.transition.direction = 'left'
            self.current = 'importer'
            connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
            cur = connection.cursor()
            sql_select_importer = "SELECT importer.companyname, importer.website, importer.imp_email, importer.phone, importer.whatsapp, importer.address, importer.contact_person, importer.social_media FROM importer INNER JOIN `market_importer` ON importer.importerID=market_importer.importer_id INNER JOIN `targetmarket` ON market_importer.marktid = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
            cur.execute(sql_select_importer,(entered_email,selected_product,selected_market,))
            data = cur.fetchall()

            i = 1
            while i < len(self.name_list):
                self.data_tables.add_row((str(i+1), self.name_list[i], self.website_list[i], self.email_list[i], self.phone_list[i], self.whatsapp_list[i], self.addresse_list[i], self.contact_list[i], self.social_list[i]))
                i+=1


    ###############################################################################
    # Exporter Data Table
    ###############################################################################
    def load_exptable(self):
        entered_email = self.ids.email1.text
        selected_product = self.ids.exppro_spinner.text
        hscode_sp = self.ids.expcode_sp.text
        
        if selected_product == "Select product":
            toast("Please Fill The Empty Field !")
        else:
            connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
            cur = connection.cursor()
            cur.execute("SELECT productthscode FROM product_exporter")
            data = cur.fetchall()
            hscode_list = []
            for i in range(len(data)):
                hscode_list.append(data[i][0])

            if hscode_sp in hscode_list:
                connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
                cur = connection.cursor()
                sql_select_importer = "SELECT exporter.company_name, exporter.website, exporter.email, exporter.phone, exporter.whatsapp, exporter.address, exporter.contact_person, exporter.social_media FROM exporter INNER JOIN `product_exporter`on exporter.exporterID = product_exporter.exporter_id INNER JOIN `product` ON product.ProductHscode = product_exporter.productthscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s;"
                cur.execute(sql_select_importer,(entered_email,selected_product,))
                data = cur.fetchall()
                expname_list = []
                expwebsite_list = []
                expemail_list = []
                expphone_list = []
                expwhatsapp_list = []
                expaddresse_list = []
                expcontact_list = []
                expsocial_list = []
                for index, item in enumerate(data):
                    expcomp_name = data[index][0]
                    expname_list.append(expcomp_name)

                    expcomp_website = data[index][1]
                    expwebsite_list.append(expcomp_website)

                    expcomp_email = data[index][2]
                    expemail_list.append(expcomp_email)

                    expcomp_phone = data[index][3]
                    expphone_list.append(expcomp_phone)

                    expcomp_whatsapp = data[index][4]
                    expwhatsapp_list.append(expcomp_whatsapp)

                    expcomp_address = data[index][5]
                    expaddresse_list.append(expcomp_address)

                    expcomp_contact = data[index][6]
                    expcontact_list.append(expcomp_contact)

                    expcomp_social = data[index][7]
                    expsocial_list.append(expcomp_social)

                self.data_tables = MDDataTable(
                    background_color_header="#075e9f",
                    background_color_cell="#000000",
                    background_color_selected_cell="#FF941D",
                    pos_hint={'center_x': .490, 'center_y': .523},
                    size_hint=(1.05, 1.05),
                    use_pagination=True,
                    rows_num = 10,
                    check=False,
                    column_data=[
                        ("ID", dp(20)),
                        ("Company Name", dp(50)),
                        ("Website", dp(50)),
                        ("E-mail", dp(50)),
                        ("Telephone", dp(30)),
                        ("WhatsApp", dp(30)),
                        ("Address", dp(50)),
                        ("Contact Person", dp(30)),
                        ("Social Media", dp(50))],
                    row_data=[
                        (f"1", expname_list[0], expwebsite_list[0], expemail_list[0], expphone_list[0], expwhatsapp_list[0], expaddresse_list[0], expcontact_list[0], expsocial_list[0])],)
                        
                self.ids.exporter_tab.add_widget(self.data_tables)

                i = 1
                while i < len(expname_list):
                    self.data_tables.add_row((str(i+1), expname_list[i], expwebsite_list[i], expemail_list[i], expphone_list[i], expwhatsapp_list[i], expaddresse_list[i], expcontact_list[i], expsocial_list[i]))
                    i+=1

                self.transition.direction = 'left'
                self.current = 'exporter'

            else:
                toast("Selected product has no exporters")


    ###############################################################################
    # Service Provider Data Table
    ###############################################################################
    def load_servtable(self):
        entered_email = self.ids.email1.text
        # connection to table user_mediato
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        cur.execute("SELECT emailluser FROM user_mediator")
        data = cur.fetchall()
        useremail_list = []
        for i in range(len(data)):
            useremail_list.append(data[i][0])

        if entered_email in useremail_list:
            connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
            cur = connection.cursor()
            sql_select_mediator = "SELECT mediatorparties.countryname, mediatorparties.companyname, mediatorparties.website, mediatorparties.email, mediatorparties.phone, mediatorparties.whatsapp, mediatorparties.address, mediatorparties.company_type FROM mediatorparties INNER JOIN `user_mediator`on mediatorparties.mediatorID = user_mediator.mediator_ID INNER JOIN user ON user.email = user_mediator.emailluser WHERE user.email = %s;"
            cur.execute(sql_select_mediator,(entered_email,))
            data = cur.fetchall()
            self.mpcountry_list = []
            self.mpcompany_list = []
            self.mpwebsite_list = []
            self.mpemail_list = []
            self.mpphone_list = []
            self.mpwhatsapp_list = []
            self.mpaddresse_list = []
            self.mpcompanytype_list = []
            for index, item in enumerate(data):
                mpcountry_name = data[index][0]
                self.mpcountry_list.append(mpcountry_name)

                mpcompany_name = data[index][1]
                self.mpcompany_list.append(mpcompany_name)

                mpcomp_website = data[index][2]
                self.mpwebsite_list.append(mpcomp_website)

                mpcomp_email = data[index][3]
                self.mpemail_list.append(mpcomp_email)

                mpcomp_phone = data[index][4]
                self.mpphone_list.append(mpcomp_phone)

                mpcomp_whatsapp = data[index][5]
                self.mpwhatsapp_list.append(mpcomp_whatsapp)

                mpcomp_address = data[index][6]
                self.mpaddresse_list.append(mpcomp_address)

                mpcompanytype = data[index][7]
                self.mpcompanytype_list.append(mpcompanytype)

            print(self.mpcountry_list)
            print(self.mpcompany_list)
            print(self.mpwebsite_list)
            print(self.mpemail_list)
            print(self.mpphone_list)
            print(self.mpwhatsapp_list)
            print(self.mpaddresse_list)
            print(self.mpcompanytype_list)    

            self.data_tables = MDDataTable(
                background_color_header="#075e9f",
                background_color_cell="#000000",
                background_color_selected_cell="#FF941D",
                pos_hint={'center_x': .493, 'center_y': .523}, 
                size_hint=(1.1, 1.05),
                use_pagination=True,
                rows_num = 10,
                check=False,
                column_data=[
                    ("ID", dp(20)),
                    ("Country Name", dp(30)),
                    ("Company Name", dp(50)),
                    ("Website", dp(50)),
                    ("E-mail", dp(50)),
                    ("Telephone", dp(30)),
                    ("WhatsApp", dp(30)),
                    ("Address", dp(50)),
                    ("Company type", dp(50))],
                row_data=[
                    (f"1", self.mpcountry_list[0], self.mpcompany_list[0], self.mpwebsite_list[0], self.mpemail_list[0], self.mpphone_list[0], self.mpwhatsapp_list[0], self.mpaddresse_list[0], self.mpcompanytype_list[0])],)
                    
            self.ids.service_tab.add_widget(self.data_tables)

            i = 1
            while i < len(self.mpcountry_list):
                self.data_tables.add_row((str(i+1), self.mpcountry_list[i], self.mpcompany_list[i], self.mpwebsite_list[i], self.mpemail_list[i], self.mpphone_list[i], self.mpwhatsapp_list[i], self.mpaddresse_list[i], self.mpcompanytype_list[i]))
                i+=1
            self.transition.direction = 'left'
            self.current = 'serviceprovider'    
        else:
            toast("There are no mediator parties!!")
    ###############################################################################
    # Market Analysis
    ###############################################################################
    def load_markettable(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        entered_email = self.ids.email1.text

        if selected_product == "Select product" or selected_market == "Select market":
            toast("Please Fill The Empty Field !")
        else:
            ## Compatitive
            self.transition.direction = 'left'
            self.current = 'marketanalysis'
            connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
            cur = connection.cursor()
            sql_select_companalysis ="SELECT MarketName, total_imports, egypt_exports, competing_market, compcountry_exports FROM targetmarket INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
            cur.execute(sql_select_companalysis,(entered_email,selected_product,selected_market,))
            data = cur.fetchall()
            self.ids.market_name_tab.secondary_text = data[0][0]
            self.ids.market_total_imports_tab.secondary_text = data[0][1]
            self.ids.egypt_total_exports_tab.secondary_text = data[0][2]
            self.ids.competing_country_tab.secondary_text = data[0][3]
            self.ids.competitive_country_exports_tab.secondary_text = data[0][4]


    ###############################################################################
    # Show PESTLE Data
    ###############################################################################
    def show_political_dialog(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        entered_email = self.ids.email1.text
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_pestle = "SELECT political, economic, social , technology, legal, enviromental FROM pestle INNER JOIN `market_pestle` ON pestle.pestleID = market_pestle.pestle_id INNER JOIN `targetmarket` ON market_pestle.marketid = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
        cur.execute(sql_select_pestle,(entered_email,selected_product,selected_market,))
        data = cur.fetchall()
        my_dialog = MDDialog(title="Political", text=str(data[0][0]), size_hint=[1, .5], auto_dismiss=True)
        my_dialog.open()
 
    def show_economic_dialog(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        entered_email = self.ids.email1.text
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_pestle = "SELECT political, economic, social , technology, legal, enviromental FROM pestle INNER JOIN `market_pestle` ON pestle.pestleID = market_pestle.pestle_id INNER JOIN `targetmarket` ON market_pestle.marketid = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
        cur.execute(sql_select_pestle,(entered_email,selected_product,selected_market,))
        data = cur.fetchall()
        my_dialog = MDDialog(title="Economic", text=data[0][1], size_hint=[1, .5], auto_dismiss=True)
        my_dialog.open()

    def show_social_dialog(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        entered_email = self.ids.email1.text
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_pestle = "SELECT political, economic, social , technology, legal, enviromental FROM pestle INNER JOIN `market_pestle` ON pestle.pestleID = market_pestle.pestle_id INNER JOIN `targetmarket` ON market_pestle.marketid = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
        cur.execute(sql_select_pestle,(entered_email,selected_product,selected_market,))
        data = cur.fetchall()
        my_dialog = MDDialog(title="Social", text=data[0][2], size_hint=[1, .5], auto_dismiss=True)
        my_dialog.open()

    def show_tech_dialog(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        entered_email = self.ids.email1.text
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_pestle = "SELECT political, economic, social , technology, legal, enviromental FROM pestle INNER JOIN `market_pestle` ON pestle.pestleID = market_pestle.pestle_id INNER JOIN `targetmarket` ON market_pestle.marketid = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
        cur.execute(sql_select_pestle,(entered_email,selected_product,selected_market,))
        data = cur.fetchall()
        my_dialog = MDDialog(title="Technlogical", text=data[0][3], size_hint=[1, .5], auto_dismiss=True)
        my_dialog.open()

    def show_legal_dialog(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        entered_email = self.ids.email1.text
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_pestle = "SELECT political, economic, social , technology, legal, enviromental FROM pestle INNER JOIN `market_pestle` ON pestle.pestleID = market_pestle.pestle_id INNER JOIN `targetmarket` ON market_pestle.marketid = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
        cur.execute(sql_select_pestle,(entered_email,selected_product,selected_market,))
        data = cur.fetchall()
        my_dialog = MDDialog(title="Legal", text=data[0][4], size_hint=[1, .5], auto_dismiss=True)
        my_dialog.open()

    def show_env_dialog(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        entered_email = self.ids.email1.text
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_pestle = "SELECT political, economic, social , technology, legal, enviromental FROM pestle INNER JOIN `market_pestle` ON pestle.pestleID = market_pestle.pestle_id INNER JOIN `targetmarket` ON market_pestle.marketid = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
        cur.execute(sql_select_pestle,(entered_email,selected_product,selected_market,))
        data = cur.fetchall()
        my_dialog = MDDialog(title="Enviromental", text=data[0][5], size_hint=[1, .5], auto_dismiss=True)
        my_dialog.open()

    ###############################################################################
    # Market Plan
    ###############################################################################
    def check_marketplan(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text

        if selected_market == "Select market" or selected_product == "Select product":
            toast("Please Fill The Empty Data !!")

        else:
            self.transition.direction = 'left'
            self.current = 'marketplan'

    def show_product(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        entered_email = self.ids.email1.text

        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_ps = "SELECT 4Ps.product, 4Ps.promotion, 4Ps.price, 4Ps.place FROM 4Ps INNER JOIN `market_4ps` ON 4Ps.4PsID=market_4ps.4ps_id INNER JOIN `targetmarket` ON market_4ps.markID = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
        cur.execute(sql_select_ps,(entered_email,selected_product,selected_market,))
        data = cur.fetchall()

        my_dialog = MDDialog(title="Product", text=data[0][0], size_hint=[1, .5], auto_dismiss=True)
        my_dialog.open()


    def show_promotion(self):
        selected_product = self.ids.pro_spinner.text
        entered_email = self.ids.email1.text
        selected_market = self.ids.market_sp.text

        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_req = "SELECT 4Ps.product, 4Ps.promotion, 4Ps.price, 4Ps.place FROM 4Ps INNER JOIN `market_4ps` ON 4Ps.4PsID=market_4ps.4ps_id INNER JOIN `targetmarket` ON market_4ps.markID = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
        cur.execute(sql_select_req,(entered_email,selected_product,selected_market,))
        data = cur.fetchall()

        my_dialog = MDDialog(title="Promotion", text=data[0][1], size_hint=[1, .5], auto_dismiss=True)
        my_dialog.open()


    def show_Price(self):
        selected_product = self.ids.pro_spinner.text
        entered_email = self.ids.email1.text
        selected_market = self.ids.market_sp.text

        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_req = "SELECT 4Ps.product, 4Ps.promotion, 4Ps.price, 4Ps.place FROM 4Ps INNER JOIN `market_4ps` ON 4Ps.4PsID=market_4ps.4ps_id INNER JOIN `targetmarket` ON market_4ps.markID = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
        cur.execute(sql_select_req,(entered_email,selected_product,selected_market,))
        data = cur.fetchall()

        my_dialog = MDDialog(title="Price", text=data[0][2], size_hint=[1, .5], auto_dismiss=True)
        my_dialog.open()


    def show_place(self):
        selected_product = self.ids.pro_spinner.text
        entered_email = self.ids.email1.text
        selected_market = self.ids.market_sp.text

        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_req = "SELECT 4Ps.product, 4Ps.promotion, 4Ps.price, 4Ps.place FROM 4Ps INNER JOIN `market_4ps` ON 4Ps.4PsID=market_4ps.4ps_id INNER JOIN `targetmarket` ON market_4ps.markID = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
        cur.execute(sql_select_req,(entered_email,selected_product,selected_market,))
        data = cur.fetchall()

        my_dialog = MDDialog(title="Place", text=data[0][3], size_hint=[1, .5], auto_dismiss=True)
        my_dialog.open()



    def show_req_data(self):
        selected_product = self.ids.pro_spinner.text
        entered_email = self.ids.email1.text

        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_req = "SELECT product_requirement FROM requirements INNER JOIN `product_requirements` ON requirements.requireID = product_requirements.require_id INNER JOIN `product` ON product.ProductHscode = product_requirements.productcode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s;"
        cur.execute(sql_select_req,(entered_email,selected_product,))
        data = cur.fetchall()

        my_dialog = MDDialog(title="Product Requirements", text=data[0][0], size_hint=[1, .5], auto_dismiss=True)
        my_dialog.open()

    ###############################################################################
    # Exporter Make Offer
    ###############################################################################
    def exp_submit_offer(self):
        exp_opp_name     = self.ids.expopport
        exp_comp_name    = self.ids.expcomp
        exp_country_name = self.ids.expcountry
        exp_contact      = self.ids.expcontact
        exp_quantity     = self.ids.expquantity
        exp_price        = self.ids.expprice
        exp_shipping     = self.ids.expshipping
        exp_payment      = self.ids.exppayment
        exp_datetime     = date.today()

        if exp_opp_name.text == "" or exp_comp_name.text == "" or exp_country_name == "" or exp_contact == "" or exp_quantity == "" or exp_price == "" or exp_shipping == "" or exp_payment == "":
            toast("Please Fill The Empty Fields !")
        else:
            connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
            cur = connection.cursor()
            sql_insert_impopportunity = '''INSERT INTO importopportunity(opportunity_date,
                                        opportunity_name, company_name, imp_country, contact_way, quantity, price, term_of_shipping, term_of_payment)
                                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'''

            cur.execute(sql_insert_impopportunity, (exp_datetime, exp_opp_name.text, exp_comp_name.text, exp_country_name.text, exp_contact.text, exp_quantity.text, exp_price.text, exp_shipping.text, exp_payment.text))
            connection.commit()
            connection.close()
            print("Data successfully inserted")

        
    ###############################################################################
    ## Import Product Spinner
    ###############################################################################
    def get_imp_product(self):
        # self.ids.imp_product_sp.values = ["data1", "data2"]
        entered_email = self.ids.email1.text

        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_prodopportunity = "SELECT ProductName FROM product INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email =%s ;"
        cur.execute(sql_select_prodopportunity, (entered_email,))
        impproductresult = cur.fetchall()
        imp_new_list = []
        for i in impproductresult:
            imp_new_list.append(i[0])
        self.ids.imp_product_sp.values = imp_new_list



    ###############################################################################
    ## Import Country Spinner
    ###############################################################################
    def get_imp_country(self, imp_pro_name):
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_impopportunity = "SELECT imp_country FROM importopportunity INNER JOIN `product_impopportunity` ON importopportunity.opportunity_id = product_impopportunity.impopportunity_id INNER JOIN `product` ON product.ProductHscode = product_impopportunity.prod_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s;"
        cur.execute(sql_select_impopportunity, (entered_email, imp_pro_name))
        impcountryresult = cur.fetchall()
        print(impcountryresult)
        imp_country_list = []
        for j in impcountryresult:
            imp_country_list.append(j[0])
            print(imp_country_list)
        self.ids.imp_country_sp.values = imp_country_list


    ###############################################################################
    ## Import Find Oppurtunity Data
    ###############################################################################
    def get_impopp_data(self, imp_country):
        imp_product_name = self.ids.imp_product_sp.text
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_opportunity = "SELECT opportunity_name, company_name, contact_way, quantity, price, term_of_shipping, term_of_payment FROM importopportunity INNER JOIN `product_impopportunity` ON importopportunity.opportunity_id = product_impopportunity.impopportunity_id INNER JOIN `product` ON product.ProductHscode = product_impopportunity.prod_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND importopportunity.imp_country= %s;"
        cur.execute(sql_select_opportunity, (entered_email, imp_product_name, imp_country))
        data = cur.fetchall()
        
        opp_list = []
        company_list = []
        contact_list = []
        quantity_list = []
        price_list = []
        shipping_list = []
        payment_list = []
        for index, item in enumerate(data):
            opp_name = data[index][0]
            opp_list.append(opp_name)

            comp_name = data[index][1]
            company_list.append(comp_name)

            contact = data[index][2]
            contact_list.append(contact)

            quant = data[index][3]
            quantity_list.append(quant)

            price = data[index][4]
            price_list.append(price)

            shipping = data[index][5]
            shipping_list.append(shipping)

            payment = data[index][6]
            payment_list.append(payment)

        print(opp_list)
        print(company_list)
        print(contact_list)
        print(quantity_list)
        print(price_list)
        print(shipping_list)
        print(payment_list)

        opp_name_value_lbl = MDLabel(
            text=opp_list[0],
            font_size="12sp",
            pos_hint={"center_x": .9, "center_y": .68}
        )
        self.ids.find_impopp_tab.add_widget(opp_name_value_lbl)


        comp_name_value_lbl = MDLabel(
            text=company_list[0],
            font_size="12sp",
            pos_hint={"center_x": .9, "center_y": .58}
        )
        self.ids.find_impopp_tab.add_widget(comp_name_value_lbl)


        contact_value_lbl = MDLabel(
            text=contact_list[0],
            font_size="12sp",
            pos_hint={"center_x": .9, "center_y": .48}
        )
        self.ids.find_impopp_tab.add_widget(contact_value_lbl)


        quantity_value_lbl = MDLabel(
            text=quantity_list[0],
            font_size="12sp",
            pos_hint={"center_x": .9, "center_y": .38}
        )
        self.ids.find_impopp_tab.add_widget(quantity_value_lbl)


        price_value_lbl = MDLabel(
            text=price_list[0],
            font_size="12sp",
            pos_hint={"center_x": .9, "center_y": .28}
        )
        self.ids.find_impopp_tab.add_widget(price_value_lbl)


        shipping_value_lbl = MDLabel(
            text=shipping_list[0],
            font_size="12sp",
            pos_hint={"center_x": .9, "center_y": .18}
        )
        self.ids.find_impopp_tab.add_widget(shipping_value_lbl)


        payment_value_lbl = MDLabel(
            text=str(payment_list[0]),
            font_size="12sp",
            pos_hint={"center_x": .9, "center_y": .095}
        )
        self.ids.find_impopp_tab.add_widget(payment_value_lbl)


    ###############################################################################
    ## Import Make Offer
    ###############################################################################
    def imp_submit_offer(self):
        imp_opp_name     = self.ids.impopport
        imp_comp_name    = self.ids.impcomp
        imp_country_name = self.ids.impcountry
        imp_contact      = self.ids.impcontact
        imp_quantity     = self.ids.impquantity
        imp_price        = self.ids.impprice
        imp_shipping     = self.ids.impshipping
        imp_payment      = self.ids.imppayment
        imp_datetime     = date.today()

        if imp_opp_name.text == "" or imp_comp_name.text == "" or imp_country_name == "" or imp_contact == "" or imp_quantity == "" or imp_price == "" or imp_shipping == "" or imp_payment == "":
            toast("Please Fill The Empty Fields !")
        else:
            connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
            cur = connection.cursor()
            sql_insert_expopportunity = '''INSERT INTO exportopportunity(opportunitydata,
                                            opportunityname, company_name, exp_country, contactway, quantity, price, term_of_shipping, term_of_payment)
                                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'''

            cur.execute(sql_insert_expopportunity, (imp_datetime, imp_opp_name.text, imp_comp_name.text, imp_country_name.text, imp_contact.text, imp_quantity.text, imp_price.text, imp_shipping.text, imp_payment.text))
            connection.commit()
            connection.close()
            print("Data successfully inserted")



    ###############################################################################
    ## Get Product Spinner
    ###############################################################################
    def get_exp_product(self):
        entered_email = self.ids.email1.text

        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_prodopportunity = "SELECT ProductName FROM product INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email =%s ;"
        cur.execute(sql_select_prodopportunity, (entered_email,))
        expproductresult = cur.fetchall()
        exp_new_list = []
        for i in expproductresult:
            exp_new_list.append(i[0])
        self.ids.exp_product_sp.values = exp_new_list



    ###############################################################################
    ## Export Country Spinner
    ###############################################################################
    def get_exp_country(self, exp_product):
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_expopportunity = "SELECT exp_country FROM exportopportunity INNER JOIN `product_expopportunity` ON exportopportunity.opportunityID = product_expopportunity.expopportunityID INNER JOIN `product` ON product.ProductHscode = product_expopportunity.prodhscode  INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s;"
        cur.execute(sql_select_expopportunity, (entered_email, exp_product))
        impcountryresult = cur.fetchall()
        print(impcountryresult)
        exp_country_list = []
        for j in impcountryresult:
            exp_country_list.append(j[0])
            print(exp_country_list)
        self.ids.exp_country_sp.values = exp_country_list



    ###############################################################################
    ## Export Find Oppurtunity Data
    ###############################################################################
    def get_expopp_data(self, exp_country):
        exp_product_name = self.ids.exp_product_sp.text
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_opportunity = "SELECT opportunityname, company_name, contactway, quantity, price, term_of_shipping, term_of_payment FROM exportopportunity INNER JOIN `product_expopportunity` ON exportopportunity.opportunityID = product_expopportunity.expopportunityID INNER JOIN `product` ON product.ProductHscode = product_expopportunity.prodhscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND exportopportunity.exp_country= %s;"
        cur.execute(sql_select_opportunity, (entered_email, exp_product_name, exp_country))
        data = cur.fetchall()
        
        opp_list = []
        company_list = []
        contact_list = []
        quantity_list = []
        price_list = []
        shipping_list = []
        payment_list = []
        for index, item in enumerate(data):
            opp_name = data[index][0]
            opp_list.append(opp_name)

            comp_name = data[index][1]
            company_list.append(comp_name)

            contact = data[index][2]
            contact_list.append(contact)

            quant = data[index][3]
            quantity_list.append(quant)

            price = data[index][4]
            price_list.append(price)

            shipping = data[index][5]
            shipping_list.append(shipping)

            payment = data[index][6]
            payment_list.append(payment)

        print(opp_list)
        print(company_list)
        print(contact_list)
        print(quantity_list)
        print(price_list)
        print(shipping_list)
        print(payment_list)

        
        opp_name_value_lbl = MDLabel(
            text=opp_list[0],
            font_size="12sp",
            pos_hint={"center_x": .9, "center_y": .68}
        )
        self.ids.find_expopp_tab.add_widget(opp_name_value_lbl)


        comp_name_value_lbl = MDLabel(
            text=company_list[0],
            font_size="12sp",
            pos_hint={"center_x": .9, "center_y": .58}
        )
        self.ids.find_expopp_tab.add_widget(comp_name_value_lbl)


        contact_value_lbl = MDLabel(
            text=contact_list[0],
            font_size="12sp",
            pos_hint={"center_x": .9, "center_y": .48}
        )
        self.ids.find_expopp_tab.add_widget(contact_value_lbl)


        quantity_value_lbl = MDLabel(
            text=quantity_list[0],
            font_size="12sp",
            pos_hint={"center_x": .9, "center_y": .38}
        )
        self.ids.find_expopp_tab.add_widget(quantity_value_lbl)


        price_value_lbl = MDLabel(
            text=price_list[0],
            font_size="12sp",
            pos_hint={"center_x": .9, "center_y": .28}
        )
        self.ids.find_expopp_tab.add_widget(price_value_lbl)


        shipping_value_lbl = MDLabel(
            text=shipping_list[0],
            font_size="12sp",
            pos_hint={"center_x": .9, "center_y": .18}
        )
        self.ids.find_expopp_tab.add_widget(shipping_value_lbl)


        payment_value_lbl = MDLabel(
            text=str(payment_list[0]),
            font_size="12sp",
            pos_hint={"center_x": .9, "center_y": .095}
        )
        self.ids.find_expopp_tab.add_widget(payment_value_lbl)


    def add_expproduct(self):
        #connect database products
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cursor = connection.cursor()
        sql_select_query = "SELECT ProductName FROM product INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email =%s ;"
        cursor.execute(sql_select_query, (entered_email,))
        productresult = cursor.fetchall()
        new_list = []
        for i in productresult:
            new_list.append(i[0])

        self.ids.exppro_spinner.values = new_list


    def add_exphscode(self, exp_pro_name):
        conn = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        curs = conn.cursor()
        sql_hscode = "SELECT `ProductHScode` FROM `product` INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email= %s and product.ProductName= %s;"
        curs.execute(sql_hscode, (entered_email, exp_pro_name))
        data = curs.fetchall()
        self.ids.expcode_sp.text = data[0][0]



    ###############################################################################
    ## Show SWOT Data
    ###############################################################################
    def show_strenghts(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        entered_email = self.ids.email1.text
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_swot = "SELECT strengths, weakness, opportunities, threats FROM swot INNER JOIN `market_swot` ON swot.swotID=market_swot.swot_id INNER JOIN `targetmarket` ON market_swot.markett_id = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
        cur.execute(sql_select_swot,(entered_email,selected_product,selected_market,))
        data = cur.fetchall()
        my_dialog = MDDialog(title="Strenghts", text=str(data[0][0]), size_hint=[1, .5], auto_dismiss=True)
        my_dialog.open()

    def show_weakness(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        entered_email = self.ids.email1.text
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_swot = "SELECT strengths, weakness, opportunities, threats FROM swot INNER JOIN `market_swot` ON swot.swotID=market_swot.swot_id INNER JOIN `targetmarket` ON market_swot.markett_id = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
        cur.execute(sql_select_swot,(entered_email,selected_product,selected_market,))
        data = cur.fetchall()
        my_dialog = MDDialog(title="Weakness", text=str(data[0][1]), size_hint=[1, .5], auto_dismiss=True)
        my_dialog.open()

    def show_opportunities(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        entered_email = self.ids.email1.text
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_swot = "SELECT strengths, weakness, opportunities, threats FROM swot INNER JOIN `market_swot` ON swot.swotID=market_swot.swot_id INNER JOIN `targetmarket` ON market_swot.markett_id = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
        cur.execute(sql_select_swot,(entered_email,selected_product,selected_market,))
        data = cur.fetchall()
        my_dialog = MDDialog(title="Opportunities", text=str(data[0][2]), size_hint=[1, .5], auto_dismiss=True)
        my_dialog.open()
        
    def show_threats(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        entered_email = self.ids.email1.text
        connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
        cur = connection.cursor()
        sql_select_swot = "SELECT strengths, weakness, opportunities, threats FROM swot INNER JOIN `market_swot` ON swot.swotID=market_swot.swot_id INNER JOIN `targetmarket` ON market_swot.markett_id = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
        cur.execute(sql_select_swot,(entered_email,selected_product,selected_market,))
        data = cur.fetchall()
        my_dialog = MDDialog(title="Threats", text=str(data[0][1]), size_hint=[1, .5], auto_dismiss=True)
        my_dialog.open()

    ###############################################################################
    ## Importer Send Email
    ###############################################################################
    def get_emails(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        entered_email = self.ids.email1.text

        if selected_product == "Select product" or selected_market == "Select market":
            toast("Please Fill The Empty Field !")
        else:
            self.transition.direction = 'left'
            self.current = 'importer'
            connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
            cur = connection.cursor()
            sql_select_importer = "SELECT importer.companyname, importer.website, importer.imp_email, importer.phone, importer.whatsapp, importer.address, importer.contact_person, importer.social_media FROM importer INNER JOIN `market_importer` ON importer.importerID=market_importer.importer_id INNER JOIN `targetmarket` ON market_importer.marktid = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
            cur.execute(sql_select_importer,(entered_email,selected_product,selected_market,))
            data = cur.fetchall()
            email_list = []
            for index, item in enumerate(data):
                comp_email = data[index][2]
                if not comp_email == "":
                    email_list.append(comp_email)

            print(email_list)
            self.ids.email_to_list.values = email_list


    def attach_files(self):
        self.file_list = []
        new_path = filedialog.askopenfilenames(initialdir='\\',initialfile='',filetypes=[("All files", "*")])
        for k in new_path:
            if k not in self.file_list:
                self.file_list.append(k)
                self.ids.attach_box.text = k.split('/')[-1]


    def send_email(self):
        email_from_input    = self.ids.email_from.text
        email_passwd_input  = self.ids.email_passwd.text
        email_to_input      = self.ids.email_to_list.text
        email_subject_input = self.ids.email_subject.text
        email_msg_input     = self.ids.email_msg.text

        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"

        msg = EmailMessage()
        
        msg['Subject'] = email_subject_input
        msg['From'] = email_from_input
        msg['To'] = email_to_input
        msg.set_content(email_msg_input)

        # attach file
        mime_type, _ = mimetypes.guess_type(self.file_list[0])
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(self.file_list[0], 'rb') as file:
            msg.add_attachment(file.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(self.file_list[0]))

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(email_from_input, email_passwd_input)
            server.send_message(msg)

        toast("Email sent successfully!!")
    ######################################################################
    # Get whatsapp Numbers
    ######################################################################
    def get_whatsapp(self):
        selected_product = self.ids.pro_spinner.text
        selected_market = self.ids.market_sp.text
        entered_email = self.ids.email1.text

        if selected_product == "Select product" or selected_market == "Select market":
            toast("Please Fill The Empty Field !")
        else:
            self.transition.direction = 'left'
            self.current = 'importer'
            connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
            cur = connection.cursor()
            sql_select_importer = "SELECT importer.companyname, importer.website, importer.imp_email, importer.phone, importer.whatsapp, importer.address, importer.contact_person, importer.social_media FROM importer INNER JOIN `market_importer` ON importer.importerID=market_importer.importer_id INNER JOIN `targetmarket` ON market_importer.marktid = targetmarket.marketID INNER JOIN `product_market`on targetmarket.marketID = product_market.market_id INNER JOIN `product` ON product.ProductHscode = product_market.product_hscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s AND targetmarket.MarketName = %s;"
            cur.execute(sql_select_importer,(entered_email,selected_product,selected_market,))
            data = cur.fetchall()
            whatsapp_list = []
            for index, item in enumerate(data):
                comp_whatsapp= data[index][4]
                if not comp_whatsapp == "":
                    whatsapp_list.append(comp_whatsapp)

            print(whatsapp_list)
            self.ids.whatsapp_to_list.values = whatsapp_list
    ###############################################################################
    ## Importer send WhatsApp
    ###############################################################################
    def send_whatsapp(self):
        whatsapp_list          = self.ids.whatsapp_to_list
        whatsapp_msg_input     = self.ids.whatsapp_msg.text

        s=Service(ChromeDriverManager().install())
        options=Options()
        options.add_argument('--user-data-dir='+final_path+'chrome-data')
        options.add_experimental_option('excludeSwitches',['enable-automation'])
        options.add_experimental_option('useAutomationExtension',False)
        options.add_argument('--incognitos')
        driver = webdriver.Chrome(service=s,options=options)
        driver.get("https://web.whatsapp.com/")
        wait = WebDriverWait(driver, 800)
        driver.get("https://web.whatsapp.com/send?phone={}".format(whatsapp_list.text))
        try:
            driver.switch_to.alert.accept()
        except:
            pass
        
        inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        input_box = wait.until(EC.presence_of_element_located((
            By.XPATH, inp_xpath)))
        input_box.send_keys(whatsapp_msg_input + Keys.ENTER)
        time.sleep(2)

    ###############################################################################
    ## Importer send WhatsApp for All numbers 
    ###############################################################################

    def send_all_whatsapp(self):
        whatsapp_list          = self.ids.whatsapp_to_list
        whatsapp_msg_input     = self.ids.whatsapp_msg.text

        whatsapp_list2=[]
        for i in whatsapp_list.values:
            whatsapp_list2.append(i)
        print(whatsapp_list2)
        s=Service(ChromeDriverManager().install())
        options=Options()
        options.add_argument('--user-data-dir='+final_path+'chrome-data')
        options.add_experimental_option('excludeSwitches',['enable-automation'])
        options.add_experimental_option('useAutomationExtension',False)
        options.add_argument('--incognitos')
        driver = webdriver.Chrome(service=s,options=options)
        driver.get("https://web.whatsapp.com/")
        wait = WebDriverWait(driver, 800)
        for phone_number in whatsapp_list2:
            driver.get("https://web.whatsapp.com/send?phone={}".format(phone_number))
            try:
                driver.switch_to.alert.accept()
            except:
                pass
                
            inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
            input_box = wait.until(EC.presence_of_element_located((
                By.XPATH, inp_xpath)))
            input_box.send_keys(whatsapp_msg_input + Keys.ENTER)
            time.sleep(2)

    ###############################################################################
    ## Contact Screen
    ###############################################################################
    def contact(self):
        sender_email = self.ids.contact_email.text
        sender_msg = self.ids.contact_msg.text
        sender_passwd = self.ids.contact_passwd.text

        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"

        msg = EmailMessage()
        
        msg['Subject'] = "Contact Us"
        msg['From'] = sender_email
        msg['To'] = "info@e-markets.org"
        msg.set_content(f'''
        Email:
        {sender_email}

        Message:
        {sender_msg}
        ''')

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, sender_passwd)
            server.send_message(msg)

        toast("Email sent successfully!!")

    ###############################################################################
    ## Exporter Send Email
    ###############################################################################
    def get_exp_emails(self):
        selected_exp_product = self.ids.exppro_spinner.text
        entered_email = self.ids.email1.text

        if selected_exp_product == "Select product":
            toast("Please Fill The Empty Field !")
        else:
            self.transition.direction = 'left'
            self.current = 'exporter'
            connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
            cur = connection.cursor()
            sql_select_importer = "SELECT exporter.company_name, exporter.website, exporter.email, exporter.phone, exporter.whatsapp, exporter.address, exporter.contact_person, exporter.social_media FROM exporter INNER JOIN `product_exporter`on exporter.exporterID = product_exporter.exporter_id INNER JOIN `product` ON product.ProductHscode = product_exporter.productthscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s;"
            cur.execute(sql_select_importer,(entered_email,selected_exp_product,))
            data = cur.fetchall()
            email_exp_list = []
            for index, item in enumerate(data):
                expcomp_email = data[index][2]
                if not expcomp_email == "":
                    email_exp_list.append(expcomp_email)

            print(email_exp_list)
            self.ids.emailexp_to_list.values = email_exp_list


    def attach_exp_files(self):
        self.file_list = []
        new_path = filedialog.askopenfilenames(initialdir='\\',initialfile='',filetypes=[("All files", "*")])
        for k in new_path:
            if k not in self.file_list:
                self.file_list.append(k)
                self.ids.attachexp_box.text = k.split('/')[-1]


    def send_exp_email(self):
        emailexp_from_input    = self.ids.emailexp_from.text
        emailexp_passwd_input  = self.ids.emailexp_passwd.text
        emailexp_to_input      = self.ids.emailexp_to_list.text
        emailexp_subject_input = self.ids.emailexp_subject.text
        emailexp_msg_input     = self.ids.emailexp_msg.text

        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"

        msg = EmailMessage()
        
        msg['Subject'] = emailexp_subject_input
        msg['From'] = emailexp_from_input
        msg['To'] = emailexp_to_input
        msg.set_content(emailexp_msg_input)

        # attach file
        mime_type, _ = mimetypes.guess_type(self.file_list[0])
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(self.file_list[0], 'rb') as file:
            msg.add_attachment(file.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(self.file_list[0]))


        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(emailexp_from_input, emailexp_passwd_input)
            server.send_message(msg)

        toast("Email sent successfully!!")
    ######################################################################
    # Get whatsapp Numbers for exporter
    ######################################################################
    def get_whatsappexp(self):
        selected_exp_product = self.ids.exppro_spinner.text
        entered_email = self.ids.email1.text

        if selected_exp_product == "Select product":
            toast("Please Fill The Empty Field !")
        else:
            self.transition.direction = 'left'
            self.current = 'exporter'
            connection = mysql.connector.connect(host="c96614.sgvps.net",user="uvjsrceoy8ma6",password="&2u*37e`12:P",database="dbmctchgw3sxy6")
            cur = connection.cursor()
            sql_select_importer = "SELECT exporter.company_name, exporter.website, exporter.email, exporter.phone, exporter.whatsapp, exporter.address, exporter.contact_person, exporter.social_media FROM exporter INNER JOIN `product_exporter`on exporter.exporterID = product_exporter.exporter_id INNER JOIN `product` ON product.ProductHscode = product_exporter.productthscode INNER JOIN user_product ON product.ProductHscode = user_product.product_hscode INNER JOIN user ON user.email = user_product.email_user WHERE user.email = %s and product.ProductName= %s;"
            cur.execute(sql_select_importer,(entered_email,selected_exp_product,))
            data = cur.fetchall()
            whatsapp_exp_list = []
            for index, item in enumerate(data):
                expcomp_whatsapp= data[index][4]
                if not expcomp_whatsapp == "":
                    whatsapp_exp_list.append(expcomp_whatsapp)

            print(whatsapp_exp_list)
            self.ids.whatsappexp_to_list.values = whatsapp_exp_list
    ###############################################################################
    ## exporter send WhatsApp
    ###############################################################################
    def send_whatsappexp(self):
        whatsapp_exp_list          = self.ids.whatsappexp_to_list
        whatsappexp_msg_input      = self.ids.whatsappexp_msg.text

        s=Service(ChromeDriverManager().install())
        options=Options()
        options.add_argument('--user-data-dir='+final_path+'chrome-data')
        options.add_experimental_option('excludeSwitches',['enable-automation'])
        options.add_experimental_option('useAutomationExtension',False)
        options.add_argument('--incognitos')
        driver = webdriver.Chrome(service=s,options=options)
        driver.get("https://web.whatsapp.com/")
        wait = WebDriverWait(driver, 800)
        driver.get("https://web.whatsapp.com/send?phone={}".format(whatsapp_exp_list))
        try:
            driver.switch_to.alert.accept()
        except:
            pass
        
        inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        input_box = wait.until(EC.presence_of_element_located((
            By.XPATH, inp_xpath)))
        input_box.send_keys(whatsappexp_msg_input + Keys.ENTER)
        time.sleep(2)

    ###############################################################################
    ## exporter send WhatsApp for All numbers 
    ###############################################################################

    def send_all_whatsappexp(self):
        whatsapp_exp_list          = self.ids.whatsappexp_to_list
        whatsappexp_msg_input      = self.ids.whatsappexp_msg.text

        whatsapp_list3=[]
        for i in whatsapp_exp_list.values:
            whatsapp_list3.append(i)
        print(whatsapp_list3)
        s=Service(ChromeDriverManager().install())
        options=Options()
        options.add_argument('--user-data-dir='+final_path+'chrome-data')
        options.add_experimental_option('excludeSwitches',['enable-automation'])
        options.add_experimental_option('useAutomationExtension',False)
        options.add_argument('--incognitos')
        driver = webdriver.Chrome(service=s,options=options)
        driver.get("https://web.whatsapp.com/")
        wait = WebDriverWait(driver, 800)
        for phone_number in whatsapp_list3:
            driver.get("https://web.whatsapp.com/send?phone={}".format(phone_number))
            try:
                driver.switch_to.alert.accept()
            except:
                pass
                
            inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
            input_box = wait.until(EC.presence_of_element_located((
                By.XPATH, inp_xpath)))
            input_box.send_keys(whatsappexp_msg_input + Keys.ENTER)
            time.sleep(2)


####################################################################################
    # Show & Hide user password
####################################################################################   
    def show_password(self, checkbox, value):
        if value:
            self.ids.password.password = False
            self.ids.password_text.text = "Hide Password"
        else:
            self.ids.password.password = True
            self.ids.password_text.text = "Show Password"
        
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.accent_palette = "Red"
        self.title = "E-Markets"
        self.icon = "images/em.png"
        Builder.load_string(KV)
        return MyNewApp()

if __name__ == '__main__':
    try:
        if getattr(sys, 'frozen', False):
            # this is a Pyinstaller bundle
            resource_add_path(sys._MEIPASS)
            resource_add_path(os.path.join(sys._MEIPASS, 'media'))
        app = MainApp()
        app.run()
    except Exception as e:
        print(e)
        input("Press enter.")

## Raghda Fouda      