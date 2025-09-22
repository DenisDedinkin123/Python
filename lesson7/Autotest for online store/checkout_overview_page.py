import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def get_total_amount(self):
        total_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        ).text  # ожидается что будет что-то вроде "Total: $58.29" или "$58.29"

        # Извлечение числового значения
        # Удаляем все, кроме цифр и точки, либо парсим по шаблону
        m = re.search(r"(\d+\.?\d*)", total_text.replace(",", "."))
        if m:
            return float(m.group(1))
        # Если вдруг не нашли число, возвращаем 0.0 или бросаем исключение
        return 0.0
