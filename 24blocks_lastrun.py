#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on February 14, 2023, at 11:34
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from recording_finish
# Recording experiment start
experimentStart = core.getTime()




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'Smart Mom'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expName, expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\user\\Desktop\\Smart Mom\\Psychopy Experiment\\Smart Mom_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "start" ---
start_text_1 = visual.TextStim(win=win, name='start_text_1',
    text='בניסוי זה יוצגו בפניך מקבצי תמונות שונים. \n\nלאחר כל מקבץ תופיע שאלה שאת התשובה לגביה \nתתבקשי לדרג בסולם של 1-7 ולאחר מכן ללחוץ "דרגי".',
    font='Open Sans',
    pos=(0, 0.25), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
start_text_2 = visual.TextStim(win=win, name='start_text_2',
    text='לחצי על מקש הרווח בשביל להתחיל.',
    font='Open Sans',
    pos=(0, -0.25), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);
example_slider = visual.Slider(win=win, name='example_slider',
    startValue=4, size=(1.0, 0.04), pos=(0, 0), units=None,
    labels=(1, 2, 3, 4, 5, 6, 7), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='White', markerColor=[1.0000, -1.0000, -1.0000], lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-2, readOnly=False)
key_space = keyboard.Keyboard()

# --- Initialize components for Routine "create_data" ---
# Run 'Begin Experiment' code from iMotions_init
import pyautogui


# --- Initialize components for Routine "reset_data" ---

# --- Initialize components for Routine "fixation" ---
fixation_point = visual.TextStim(win=win, name='fixation_point',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.14, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "images" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.8, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "rating" ---
rating_text = visual.TextStim(win=win, name='rating_text',
    text='באיזו מידה את מרגישה צורך להשתמש בפלאפון שלך כעת?',
    font='Open Sans',
    pos=(0, 0.35), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
warning_text = visual.TextStim(win=win, name='warning_text',
    text='אנא בחרי דירוג',
    font='Open Sans',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='Red', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);
rating_slider = visual.Slider(win=win, name='rating_slider',
    startValue=None, size=(1.0, 0.04), pos=(0, 0), units=None,
    labels=(1, 2, 3, 4, 5, 6, 7), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='White', markerColor=[1.0000, -1.0000, -1.0000], lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-2, readOnly=False)
rating_button = visual.ButtonStim(win, 
    text='Rate', font='Arvo',
    pos=(0, -0.3),
    letterHeight=0.05,
    size=[0.2, 0.1], borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='rating_button'
)
rating_button.buttonClock = core.Clock()

# --- Initialize components for Routine "finish" ---
finish_text = visual.TextStim(win=win, name='finish_text',
    text='תודה רבה על ההשתתפות!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
key_finish = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "start" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
example_slider.reset()
key_space.keys = []
key_space.rt = []
_key_space_allKeys = []
# keep track of which components have finished
startComponents = [start_text_1, start_text_2, example_slider, key_space]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "start" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_text_1* updates
    if start_text_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        start_text_1.frameNStart = frameN  # exact frame index
        start_text_1.tStart = t  # local t and not account for scr refresh
        start_text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text_1, 'tStartRefresh')  # time at next scr refresh
        start_text_1.setAutoDraw(True)
    
    # *start_text_2* updates
    if start_text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        start_text_2.frameNStart = frameN  # exact frame index
        start_text_2.tStart = t  # local t and not account for scr refresh
        start_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text_2, 'tStartRefresh')  # time at next scr refresh
        start_text_2.setAutoDraw(True)
    
    # *example_slider* updates
    if example_slider.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        example_slider.frameNStart = frameN  # exact frame index
        example_slider.tStart = t  # local t and not account for scr refresh
        example_slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example_slider, 'tStartRefresh')  # time at next scr refresh
        example_slider.setAutoDraw(True)
    
    # *key_space* updates
    waitOnFlip = False
    if key_space.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_space.frameNStart = frameN  # exact frame index
        key_space.tStart = t  # local t and not account for scr refresh
        key_space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_space, 'tStartRefresh')  # time at next scr refresh
        key_space.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_space.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_space.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_space.status == STARTED and not waitOnFlip:
        theseKeys = key_space.getKeys(keyList=['space'], waitRelease=False)
        _key_space_allKeys.extend(theseKeys)
        if len(_key_space_allKeys):
            key_space.keys = _key_space_allKeys[-1].name  # just the last key pressed
            key_space.rt = _key_space_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "start" ---
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "create_data" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from data_creator
import random

