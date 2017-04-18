# Author: Justin Gavin
# Description: A module to issue commands to a smartlight controller.
#               The IP of the controller should be specified in LIGHT_CONTROLLER_IP
#
#
# Note: this has been converted for demo purposes, uses the dummy_light instead of
#           ledcontroller


# import ledcontroller
from jargon.conf.module.light import dummy_light

LIGHT_CONTROLLER_IP = "10.0.0.30"


def module_main(args):
    command_string = args["command"]
    # led = ledcontroller.LedController(LIGHT_CONTROLLER_IP)
    led = dummy_light.dummy_light()

    if "off" in command_string:
        led.off()
        return
    if "on" in command_string:
        led.on()
    if "white" in command_string:
        led.white()
    if "red" in command_string:
        led.set_color("orange")
        # led.set_brightness(50)
    if "bright" in command_string:  # 'brighter' and 'brightness' also flags this
        if "brightness" in command_string:
            # assuming a numeric brightness level is specified, find it
            for i in command_string:
                if i.isdigit():
                    led.set_brightness(int(i))
                    return
        # if "brightness" not found, must be bright or brighter
        led.set_brightness(70)
        return
    if "dim" in command_string:
        led.set_brightness(30)
        return
# Example use:
# module_main({'command': 'on white brighter'})