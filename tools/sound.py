"""Sound support has been removed.
This module now contains dummy functions used throughout the codebase so that
the rest of the application does not need to change."""


class Music:
    """Dummy music player used in place of pygame's mixer."""

    def __init__(self):
        self.playing = False

    def play(self, *_args, **_kwargs):
        self.playing = False

    def stop(self):
        self.playing = False

    def is_playing(self):
        return False


def play_click(*_args, **_kwargs):
    pass


def play_start(*_args, **_kwargs):
    pass


def play_move(*_args, **_kwargs):
    pass


def play_drag(*_args, **_kwargs):
    pass

