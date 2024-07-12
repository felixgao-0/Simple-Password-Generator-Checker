# Simple Password Generate & Checker

This generator can generate passwords in 2 modes and check your passwords too.

## Creating a password w/o a phrase
This is the easiest mode. You can just enter how many characters you want and the script will generate a password. Checked to ensure it isn't in any breaches and to ensure its a secure password.

Example:
```
How many characters? 20
Generated a password: vxgOwmJ#q4N^FAz1SL$8
```
*Obviously don't use that password

## Creating a password w/ a phrase
This mode is like the previous expect the result is based on the phrase you give. Checked to ensure it isn't in any breaches and to ensure it's a secure password.


Example:
```
Input a passphrase: I love coding!
Generated a password: I_1ovE_c0d1ng!763
```
*Obviously don't use that password

## Checking your passwords
This mode checks to see if your password has been found in any data breaches.

```
Password to check: password
This password has been PWNED 10434004 times!
```
Maybe using 'password' as a password wasn't a great choice after all. Oops.

Credits to https://haveibeenpwned.com/ for the pwned data!
