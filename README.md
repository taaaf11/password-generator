# password-generator
A random password generator in your toolset.


## Usage
- Generate a password (length is 8 characters by default).
```bash
passwd-gen
```

- Generate a password of custom length.
```bash
passwd-gen -l <required length>
```

- Don't want to include alphabets, numbers or symbols
```bash
passwd-gen -a  # would not include alphabets
```
```bash
passwd-gen -n  # would not include numbers
```
```bash
passwd-gen -p  # would not include symbols
```
You can even combine these options, e.g.
```bash
passwd-gen -np -l 12  # generates a password of 12 characters that would not include numbers and symbols.
```


## Installation
1. Clone the repository or download zip.
2. `cd` into project root.
3. Run `pip install .`.
