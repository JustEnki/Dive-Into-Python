import re
from BaseHTMLProcessor import BaseHTMLProcessor

class Dialectizer(BaseHTMLProcessor):
  subs = ()
  
  def reset(self):
    # extend (called from __init__ in ancestor)
    # Reset all data attributes
    self.verbatim = 0
    BaseHTMLProcessor.reset(self)
    
  def start_pre(self, attrs):
    # called for every <pre> tag in HTML source
    # Increment verbatim mode count, then handle tag like normal
    self.verbatim += 1
    self.unknown_starttag("pre", attrs)
    
  def end_pre(self):
    # called for every </pre> tag in HTML source
    # Decrement verbatim mode count
    self.unknown_endtag("pre")
    self.verbatim -= 1
    
  def handle_data(self, text):
    # override
    # called for every block of text in HTML source
    # If in verbatim mode, save text unaltered;
    # otherwise process the text with a series of substitutions
    self.pieces.append(self.verbatim and text or self.process(text))
    
  def process(self, text):
    # called from handle_data
    # Process text block by performing series of regular expression
    # substitutions (actual substitutions are defined in descendant)
    for fromPattern, toPattern in self.subs:
      text = re.sub(fromPattern, toPattern, text)
    return text
    
class ChefDialectizer(Dialectizer):
  """convert HTML to Swedish Chef-speak
  
  based on the classic chef.x, copyright (c) 1992, 1993 John Hagerman
  """
  subs = ((r'a([nu])', r'u\1'),
              (r'A([nu])', r'U\1'),
              (r'a\B', r'e'),
              (r'A\B', r'E'),
              (r'en\b', r'ee'),
              (r'\Bew', r'oo'),
              (r'\Be\b', r'e-a'),
              (r'\be', r'i'),
              (r'\bE', r'I'),
              (r'\Bf', r'ff'),
              (r'\Bir', r'ur'),
              (r'(\w*?)i(\w*?)$', r'\lee\2'),
              (r'\bow', r'oo'),
              (r'\bo', r'oo'),
              (r'\bO', r'Oo'),
              (r'the', r'zee'),
              (r'The',r'Zee'),
              (r'th\b', r't'),
              (r'\Btion',r'shun'),
              (r'\Bu', r'oo'),
              (r'\BU', r'Oo'),
              (r'v', r'f'),
              (r'V', r'F'),
              (r'w', r'w'),
              (r'W', r'W'),
              (r'([a-z])[.]', r'\1. Bork Bork Bork!'))
              
class FuddDialectizer(Dialectizer):
  """convert HTML to Elmer Fudd-speak."""
  subs = ((r'[rl]', r'w'),
              (r'qu', r'qw'),
              (r'th\b', r'f'),
              (r'th', r'd'),
              (r'n[.]', r'n, uh-hah-hah-hah.'))
              
class OldeDialectizer(Dialectizer):
  """convert HTML to mock Middle English"""
  subs = ((r'i([bcdfghjklmnpqrstvwxyz])e\b', r'y\1'),
              (r'i([bcdfgjklmnpqrstvwxyz])e', r'y\1\1e'),
              (r'ick\b', r'yk'),
              (r'ia([bcdfghjklmnpqrstvwxyz])', r'e\1e'),
              (r'e[ea]([bcdfghjklmnpqrstvwxyz])', r'e\1e'),
              (r'([bcdfghjklmnpqrstvwxyz])y', r'\1ee'),
              (r'([aeiou]re\b', r'\1r'),
              (r'ia[bcdfgjklmnpqrstvwxyz])', r'i\1e'),
              