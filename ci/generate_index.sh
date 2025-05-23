#!/bin/bash

echo "Generating main index.html..."

cat <<EOF > public/index.html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Отчеты проекта django-gcw</title>
  <style>
    body {
      font-family: sans-serif;
      background-color: #f9f9f9;
      color: #333;
      padding: 2rem;
    }
    h1 {
      text-align: center;
      color: #222;
    }
    .links {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1rem;
      margin-top: 2rem;
    }
    a {
      display: block;
      padding: 1rem 2rem;
      text-decoration: none;
      background-color: #0057d8;
      color: white;
      border-radius: 8px;
      transition: background-color 0.3s ease;
    }
    a:hover {
      background-color: #003f9a;
    }
  </style>
</head>
<body>
  <h1>Отчеты проекта <code>django-gcw</code></h1>
  <div class="links">
    <a href="documentation/index.html" target="_blank">📄 Документация</a>
    <a href="coverage-report/index.html" target="_blank">✅ Покрытие кода (Coverage)</a>
    <a href="pylint-report/pylint.html" target="_blank">🧪 Статический анализ (Pylint)</a>
  </div>
</body>
</html>
EOF

echo "Created index.html:"
ls -la public/index.html 