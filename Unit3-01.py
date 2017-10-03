# Created by: Scarlett Gao
# Created on: Sep 2017
# Created for: ICS3U
# This program shows how to use an if statement

import ui

MAX_NUMBER_OF_STUDENTS = 5

def check_number_of_students_touch_up_inside(sender):
    # check the number of students entered verses the constant above
    
    # input
    number_entered = int(view['number_of_students_textfield'].text)
    
    # process
    if number_entered > MAX_NUMBER_OF_STUDENTS:
        # output
        view['too_many_students_label'].text = "Too many students!"
    
view = ui.load_view()
view.present('full_sheet')
