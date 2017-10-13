# Password Strength Calculator

Script evaluate password and prints strength score in (0, 10) range

# Requirements

Script requires `zxcvbn-python` library installed to run
```
pip install zxcvbn-python
```
# Usage 
#### Run script:
```
python password_strength.py <password>
```
where  `<password>` - password to test

#### Output:
Strength score of input password in range from 0 (weakest) to 10 (strongest)

#### Run script example:
```
python lang_frequency.py 1234_5678
```
#### Output example:
```
Password strength in (0, 10) range is: 5

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
