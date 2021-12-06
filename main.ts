let pocatek = 0
let povoleni = false
let suma = 0
povoleni = true
control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_A, EventBusValue.MICROBIT_BUTTON_EVT_UP, function on_microbit_id_button_a_evt_up() {
    
    povoleni = true
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    let suma = 0
    whaleysans.showNumber(suma)
})
basic.forever(function on_forever() {
    let time: number;
    
    if (input.buttonIsPressed(Button.A)) {
        time = control.millis() - pocatek
        if (time < 250 && povoleni == true) {
            suma += 1
            povoleni = false
            console.log(suma)
            whaleysans.showNumber(suma)
        } else if (time >= 250) {
            suma += 1
            whaleysans.showNumber(suma)
            basic.pause(150)
        }
        
    } else {
        pocatek = control.millis()
    }
    
})
