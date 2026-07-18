from kivy.lang import Builder
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import platform

# For runtime permission compliance on Android
if platform == 'android':
    from android.permissions import request_permissions, Permission

KV = '''
<CustomMascotButton>:
    orientation: 'horizontal'
    size_hint: (0.9, None)
    height: "110dp"
    spacing: "0dp"
    pos_hint: {"center_x": .5}

    # Left Profile Image Box (White Background with Black Border)
    BoxLayout:
        size_hint: (None, 1)
        width: "110dp"
        padding: "8dp"
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [18]
            Color:
                rgba: 0, 0, 0, 1
            Line:
                rounded_rectangle: (self.x, self.y, self.width, self.height, 18)
                width: 2

        Image:
            source: root.image_source
            allow_stretch: True
            keep_ratio: True

    # Spacer between square image and text bubble
    Widget:
        size_hint_x: None
        width: "12dp"

    # Right Content Area (Teal rounded button containing text)
    BoxLayout:
        size_hint: (1, 1)
        padding: ["20dp", "0dp"]
        canvas.before:
            Color:
                rgba: 0.31, 0.51, 0.46, 1  # #4e8276 custom hex equivalent
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [25]
            Color:
                rgba: 0, 0, 0, 1
            Line:
                rounded_rectangle: (self.x, self.y, self.width, self.height, 25)
                width: 2

        MDLabel:
            text: root.button_text
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1  # Solid Black Text
            font_style: "H6"
            bold: True
            valign: 'middle'
            halign: 'left'


<BarangaySubButton@ButtonBehavior+BoxLayout>:
    button_text: ""
    orientation: 'horizontal'
    size_hint_y: None
    height: "55dp"
    padding: ["15dp", "0dp"]
    canvas.before:
        Color:
            rgba: 0.22, 0.40, 0.36, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [12]
    MDLabel:
        text: root.button_text
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "Subtitle1"
        bold: True
        valign: 'middle'


# Root navigation layout to hold screen content and the sliding drawer
MDNavigationLayout:

    MDScreenManager:
        id: screen_manager 

        # -------------------------------------------------------------
        # 1. MAIN LANDING SCREEN
        # -------------------------------------------------------------
        MDScreen:
            name: 'main_screen'
            MDBoxLayout:
                orientation: 'vertical'

                MDTopAppBar:
                    title: "LegaSafe"
                    anchor_title: "left"
                    elevation: 4
                    md_bg_color: 0.22, 0.40, 0.36, 1
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                MDBottomNavigation:
                    id: bottom_nav
                    panel_color: 0.96, 0.96, 0.96, 1
                    selected_color_background: 0.69, 0.51, 0.28, 0.2
                    text_color_active: 0.22, 0.40, 0.36, 1

                    MDBottomNavigationItem:
                        name: 'location_screen'
                        text: 'Location'
                        icon: 'map-marker'

                        MDFloatLayout:
                            MDBoxLayout:
                                orientation: 'vertical'
                                size_hint: (1, None)
                                height: self.minimum_height
                                spacing: "30dp"
                                pos_hint: {"center_x": .5, "center_y": .5}

                                Image:
                                    source: "logo.png" 
                                    size_hint: None, None
                                    size: "160dp", "160dp"
                                    pos_hint: {"center_x": .5}

                                CustomMascotButton:
                                    button_text: "Volcanic Activity"
                                    image_source: "logo1.png"
                                    on_release: 
                                        app.on_button_click("Volcanic Activity")
                                        screen_manager.current = 'volcano_screen'

                                CustomMascotButton:
                                    button_text: "Flood"
                                    image_source: "logo2.png"
                                    on_release: 
                                        app.on_button_click("Flood")
                                        screen_manager.current = 'flood_screen'

                    MDBottomNavigationItem:
                        name: 'about_screen'
                        text: 'About'
                        icon: 'information'
                        
                        ScrollView:
                            MDBoxLayout:
                                orientation: 'vertical'
                                padding: "24dp"
                                spacing: "16dp"
                                size_hint_y: None
                                height: self.minimum_height

                                MDLabel:
                                    text: "LegaSafe App"
                                    font_style: "H4"
                                    bold: True
                                    halign: "center"
                                    size_hint_y: None
                                    height: self.texture_size[1]

                                MDLabel:
                                    text: "version: 1.0.1"
                                    font_style: "Subtitle1"
                                    theme_text_color: "Secondary"
                                    halign: "center"
                                    size_hint_y: None
                                    height: self.texture_size[1]

                                MDIcon:
                                    icon: "information-outline"
                                    pos_hint: {"center_x": .5}
                                    font_size: "48sp"
                                    theme_text_color: "Custom"
                                    text_color: 0.22, 0.40, 0.36, 1

                                MDLabel:
                                    text: "Story:"
                                    font_style: "H6"
                                    bold: True
                                    size_hint_y: None
                                    height: self.texture_size[1]

                                MDLabel:
                                    text: "LEGASAFE is a disaster preparedness and evacuation assistance app created for the people of Legazpi City, Albay. It combines Geographic Information Systems with mobile technology to provide real‑time evacuation routes and information on what to do before, during, and after the flood or the volcanic activity. The app guides residents to the nearest evacuation centers, shows their capacity and availability. Designed with inclusivity in mind, LEGASAFE offers a simple interface so that children, the elderly, and persons with disabilities can easily access life‑saving information. Its purpose is to bridge the gap in disaster preparedness by ensuring that every household has reliable evacuation guidance and timely hazard information, ultimately strengthening community resilience and safety."
                                    font_style: "Body1"
                                    size_hint_y: None
                                    height: self.texture_size[1]

                                MDSeparator:
                                    height: "1dp"

                                MDLabel:
                                    text: "Connect With:"
                                    font_style: "H6"
                                    bold: True
                                    size_hint_y: None
                                    height: self.texture_size[1]

                                MDLabel:
                                    text: "legasafe12@gmail.com"
                                    font_style: "Body1"
                                    theme_text_color: "Custom"
                                    text_color: 0.22, 0.40, 0.36, 1
                                    size_hint_y: None
                                    height: self.texture_size[1]

                                MDSeparator:
                                    height: "1dp"

                                MDLabel:
                                    text: "Developers:"
                                    font_style: "H6"
                                    bold: True
                                    size_hint_y: None
                                    height: self.texture_size[1]

                                MDLabel:
                                    text: "Abion, Maria Dalisa A.\\nAzupardo, Stephanie B.\\nPaluyo, Mark Francis E.\\nResare, Jerwin T."
                                    font_style: "Body1"
                                    line_height: 1.3
                                    size_hint_y: None
                                    height: self.texture_size[1]

        # -------------------------------------------------------------
        # 2. VOLCANIC ACTIVITY DASHBOARD (With 5 Sub-Buttons)
        # -------------------------------------------------------------
        MDScreen:
            name: 'volcano_screen'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Volcanic Activity Evacuation Center"
                    anchor_title: "left"
                    elevation: 4
                    md_bg_color: 0.22, 0.40, 0.36, 1
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'main_screen')]]
                
                ScrollView:
                    MDBoxLayout:
                        orientation: 'vertical'
                        padding: "20dp"
                        spacing: "15dp"
                        size_hint_y: None
                        height: self.minimum_height
                        
                        MDLabel:
                            text: "Volcanic Activity Evacuation Center"
                            font_style: "H5"
                            halign: "center"
                            bold: True
                            size_hint_y: None
                            height: "40dp"

                        BarangaySubButton:
                            button_text: "Barangay Padang"
                            on_release: screen_manager.current = 'v_sub1'

                        BarangaySubButton:
                            button_text: "Barangay Buyoan"
                            on_release: screen_manager.current = 'v_sub2'

                        BarangaySubButton:
                            button_text: "Barangay Matanag"
                            on_release: screen_manager.current = 'v_sub3'

                        BarangaySubButton:
                            button_text: "Barangay Bonga"
                            on_release: screen_manager.current = 'v_sub4'

                        BarangaySubButton:
                            button_text: "Barangay Mabinit"
                            on_release: screen_manager.current = 'v_sub5'

        # -------------------------------------------------------------
        # 3. FLOOD DASHBOARD (With All 22 Sub-Buttons)
        # -------------------------------------------------------------
        MDScreen:
            name: 'flood_screen'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Flood Evacuation Centers"
                    anchor_title: "left"
                    elevation: 4
                    md_bg_color: 0.22, 0.40, 0.36, 1
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'main_screen')]]
                
                ScrollView:
                    MDBoxLayout:
                        orientation: 'vertical'
                        padding: "20dp"
                        spacing: "15dp"
                        size_hint_y: None
                        height: self.minimum_height
                        
                        MDLabel:
                            text: "Flood Evacuation Center"
                            font_style: "H5"
                            halign: "center"
                            bold: True
                            size_hint_y: None
                            height: "40dp"

                        BarangaySubButton:
                            button_text: "Barangay Ilawod East"
                            on_release: screen_manager.current = 'f_sub1'

                        BarangaySubButton:
                            button_text: "Barangay Ilawod"
                            on_release: screen_manager.current = 'f_sub2'

                        BarangaySubButton:
                            button_text: "Barangay Ilawod West"
                            on_release: screen_manager.current = 'f_sub3'

                        BarangaySubButton:
                            button_text: "Barangay Rizal Street Area"
                            on_release: screen_manager.current = 'f_sub4'

                        BarangaySubButton:
                            button_text: "Barangay Bañadero"
                            on_release: screen_manager.current = 'f_sub5'

                        BarangaySubButton:
                            button_text: "Barangay Bonga"
                            on_release: screen_manager.current = 'f_sub6'

                        BarangaySubButton:
                            button_text: "Barangay Buyoan"
                            on_release: screen_manager.current = 'f_sub7'

                        BarangaySubButton:
                            button_text: "Barangay Cabangan"
                            on_release: screen_manager.current = 'f_sub8'

                        BarangaySubButton:
                            button_text: "Barangay Dita"
                            on_release: screen_manager.current = 'f_sub9'

                        BarangaySubButton:
                            button_text: "Barangay Gogon"
                            on_release: screen_manager.current = 'f_sub10'

                        BarangaySubButton:
                            button_text: "Barangay Imperial Court Subdivision"
                            on_release: screen_manager.current = 'f_sub11'

                        BarangaySubButton:
                            button_text: "Barangay Mabinit"
                            on_release: screen_manager.current = 'f_sub12'

                        BarangaySubButton:
                            button_text: "Barangay Maoyod"
                            on_release: screen_manager.current = 'f_sub13'

                        BarangaySubButton:
                            button_text: "Barangay Matanag"
                            on_release: screen_manager.current = 'f_sub14'

                        BarangaySubButton:
                            button_text: "Barangay Oro Site"
                            on_release: screen_manager.current = 'f_sub15'

                        BarangaySubButton:
                            button_text: "Barangay Padang"
                            on_release: screen_manager.current = 'f_sub16'

                        BarangaySubButton:
                            button_text: "Barangay Rawis"
                            on_release: screen_manager.current = 'f_sub17'

                        BarangaySubButton:
                            button_text: "Barangay San Joaquin"
                            on_release: screen_manager.current = 'f_sub18'

                        BarangaySubButton:
                            button_text: "Barangay San Roque"
                            on_release: screen_manager.current = 'f_sub19'

                        BarangaySubButton:
                            button_text: "Barangay Tula-tula"
                            on_release: screen_manager.current = 'f_sub20'

                        BarangaySubButton:
                            button_text: "Barangay North Victory Village"
                            on_release: screen_manager.current = 'f_sub21'

                        BarangaySubButton:
                            button_text: "Barangay South Victory"
                            on_release: screen_manager.current = 'f_sub22'

        # -------------------------------------------------------------
        # 4. VOLCANO SUB-SCREENS
        # -------------------------------------------------------------
        MDScreen:
            name: 'v_sub1'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Padang"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'volcano_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'v_sub2'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Buyoan"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'volcano_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'v_sub3'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Matanag"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'volcano_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'v_sub4'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Bonga"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'volcano_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'v_sub5'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Mabinit"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'volcano_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        # -------------------------------------------------------------
        # 5. FLOOD SUB-SCREENS
        # -------------------------------------------------------------
        MDScreen:
            name: 'f_sub1'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Ilawod East"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub2'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Ilawod"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub3'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Ilawod West"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub4'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Rizal Street Area"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub5'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Bañadero"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub6'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Bonga"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub7'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Buyoan"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub8'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Cabangan"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub9'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Dita"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub10'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Gogon"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub11'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Imperial Court Subdivision"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub12'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Mabinit"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub13'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Maoyod"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub14'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Matanag"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub15'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Oro Site"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub16'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Padang"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub17'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Rawis"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub18'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay San Joaquin"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub19'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay San Roque"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub20'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay Tula-tula"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub21'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay North Victory Village"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        MDScreen:
            name: 'f_sub22'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Barangay South Victory Village"
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'flood_screen')]]
                MDLabel:
                    text: "Current Evacuation Center"
                    halign: 'center'

        # -------------------------------------------------------------
        # 6. SETTING SCREEN
        # -------------------------------------------------------------
        MDScreen:
            name: 'setting_screen'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Setting"
                    anchor_title: "left"
                    elevation: 4
                    md_bg_color: 0.22, 0.40, 0.36, 1
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'main_screen')]]
                
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: "24dp"
                    spacing: "15dp"

                    MDLabel:
                        text: "App Interface Customization"
                        font_style: "H5"
                        bold: True
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Select your layout visualization mode. Switching modes dynamically alters base structural tones."
                        font_style: "Body1"
                        theme_text_color: "Secondary"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDSeparator:
                        height: "1dp"

                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: "48dp"
                        spacing: "10dp"
                        MDCheckbox:
                            id: light_checkbox
                            group: "theme_group"
                            active: True
                            size_hint: None, None
                            size: "48dp", "48dp"
                            on_active: if self.active: app.set_theme_mode("Light")
                        MDLabel:
                            text: "Light Mode Style Layout"
                            font_style: "Body1"
                            valign: 'middle'

                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: "48dp"
                        spacing: "10dp"
                        MDCheckbox:
                            id: dark_checkbox
                            group: "theme_group"
                            active: False
                            size_hint: None, None
                            size: "48dp", "48dp"
                            on_active: if self.active: app.set_theme_mode("Dark")
                        MDLabel:
                            text: "Dark Mode Style Layout"
                            font_style: "Body1"
                            valign: 'middle'
                    Widget:

        # -------------------------------------------------------------
        # 7. ACCESS SCREEN
        # -------------------------------------------------------------
        MDScreen:
            name: 'access_screen'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "Access Control"
                    anchor_title: "left"
                    elevation: 4
                    md_bg_color: 0.22, 0.40, 0.36, 1
                    left_action_items: [["arrow-left", lambda x: setattr(screen_manager, 'current', 'main_screen')]]
                
                MDFloatLayout:
                    Button:
                        text: "Locate Access"
                        size_hint: (0.6, None)
                        height: "50dp"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        on_release: app.request_location_permission()

    # Sliding Navigation Drawer Component
    MDNavigationDrawer:
        id: nav_drawer
        radius: (0, 16, 16, 0)
        MDNavigationDrawerMenu:
            MDNavigationDrawerHeader:
                title: "Menu"
                text: "Navigation Options"
                spacing: "12dp"
                padding: "16dp", "16dp", "16dp", "16dp"
                Image:
                    source: "logo.png" 
                    size_hint: None, None
                    size: "72dp", "72dp" 
                    pos_hint: {"left": 1}

            MDNavigationDrawerItem:
                icon: "map-marker"
                text: "Location"
                on_release: 
                    nav_drawer.set_state("close")
                    screen_manager.current = 'main_screen'
                    bottom_nav.switch_tab('location_screen')

            MDNavigationDrawerItem:
                icon: "cog"
                text: "Setting"
                on_release: 
                    nav_drawer.set_state("close")
                    screen_manager.current = 'setting_screen'

            MDNavigationDrawerItem:
                icon: "key"
                text: "Access"
                on_release: 
                    nav_drawer.set_state("close")
                    screen_manager.current = 'access_screen'

            MDNavigationDrawerItem:
                icon: "information"
                text: "About Us"
                on_release: 
                    nav_drawer.set_state("close")
                    screen_manager.current = 'main_screen'
                    bottom_nav.switch_tab('about_screen')
'''

