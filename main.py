from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
import random

FONT = "gui_assets/font/Knewave-Regular.ttf"

# Untuk Halaman Home
class HomePage(Entity):
    def __init__(self):
        super().__init__()

        print("Initializing Home Page")
        self.main_menu = Entity(
            parent=self,
            enabled=True,
        )

        Entity(
            model="quad",
            parent=self.main_menu,
            position=(0, 0, 1),
            scale=(200 / 12, 141 / 12),
            texture="gui_assets/home_bg.gif",
        )

        Entity(
            model="quad",
            parent=self.main_menu,
            position=(0.15, -1, 0.02),
            scale=(579 / 140, 434 / 140),
            texture="gui_assets/mbim.png",
        )

        # self.title = Text(
        #     text="Pakuan Racing",
        #     position=(-0.5, 0.4, 0),
        #     scale=2,
        #     font=FONT,
        #     color=color.rgb(55 / 255, 31 / 255, 83 / 255),
        #     parent=self.main_menu,
        #     enabled=True,
        # )

        Entity(
            parent=self.main_menu,
            model="quad",
            texture="gui_assets/unpak_racing_logo.png",
            position=(0, 2.5, 0),
            scale=(825 / 100, 466 / 100),
        )

        self.start_button = Button(
            text="Start Game",
            color=color.rgba(1, 1, 1, 0.8),
            scale=(5, 1),
            y=-0.1,
            parent=self.main_menu,
            radius=0.25,
            highlight_color=color.rgba(161 / 255, 89 / 255, 1, 0.8),
        )
        self.start_button.text_entity.font = FONT
        self.start_button.text_entity.color = color.rgb(55 / 255, 31 / 255, 83 / 255)
        self.start_button.on_click = self.start_game

        self.settings_button = Button(
            text="Settings",
            color=color.rgba(1, 1, 1, 0.8),
            scale=(5, 1),
            y=-1.3,
            parent=self.main_menu,
            radius=0.25,
            highlight_color=color.rgba(161 / 255, 89 / 255, 1, 0.8),
        )
        self.settings_button.text_entity.font = FONT
        self.settings_button.text_entity.color = color.rgb(55 / 255, 31 / 255, 83 / 255)
        self.settings_button.on_click = self.show_settings

        self.quit_button = Button(
            text="Quit",
            color=color.rgba(1, 1, 1, 0.8),
            scale=(5, 1),
            y=-2.5,
            parent=self.main_menu,
            radius=0.25,
            highlight_color=color.rgba(161 / 255, 89 / 255, 1, 0.8),
        )
        self.quit_button.text_entity.font = FONT
        self.quit_button.text_entity.color = color.red
        self.quit_button.on_click = application.quit

    def start_game(self):
        print("Start Game button clicked")
        self.disable()
        gameplay.enable()

    def show_settings(self):
        print("Settings button clicked")
        self.disable()
        settings_page.enable()


