# Instrument SEP2-7

## 1. Introduction

An online musical instruments store with python and flask

## 2. Development Usage

### 2.1 Basic Usage

```
# run server
bash run.sh

-> avaliable on https://comp3030j.ucd.ie:5007
```

### 2.2 Database Tools

We provide `predifined data` under app/dev/_dev_data.py for development and testing
```
# Clear database
$ python dev_tools.py -reset

# Create and insert data
$ python dev_tools.py -reset -insert -a

# ...
...
```

### 2.3 MultiLanguage Support
We provide English and Chinese support for our website by using `python_bible` replacing all the English terms.

To build a new language support:
```
# 0. Add new language abbreviation (e.g. 'zh') in Config.py
# 1. Extract terms from specified .py and html files into messages.pot
$ pybabel extract -F babel.cfg -k _l -o messages.pot --input-dirs=.

# 2. Initiate language dictionary
$ pybabel init -i messages.pot -d app/translations -l <language-abbrivation>

# 3. Add translations in new created 'app/translations/<language-abbrivation>/LC_MESSAGE/messages.po'

# 4. compile message.po
$ pybabel compile -d app/translations
```

To update existed translation
```
# 1. Extract terms from specified .py and html files into messages.pot
$ pybabel extract -F babel.cfg -k _l -o messages.pot --input-dirs=.

# 2. Update dictionary
$ pybabel update -i messages.pot -d app/translations

# 3. Change dictionary in 'app/translations/<language-abbrivation>/LC_MESSAGE/messages.po'

# 4. compile message.po
$ pybabel compile -d app/translations
```

## 3. References

[1] [jq22](https://www.jq22.com/jquery-info22291)

[2] [datta-able-bootstrap-lite](https://codedthemes.com/item/datta-able-bootstrap-lite/)

[3] [Agora Document](https://docs.agora.io/cn/live-streaming/landing-page?platform=Web)

[4] [Agora Sample Repo](https://github.com/AgoraIO/API-Examples-Web/tree/main/Demo/basicLive)

[5] [沃梦达](http://www.womengda.cn) [INVALID NOW]

[6] [沃梦达](https://www.genban.org/moban/xys/moban-26996.html) 


