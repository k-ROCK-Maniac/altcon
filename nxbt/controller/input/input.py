""" Reads the inputs of the keyboard/gamepad/mouse and converts them to 
    their appropriate controller inputs 
"""

## Imports ##
import keyboard
import json


## Variables ##
config: str = str(open("../../../test/xdg.txt", "r").read())
config_json = json.load(open(config, "r"))

## Classes ##
class InputDevice:
    def __init__(self, profile: str):
        self.profile = profile
        self.keybinds = config_json[f"{self.profile}"]["keybinds"]

    def conv(self, input):
        """ Converts inputs to Nintendo Switch capable inputs. """
        nx_inputs = []
        
        for ctl_grp_id in self.keybinds:
            ctl_grp = self.keybinds[ctl_grp_id]
            if isinstance(ctl_grp, dict):
                nx_inputs = [f"{ctl_grp_id}_{ctl}" for ctl in ctl_grp if ctl_grp[ctl] == input]
            else:
                ctl_grp == input and nx_inputs.append(ctl_grp_id)
        
        if len(nx_inputs) > 1:
            print(f"The Nintendo Switch controls {', '.join(nx_inputs)} share the same binding! Executing both...") # This print statement is temporary, we can replace this with a notification once the GUI is set up
            return "\n".join(nx_inputs)

        if nx_inputs != []:
            return nx_inputs[0]

        return "Binding not found"


class Keyboard(InputDevice):
    def __init__(self, profile):
        super().__init__(profile)
        
    def listen(self):
        if keyboard.read_event(suppress=True).event_type == "down":
            return str(keyboard.read_key(suppress=True))


####### TESTING #######
dev = Keyboard("profile1")
while True:
    print(dev.conv(dev.listen()))




