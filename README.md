## Keyboard Remapping based on AutoHotKey

제 필요에 맞춰 키보드의 몇몇 키들을 리패밍한 AutoHotKey 스크립트들입니다.

각각의 스크립트들에 대한 설명은 다음과 같습니다.

1. `Keyboard_fundamental_remapping.ahk`
   - 제가 실제 사용중인 스크립트입니다.
   - CapsLock키를 방향키 등으로 리패밍하는 스크립트(Kill-Capslo) 외에도, 서피스 프로의 키보드 입력을 방지하는 스크립트, 87키 키보드에서 계산기 단축키 등등의 스크립트가 포함되어 있습니다.

2. `Kill-Capslock.ahk`
   - CapsLock + WASD, IJKL / QE, UO키를 방향키 및 Home/End키로 리매핑하는 스크립트입니다.
   - 자세한 설명은 [제 블로그글](https://dieyoung211.tistory.com/entry/AutoHotKey-CapsLock%ED%82%A4%EB%A5%BC-%EB%8B%A4%EC%96%91%ED%95%98%EA%B2%8C-%ED%99%9C%EC%9A%A9%ED%95%A0-%EC%88%98-%EC%9E%88%EA%B2%8C-%ED%95%B4%EC%A3%BC%EB%8A%94-%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8)을 참고하세요!

3. `Surface-pro-key-freeze.ahk`
   - 서피스 프로 펜 사용시, 키보드가 눌리는 경우를 방지하고자 작성한 스크립트입니다.
   - `\` + `-`키를 누르면 키보드가 동작하지 않고, 반대로 `\` +`=`키를 누르면 다시 키보드가 동작합니다.