#!/usr/bin/env ruby

require './python_writer'

SCANNER = <<-SCAN.gsub(/^ {12}/, '')
            for line in target.readlines():
              if(line[0] != '#'):
                if (method_match.search(line) is not None):
                  method.add(method_match.search(line).group())
                if (variable_match.search(line) is not None):
                  variable.add(variable_match.search(line).group())
                if (key_word_match.search(line) is not None):
                  key_word.add(key_word_match.search(line).group())
          SCAN

TOKENS = %w(method variable key_word)

REGEXES = { variable: ['\s*(\w*?)=', '\s(\w*?)\s', '\s(\w*?)\.'],
            method: ['\s*(\w*?)\(.*\)', '\.(\w*?)\(.*\)'],
            key_word: ['\s*(\w*?)\s']
          }


parser = PythonWriter.new ARGV.shift

Dir.chdir('..')

path = 'my_dir'

# Add our imports
['re', 'inspect', 'os', 'sys'].each { |mod| parser.add_import mod }
parser.add_import 'Set', 'sets'

# Build the file list
parser.write "files = #{Dir.glob('**/*py')}"

# Initialize the specific sets.
TOKENS.each do |set|
  parser.write "#{set} = Set([])"
end

# Compile the regular expressions
TOKENS.each do |token|
  parser.write "#{token}_match = re.compile('#{REGEXES[token.to_sym].join('|')}')"
end

parser.for_in 'files', 'file'
parser.indent
parser.write 'target = open(file)'
parser.write SCANNER
parser.undent

parser.add_print "Here are the Methods: %r", 'method'
parser.add_print "Here are the Variables: %r", 'variable'
parser.add_print "Here are the Key Words: %r", 'key_word'