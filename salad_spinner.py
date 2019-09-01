import random

try:
    from PyQt5.QtWidgets import *
except ImportError:
    err_msg = "\n\nPlease install Qt by running the following command:\npip install PyQt5\nand try again.\n\n"
    print(err_msg)
    raise ImportError(err_msg)
from PyQt5 import QtTest
# QtTest.QTest.qWait(1000)
from PyQt5.QtGui import QIcon, QPixmap


class SaladSpinner(QDialog):
    '''
    A slot machine for selecting salad ingredients

    TODO: Macros readout
    '''

    def __init__(self):
        self.base = ['lettuce', 'spinach', 'kale', 'chard', 'collards', 'arugula', 'pea_shoots', 'cabbage']
        self.crunch = ['carrots', 'sprouts', 'cucumber', 'croutons', 'zucchini', 'bell_pepper', 'apple', 'seeds']
        self.soft = ['roasted_sweet_potatoes', 'cheese', 'avocado', 'tomatoes', 'rice', 'olives']
        self.unexpected = ['watermelon_cubes', 'cottage_cheese', 'hummus', 'bacon', 'pickled_veggies', 'herbs', 'dried_fruit']
        self.protein = ['beans', 'eggs', 'tuna', 'chicken', 'steak', 'tofu', 'peas', 'quinoa', 'nuts']
        self.dressing = ['mustard_based', 'tahini_based', 'dairy_based', 'vinaigrette', 'pesto_based', 'fruity']

        self.sections = [self.base, self.crunch, self.soft, self.unexpected, self.protein, self.dressing]

        self.bad_combos = [
            ['pea shoots', 'sprouts'],
            ['cheese', 'cottage cheese'],
            ['dairy_based', 'cottage cheese'],
            ['steak', 'fruity'],
            ['croutons', 'rice'],
            ['vinaigrette', 'cottage cheese']
        ]

        self.salad = []

        QDialog.__init__(self)

        self.setWindowTitle("Salad Spinner")
        print("\n\nSalad Spinner\n\n")

        def load_images():
            self.lettuce_img = QPixmap('./images/lettuce.png')
            self.spinach_img = QPixmap('./images/spinach.png')
            self.kale_img = QPixmap('./images/kale.png')
            self.chard_img = QPixmap('./images/chard.png')
            self.collards_img = QPixmap('./images/collards.png')
            self.arugula_img = QPixmap('./images/arugula.png')
            self.pea_shoots_img = QPixmap('./images/pea_shoots.png')
            self.cabbage_img = QPixmap('./images/cabbage.png')
            self.base_imgs = [self.lettuce_img, self.spinach_img, self.kale_img, self.chard_img, self.collards_img, self.arugula_img, self.pea_shoots_img, self.cabbage_img]

            self.carrots_img = QPixmap('./images/carrots.png')
            self.sprouts_img = QPixmap('./images/sprouts.png')
            self.cucumber_img = QPixmap('./images/cucumber.png')
            self.croutons_img = QPixmap('./images/croutons.png')
            self.zucchini_img = QPixmap('./images/zucchini.png')
            self.bell_pepper_img = QPixmap('./images/bell_pepper.png')
            self.apple_img = QPixmap('./images/apple.png')
            self.seeds_img = QPixmap('./images/seeds.png')
            self.crunch_imgs = [self.carrots_img, self.sprouts_img, self.cucumber_img, self.croutons_img, self.zucchini_img, self.bell_pepper_img, self.apple_img, self.seeds_img]

            self.roasted_sweet_potatoes_img = QPixmap('./images/roasted_sweet_potatoes.png')
            self.cheese_img = QPixmap('./images/cheese.png')
            self.avocado_img = QPixmap('./images/avocado.png')
            self.tomatoes_img = QPixmap('./images/tomatoes.png')
            self.rice_img = QPixmap('./images/rice.png')
            self.olives_img = QPixmap('./images/olives.png')
            self.soft_imgs = [self.roasted_sweet_potatoes_img, self.cheese_img, self.avocado_img, self.tomatoes_img, self.rice_img, self.olives_img]

            self.watermelon_cubes_img = QPixmap('./images/watermelon_cubes.png')
            self.cottage_cheese_img = QPixmap('./images/cottage_cheese.png')
            self.hummus_img = QPixmap('./images/hummus.png')
            self.bacon_img = QPixmap('./images/bacon.png')
            self.pickled_veggies_img = QPixmap('./images/pickled_veggies.png')
            self.herbs_img = QPixmap('./images/herbs.png')
            self.dried_fruit_img = QPixmap('./images/dried_fruit.png')
            self.unexpected_imgs = [self.watermelon_cubes_img, self.cottage_cheese_img, self.hummus_img, self.bacon_img, self.pickled_veggies_img, self.herbs_img, self.dried_fruit_img]

            self.beans_img = QPixmap('./images/beans.png')
            self.eggs_img = QPixmap('./images/eggs.png')
            self.tuna_img = QPixmap('./images/tuna.png')
            self.chicken_img = QPixmap('./images/chicken.png')
            self.steak_img = QPixmap('./images/steak.png')
            self.tofu_img = QPixmap('./images/tofu.png')
            self.peas_img = QPixmap('./images/peas.png')
            self.quinoa_img = QPixmap('./images/quinoa.png')
            self.nuts_img = QPixmap('./images/nuts.png')
            self.protein_imgs = [self.beans_img, self.eggs_img, self.tuna_img, self.chicken_img, self.steak_img, self.tofu_img, self.peas_img, self.quinoa_img, self.nuts_img]

            self.mustard_based_img = QPixmap('./images/mustard_based.png')
            self.tahini_based_img = QPixmap('./images/tahini_based.png')
            self.dairy_based_img = QPixmap('./images/dairy_based.png')
            self.vinaigrette_img = QPixmap('./images/vinaigrette.png')
            self.pesto_based_img = QPixmap('./images/pesto_based.png')
            self.fruity_img = QPixmap('./images/fruity.png')
            self.dressing_imgs = [self.mustard_based_img, self.tahini_based_img, self.dairy_based_img, self.vinaigrette_img, self.pesto_based_img, self.fruity_img]

            self.img_groups = [self.base_imgs, self.crunch_imgs, self.soft_imgs, self.unexpected_imgs, self.protein_imgs, self.dressing_imgs]
        load_images()

        def set_widgets():
            self.picker1 = QComboBox()
            self.picker1.addItems(['base'] + self.base)
            self.picker2 = QComboBox()
            self.picker2.addItems(['crunch'] + self.crunch)
            self.picker3 = QComboBox()
            self.picker3.addItems(['soft'] + self.soft)
            self.picker4 = QComboBox()
            self.picker4.addItems(['unexpected'] + self.unexpected)
            self.picker5 = QComboBox()
            self.picker5.addItems(['protein'] + self.protein)
            self.picker6 = QComboBox()
            self.picker6.addItems(['dressing'] + self.dressing)
            self.pickers = [self.picker1, self.picker2, self.picker3, self.picker4, self.picker5, self.picker6]
            for i, picker in enumerate(self.pickers):
                picker.setObjectName("picker" + str(i))
                picker.setMinimumWidth(200)
                picker.currentIndexChanged.connect(self.pick)

            self.img_display_1 = QLabel("img_display_1")
            self.img_display_1.setPixmap(random.choice(self.base_imgs))
            self.img_display_2 = QLabel("img2")
            self.img_display_2.setPixmap(random.choice(self.crunch_imgs))
            self.img_display_3 = QLabel("img_display_3")
            self.img_display_3.setPixmap(random.choice(self.soft_imgs))
            self.img_display_4 = QLabel("img_display_4")
            self.img_display_4.setPixmap(random.choice(self.unexpected_imgs))
            self.img_display_5 = QLabel("img_display_5")
            self.img_display_5.setPixmap(random.choice(self.protein_imgs))
            self.img_display_6 = QLabel("img_display_6")
            self.img_display_6.setPixmap(random.choice(self.dressing_imgs))
            self.img_displays = [self.img_display_1, self.img_display_2, self.img_display_3, self.img_display_4, self.img_display_5, self.img_display_6]
            for i, img in enumerate(self.img_displays):
                img.setObjectName("img" + str(i))
                img.setMinimumWidth(200)
                img.setMinimumHeight(200)
                # img.clicked.connect(self.spin_one)

            self.all_spinner = QPushButton("SPIN\nALL!")
            self.all_spinner.setMinimumHeight(200)
            self.all_spinner.clicked.connect(self.spin_all)

            self.spinner1 = QPushButton("Spin this")
            self.spinner2 = QPushButton("Spin this")
            self.spinner3 = QPushButton("Spin this")
            self.spinner4 = QPushButton("Spin this")
            self.spinner5 = QPushButton("Spin this")
            self.spinner6 = QPushButton("Spin this")
            self.spinners = [self.spinner1, self.spinner2, self.spinner3, self.spinner4, self.spinner5, self.spinner6]
            for i, spinner in enumerate(self.spinners):
                spinner.setObjectName("spinner" + str(i))
                spinner.setMinimumWidth(200)
                spinner.clicked.connect(self.spin_one)

            self.lock_btn_1 = QPushButton("Lock")
            self.lock_btn_2 = QPushButton("Lock")
            self.lock_btn_3 = QPushButton("Lock")
            self.lock_btn_4 = QPushButton("Lock")
            self.lock_btn_5 = QPushButton("Lock")
            self.lock_btn_6 = QPushButton("Lock")
            self.lock_btns = [self.lock_btn_1, self.lock_btn_2, self.lock_btn_3, self.lock_btn_4, self.lock_btn_5, self.lock_btn_6]
            for i, lock_btn in enumerate(self.lock_btns):
                lock_btn.setObjectName("lock_btn" + str(i))
                lock_btn.setMinimumWidth(200)
                lock_btn.clicked.connect(self.lock)
        set_widgets()

        def build_layout():
            lock_btn_row = QHBoxLayout()

            picker_row = QHBoxLayout()
            img_row = QHBoxLayout()
            spinner_row = QHBoxLayout()
            lock_btn_row = QHBoxLayout()

            for i, picker in enumerate(self.pickers):
                picker_row.addWidget(picker, i * 10 + 10)
            for i, img in enumerate(self.img_displays):
                img_row.addWidget(img, i * 10 + 10)
            for i, spinner in enumerate(self.spinners):
                spinner_row.addWidget(spinner, i * 10 + 10)
            for i, lock_btn in enumerate(self.lock_btns):
                lock_btn_row.addWidget(lock_btn, i * 10 + 10)

            # Main layout
            layout = QGridLayout()
            layout.addWidget(self.all_spinner, 20, 0)
            layout.addLayout(picker_row, 10, 10)
            layout.addLayout(img_row, 20, 10)
            layout.addLayout(spinner_row, 30, 10)
            layout.addLayout(lock_btn_row, 40, 10)
            return layout
        layout = build_layout()

        self.setLayout(layout)

    def choose_good_salad(self):
        # Only go to 1000, just to avoid "while True" infinite loop
        for _ in range(1000):
            salad = [random.choice(section) for section in self.sections]

            # Weed out the bad ones
            for bad_combo in self.bad_combos:
                if all(ingredients in salad for ingredients in bad_combo):
                    continue

            # If it got to here, then it's all good!
            print(salad)
            return salad

    def pick(self):
        # Set this spinner to the picked value
        s = self.sender()
        num = int(s.objectName()[-1])
        img_display = self.img_displays[num]

        food = s.currentText()
        # To get the right image, we have to load it again, since we only have the name
        img_to_use = QPixmap('./images/' + food + '.png')
        img_display.setPixmap(img_to_use)

    def spin_all(self):
        # Spin all the spinners!
        delay = 0.001
        delay_increment = 0.001
        display_counter = 0
        choice_counter = 0
        while delay < 0.2:
            # Loop through all choices and displays, and update all images
            display_num = display_counter % len(self.img_displays)
            display_counter += 1

            if not self.is_locked(display_num):

                display_to_use = self.img_displays[display_num]

                choices = self.img_groups[display_num]
                # Cycle through them in order
                img_to_use = choices[choice_counter % len(choices)]
                # Or pick a random one for each tick
                if delay >= 0.4:
                    img_to_use = random.choice(choices)

                display_to_use.setPixmap(img_to_use)

            # Only slow down once per full loop
            if display_num == 0:
                QtTest.QTest.qWait(delay * 1000)
                delay += delay_increment
                delay_increment += 0.001
                choice_counter += 1

        # 'salad' looks like
        # ['pea_shoots', 'carrots', 'avocado', 'herbs', 'eggs', 'fruity']
        self.salad = self.choose_good_salad()
        for i, img_display in enumerate(self.img_displays):
            if not self.is_locked(i):
                # To get the right image, we have to load it again, since we only have the name
                img_to_use = QPixmap('./images/' + self.salad[i] + '.png')
                img_display.setPixmap(img_to_use)

    def spin_one(self):
        # Spin just this one spinner
        s = self.sender()
        num = int(s.objectName()[-1])
        img_display = self.img_displays[num]
        selection = self.img_groups[num]

        delay = 0.001
        delay_increment = 0.001
        counter = 0
        while delay < 0.2:
            if not self.is_locked(num):
                img_to_use = selection[counter % len(selection)]
                img_display.setPixmap(img_to_use)
                QtTest.QTest.qWait(delay * 1000)
                counter += 1
            delay += delay_increment
            delay_increment += 0.001

        if not self.is_locked(num):
            img_display.setPixmap(random.choice(selection))

    def lock(self):
        # Toggle the lock on the spinner in this place
        # Toggle the name of this button to UNLOCK or LOCK
        s = self.sender()
        num = int(s.objectName()[-1])
        text = self.lock_btns[num].text()
        if text.startswith("LOCKED"):
            s.setText("Lock")
        else:
            s.setText("LOCKED (click to unlock)")

    def is_locked(self, num):
        text = self.lock_btns[num].text()
        return text.startswith("LOCKED")

try:
    app = QApplication([])
    dialog = SaladSpinner()
    dialog.show()
    # dialog.load_objs()
    app.exec_()
except Exception as e:
    print(str(e))