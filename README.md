# Gendiff

### Hexlet tests, linter status, Quality gate status and Coverage SonarQube:
[![Actions Status](https://github.com/ramilabd/python-project-lvl2/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ramilabd/python-project-lvl2/actions)
[![Quality gate status](https://sonarcloud.io/api/project_badges/measure?project=ramilabd_python-project-lvl2&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=ramilabd_python-project-lvl2)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=ramilabd_python-project-lvl2&metric=coverage)](https://sonarcloud.io/summary/new_code?id=ramilabd_python-project-lvl2)

## Описание

**Gendiff** — утилита командной строки для сравнения двух конфигурационных файлов (JSON, в дальнейшем — и YAML) и вывода их различий.

Программа определяет, какие ключи были добавлены, удалены или изменены при переходе от первого файла ко второму, и показывает разницу с помощью знаков `+`/`-` — по аналогии с `diff`, но для структурированных данных, а не текста.

## Установка

```bash
git clone git@github.com:ramilabd/python-project-lvl2.git
cd python-project-lvl2
uv sync
```

## Использование

```bash
uv run gendiff first_file.json second_file.json
```

Пример:

```
$ uv run gendiff tests/test_data/file1.json tests/test_data/file2.json
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

## Демонстрация

[![asciicast](https://asciinema.org/a/1262182.svg)](https://asciinema.org/a/1262182)

[![asciicast](https://asciinema.org/a/1262183.svg)](https://asciinema.org/a/1262183)
