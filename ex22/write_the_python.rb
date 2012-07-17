#!/usr/bin/env ruby

require './python_writer'

USAGE = <<USE
  Usage:
  
  write_the_python.rb <python_file>

  <python_file> should be the name of the file to be generated.
USE

if ARGV.empty?
  puts USAGE
  exit
end

parser = PythonWriter.new ARGV.shift

SCANNER = <<-SCAN.gsub(/^ {12}/, '')
            for line in target.readlines():
              if (line[0] != '#'):
                if (method_match.search(line) is not None):
                  for match in method_match.finditer(line):
                    method.add(match.group().strip())
                if (variable_match.search(line) is not None):
                  for match in variable_match.finditer(line):
                    variable.add(match.group().strip())
                if (key_word_match.search(line) is not None):
                  for match in key_word_match.finditer(line):
                    key_word.add(match.group().strip())
          SCAN

TOKENS = %w(method variable key_word)

REGEXES = { :variable => ['\s*(\w+?)\s?=', '[(|\s](\w+?)[,|)]'],
            :method => ['\s*(\w+?)\(', '\.(\w+?)\('],
            :key_word => ['(?<!")\w*?\s*?(\w+?)\s(?!=)|(?!=")']
          }


Dir.chdir('..')

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

parser.add_print "Here are the Methods: %r\\n", 'method'
parser.add_print "Here are the Variables: %r\\n", 'variable'
parser.add_print "Here are the Key Words: %r", 'key_word'