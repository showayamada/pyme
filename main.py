import pyautogui
import time
import pyperclip
from pynput import keyboard

import llama_module


def convert_to_gyaru(text):
    return llama_module.predict(text)

def on_press(key):
    try:
        if key == keyboard.Key.space:
            print("スペースキーが押されました")
            time.sleep(0.1)  # 入力バッファを待つ
            print("入力テキストを取得します...")
            pyautogui.hotkey("ctrl", "a")  # 全選択
            pyautogui.hotkey("ctrl", "c")  # クリップボードにコピー
            time.sleep(0.1)  # コピー待機

            text = pyperclip.paste()  # クリップボードの内容を取得
            print(f"入力テキスト: {text}")
            
            converted = convert_to_gyaru(text)
            print(f"変換後テキスト: {converted}")

            if text != converted:
                pyautogui.hotkey("ctrl", "a")  # 全選択
                pyautogui.press("backspace")   # 削除
                pyperclip.copy(converted)
                pyautogui.hotkey("ctrl", "v")
                print("変換しました")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

def main():
    # スペースキー監視
    with keyboard.Listener(on_press=on_press) as listener:
        print("ギャル語IME起動中... (Ctrl+Cで終了)")
        listener.join()

if __name__ == "__main__":
    main()
