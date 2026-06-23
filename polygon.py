import tkinter as tk
from tkinter import messagebox
import math
from fractions import Fraction

def draw_polygon():
    # キャンバスのクリア
    canvas.delete("all")
    
    # 入力値の取得とチェック
    input_val = entry.get()
    try:
        n = float(input_val)
        if n < 3:
            raise ValueError("3以上の数値を入力してください。")
    except ValueError as e:
        messagebox.showerror("エラー", f"有効な3以上の数値を入力してください。\n({e})")
        return

    # キャンバスの中心と半径
    cx, cy = 250, 250
    r = 200

    # 小数を分数（p/q）に変換（誤差を考慮して最大分母を制限）
    # 例: 5.5 -> 11/2 (p=11, q=2)
    frac = Fraction(n).limit_denominator(100)
    p = frac.numerator
    q = frac.denominator

    # 頂点の座標を計算
    # 星型正多角形（p/q角形）は、360度をp等分した頂点を、q個飛ばしで結ぶ
    points = []
    for i in range(p + 1):  # 最後に始点に戻るために p+1 までループ
        # 角度の計算 (ラジアン)
        # 通常の正多角形(q=1)なら 2 * pi * i / p
        theta = 2 * math.pi * q * i / p - math.pi / 2 # -math.pi/2 で真上から開始
        
        x = cx + r * math.cos(theta)
        y = cy + r * math.sin(theta)
        points.append((x, y))

    # 線の描画
    for i in range(len(points) - 1):
        canvas.create_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], fill="blue", width=2)

    # 情報の表示
    info_label.config(text=f"描画: {n} 角形 (分数表記: {p}/{q} 角形)")

# メインウィンドウの設定
root = tk.Tk()
root.title("可変正多角形ジェネレーター")
root.geometry("500x600")

# 入力エリアのフレーム
frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(frame, text="角数 n (小数可):")
label.pack(side=tk.LEFT, padx=5)

entry = tk.Entry(frame, width=10)
entry.insert(0, "5.5")  # 初期値
entry.pack(side=tk.LEFT, padx=5)

btn = tk.Button(frame, text="描画", command=draw_polygon)
btn.pack(side=tk.LEFT, padx=5)

# 描画情報のラベル
info_label = tk.Label(root, text="", fg="darkgreen")
info_label.pack()

# キャンバスの設定
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack(pady=10)

# 初回描画
draw_polygon()

root.mainloop()