import flet as ft

# --- Color Palette ---
BG_COLOR = "#281e3c"  # Dark Purple
NAV_BG_COLOR = "#3f1f4d"  # Light Purple
ACCENT_COLOR = "#ff9e43"  # Orange
UNSELECTED_COLOR = "#b3b3b3"  # Grey
TEXT_COLOR = "white"


def main(page: ft.Page):
    # --- Page Configuration ---
    page.title = "TurfPe"
    # Wrap theme_mode in try/except for safety on very old versions
    try:
        page.theme_mode = ft.ThemeMode.DARK
    except:
        page.theme_mode = "dark"

    page.bgcolor = BG_COLOR
    page.padding = 0

    # --- Content Area ---
    # We use a simple Column to center the text instead of "alignment.center"
    # This is the most compatible way to center things across all versions.
    body_content = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("Home", size=30, color=TEXT_COLOR, weight=ft.FontWeight.BOLD)
        ]
    )

    body_container = ft.Container(
        expand=True,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[body_content]
        )
    )

    # --- Custom Navigation Bar ---
    # We build this manually so it never crashes on "NavigationDestination" errors
    current_tab_index = 0

    def on_tab_click(e):
        nonlocal current_tab_index
        current_tab_index = e.control.data

        # Update Text
        tab_names = ["Home", "Team", "You", "Analytics", "Settings"]
        body_content.controls[0].value = tab_names[current_tab_index]

        # Update Icons
        nav_bar.content.controls = build_nav_icons()
        page.update()

    def build_nav_icons():
        icons = [
            ("home", "Home"),
            ("group", "Team"),
            ("person", "You"),
            ("analytics", "Analytics"),
            ("settings", "Settings")
        ]

        nav_items = []
        for index, (icon_name, label) in enumerate(icons):
            is_selected = (current_tab_index == index)
            color = ACCENT_COLOR if is_selected else UNSELECTED_COLOR

            nav_items.append(
                ft.Container(
                    expand=True,
                    padding=10,
                    data=index,
                    on_click=on_tab_click,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=2,
                        controls=[
                            # Use positional arguments for Icon (safe for all versions)
                            ft.Icon(icon_name, color=color, size=24),
                            ft.Text(label, color=color, size=10)
                        ]
                    )
                )
            )
        return nav_items

    nav_bar = ft.Container(
        bgcolor=NAV_BG_COLOR,
        height=70,
        content=ft.Row(
            spacing=0,
            controls=build_nav_icons()
        )
    )

    # --- Assemble Layout ---
    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[
                body_container,
                nav_bar
            ]
        )
    )


# Use target=main to satisfy older Flet versions
ft.app(target=main)