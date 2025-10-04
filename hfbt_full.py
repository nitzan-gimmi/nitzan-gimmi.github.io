#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HFBT - Hebrew Full Byte Tokenizer
A minimal tokenizer for Hebrew text
"""

import sys
import unicodedata


class HebrewTokenizer:
    """Simple Hebrew tokenizer"""
    
    def __init__(self):
        # Hebrew Unicode range: 0x0590 - 0x05FF
        self.hebrew_range = range(0x0590, 0x0600)
    
    def is_hebrew(self, char):
        """Check if character is Hebrew"""
        return ord(char) in self.hebrew_range
    
    def tokenize(self, text):
        """
        Tokenize Hebrew text into words and tokens
        
        Args:
            text (str): Input text to tokenize
            
        Returns:
            list: List of tokens
        """
        tokens = []
        current_token = []
        
        for char in text:
            if self.is_hebrew(char):
                current_token.append(char)
            elif char.isalnum():
                current_token.append(char)
            else:
                if current_token:
                    tokens.append(''.join(current_token))
                    current_token = []
                if not char.isspace():
                    tokens.append(char)
        
        if current_token:
            tokens.append(''.join(current_token))
        
        return tokens


def main():
    """Main entry point"""
    tokenizer = HebrewTokenizer()
    
    if len(sys.argv) > 1:
        # Tokenize command line argument
        text = ' '.join(sys.argv[1:])
    else:
        # Read from stdin
        text = sys.stdin.read()
    
    tokens = tokenizer.tokenize(text)
    
    # Output tokens
    for token in tokens:
        print(token)


if __name__ == '__main__':
    main()
