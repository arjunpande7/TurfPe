from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivy_garden.mapview import MapView, MapMarkerPopup


KV = '''

<TurfInfoCard>:
    orientation: "vertical"
    size_hint: None, None
    size: "280dp", "190dp"
    md_bg_color: 0.12, 0.12, 0.12, 1 
    radius: [15] 
    padding: "12dp"
    spacing: "8dp"
    
    #top row --------------------------------------------------------------
    BoxLayout: 
        size_hint_y: None
        height: "20dp"
        spacing: "5dp"
        
        MDCard: 
            size_hint: None, None
            size: "80dp", "20dp"
            md_bg_color: 0.1, 0.5, 0.1, 1 
            radius: [4]
            elevation: 0 
            padding: 0
            MDLabel: 
                text: "Competitive"
                font_style: "Caption"
                color: 0.5, 1, 0.5, 1
                halign: "center"
                pos_hint: {"center_y": .5}
        
        MDCard:
            size_hint: None, None
            size: "80dp", "20dp"
            md_bg_color: 0.3, 0.3, 0.3, 1 
            radius: [4]
            elevation: 0 
            padding: 0
            MDLabel: 
                text: "600 avg"
                font_style: "Caption"
                theme_text_color: "Custom"
                text_color: 0.8, 0.8, 0.8, 1
                halign: "center"
                pos_hint: {"center_y": .5}
    
    #title + price --------------------------------------------------------
    BoxLayout: 
        size_hint_y: None
        height: "30dp"
        MDLabel:
            text: root.turf_name
            bold: True
            theme_text_color: "Custom"
            text_color: "white"
            font_style: "Subtitle1"
            pos_hint: {"center_y": .5}
        
        BoxLayout:
            orientation: "vertical"
            size_hint_x: None
            width: "60dp"
            pos_hint: {"center_y": .5}
            MDLabel: 
                text: "₹xyz"
                bold: True
                halign: "right"
                theme_text_color: "Custom"
                text_color: "white"
                font_size: "14sp"
            MDLabel: 
                text: "per player"
                font_style: "Caption"
                halign: "right"
                theme_text_color: "Custom"
                text_color: 0.7, 0.7, 0.7, 1
    
    #time and location ----------------------------------------------
    BoxLayout:
        size_hint_y: None
        height: "30dp"
        spacing: "10dp"
        
        MDIcon:
            icon: "clock-outline"
            theme_text_color: "Custom"
            text_color: 0.6, 0.6, 0.6, 1
            font_size: "16sp"
            size_hint_x: None
            width: "20dp"
            pos_hint: {"center_y": .5}
        MDLabel:
            text: "7pm xx.xx.xx"
            font_style: "Caption"
            theme_text_color: "Custom"
            text_color: 0.8, 0.8, 0.8, 1
            pos_hint: {"center_y": .5}
            
        MDIcon: 
            icon: "map-marker-outline"
            theme_text_color: "Custom"
            text_color: 0.6, 0.6, 0.6, 1
            font_size: "16sp"
            size_hint_x: None
            width: "20dp"
            pos_hint: {"center_y": .5}
            
        MDLabel: 
            text: "Pitch A"
            font_style: "Caption"
            theme_text_color: "Custom"
            text_color: 0.8, 0.8, 0.8, 1
            pos_hint: {"center_y": .5}
    
    #players joined ----------------------------
    MDProgressBar:
        value: 80
        color: 0.2, 0.8, 0.2, 1
        size_hint_y: None
        height: "5dp"
    
    MDLabel: 
        text: "11/14 players joined"
        font_style: "Caption"
        theme_text_color: "Custom"
        text_color: 0.7, 0.7, 0.7, 1
        size_hint_y: None
        height: "15dp"
    
    #join button ------------------------------
    MDFillRoundFlatButton: 
        text: "First Payment then Enjoyment"
        size_hint_x: 1
        md_bg_color: 0.2, 0.8, 0.2, 1
        text_color: "black"
        bold: True
    
            
                
MDScreen:
    #main background color
    md_bg_color : 0, 0, 0, 1
    

    MDBottomNavigation:
        #the navigation bar
        panel_color : 0.1, 0.1, 0.1, 1
        
        #text when not interacted
        text_color_normal: 0.5, 0.5, 0.5, 1
        
        #text when interacted with
        text_color_active: 0.2, 0.6, 1, 1
        
        selected_color_background: 0, 0, 0, 0
        
        id: nav_bar
        
        #the changing interaction based on what tab you are on
        on_switch_tabs: app.on_tab_switch(*args)
     

        # Tab 1: Solo
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Solo'
            icon: 'account-badge'
            
            FloatLayout: 
                
                MapView:
                    lat: 28.4595
                    lon: 77.0266
                    zoom: 12
                    double_tap_zoom: True
                    
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    
                    MapMarkerPopup:
                        lat: 28.4091
                        lon: 77.0901
                        TurfInfoCard: 
                            turf_name: "FaceOff 7v7"
                        
                    MapMarkerPopup:
                        lat: 28.4252
                        lon: 77.0943
                        TurfInfoCard:
                            turf_name: "ClayGrounds Sec-56"
        

        # Tab 2: Team
        MDBottomNavigationItem:
            name: 'screen 2'
            text: ''
            icon: 'account-group'

            MDLabel:
                text: 'TEAM'
                halign: 'center'
                theme_text_color: "Custom"
                text_color: "white"

        # Tab 3: You
        MDBottomNavigationItem:
            name: 'screen 3'
            text: ''
            icon: 'arm-flex'

            MDLabel:
                text: 'You page'
                halign: 'center'
                theme_text_color: "Custom"
                text_color: "white"

        # Tab 4: Host
        MDBottomNavigationItem:
            name: 'screen 4'
            text: ''
            icon: 'human-capacity-increase'

            MDLabel:
                text: 'host a game'
                halign: 'center'
                theme_text_color: "Custom"
                text_color: "white"

        # Tab 5: Settings
        MDBottomNavigationItem:
            name: 'screen 5'
            text: ''
            icon: 'cog'

            MDLabel:
                text: 'Settings'
                halign: 'center'
                theme_text_color: "Custom"
                text_color: "white"
'''


from kivy.properties import StringProperty

class TurfInfoCard(MDCard):
    turf_name = StringProperty("Turf Name")

class TurfPeMVP(MDApp):
    tab_names ={
        "screen 1":"SOLO",
        "screen 2":"TEAM",
        "screen 3":"YOU",
        "screen 4":"HOST",
        "screen 5":"SETTINGS",
    }
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_string(KV)

    #instance_tabs is navi bar
    #instance_tab_label is which icon is clicked
    #instance_tab_screen_name is the name of the screen
    def on_tab_switch(self,instance_tabs, instance_tab_label,instance_tab_screen_name):

        all_screens = instance_tabs.ids.tab_manager.screens

        for screen in all_screens:
            if screen.header:
                screen.header.text = ""

        correct_text = self.tab_names.get(instance_tab_screen_name,"")
        instance_tab_label.text = correct_text




if __name__ == '__main__':
    TurfPeMVP().run()