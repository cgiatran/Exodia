import uvage
from pygame import mixer
import random
mixer.init()
mixer.music.load("Heaven.mp3")
mixer.music.play()
camera = uvage.Camera(800,600)
background = uvage.from_image(400,300,"Untitled_Artwork 2.png")
background.width = 800
OctoSquish_images = uvage.load_sprite_sheet("OctoSquish.png",1,4)
PineSquish_images = uvage.load_sprite_sheet("PineSquish.png",1,4)
OctoSquish = uvage.from_image(400,400,OctoSquish_images[0])
PineSquish = uvage.from_image(400,400,PineSquish_images[0])
restart_images = uvage.load_sprite_sheet("EnterRestart.png",2,1)
restart_int = 0
restart_text = uvage.from_image(400,200, restart_images[restart_int])
clicksquish_images = uvage.load_sprite_sheet("ClickSquish.png",2,1)
clicksquish_int = 0
clicksquish_text = uvage.from_image(400,500, clicksquish_images[clicksquish_int])
squishmallows = [
    [uvage.from_image(400,400,OctoSquish_images[0]), uvage.load_sprite_sheet("OctoSquish.png",1,4)],
    [uvage.from_image(400,400,PineSquish_images[0]), uvage.load_sprite_sheet("PineSquish.png",1,4)]
]
arrows = uvage.load_sprite_sheet("Arrows.png",4,2)
base_arrows_list = [
    ["left arrow", uvage.from_image(250,500,arrows[0]), False, False],
    ["up arrow", uvage.from_image(450,500,arrows[2]), False, False],
    ["right arrow", uvage.from_image(550,500,arrows[4]), False, False],
    ["down arrow", uvage.from_image(350,500,arrows[6]), False, False]
]
falling_arrows_list = [
    ["left arrow", uvage.from_image(250,0,arrows[0]), False, False],
    ["up arrow", uvage.from_image(450,-200,arrows[2]), False, False],
    ["right arrow", uvage.from_image(550,-400,arrows[4]), False, False],
    ["down arrow", uvage.from_image(350,-600,arrows[6]), False, False],
]
game_end = False
coordinate = -800
arrow_total = 1
def generate_arrows():
    global coordinate
    y = random.randint(1,10)
    if y > 3:
        x = random.randint(1, 4)
        if x == 1:
            arrow = ["left arrow",uvage.from_image(250,coordinate,arrows[0]),False, False]
        if x == 2:
            arrow = ["down arrow",uvage.from_image(350,coordinate,arrows[6]),False, False]
        if x == 3:
            arrow = ["up arrow",uvage.from_image(450,coordinate,arrows[2]),False, False]
        if x == 4:
            arrow = ["right arrow",uvage.from_image(550,coordinate,arrows[4]),False, False]
    if y <= 3:
        x = random.randint(5,10)
        if x == 5:
            arrow = ["right arrow",uvage.from_image(550,coordinate,arrows[4]),False, False]
            arrow1 = ["down arrow",uvage.from_image(350,coordinate,arrows[6]),False, False]
            falling_arrows_list.append(arrow1)
        if x == 6:
            arrow = ["right arrow",uvage.from_image(550,coordinate,arrows[4]),False, False]
            arrow1 = ["up arrow",uvage.from_image(450,coordinate,arrows[2]),False, False]
            falling_arrows_list.append(arrow1)
        if x == 7:
            arrow = ["right arrow", uvage.from_image(550, coordinate, arrows[4]), False, False]
            arrow1 = ["left arrow", uvage.from_image(250, coordinate, arrows[0]), False, False]
            falling_arrows_list.append(arrow1)
        if x == 8:
            arrow1 = ["down arrow", uvage.from_image(350, coordinate, arrows[6]), False, False]
            arrow = ["up arrow",uvage.from_image(450,coordinate,arrows[2]),False, False]
            falling_arrows_list.append(arrow1)
        if x == 9:
            arrow1 = ["down arrow", uvage.from_image(350, coordinate, arrows[6]), False, False]
            arrow = ["left arrow", uvage.from_image(250, coordinate, arrows[0]), False, False]
            falling_arrows_list.append(arrow1)
        if x == 10:
            arrow1 = ["up arrow",uvage.from_image(450,coordinate,arrows[2]),False, False]
            arrow = ["left arrow", uvage.from_image(250, coordinate, arrows[0]), False, False]
            falling_arrows_list.append(arrow1)
    falling_arrows_list.append(arrow)
    coordinate -= 200
