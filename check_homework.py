"""
==============================================================================
Цей файл є тестом домашнього завдання.
Будь ласка, НЕ вносьте зміни до цього файлу без попереднього узгодження з ментором.
==============================================================================
"""

from collections import UserDict
import unittest

import main


RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"


class CustomTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.write(f"{GREEN} {test.shortDescription()} {RESET}\n")

    def addFailure(self, test, err):
        # err містить трійку (type, value, traceback). Ми беремо лише value (AssertionError)
        self.failures.append((test, str(err[1])))
        self._mirrorOutput = True
        self.stream.write(f"{RED} {str(err[1])} {RESET}\n")

    def printErrors(self):
        if self.errors:
            print(
                f"{RED}Ваш код викликає помилки при виконанні тесту. {self.errors} {RESET}"
            )
            self.printErrorList("ERROR:", self.errors)
        self.stream.write(f"\nВсього пройдено {self.testsRun} тестів.\n")
        failed, errored = len(self.failures), len(self.errors)
        if failed:
            self.stream.write(f"{RED}Провалених тестів: {failed} {RESET}\n")
        if errored:
            self.stream.write(
                f"{RED} Помилок при виконанні тестів: {errored} {RESET}\n"
            )

    def getDescription(self, test):
        return ""


class CustomTestRunner(unittest.TextTestRunner):
    resultclass = CustomTestResult


