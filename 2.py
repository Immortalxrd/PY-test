from pywinauto import Application
import time


def perform_operations(calc, number):
    calc[number].click()
    calc['Multiply by'].click()
    calc['Two'].click()
    calc['='].click()
    time.sleep(1)  

    calc['Divide by'].click()
    calc['Two'].click()
    calc['='].click()
    time.sleep(1)  


def check_display_empty(calc):
    result = calc.child_window(title="Display", control_type="Text").window_text()
    result = result.replace("Display is", "").strip()  
    assert result == "0" or result == "", f"Expected display to be empty, but got {result}"


app = Application().start("calc.exe")
calc = app.window(title='Calculator')


time.sleep(2)


calc['One'].click()
calc['Zero'].click()


perform_operations(calc, 'One')  
perform_operations(calc, 'Zero')


calc['Clear'].click()
time.sleep(1)  


check_display_empty(calc)


calc.close()
print("Тест успешно завершен.")