# Untuk Halaman Settings
class SettingPage(Entity):
    def __init__(self):
        super().__init__()

        print("Initializing Setting Page")
        self.game_settings = Entity(
            parent=self,
            enabled=True,
        )

        Entity(
            model="quad",
            parent=self.game_settings,
            position=(0, 0, 1),
            scale=(500 / 30, 283 / 30),
            texture="gui_assets/settings_bg.gif",
        )

        Entity(
            parent=self.game_settings,
            model="quad",
            texture="gui_assets/unpak_racing_logo.png",
            position=(5, 3.4, 0),
            scale=(825 / 250, 466 / 250),
        )

        self.back_button = Button(
            text="Back",
            color=color.rgba(1, 1, 1, 0.8),
            scale=(3, 0.8),
            position=(-5, 3.4, 0),
            parent=self.game_settings,
            radius=0.25,
            highlight_color=color.rgba(161 / 255, 89 / 255, 1, 0.8),
            enabled=False,
        )
        self.back_button.text_entity.font = FONT
        self.back_button.text_entity.color = color.rgb(55 / 255, 31 / 255, 83 / 255)
        self.back_button.on_click = self.go_back

        self.container = Entity(
            model="quad",
            color=color.rgba(55 / 255, 31 / 255, 83 / 255, 0.6),
            scale=(10, 5),
            position=(-1.5, 0, 0),
            enabled=False,
        )

        self.music_dropdown = DropdownMenu(
            "Music: On",
            buttons=[DropdownMenuButton("On"), DropdownMenuButton("Off")],
            position=(-5, 1.8, -0.02),
            scale=(7, 0.7),
            enabled=False,
        )
        self.music_dropdown.parent = self.game_settings

        self.volume_slider = Slider(
            min=0,
            max=100,
            default=100,
            position=(-3.8, 0, -0.01),
            text="Volume",
            scale=(10, 10),
            enabled=False,
        )
        self.volume_slider.parent = self.game_settings

    def enable(self):
        super().enable()
        self.back_button.enabled = True
        self.container.enabled = True
        self.music_dropdown.enabled = True
        self.volume_slider.enabled = True

    def disable(self):
        super().disable()
        self.back_button.enabled = False
        self.container.enabled = False
        self.music_dropdown.enabled = False
        self.volume_slider.enabled = False

    def go_back(self):
        print("Back button clicked")
        self.disable()
        home_page.enable()


