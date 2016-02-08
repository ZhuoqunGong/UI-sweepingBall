import eventBasedAnimation

def sweepingBallInitFn(data):
    (data.x, data.y) = (data.width/2, data.height/2)
    data.speed = 10
    data.aboutText = data.windowTitle = "Sweeping ball"

def sweepingBallKeyFn(event, data):
    if (event.keysym == "Up"):
        data.y = (data.y - data.speed) % data.height
    elif (event.keysym == "Down"):
        data.y = (data.y + data.speed) % data.height

def sweepingBallMouseFn(event, data):
    (data.x, data.y) = (event.x, event.y)

def sweepingBallStepFn(data):
    data.x = (data.x + data.speed) % data.width

def sweepingBallDrawFn(canvas, data):
    (cx, cy, r) = (data.x, data.y, 20)
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="chartreuse")
    canvas.create_text(data.width/2, 20,
                       text="up/down keys or mouse click anywhere")

eventBasedAnimation.run(
    initFn=sweepingBallInitFn,
    stepFn=sweepingBallStepFn,
    mouseFn=sweepingBallMouseFn,
    keyFn=sweepingBallKeyFn,
    drawFn=sweepingBallDrawFn,
    timerDelay=100,
    width=400,
    height=500
    )