def falling_arrows():
    if len(falling_arrows_list) < arrow_total+1:
        generate_arrows()
    for arrow in falling_arrows_list:
        if not arrow[2]:
            arrow[1].y += 10
            camera.draw(arrow[1])
        if arrow[0] == "left arrow":
            left_arrow = base_arrows_list[0]
            if arrow[1].y in range(450,550) and left_arrow[2]:
                arrow[2] = True
                generate_feedback(arrow[1])
        if arrow[0] == "up arrow":
            up_arrow = base_arrows_list[1]
            if arrow[1].y in range(450,550) and up_arrow[2]:
                arrow[2] = True
                generate_feedback(arrow[1])
        if arrow[0] == "right arrow":
            right_arrow = base_arrows_list[2]
            if arrow[1].y in range(450,550) and right_arrow[2]:
                arrow[2] = True
                generate_feedback(arrow[1])
        if arrow[0] == "down arrow":
            down_arrow = base_arrows_list[3]
            if arrow[1].y in range(450,550) and down_arrow[2]:
                arrow[2] = True
                generate_feedback(arrow[1])
feedback_list = []
def generate_feedback(arrow):
    arrow.y = abs(500-arrow.y)
    score = ""
    if 12.5 >= arrow.y >= 0:
        score = "Perfect!"
    if 25 >= arrow.y > 12.5:
        score = "Good!"
    if 37.5 >= arrow.y > 25:
        score = "Okay!"
    if 50 <= arrow.y < 37.5:
        score = "Miss!"
    feedback = [score,uvage.from_text(arrow.x - 20, 500 - 10, score, 30, "light blue")]
    feedback_list.append(feedback)
def draw_feedback():
    if len(feedback_list) > 0:
        for feedback in feedback_list:
            camera.draw(feedback[1])
            feedback[1].y -= 10
def calculate_score():
    global feedback_list
    perfect_count = 0
    good_count = 0
    okay_count = 0
    miss_count = 0
    for feedback in feedback_list:
        if feedback[0] == "Perfect!":
            perfect_count += 1
        if feedback[0] == "Good!":
            good_count += 1
        if feedback[0] == "Okay!":
            okay_count += 1
        if feedback[0] == "Miss!":
            miss_count += 1
    return [perfect_count,good_count,okay_count,miss_count]
def base_arrows():
    squishmallow = squishmallows[squishmallow_integer][0]
    squishmallow_images = squishmallows[squishmallow_integer][1]
    left_arrow = base_arrows_list[0]
    up_arrow = base_arrows_list[1]
    right_arrow = base_arrows_list[2]
    down_arrow = base_arrows_list[3]
    for arrow in base_arrows_list:
        camera.draw(arrow[1])
    if uvage.is_pressing("left arrow"):
        left_arrow[1].image = arrows[1]
        left_arrow[2] = True
        squishmallow.image = squishmallow_images[3]
    if not uvage.is_pressing("left arrow"):
        left_arrow[1].image = arrows[0]
        left_arrow[2] = False
    if uvage.is_pressing("up arrow"):
        up_arrow[1].image = arrows[3]
        up_arrow[2] = True
        squishmallow.y = 350
    if not uvage.is_pressing("up arrow"):
        up_arrow[1].image = arrows[2]
        up_arrow[2] = False
    if uvage.is_pressing("right arrow"):
        right_arrow[1].image = arrows[5]
        right_arrow[2] = True
        squishmallow.image = squishmallow_images[2]
    if not uvage.is_pressing("right arrow"):
        right_arrow[1].image = arrows[4]
        right_arrow[2] = False
    if uvage.is_pressing("down arrow"):
        down_arrow[1].image = arrows[7]
        down_arrow[2] = True
        squishmallow.image = squishmallow_images[1]
    if not uvage.is_pressing("down arrow"):
        down_arrow[1].image = arrows[6]
        down_arrow[2] = False
    if not uvage.is_pressing("down arrow") and not uvage.is_pressing("up arrow") and not uvage.is_pressing("left arrow") and not uvage.is_pressing("right arrow"):
        squishmallow.image = squishmallow_images[0]
        squishmallow.y = 400
