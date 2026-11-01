# ysdprojects.space

Портфолио YSD DEV на GitHub Pages — открывается из России (в отличие от Cloudflare).

- `/<работа>/` — 52 работы портфолио. Копируются автоматически с Cloudflare (`tools/mirror.py`, Actions → mirror → Run workflow).
- `/clients/<клиент>/` — временные сайты клиентов, см. `clients/README.md`.
- `/d/<проект>/` — демо, которые бот собирает клиентам: страница (`tools/404.html`) подгружает их с сервера бота
  `app.ysddev.com/p/<проект>/`, адрес у клиента — ysdprojects.space.
- Основной сайт студии — https://ysddev.com (отдельный репозиторий).