class CustomMascotButton(ButtonBehavior, BoxLayout):
    button_text = StringProperty("Button")
    image_source = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LegaSafeApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Amber" 
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def set_theme_mode(self, mode_name):
        self.theme_cls.theme_style = mode_name

    def on_button_click(self, button_title):
        print(f"'{button_title}' button clicked smoothly!")

    def request_location_permission(self):
        if platform == 'android':
            request_permissions([Permission.ACCESS_FINE_LOCATION, Permission.ACCESS_COARSE_LOCATION])
        else:
            content = BoxLayout(orientation='vertical', padding=10, spacing=10)
            lbl = Label(text="Allow LegaSafe to access your device location?")
            btn_layout = BoxLayout(spacing=10, size_hint_y=None, height=40)
            btn_allow = Button(text="Allow")
            btn_while = Button(text="While using app")
            btn_deny = Button(text="Deny")
            
            btn_layout.add_widget(btn_allow)
            btn_layout.add_widget(btn_while)
            btn_layout.add_widget(btn_deny)
            content.add_widget(lbl)
            content.add_widget(btn_layout)
            
            popup = Popup(title='Permission Requirement', content=content, size_hint=(0.8, 0.4))
            btn_allow.bind(on_release=lambda x: [print("Allowed"), popup.dismiss()])
            btn_while.bind(on_release=lambda x: [print("While Using"), popup.dismiss()])
            btn_deny.bind(on_release=lambda x: [print("Denied"), popup.dismiss()])
            popup.open()


if __name__ == '__main__':
    LegaSafeApp().run()
    