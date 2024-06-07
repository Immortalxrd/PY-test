from pywinauto import Application
import time


def perform_and_check_operation(calc, button1, operation, button2, expected_result):
    calc[button1].click()
    calc[operation].click()
    calc[button2].click()
    calc['='].click()
    time.sleep(1)  

    result = calc.child_window(title="Display", control_type="Text").window_text()
    result = result.replace("Display is", "").strip() 


    try:
        result_value = float(result)
    except ValueError:
        result_value = int(result)

    assert result_value == expected_result, f"Expected {expected_result}, but got {result}"


app = Application().start("calc.exe")
calc = app.window(title='Calculator')


time.sleep(2)


perform_and_check_operation(calc, 'Five', 'Plus', 'Seven', 12)
perform_and_check_operation(calc, 'Seven', 'Minus', 'Five', 2)
perform_and_check_operation(calc, 'Five', 'Multiply by', 'Seven', 35)
perform_and_check_operation(calc, 'Seven', 'Divide by', 'Five', 1.4)


calc.close()
print("Тест успешно завершен.")