# Declare base variables
numOfImages = range(30)
numOfUniqueBlocks = 6
numOfBlocks = numOfUniqueBlocks * 3
ratingList = []

# Declare arries
stim_netural = []
stim_phone_on = []
stim_phone_off = []
blocks_order = []

# Declare loop counters
neturalCounter = 0
phoneOnCounter = 0
phoneOffCounter = 0

# Create the order of blocks (blocks_order)
for stim in ['stim_netural', 'stim_phone_on', 'stim_phone_off']:
    blocks_order += [stim] * numOfUniqueBlocks
    
random.shuffle(blocks_order)
    
    
# Create the stim arraies
for item in [stim_netural, stim_phone_on, stim_phone_off]:
    for num in numOfImages:
        if item == stim_netural:
            item.append(f"images/Nophone_{num+1}.jpg")
            
        elif item == stim_phone_on:
             item.append(f"images/Phone_on_{num+1}.jpg")
             
        elif item == stim_phone_off:
             item.append(f"images/Phone_off_{num+1}.jpg")
        
    random.shuffle(item)
    





# keep track of which components have finished
create_dataComponents = []
for thisComponent in create_dataComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "create_data" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in create_dataComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "create_data" ---
for thisComponent in create_dataComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "create_data" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block_loop = data.TrialHandler(nReps=numOfBlocks, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block_loop')
thisExp.addLoop(block_loop)  # add the loop to the experiment
thisBlock_loop = block_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_loop.rgb)
if thisBlock_loop != None:
    for paramName in thisBlock_loop:
        exec('{} = thisBlock_loop[paramName]'.format(paramName))

