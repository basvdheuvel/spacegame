from pygame.locals import *

def handle_event(event, game):
    '''
    Handle a PyGame event and dispatch it to the given game.
    '''

    # To avoid a crash when the event is not handled by the game, handle the
    # exception.
    try:
        if event.type == QUIT:
            game.on_exit()
        elif event.type >= USEREVENT:
            game.on_user(event)
        elif event.type == VIDEOEXPOSE:
            game.on_expose()
        elif event.type == VIDEORESIZE:
            game.on_resize(event)
        elif event.type == KEYUP:
            game.on_key_up(event)
        elif event.type == KEYDOWN:
            game.on_key_down(event)
        elif event.type == MOUSEMOTION:
            game.on_mouse_move(event)
        elif event.type == MOUSEBUTTONUP:
            if event.button == 0:
                game.on_lbutton_up(event)
            elif event.button == 1:
                game.on_mbutton_up(event)
            elif event.button == 2:
                game.on_rbutton_up(event)
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 0:
                game.on_lbutton_down(event)
            elif event.button == 1:
                game.on_mbutton_down(event)
            elif event.button == 2:
                game.on_rbutton_down(event)
        elif event.type == ACTIVEEVENT:
            if event.state == 1:
                if event.gain:
                    game.on_mouse_focus()
                else:
                    game.on_mouse_blur()
            elif event.state == 2:
                if event.gain:
                    game.on_input_focus()
                else:
                    game.on_input_blur()
            elif event.state == 4:
                if event.gain:
                    game.on_restore()
                else:
                    game.on_minimize()
    except AttributeError:
        pass
