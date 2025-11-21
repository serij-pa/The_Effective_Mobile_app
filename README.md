# Описание проекта
Проект представляет собой backend-составляющую cистему аутентификации и авторизации. Основной задачей разработки 
является продумывание и предложение собственной системы доступа к ресурсам.

## Используемые инструменты
* **Python** (3.12);
* **Django** (бесплатный веб-фреймворк для языка Python);

## Сборка и запуск приложения

1. Скачиваем содержимое репозитория в отдельную папку:
    ```
    git clone ssh://git@github.com:serij-pa/The_Effective_Mobile_app.git
    ```
   
2. Переходим в директорию The_Effective_Mobile_app.
   Создаем виртуальное окружение:    
    ```
    python -m venv .venv
    ```

3. В директорию The_Effective_Mobile_app копируем requirements.txt и устанавливаем зависимости:
    ```
    pip istall -r requirements.txt
    ```

4. Создаем django-проект: 
    ```
    python -m django startproject backend
    ```
   (ну или другое имя проекту заменив backend)

5. Выполняем миграции:   
    ```
    python manage.py migrate
    ```
   
6. Запускаем тестовый сервер:
    ```
    python manage.py runserver
    ```

## Основные модули системы
### 1. Взаимодействие с пользователем
Позволяет пользователям регистрироваться, входить в систему, выходить из учетной записи, обновлять свои данные и удалять аккаунт.
* Регистрация: Ввод имени, фамилии, отчества, email, пароля, повтор пароля.

![](Effective_Mobile/screenshots/register_1.png)

* Обновление информации: 
* Пользователь может редактировать свой профиль как изменение аватарки так и всю информацию.

![](Effective_Mobile/screenshots/izmenenie_dannih_1.png) ![](Effective_Mobile/screenshots/izmenenie_dannih_2.png)

* Мягкое удаление пользователя утем изменения is_active на False

![](Effective_Mobile/screenshots/Delete.png)

* Login: пользователь входить в систему по email и паролю.
* Реализованы оба бэкенда: и по логину и по E-mail

![](Effective_Mobile/screenshots/login_1.png)

![](Effective_Mobile/screenshots/login_2.png)

* Logout: пользователь выходит из системы.

### 2. Система разграничения прав доступа. 

* В самих шаблонах стоит проверка на аутентификацию 

![](Effective_Mobile/screenshots/ogranichenie_dostupa_1.png)

* В классах подключены механизмы контроля доступа к ресурсам

![](Effective_Mobile/screenshots/ogranichenie_dostupa_2.png)

* Для удобства изменения данных АДМИНОМ выгружается список всех пользователей с возможностью изменения профиля.

![](Effective_Mobile/screenshots/profil_1.png)

![](Effective_Mobile/screenshots/profil_2.png)

![](Effective_Mobile/screenshots/profil_3.png)

* Вносить изменения в профиль могут или Админ или сам пользователь кому принадлежить профиль.

![](Effective_Mobile/screenshots/ogranichenie_dostupa_3.png)

* Если пользователь определен, но запрашиваемый ресурс ему не доступен то

![](Effective_Mobile/screenshots/ogranichenie_dostupa_4.png)

* Реализовано API с возможностью получения и изменения этих правил пользователю.
* Первый вариант через API самого пользоватедя путем добавления ему необходимых прав

![](Effective_Mobile/screenshots/API_user.png)

* Второй вариант через API группы путем добавления пользователя в группу и добавления группе необходимых прав

![](Effective_Mobile/screenshots/API_groups.png)

* Третий вариант через Swagger или Redoc

![](Effective_Mobile/screenshots/Swager.png)