for thisBlock_loop in block_loop:
    currentLoop = block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_loop.rgb)
    if thisBlock_loop != None:
        for paramName in thisBlock_loop:
            exec('{} = thisBlock_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "reset_data" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from reset_variables
    # Initiate current block variable
    currentBlock = blocks_order[block_loop.thisN]
    
    # Initiate the images order variable
    images_in_block = []
    
    # Run 'Begin Routine' code from iMotions_start
    blockType = blocks_order[block_loop.thisN]
    
    
    if currentBlock == 'stim_netural':
        pyautogui.press('1')
        print(111)
        
    elif currentBlock == 'stim_phone_on':
        pyautogui.press('2')
        print(222)
         
    elif currentBlock == 'stim_phone_off':
        pyautogui.press('3')
        print(333)
    # keep track of which components have finished
    reset_dataComponents = []
    for thisComponent in reset_dataComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "reset_data" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reset_dataComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reset_data" ---
    for thisComponent in reset_dataComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "reset_data" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fixation_point]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_point* updates
        if fixation_point.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_point.frameNStart = frameN  # exact frame index
            fixation_point.tStart = t  # local t and not account for scr refresh
            fixation_point.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_point, 'tStartRefresh')  # time at next scr refresh
            fixation_point.setAutoDraw(True)
        if fixation_point.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_point.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                fixation_point.tStop = t  # not accounting for scr refresh
                fixation_point.frameNStop = frameN  # exact frame index
                fixation_point.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation" ---
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # set up handler to look after randomisation of conditions etc
    give_images_loop = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='give_images_loop')
    thisExp.addLoop(give_images_loop)  # add the loop to the experiment
    thisGive_images_loop = give_images_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGive_images_loop.rgb)
    if thisGive_images_loop != None:
        for paramName in thisGive_images_loop:
            exec('{} = thisGive_images_loop[paramName]'.format(paramName))
    
    for thisGive_images_loop in give_images_loop:
        currentLoop = give_images_loop
        # abbreviate parameter names if possible (e.g. rgb = thisGive_images_loop.rgb)
        if thisGive_images_loop != None:
            for paramName in thisGive_images_loop:
                exec('{} = thisGive_images_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "images" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from display_image
        if currentBlock == 'stim_netural':
            blockPosition = stim_netural[give_images_loop.thisN+(neturalCounter*5)]
            image.image = blockPosition
            images_in_block.append(blockPosition)
        #   image_path.text = blockPosition
        #   stim_var.text = stim_netural
            
        elif currentBlock == 'stim_phone_on':
            blockPosition = stim_phone_on[give_images_loop.thisN+(phoneOnCounter*5)]
            image.image = blockPosition
            images_in_block.append(blockPosition)
        #   image_path.text = blockPosition
        #   stim_var.text = stim_phone_on
             
        elif currentBlock == 'stim_phone_off':
            blockPosition = stim_phone_off[give_images_loop.thisN+(phoneOffCounter*5)]
            image.image = blockPosition
            images_in_block.append(blockPosition)
        #   image_path.text = blockPosition
        #   stim_var.text = stim_phone_off
        
        
        # keep track of which components have finished
        imagesComponents = [image]
        for thisComponent in imagesComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "images" ---
        while continueRoutine and routineTimer.getTime() < 4.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in imagesComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "images" ---
        for thisComponent in imagesComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-4.000000)
    # completed 5.0 repeats of 'give_images_loop'
    
    
    # --- Prepare to start Routine "rating" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    rating_slider.reset()
    # Run 'Begin Routine' code from marker_size
    rating_slider.marker.size = [0.03, 0.03]
    # Run 'Begin Routine' code from show_warning
    warning = False
    # Run 'Begin Routine' code from record_data
    ratingStart = core.getTime()
    # keep track of which components have finished
    ratingComponents = [rating_text, warning_text, rating_slider, rating_button]
    for thisComponent in ratingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "rating" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rating_text* updates
        if rating_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_text.frameNStart = frameN  # exact frame index
            rating_text.tStart = t  # local t and not account for scr refresh
            rating_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_text, 'tStartRefresh')  # time at next scr refresh
            rating_text.setAutoDraw(True)
        
        # *warning_text* updates
        if warning_text.status == NOT_STARTED and warning:
            # keep track of start time/frame for later
            warning_text.frameNStart = frameN  # exact frame index
            warning_text.tStart = t  # local t and not account for scr refresh
            warning_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(warning_text, 'tStartRefresh')  # time at next scr refresh
            warning_text.setAutoDraw(True)
        
        # *rating_slider* updates
        if rating_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_slider.frameNStart = frameN  # exact frame index
            rating_slider.tStart = t  # local t and not account for scr refresh
            rating_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_slider, 'tStartRefresh')  # time at next scr refresh
            rating_slider.setAutoDraw(True)
        
        # *rating_button* updates
        if rating_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            rating_button.frameNStart = frameN  # exact frame index
            rating_button.tStart = t  # local t and not account for scr refresh
            rating_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_button, 'tStartRefresh')  # time at next scr refresh
            rating_button.setAutoDraw(True)
        if rating_button.status == STARTED:
            # check whether rating_button has been pressed
            if rating_button.isClicked:
                if not rating_button.wasClicked:
                    rating_button.timesOn.append(rating_button.buttonClock.getTime()) # store time of first click
                    rating_button.timesOff.append(rating_button.buttonClock.getTime()) # store time clicked until
                else:
                    rating_button.timesOff[-1] = rating_button.buttonClock.getTime() # update time clicked until
                if rating_slider.getRating() != None:
                    continueRoutine = False
                else:
                    warning = True
                rating_button.wasClicked = True  # if rating_button is still clicked next frame, it is not a new click
            else:
                rating_button.wasClicked = False  # if rating_button is clicked next frame, it is a new click
        else:
            rating_button.wasClicked = False  # if rating_button is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ratingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "rating" ---
    for thisComponent in ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_loop.addData('rating_slider.response', rating_slider.getRating())
    # Run 'End Routine' code from record_data
    # Get block category
    block_loop.addData('imageCategory', currentBlock)
    
    # Get rating timestamps
    ratingEnd = core.getTime()
    ratingDuration = ratingEnd - ratingStart
    block_loop.addData('ratingStart', ratingStart)
    block_loop.addData('ratingEnd', ratingEnd)
    block_loop.addData('ratingDuration', ratingDuration)
    
    # Save images block order
    thisExp.addData("imagesInBlock", images_in_block)
    
    # Save rating in list
    ratingList.append(rating_slider.getRating())
    
    # Run 'End Routine' code from counter
    if currentBlock == 'stim_netural':
        neturalCounter+=1
    
    elif currentBlock == 'stim_phone_on':
        phoneOnCounter+=1
        
    elif currentBlock == 'stim_phone_off':
        phoneOffCounter+=1
        
    # Run 'End Routine' code from iMotions_end
    blockType = blocks_order[block_loop.thisN]
    
    
    if currentBlock == 'stim_netural':
        pyautogui.press('1')
        print(111)
        
    elif currentBlock == 'stim_phone_on':
        pyautogui.press('2')
        print(222)
         
    elif currentBlock == 'stim_phone_off':
        pyautogui.press('3')
        print(333)
    # the Routine "rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed numOfBlocks repeats of 'block_loop'


