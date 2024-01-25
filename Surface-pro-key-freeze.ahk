;----------------------------------------------
;서피스 프로용 키보드 잠금/해제 스크립트
;----------------------------------------------

#SingleInstance force

~\ & -::hk(1,0,"KEYBOARB LOCKED.`n\ + - to LOCK")              ; Disable all keyboard keys and mouse buttons
~\ & =::hk(0,0,"KEYBOARD UNLOCKED. `\ + = to UNLOCK")              ; Enable all keyboard keys and mouse buttons
; !F3::hk(1,1,"KEYBOARD MOUSE AND SCREEN LOCKED!  -  ALT+F2 TO UNLOCK",,,1,"teal")   ; Disable keyboard mouse and screen


hk(keyboard:=false, mouse:=0, message:="", timeout:=3, displayonce:=false,screen:=false, screencolor:="blue") { 

;keyboard (true/false).......................... disable/enable keyboard
;mouse=1........................................ disable all mouse buttons
;mouse=2........................................ disable right mouse button only
;msessage....................................... display a message
;timeout........................................ how long to display the message in sec
;displayonce (true/false) ...................... display a message only once or always
;hide the screen (true/false)................... hide or show everything
;ScreenColor ................................... RGB Hex background color for the hiding GUI 


   static AllKeys, z, d, kb, ms, sc
   z:=message, d:=displayonce, kb:=keyboard, ms:=mouse, sc:=screen

      For k,v in AllKeys {
           Hotkey, *%v%, Block_Input, off         ; initialisation
      }
   if !AllKeys {
      s := "||NumpadEnter|Home|End|PgUp|PgDn|Left|Right|Up|Down|Del|Ins|"
      Loop, 254
         k := GetKeyName(Format("VK{:0X}", A_Index))
       , s .= InStr(s, "|" k "|") ? "" : k "|"
      For k,v in {Control:"Ctrl",Escape:"Esc"}
         AllKeys := StrReplace(s, k, v)
      AllKeys := StrSplit(Trim(AllKeys, "|"), "|")
   }
   ;------------------
   if (mouse!=2)  ; if mouse=1 disable right and left mouse buttons  if mouse=0 don't disable mouse buttons
    {
        For k,v in AllKeys {
           IsMouseButton := Instr(v, "Wheel") || Instr(v, "Button")
           Hotkey, *%v%, Block_Input, % (keyboard && !IsMouseButton) || (mouse && IsMouseButton) ? "On" : "Off"
        }
    }
   if (mouse=2)   ;disable right mouse button (but not left mouse)
    {                
     ExcludeKeys:="LButton"
      For k,v in AllKeys {
           IsMouseButton := Instr(v, "Wheel") || Instr(v, "Button")
           if v not in %ExcludeKeys%
           Hotkey, *%v%, Block_Input, % (keyboard && !IsMouseButton) || (mouse && IsMouseButton) ? "On" : "Off"
        }
    }
   if d
    {
   if (z != "") {
      Progress, +AlwaysOnTop Y700 W200 H40 b1 zh0 cwFF0000 FM10 CT000000,, %z%
      SetTimer, TimeoutTimer, % -timeout*500
   }
   else
      Progress, Off
     }
   Block_Input:
   if (d!=1)
    {
   if (z != "") {
	    if (kb || ms)
			Progress, +AlwaysOnTop Y250 W200 H40 b1 zh0 cwFF0000 FM10 CTFFFFFF,, %z%
		else
			Progress, +AlwaysOnTop Y250 W200 H40 b1 zh0 cw0000FF FM10 CTFFFFFF,, %z%
		SetTimer, TimeoutTimer, % -timeout*500
   }
   else
      Progress, Off
     }


if (sc=1)
   { 
     Gui screen:  -Caption
     Gui screen: Color,  % screencolor
     Gui screen: Show, x0 y0 h74 w%a_screenwidth% h%a_screenheight%, New GUI Window
   }
   else
      gui screen: Hide


   Return
   TimeoutTimer:
   Progress, Off
   Return
}