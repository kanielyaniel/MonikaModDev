# stuff

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="dev_gradual_zoom_test",
            category=["dev"],
            prompt="GRADUAL ZOOM TEST",
            pool=True,
            unlocked=True
        )
    )

label dev_gradual_zoom_test:
    m 1eua "first I reset my zoom to normal, Fast!"
    $ store.mas_sprites.reset_zoom()

    m "now to become max zoom, with a 0.00005 in between"
    $ store.mas_sprites.gradual_zoom(20, 0.00005)

    m "now to become min zoom, with a 0.000005 in between"
    $ store.mas_sprites.gradual_zoom(0, 0.000005)

    m "ookay! i think we did a good!"
    m "lets gradual reset though!"
    $ store.mas_sprites.reset_zoom(True, 0.000001)

    m "think that was good!"
    return
