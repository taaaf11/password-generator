# password-generator
A random password generator in your toolset.


## Usage
- Generate a password (length is 8 characters by default).
```bash
pwgen
```

- Generate a password of custom length.
```bash
pwgen -l <required length>
```

- Don't want to include alphabets, numbers or symbols
```bash
pwgen -a  # would not include alphabets
```
```bash
pwgen -n  # would not include numbers
```
```bash
pwgen -p  # would not include symbols
```
You can even combine these options, e.g.
```bash
pwgen -np -l 12  # generates a password of 12 characters that would not include numbers and symbols.
```


## Installation
1. Clone the repository or download zip.
2. `cd` into project root.
3. Run `pip install .`.
