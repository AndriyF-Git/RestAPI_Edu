
# ✅ Чекліст для вивчення Git та Docker

## 🔹 Git

| Тема | Команди / Приклади | Статус  |
|------|--------------------|---------|
| **1. Робота з гілками** | `git branch`, `git checkout -b featureX`, `git merge`, `git rebase` | ⬜       |
| **2. Pull requests (code review)** | Створення PR у GitHub/GitLab | ⬜       |
| **3. Конфлікти злиття** | `git merge`, вирішення конфліктів вручну | not yet |
| **4. Історія комітів** | `git log --oneline`, `git diff`, `git blame` | ⬜       |
| **5. Відкат змін** | `git reset --hard`, `git revert`, `git restore` | ⬜       |
| **6. Stashing** | `git stash`, `git stash pop` | ⬜       |
| **7. Cherry-picking** | `git cherry-pick <commit>` | ⬜       |
| **8. Submodules** | `git submodule add <repo>` | ⬜       |
| **9. Git hooks** | Налаштування `.git/hooks/pre-commit` | ⬜       |

---

## 🔹 Docker

| Тема | Команди / Приклади | Статус |
|------|--------------------|--------|
| **1. Базові образи** | `docker pull ubuntu`, `docker run -it ubuntu bash` | ⬜ |
| **2. Dockerfile Basics** | `FROM`, `COPY`, `RUN`, `CMD` | ⬜ |
| **3. Оптимізація Dockerfile** | Multi-stage builds, Alpine images | ⬜ |
| **4. Docker Compose** | `docker-compose up -d` (app + DB) | ⬜ |
| **5. Volume** | `docker volume create`, `docker run -v` | ⬜ |
| **6. Network** | `docker network create`, `docker run --network` | ⬜ |
| **7. Моніторинг контейнерів** | `docker ps`, `docker stats`, `docker logs` | ⬜ |
| **8. Docker Registry** | `docker login`, `docker push myapp:1.0` | ⬜ |
| **9. Best Practices** | `.dockerignore`, `HEALTHCHECK`, малий розмір образів | ⬜ |

---

## 🔹 Практичні завдання

| Проєкт | Що зробити | Статус |
|--------|------------|--------|
| **Git Mini-Project** | Створити репозиторій, попрацювати з гілками, зробити PR, вирішити конфлікт | ⬜ |
| **Docker App** | Запакувати Flask/Node.js app у контейнер | ⬜ |
| **Docker Compose** | Додати базу даних (Postgres або MySQL) через `docker-compose.yml` | ⬜ |
| **Docker Hub** | Зібрати свій образ і залити на Docker Hub | ⬜ |
