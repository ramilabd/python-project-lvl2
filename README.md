# Gendiff

### Hexlet tests and linter status:
[![Actions Status](https://github.com/ramilabd/python-project-lvl2/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ramilabd/python-project-lvl2/actions)

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
$ uv run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
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

[![asciicast](https://asciinema.org/a/dnarm1QJsZdGEkh0.svg)](https://asciinema.org/a/dnarm1QJsZdGEkh0)