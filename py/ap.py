import ipywidgets as widgets
from IPython.display import display, clear_output

# 建立標題
title = widgets.HTML("<h2>次方與根號計算</h2>")

# 建立輸入框與下拉選單
input_x = widgets.FloatText(description='x:', value=0)
op_dropdown = widgets.Dropdown(
    options=[('^ (次方)', 'pow'), ('√ (根號)', 'root')],
    description='運算：',
)
input_y = widgets.FloatText(description='y:', value=0)
btn_calc = widgets.Button(description="計算", button_style='primary')
output = widgets.Output()

def on_button_clicked(b):
    with output:
        clear_output() # 每次按按鈕先清空上次結果
        try:
            x = input_x.value
            y = input_y.value
            op = op_dropdown.value
            
            if op == 'pow':
                result = x ** y
                print(f"結果：{x} 的 {y} 次方 = {result}")
            elif op == 'root':
                if y == 0:
                    print("錯誤：根號階數不能為 0")
                elif x < 0 and y % 2 == 0:
                    print("錯誤：負數不能開偶次方根")
                else:
                    result = x ** (1/y)
                    print(f"結果：{x} 的 {y} 次方根 = {result}")
        except Exception as e:
            print(f"發生錯誤: {e}")

# 設定按鈕點擊事件
btn_calc.on_click(on_button_clicked)

# 顯示介面
display(title, input_x, op_dropdown, input_y, btn_calc, output)