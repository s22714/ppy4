def calc_panel_number(podlogaL, podlogaSz, panelL, panelSz, panelIwOpak):
    pomieszczeniePow = podlogaL * podlogaSz
    print(pomieszczeniePow)

    pomieszczeniePow += pomieszczeniePow*0.1
    print(pomieszczeniePow)

    panelPow = panelL * panelSz
    print(panelPow)

    ilePaneliWPomieszczeniu = pomieszczeniePow / panelPow
    print(ilePaneliWPomieszczeniu)

    print(f"Potrzeba: {round(ilePaneliWPomieszczeniu/panelIwOpak)}")


