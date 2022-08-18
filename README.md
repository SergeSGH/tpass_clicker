# Тестовый проект - генерация короткой ссылки для редиректа
### Стэк:
```
Python, Django
```

###  Основные функции:

```
Получить короткую ссылку - POST запрос на http://host_url/get_link/
host_url - локальный (или глобальный если необходимо) адрес сервера
стандартно для локального деплоя используется http://127.0.0.1:8000/
авторизация не нужна
json запроса: "link" : "ДЛИННАЯ_ССЫЛКА", "expires_in" : "СРОК ССЫЛКИ В ЧАСАХ"
```
```
json ответа сервера: "short_link" : "СОКРАЩЕННАЯ_ССЫЛКА" (последовательность символов),
"expires" : "ВРЕМЯ ОКОНЧАНИЯ ДЕЙСТВИЯ"
```
```
Использование ссылки:
http://host_url/СОКРАЩЕННАЯ_ССЫЛКА/
(редирект на указанную станицу)
```
```
Для генерации ссылок используется первые 5 символов хэша на SHA224, полученного с помощью
библиотеки hashlib
в случае коллизии (одинаковые 5 символов для разных ссылок) число символов увеличивается 
```
```
Примечания:
1. 2 приложения (api и redirect), чтобы можно было переключиться на структуру
с нужным фронтэндом. С точки зрения размера задачи одно приложение целесообразнее конечно
2. Возможности для улучшения:
   - другая хэш-функция для генерации ссылок, например генерирующая хэши не только со строчными,
   но и с прописными буквами, генерирующая сразу короткую строку 
   - более быстрая БД при необходимости
   и т.д.
```