loading_screen_images = uvage.load_sprite_sheet("Loading Screen.png",4,3)
loading_screen = uvage.from_image(400,300,loading_screen_images[0])
integer = 0
def intro():
    global squishmallow_integer
    camera.clear("White")
    camera.draw(PineSquish)
    global integer
    global clicksquish_int
    camera.draw(loading_screen)
    loading_screen.image = loading_screen_images[integer]
    integer += 1
    loading_screen.width = 800
    if integer > 11:
        integer = 0
    PineSquish.x = 200
    PineSquish.y = 450
    OctoSquish.x = 600
    OctoSquish.y = 475
    PineSquish.width = 400
    OctoSquish.width = 300
    camera.draw(PineSquish)
    camera.draw(OctoSquish)
    if camera.mouseclick:
        if camera.mouse[0] in range(PineSquish.x - PineSquish.size[0]//2,PineSquish.x + (PineSquish.size[0]//2)) and camera.mouse[1] in range(PineSquish.y - (PineSquish.size[1]//2),PineSquish.y + (PineSquish.size[1]//2)):
            squishmallow_integer = 1
        if camera.mouse[0] in range(OctoSquish.x - OctoSquish.size[0] // 2,
                                    OctoSquish.x + (OctoSquish.size[0] // 2)) and camera.mouse[1] in range(
                OctoSquish.y - (OctoSquish.size[1] // 2), OctoSquish.y + (OctoSquish.size[1] // 2)):
            squishmallow_integer = 0
    camera.draw(clicksquish_text)
    clicksquish_text.image = clicksquish_images[int(clicksquish_int)]
    clicksquish_text.width = 400
    clicksquish_int += 0.1
    if clicksquish_int > 1.5:
        clicksquish_int = 0
squishmallow_integer = None
time = 0
lock = False
trigger_fadeout = False
reset_bool = False
def reset():
    global reset_bool
    global falling_arrows_list
    global game_end
    global coordinate
    falling_arrows_list = [
    ["left arrow", uvage.from_image(250,0,arrows[0]), False, False],
    ["up arrow", uvage.from_image(450,-200,arrows[2]), False, False],
    ["right arrow", uvage.from_image(550,-400,arrows[4]), False, False],
    ["down arrow", uvage.from_image(350,-600,arrows[6]), False, False],
]
    game_end = False
    coordinate = -800
    global squishmallow_integer
    squishmallow_integer = None
    global integer
    integer = 0
    global feedback_list
    feedback_list = []
    global place
    place = 0
    global time
    time = 0
    global lock
    lock = False
    global trigger_fadeout
    trigger_fadeout = False
    mixer.music.play()
    reset_bool = False
def tick():
    global game_end
    global squishmallows
    global play_music
    global time
    global lock
    global trigger_fadeout
    global reset_bool
    global restart_int
    if squishmallow_integer == None:
        intro()
    if not squishmallow_integer == None and not game_end:
        camera.draw(background)
        camera.draw(squishmallows[squishmallow_integer][0])
        base_arrows()
        falling_arrows()
        draw_feedback()
    if falling_arrows_list[-1][2] or falling_arrows_list[-1][1].y > 700:
        time += 1/30
        trigger_fadeout = True
        if time > 5:
            game_end = True
    if trigger_fadeout and not lock:
        mixer.music.fadeout(4000)
    if game_end:
        if uvage.is_pressing("return"):
            reset_bool = True
        if reset_bool:
            reset()
        end_screen = uvage.from_image(400,350,"Endscreen.png")
        end_screen.width = 800
        camera.draw(end_screen)
        score_list = calculate_score()
        score = 10*score_list[0] + 7*score_list[1] + 4*score_list[2]
        score_text = uvage.from_text(400,525,str(score),100,"Green")
        camera.draw(restart_text)
        restart_text.image = restart_images[int(restart_int)]
        restart_text.width = 700
        restart_int += 0.1
        if restart_int > 1.5:
            restart_int = 0
        camera.draw(score_text)
        camera.draw(uvage.from_text(675, 330, "Perfect!'s: " + str(score_list[0]), 40, "Yellow"))
        camera.draw(uvage.from_text(675,360,"Good!'s: "+str(score_list[1]),40,"Yellow"))
        camera.draw(uvage.from_text(675,390,"Okay!'s: "+str(score_list[2]),40,"Yellow"))
        camera.draw(uvage.from_text(675,420,"Miss!'s: "+str(arrow_total-score_list[0]-score_list[1]-score_list[2]),40,"Yellow"))
    if trigger_fadeout:
        lock = True
    camera.display()
    camera.clear("White")
uvage.timer_loop(30, tick)