# --- Prepare to start Routine "finish" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from recording_finish
import statistics

# Recording experiment end and duration
experimentEnd = core.getTime()
experimentDuration = experimentEnd - experimentStart


# Add experiment timestamps data
thisExp.addData("experimentStart", experimentStart)
thisExp.addData("experimentEnd", experimentEnd)
thisExp.addData("experimentDuration", experimentDuration)


# Add experiment order of blocks and images
thisExp.addData("neturalImagesOrder", stim_netural)
thisExp.addData("phoneOnOrder", stim_phone_on)
thisExp.addData("phoneOffOrder", stim_phone_off)
thisExp.addData("blocksOrder", blocks_order)


# Calculate rating statistics
thisExp.addData("ratingList", ratingList)

ratingAverage = statistics.mean(ratingList)
thisExp.addData("ratingAverage", ratingAverage)

def getRange(numbers):
    return max(numbers) - min(numbers)
listRange = getRange(ratingList)   
thisExp.addData("listRange", listRange)

ratingStdev = statistics.stdev(ratingList)
thisExp.addData("ratingStDev", ratingStdev)

ratingMedian = statistics.median(ratingList)
thisExp.addData("ratingMedian", ratingMedian)

ratingVariance = statistics.variance(ratingList)
thisExp.addData("ratingVariance", ratingVariance)


# Create a new data line
thisExp.nextEntry()
key_finish.keys = []
key_finish.rt = []
_key_finish_allKeys = []
# keep track of which components have finished
finishComponents = [finish_text, key_finish]
for thisComponent in finishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "finish" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finish_text* updates
    if finish_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finish_text.frameNStart = frameN  # exact frame index
        finish_text.tStart = t  # local t and not account for scr refresh
        finish_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finish_text, 'tStartRefresh')  # time at next scr refresh
        finish_text.setAutoDraw(True)
    
    # *key_finish* updates
    waitOnFlip = False
    if key_finish.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_finish.frameNStart = frameN  # exact frame index
        key_finish.tStart = t  # local t and not account for scr refresh
        key_finish.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_finish, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_finish.started')
        key_finish.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_finish.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_finish.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_finish.status == STARTED and not waitOnFlip:
        theseKeys = key_finish.getKeys(keyList=['space'], waitRelease=False)
        _key_finish_allKeys.extend(theseKeys)
        if len(_key_finish_allKeys):
            key_finish.keys = _key_finish_allKeys[-1].name  # just the last key pressed
            key_finish.rt = _key_finish_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "finish" ---
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_finish.keys in ['', [], None]:  # No response was made
    key_finish.keys = None
thisExp.addData('key_finish.keys',key_finish.keys)
if key_finish.keys != None:  # we had a response
    thisExp.addData('key_finish.rt', key_finish.rt)
thisExp.nextEntry()
# the Routine "finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