class TestHomeWork10(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(
            f"\n{BLUE}================================================================{RESET}"
        )
        print(f"{BLUE}Виконуємо перевірку що всі класи та методи були об'явлені{RESET}")
        print(
            f"{BLUE}================================================================{RESET}\n"
        )

    def test_001(self):
        """
        1. Класс Field в коді оголошено
        """
        assert hasattr(main, "Field"), """1. Класс Field в коді не оголошено!"""

    def test_002(self):
        """
        2. Класс Name в коді оголошено
        """
        assert hasattr(main, "Name"), """2. Класс Name в коді не оголошено!"""

    def test_003(self):
        """
        3. Класс Name наслідується від класу Field в коді
        """
        if hasattr(main, "Name"):
            assert (
                main.Name.__base__ == main.Field
            ), """3. Класс Name не наслідується від класу Field в коді"""
        else:
            raise AssertionError(
                """3. Класс Name не наслідується від класу Field в коді"""
            )

    def test_004(self):
        """
        4. Класс Phone в коді оголошено
        """
        assert hasattr(main, "Phone"), """4. Класс Phone в коді не оголошено!"""

    def test_005(self):
        """
        5. Класс Phone наслідується від класу Field в коді
        """
        if hasattr(main, "Phone"):
            assert (
                main.Phone.__base__ == main.Field
            ), """5. Класс Phone не наслідується від класу Field в коді"""
        else:
            raise AssertionError(
                """5. Класс Phone не наслідується від класу Field в коді"""
            )

    def test_006(self):
        """
        6. Класс Phone зберігає валідний телефон "0504567890" в атрибуті value
        """
        msg = """6. Класс Phone не зберігає валідний телефон 0504567890 в атрибуті value"""
        if hasattr(main, "Phone"):
            phone = main.Phone("0504567890")
            assert hasattr(phone, "value"), msg
            assert phone.value == "0504567890", msg
        else:
            raise AssertionError(msg)

    def test_007(self):
        """
        7. Класс Phone не зберігає не валідний телефон "12345abcde" в атрибуті value та викидає виключення ValueError
        """
        msg = """7. Класс Phone зберігає не валідний телефон 12345abcde в атрибуті value та не викидає виключення ValueError"""
        if hasattr(main, "Phone"):
            try:
                main.Phone("12345abcde")
                assert False, msg
            except ValueError:
                pass
            except Exception as e:
                assert False, msg
        else:
            raise AssertionError(msg)

    def test_008(self):
        """
        8. Класс Phone не зберігає не валідний телефон "050456789" в атрибуті value та викидає виключення ValueError
        """
        msg = """8. Класс Phone зберігає не валідний телефон 050456789 в атрибуті value та не викидає виключення ValueError"""
        if hasattr(main, "Phone"):
            try:
                main.Phone("050456789")
                assert False, msg
            except ValueError:
                pass
            except Exception as e:
                assert False, msg
        else:
            raise AssertionError(msg)

    def test_009(self):
        """
        9. Класс Phone не зберігає не валідний телефон "05045678901" в атрибуті value та викидає виключення ValueError
        """
        msg = """9. Класс Phone зберігає не валідний телефон 05045678901 в атрибуті value та не викидає виключення ValueError"""
        if hasattr(main, "Phone"):
            try:
                main.Phone("05045678901")
                assert False, msg
            except ValueError:
                pass
            except Exception as e:
                assert False, msg
        else:
            raise AssertionError(msg)

    def test_010(self):
        """
        10. Класс Record в коді оголошено
        """
        assert hasattr(main, "Record"), """10. Класс Record в коді не оголошено!"""

    def test_011(self):
        """
        11. Класс Record має метод add_phone
        """
        msg = """11. Класс Record не має метод add_phone!"""
        if hasattr(main, "Record"):
            assert "add_phone" in dir(main.Record), msg
        else:
            raise AssertionError(msg)

    def test_012(self):
        """
        12. Класс Record має метод remove_phone
        """
        msg = """12. Класс Record не має метод remove_phone!"""
        if hasattr(main, "Record"):
            assert "remove_phone" in dir(main.Record), msg
        else:
            raise AssertionError(msg)

    def test_013(self):
        """
        13. Класс Record має метод edit_phone
        """
        msg = """13. Класс Record не має метод edit_phone!"""
        if hasattr(main, "Record"):
            assert "edit_phone" in dir(main.Record), msg
        else:
            raise AssertionError(msg)

    def test_014(self):
        """
        14. Класс Record має метод find_phone
        """
        msg = """14. Класс Record не має метод find_phone!"""
        if hasattr(main, "Record"):
            assert "find_phone" in dir(main.Record), msg
        else:
            raise AssertionError(msg)

    def test_015(self):
        """
        15. Класс AddressBook в коді оголошено
        """
        assert hasattr(
            main, "AddressBook"
        ), """15. Класс AddressBook в коді не оголошено!"""

    def test_016(self):
        """
        16. Класс AddressBook наслідується від класу UserDict в коді
        """
        msg = """16. Класс AddressBook не наслідується від класу UserDict в коді"""
        if hasattr(main, "AddressBook"):
            assert main.AddressBook.__base__ == UserDict, msg
        else:
            raise AssertionError(msg)

    def test_017(self):
        """
        17. Класс AddressBook має метод add_record
        """
        msg = """17. Класс AddressBook не має метод add_record!"""
        if hasattr(main, "AddressBook"):
            assert "add_record" in dir(main.AddressBook), msg
        else:
            raise AssertionError(msg)

    def test_018(self):
        """
        18. Класс AddressBook має метод find
        """
        msg = """18. Класс AddressBook не має метод find!"""
        if hasattr(main, "AddressBook"):
            assert "find" in dir(main.AddressBook), msg
        else:
            raise AssertionError(msg)

    def test_019(self):
        """
        19. Класс AddressBook має метод delete
        """
        msg = """19. Класс AddressBook не має метод delete!"""
        if hasattr(main, "AddressBook"):
            assert "delete" in dir(main.AddressBook), msg
        else:
            raise AssertionError(msg)


class TestHomeWorking10(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(
            f"\n{BLUE}================================================================{RESET}"
        )
        print(
            f"{BLUE}Виконуємо перевірку що всі методи класу AddressBook працюють вірно{RESET}"
        )
        print(
            f"{BLUE}================================================================{RESET}\n"
        )

    def setUp(self):
        self.book = None
        if (
            hasattr(main, "AddressBook")
            and hasattr(main, "Record")
            and ("add_phone" in dir(main.Record))
        ):
            self.book = main.AddressBook()
            self.john_record = main.Record("John")
            self.john_record.add_phone("1234567890")
            self.john_record.add_phone("5555555555")

    def test_001(self):
        """
        1. Перевірка виконання методу add_record класу AddressBook успішна
        """
        msg = """1. Метод add_record класу AddressBook не зберіг запис Record!"""
        if hasattr(main, "AddressBook") and isinstance(self.book, main.AddressBook):
            self.book.add_record(self.john_record)
            assert "John" in self.book.data, msg
        else:
            raise AssertionError(msg)

    def test_002(self):
        """
        2. Перевірка виконання методу find класу AddressBook успішна
        """
        msg = """2. Метод find класу AddressBook не повернув запис Record який був збережений!"""
        if hasattr(main, "AddressBook") and isinstance(self.book, main.AddressBook):
            self.book.add_record(self.john_record)
            assert self.book.find("John") == self.john_record, msg
        else:
            raise AssertionError(msg)

    def test_003(self):
        """
        3. Перевірка виконання методу find класу AddressBook з записом, що не існує успішна
        """
        msg = """3. Провалена перевірка. Якщо запису не існує то метод find класу AddressBook повинен повернути None!"""
        if hasattr(main, "AddressBook") and isinstance(self.book, main.AddressBook):
            self.book.add_record(self.john_record)
            assert self.book.find("Jane") is None, msg
        else:
            raise AssertionError(msg)

    def test_004(self):
        """
        4. Перевірка виконання методу delete класу AddressBook успішна
        """
        msg = """2. Метод delete класу AddressBook не видалив запис Record який був збережений!"""
        if hasattr(main, "AddressBook") and isinstance(self.book, main.AddressBook):
            self.book.add_record(self.john_record)
            self.book.delete("John")
            assert self.book.find("John") is None, msg
        else:
            raise AssertionError(msg)

    def test_005(self):
        """
        5. Перевірка виконання методу delete класу AddressBook з записом, що не існує успішна
        """
        msg = """3. Провалена перевірка. Метод delete класу AddressBook не видалив запис!"""
        if hasattr(main, "AddressBook") and isinstance(self.book, main.AddressBook):
            self.book.add_record(self.john_record)
            self.book.delete("Jane")
            assert self.book.find("Jane") is None, msg
        else:
            raise AssertionError(msg)


class TestHomeWorking10_1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(
            f"\n{BLUE}================================================================{RESET}"
        )
        print(
            f"{BLUE}Виконуємо перевірку що всі методи класу Record працюють вірно{RESET}"
        )
        print(
            f"{BLUE}================================================================{RESET}\n"
        )

    def setUp(self):
        self.record = None
        if hasattr(main, "Record") and ("add_phone" in dir(main.Record)):
            self.record = main.Record("John")
            self.record.add_phone("1234567890")
            self.record.add_phone("5555555555")

    def test_001(self):
        """
        1. Перевірка виконання методу find_phone класу Record. Успішно знайдено перший номер контакту
        """
        msg = """1. Метод find_phone класу Record не знайшов перший номер контакту!"""
        if (
            hasattr(main, "Record")
            and isinstance(self.record, main.Record)
            and ("find_phone" in dir(main.Record))
        ):
            try:
                phone = self.record.find_phone("1234567890")
                assert phone.value == "1234567890", msg
            except Exception:
                assert False, msg
        else:
            raise AssertionError(msg)

    def test_002(self):
        """
        2. Перевірка виконання методу find_phone класу Record. Успішно знайдено другий номер контакту
        """
        msg = """2. Метод find_phone класу Record не знайшов другий номер контакту!"""
        if (
            hasattr(main, "Record")
            and isinstance(self.record, main.Record)
            and ("find_phone" in dir(main.Record))
        ):
            try:
                phone = self.record.find_phone("5555555555")
                assert phone.value == "5555555555", msg
            except Exception:
                assert False, msg
        else:
            raise AssertionError(msg)

    def test_003(self):
        """
        3. Перевірка виконання методу find_phone класу Record для не існуючого номеру. Повернуто значення None
        """
        msg = """3. Провалена перевірка. Якщо номеру телефона не існує то метод find_phone класу Record повинен повернути None!"""
        if (
            hasattr(main, "Record")
            and isinstance(self.record, main.Record)
            and ("find_phone" in dir(main.Record))
        ):
            phone = self.record.find_phone("1111111111")
            assert phone is None, msg
        else:
            raise AssertionError(msg)

    def test_004(self):
        """
        4. Перевірка редагування номера телефону методом edit_phone класу Record успішна
        """
        msg = """4. Метод edit_phone класу Record не відреагував номер телефону, що існує!"""
        if (
            hasattr(main, "Record")
            and isinstance(self.record, main.Record)
            and ("edit_phone" in dir(main.Record))
            and ("find_phone" in dir(main.Record))
        ):
            self.record.edit_phone("1234567890", "4444444444")
            try:
                phone = self.record.find_phone("4444444444")
                assert phone.value == "4444444444", msg
            except Exception:
                assert False, msg
        else:
            raise AssertionError(msg)

    def test_005(self):
        """
        5. Перевірка редагування номера телефону, що не існує, методом edit_phone класу Record успішна. Викинуте виключення ValueError
        """
        msg = """5. Провалена перевірка. Якщо номеру телефону не існує то метод edit_phone класу Record повинен викинути виключення ValueError!"""
        if (
            hasattr(main, "Record")
            and isinstance(self.record, main.Record)
            and ("edit_phone" in dir(main.Record))
        ):
            try:
                self.record.edit_phone("1111111111", "4444444444")
                assert False, msg
            except ValueError:
                pass
            except Exception:
                assert False, msg
        else:
            raise AssertionError(msg)

    def test_006(self):
        """
        6. Перевірка видалення номера телефону методом remove_phone класу Record успішна
        """
        msg = """6. Провалена перевірка. Метод remove_phone класу Record не видаляє номер телефону!"""
        if (
            hasattr(main, "Record")
            and isinstance(self.record, main.Record)
            and ("remove_phone" in dir(main.Record))
            and ("find_phone" in dir(main.Record))
        ):
            self.record.remove_phone("1234567890")
            phone = self.record.find_phone("1234567890")
            assert phone is None, msg
        else:
            raise AssertionError(msg)


if __name__ == "__main__":
    runner = CustomTestRunner(verbosity=0)
    unittest.main(testRunner=runner)
