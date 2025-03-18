#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division
import urwid


PALETTE = [
    ('normal', '', ''),
    ('bold', 'bold', ''),
    ('blue', 'bold', 'dark blue'),
    ('highlight', 'black', 'dark blue'),
]


def show_or_exit(key):
    if key in ('q', 'Q', 'esc'):
        raise urwid.ExitMainLoop()


class CustomButton(urwid.Button):
    button_left = urwid.Text('[')
    button_right = urwid.Text(']')


def custom_button(*args, **kwargs):
    b = CustomButton(*args, **kwargs)
    b = urwid.AttrMap(b, '', 'highlight')
    b = urwid.Padding(b, left=4, right=4)
    return b



if __name__ == '__main__':
    header = urwid.Text('Header')
    footer = urwid.Text('Footer')
    onclick = lambda w: footer.set_text('clicked: %r' % w)
    widget = urwid.Pile([
        header,
        urwid.Text('Simple custom buttons:'),
        urwid.Columns([
            custom_button('OK', on_press=onclick),
            custom_button('Cancel', on_press=onclick),
        ]),
        urwid.Text('Box bordered buttons:'),
        urwid.Columns([
            urwid.Padding(BoxButton('OK', on_press=onclick), left=4, right=4),
            BoxButton('Cancel', on_press=onclick),
        ]),
        footer,
    ])
    widget = urwid.Filler(widget, 'top')
    loop = urwid.MainLoop(widget, PALETTE, unhandled_input=show_or_exit)
    loop.run()