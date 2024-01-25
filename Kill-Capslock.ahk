;-----------------------------------------------------
;캡스락을 죽입시다. 캡스락은 나의 적
;-----------------------------------------------------
SetCapsLockState AlwaysOff

CapsLock & Space::Send {BackSpace}

; Ctrl & Space::SendInput, {Space 4} ;; it overlaps whale quick search hotkeys



CapsLock & e::End
CapsLock & q::Home
CapsLock & a::Left
CapsLock & d::Right
CapsLock & w::Up
CapsLock & s::Down
CapsLock & /::\

CapsLock & o::End
CapsLock & u::Home
CapsLock & j::Left
CapsLock & l::Right
CapsLock & i::Up
CapsLock & k::Down

;윈도우 작업표시줄 단축키 win + num => CapsLock + num
CapsLock & 1::#1
CapsLock & 2::#2
CapsLock & 3::#3
CapsLock & 4::#4
CapsLock & 5::#5
CapsLock & 6::#6
CapsLock & 7::#7
CapsLock & 8::#8