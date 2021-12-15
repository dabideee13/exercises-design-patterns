"""
Source: https://medium.com/design-patterns-in-python/undo-redo-pattern-in-python-70ade29644b3
"""

from abc import ABCMeta, abstractstaticmethod
import time


class ICommand(metaclass=ABCMeta):

    @abstractstaticmethod
    def execute(*args):
        pass


class IUndoRedo(metaclass=ABCMeta):

    @abstractstaticmethod
    def history():
        pass

    @abstractstaticmethod
    def undo():
        pass

    @abstractstaticmethod
    def redo():
        pass


class Slider(IUndoRedo):

    def __init__(self):
        self._commands = {}
        self._history = [(0.0, "OFF", ())]
        self._history_position = 0

    @property
    def history(self):
        return self._history

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name, *args):
        if command_name in self._commands.keys():
            self._history_position += 1
            self._commands[command_name].execute(args)

            if len(self._history) == self._history_position:
                self._history.append((time.time(), command_name, args))

            else:
                self._history = self._history[:self._history_position + 1]
                self._history[self._history_position] = {
                    time.time(): [command_name, args]
                }

        else:
            print(f"Command [{command_name}] not recognized")

    def undo(self):
        if self._history_position > 0:
            self._history_position -= 1
            self._commands[
                self._history[self._history_position][1]
            ].execute(self._history[self._history_position][2])

        else:
            print("nothing to undo")

    def redo(self):
        if self._history_position + 1 < len(self._history):
            self._history_position += 1
            self._commands[
                self._history[self._history_position][1]
            ].execute(self._history[self._history_position][2])

        else:
            print("nothing to redo")


class Heater:

    def set_to_max(self):
        print("Heater is ON and set to MAX (100%)")

    def set_to_percent(self, *args):
        print(f"Heater is ON and set to {args[0][0]}%")

    def turn_off(self):
        print("Heater is OFF")


class SliderMaxCommand(ICommand):

    def __init__(self, heater):
        self._heater = heater

    def execute(self, *args):
        self._heater.set_to_max()


class SliderPercentCommand(ICommand):

    def __init__(self, heater):
        self._heater = heater

    def execute(self, *args):
        self._heater.set_to_percent(args[0])


class SliderOffCommand(ICommand):

    def __init__(self, heater):
        self._heater = heater

    def execute(self, *args):
        self._heater.turn_off()


if __name__ == "__main__":

    HEATER = Heater()

    SLIDER_MAX = SliderMaxCommand(HEATER)
    SLIDER_PERCENT = SliderPercentCommand(HEATER)
    SLIDER_OFF = SliderOffCommand(HEATER)

    SLIDER = Slider()
    SLIDER.register("MAX", SLIDER_MAX)
    SLIDER.register("PERCENT", SLIDER_PERCENT)
    SLIDER.register("OFF", SLIDER_OFF)

    SLIDER.execute("PERCENT", 10)
    SLIDER.execute("PERCENT", 20)
    SLIDER.execute("PERCENT", 30)

    print(SLIDER.history)

    # SLIDER.undo()

    print(SLIDER.history)