# Untuk Gameplay
class GamePlay(Entity):
    def __init__(self):
        super().__init__()

        print("Initializing Game Play")
        self.gameplay_elements = []

        self.car = Entity(
            model="quad",
            texture="gameplay_assets/car",
            collider="box",
            scale=(5 / 3.5, 2 / 3.5),
            rotation_z=90,
            y=-3,
            enabled=False,
        )
        self.gameplay_elements.append(self.car)

        self.road_1 = Entity(
            model="quad", texture="gameplay_assets/road", scale=9, z=1, enabled=False
        )
        # y=9 (= scale) agar tile persis nyambung tanpa celah
        self.road_2 = duplicate(self.road_1, y=9, enabled=False)
        self.pair = [self.road_1, self.road_2]
        self.gameplay_elements.extend(self.pair)

        self.enemies = []
        self.spawning = False  # Flag untuk kontrol spawn musuh
        self.game_active = False

        # --- Game Over Screen (UI layer) ---
        self.game_over_screen = Entity(parent=camera.ui, enabled=False)

        Entity(
            parent=self.game_over_screen,
            model="quad",
            color=color.rgba(0, 0, 0, 0.75),
            scale=(2, 2),
            z=1,
        )

        Text(
            text="GAME OVER",
            parent=self.game_over_screen,
            origin=(0, 0),
            y=0.12,
            scale=5,
            font=FONT,
            color=color.red,
            z=0,
        )

        self.retry_button = Button(
            text="Play Again",
            parent=self.game_over_screen,
            y=-0.02,
            scale=(0.32, 0.08),
            color=color.rgba(1, 1, 1, 0.9),
            highlight_color=color.rgba(161 / 255, 89 / 255, 1, 0.9),
            radius=0.15,
            z=0,
        )
        self.retry_button.text_entity.font = FONT
        self.retry_button.text_entity.color = color.rgb(55 / 255, 31 / 255, 83 / 255)
        self.retry_button.on_click = self.retry

        self.menu_button = Button(
            text="Main Menu",
            parent=self.game_over_screen,
            y=-0.12,
            scale=(0.32, 0.08),
            color=color.rgba(1, 1, 1, 0.9),
            highlight_color=color.rgba(161 / 255, 89 / 255, 1, 0.9),
            radius=0.15,
            z=0,
        )
        self.menu_button.text_entity.font = FONT
        self.menu_button.text_entity.color = color.rgb(55 / 255, 31 / 255, 83 / 255)
        self.menu_button.on_click = self.go_to_menu

    def newenemy(self):
        if not self.spawning:
            return
        val = random.uniform(-4 / 3.5, 3 / 3.5)
        new = Entity(
            model="quad",
            texture="gameplay_assets/enemy",
            x=2 * val / 3.5,
            y=25 / 3.5,
            color=color.random_color(),
            rotation_z=-90 if val < 0 else 90,
            enabled=True,
            scale=(5 / 3.5, 2 / 3.5),
        )
        self.enemies.append(new)
        self.gameplay_elements.append(new)
        invoke(self.newenemy, delay=1)  # Lanjut spawn selama spawning=True

    def show_game_over(self):
        self.game_active = False
        self.spawning = False
        self.game_over_screen.enabled = True

    def retry(self):
        self.game_over_screen.enabled = False
        # Reset posisi mobil
        self.car.x = 0
        self.car.y = -3
        # Reset jalan
        self.road_1.y = 0
        self.road_2.y = 9
        # Hancurkan semua musuh
        for enemy in self.enemies[:]:
            if enemy in self.gameplay_elements:
                self.gameplay_elements.remove(enemy)
            destroy(enemy)
        self.enemies.clear()
        # Mulai lagi
        self.game_active = True
        self.spawning = True
        invoke(self.newenemy, delay=1)

    def go_to_menu(self):
        self.game_over_screen.enabled = False
        self.disable()
        home_page.enable()

    def enable(self):
        super().enable()
        print("Gameplay enabled")
        # Reset posisi jalan & mobil setiap kali masuk gameplay
        self.car.x = 0
        self.car.y = -3
        self.road_1.y = 0
        self.road_2.y = 9
        for element in self.gameplay_elements:
            element.enabled = True
        self.game_active = True
        if not self.spawning:
            self.spawning = True
            invoke(self.newenemy, delay=1)  # Mulai spawn musuh

    def disable(self):
        self.spawning = False  # Hentikan spawn musuh
        # Hancurkan semua musuh yang ada
        for enemy in self.enemies[:]:
            if enemy in self.gameplay_elements:
                self.gameplay_elements.remove(enemy)
            destroy(enemy)
        self.enemies.clear()
        super().disable()
        print("Gameplay disabled")
        for element in self.gameplay_elements:
            element.enabled = False

    def control_car(self):
        self.car.x -= held_keys["left arrow"] * 5 * time.dt
        self.car.x += held_keys["right arrow"] * 5 * time.dt
        self.car.y -= held_keys["down arrow"] * 2 * time.dt
        self.car.y += held_keys["up arrow"] * 2 * time.dt

    def move_roads(self):
        for road in self.pair:
            road.y -= 3 * time.dt
            # Saat tile keluar layar bawah, langsung sambung ke atas (2 * scale = 18)
            if road.y < -9:
                road.y += 18

    def move_enemies(self):
        for enemy in self.enemies[:]:
            if not enemy:  # Ensure the enemy is valid
                continue
            if enemy.x < 0:
                enemy.y -= 10 * time.dt
            else:
                enemy.y -= 5 * time.dt
            if enemy.y < -15:
                if enemy in self.enemies:
                    self.enemies.remove(enemy)
                destroy(enemy)
            elif enemy in self.enemies and self.car.intersects(enemy).hit:
                print("Collision detected! Game Over")
                self.show_game_over()
                return

    def updategame(self):
        if not self.game_active:
            return
        self.control_car()
        self.move_roads()
        self.move_enemies()


app = Ursina(icon="gui_assets/unpak_racing_icon.ico", fullscreen=True)

home_page = HomePage()
settings_page = SettingPage()
gameplay = GamePlay()

settings_page.enabled = False
gameplay.enabled = False


def update():
    if gameplay.enabled:
        gameplay.updategame()

def input(key):
    if key == 'escape':
        application.quit()

app.run()
