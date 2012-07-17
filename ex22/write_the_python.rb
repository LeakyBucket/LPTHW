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

TOKENS = %w(method variable key_word)

REGEXES = { :variable => ['\s*(\w+?)\s?=', '[(|\s](\w+?)[,|)]'],
            :method => ['\s*(\w+?)\(', '\.(\w+?)\('],
            :key_word => ['(?<!")\s+?(\w+?)\s(?!=)|(?!=")']
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
parser.for_in 'target.readlines()', 'line'
parser.indent
parser.write 'if (line[0] != \'#\'):'
parser.indent

TOKENS.each do |token|
  parser.write "if (#{token}_match.search(line) is not None):"
  parser.indent
  parser.for_in "#{token}_match.finditer(line)", "match"
  parser.indent
  parser.write "#{token}.add(match.group().strip())"
  parser.undent
  parser.undent
end

#parser.write SCANNER
1.upto(3) do
  parser.undent
end

parser.add_print "Here are the Methods: %r\\n", 'method'
parser.add_print "Here are the Variables: %r\\n", 'variable'
parser.add_print "Here are the Key Words: %r", 'key_word'