pocatek = 0
povoleni = False
suma = 0
povoleni = True
def on_microbit_id_button_a_evt_up():
    global povoleni
    povoleni = True
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_A,
    EventBusValue.MICROBIT_BUTTON_EVT_UP,
    on_microbit_id_button_a_evt_up)

def on_button_pressed_b():
        suma=0
        whaleysans.show_number(suma)
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_forever():
    global suma, povoleni, pocatek
    if input.button_is_pressed(Button.A):
        time = control.millis() - pocatek
        if time < 250 and povoleni == True:
            suma += 1
            povoleni = False
            print(suma)
            whaleysans.show_number(suma)
        elif time>=250:
            suma += 1
            whaleysans.show_number(suma)
            basic.pause(150)
    else:
        pocatek = control.millis()
basic.forever(on_forever)