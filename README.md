# OTUS_Selenium

1) ДЗ Ожидания элементов  
В файле conftest содержится фикстура для запуска разных браузеров.   
Добавлены опции командной строки для headless режима и базового урла opencart  
В папке tests лежат файлы с тестами на 5 страниц опенкарта, а так же файл с тестовыми сценариями для третьей части ДЗ  

2) ДЗ Page Objects  
В папке page_objects содержатся файлы с классами страниц и элементов, куда вынесены методы тестов.  
Отредактированы все тесты из папки tests.  
В файл test_scenarios добавлены 4 новых сценария.

3) ДЗ Allure  
Настроено логгирование и отчеты по результатам прогонов с помощью Allure    

4) ДЗ Selenoid  
Добавлена возможность запуска автотестов с помощью Selenoid.  
Настроены для запуска через Selenoid браузеры Chrome, Firefox, Safari.
Добавлена возможность через addoption "--launch_mode" выбирать запуск тестов локально или удаленно.

