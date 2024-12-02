# AES-Project
# Advanced Encryption Standard (AES) Project

This project implements the Advanced Encryption Standard (AES), a widely used symmetric encryption algorithm. It supports various encryption-related functionalities, including key scheduling, substitution, and matrix transformations. The codebase is organized into multiple Python scripts to ensure modularity and clarity.

## Project Structure

```
.idea/				# IDE settings (excluded via .gitignore)
resources/Images/		# Resources used in the project
ImagesChiffrees/		# Encrypted images output
__pycache__/			# Compiled Python files (excluded via .gitignore)
tests/				# Unit tests for the various components
.gitignore			# Git ignore file
README.md			# Documentation for the project
aes_encryption.py		# Implementation of AES encryption
aes_key_schedule.py		# Key scheduling functions for AES
data.txt			# Substitution box data file
data_structure.py		# Data transformation functions
gf256_multiplication.py	        # Operations in GF(2^8)
main.py			        # Entry point for the project
mode_of_operation.py	        # Cipher modes like CBC, ECB
picture.py			# Image encryption/decryption functions
roundfunction.py		# Functions for AES rounds
substitution.py			# Substitution and inverse substitution functions
```

## Key Features

1. **AES Encryption Core:**

   - Implementation of AES encryption with key expansion.
   - Round transformations including substitution, shift rows, mix columns, and add round key.

2. **Substitution Box (S-Box):**

   - Loading and using the AES substitution box from `data.txt`.
   - Inverse substitution box functionality.

3. **GF(2^8) Arithmetic:**

   - Operations for finite field multiplication.
   - Essential for mix columns transformations.

4. **Image Encryption:**

   - Ability to encrypt and decrypt images using AES.

5. **Testing Framework:**

   - Unit tests covering key components such as substitution, GF multiplication, and data transformations.

## Prerequisites

- Python 3.10 or higher

## Usage

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd AES-Project
   ```

2. Run the main program:

   ```bash
   python main.py
   ```

3. Run unit tests to verify functionality:

   ```bash
   python -m unittest discover tests
   ```

## Tests

The `tests/` folder contains unit tests to ensure the correctness of all implemented functions. Use the following command to execute tests:

```bash
python -m unittest discover tests
```

##

